from torch import nn
from torch.nn import Module


class CRNN(Module):
    def __init__(self,input_size,hidden_dim,num_classes):
        super().__init__()
        self.cnn_lay0=nn.Sequential(
            nn.Conv2d(input_size,hidden_dim,3,stride=2,padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(hidden_dim),
            nn.MaxPool2d((2,1),(2,1))
        )
        
        self.cnn_lay1=nn.Sequential(
            nn.Conv2d(hidden_dim,hidden_dim*2,3,stride=2,padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(hidden_dim*2),
            nn.MaxPool2d((2,1),(2,1))
        )
                
        self.cnn_lay2=nn.Sequential(
            nn.Conv2d(hidden_dim*2,hidden_dim*4,3,stride=2,padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(hidden_dim*4),
            nn.MaxPool2d((2,1),(2,1))
        )
        self.cnn_lay3=nn.Sequential(
            nn.Conv2d(hidden_dim*4,hidden_dim*8,3,stride=1,padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(hidden_dim*8),
            nn.MaxPool2d((2,1),(2,1))
        )
        self.cnn_lay4=nn.Sequential(
            nn.Conv2d(hidden_dim*8,hidden_dim*16,3,stride=1,padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(hidden_dim*16),
            nn.MaxPool2d((2,1),(2,1))
        )
        self.rec_part=nn.LSTM(hidden_dim*16,hidden_dim*4,num_layers=1,bidirectional=True)
        self.dropaut=nn.Dropout(0.15)
        self.fin_lin=nn.Linear(hidden_dim*8,num_classes+1)


    def forward(self,x):
        out0=self.cnn_lay0(x)

        out1=self.cnn_lay1(out0)

        out2=self.cnn_lay2(out1)


        out3=self.cnn_lay3(out2)


        out4=self.cnn_lay4(out3)#мб 2_0_1#попробовать батч фёрст

        #print(out4.shape)
        out4=out4.squeeze(2).permute(2,0,1)


        

        rec_out,_=self.rec_part(out4)
 
        pred=self.fin_lin(self.dropaut(rec_out))
        
        return pred



class Resnet_Block(Module):
    def __init__(self,in_channels,hid_dim:int,stride:int):
        super(Resnet_Block,self).__init__()

        self.relu=nn.ReLU(inplace=True)

        self.conv0=nn.Conv2d(in_channels,hid_dim,kernel_size=3,padding=1,stride=stride)
        self.norm0=nn.BatchNorm2d(hid_dim)
        self.conv1=nn.Conv2d(hid_dim,hid_dim,kernel_size=3,padding=1,stride=1)
        self.norm1=nn.BatchNorm2d(hid_dim)


        #для скип конекшена
        self.skip_con=nn.Sequential(
            nn.Conv2d(in_channels,hid_dim,kernel_size=1,stride=stride),
            nn.BatchNorm2d(hid_dim)
        )

    def forward(self,x):

        out0=self.relu(self.norm0(self.conv0(x)))
        out1=self.norm1(self.conv1(out0))
        out1+=self.skip_con(x)
        return self.relu(out1)

class Resnet50_CRNN(Module):
    def __init__(self,input_size,hiden_size,num_classes):
        super(Resnet50_CRNN,self).__init__()

        #входные слои
        self.inital_conv=nn.Conv2d(input_size,hiden_size,kernel_size=7,stride=2,padding=3)
        self.inital_norm=nn.BatchNorm2d(hiden_size)
        self.relu=nn.ReLU()
        self.maxpool=nn.MaxPool2d(3,2,1)



        #основные слои
        self.lay0=self.make_layers(Resnet_Block,hiden_size,hiden_size,1,2)
        self.lay1=self.make_layers(Resnet_Block,hiden_size,hiden_size*2,1,2)
        self.lay2=self.make_layers(Resnet_Block,hiden_size*2,hiden_size*2,1,(2,1))
        self.lay3=self.make_layers(Resnet_Block,hiden_size*2,hiden_size*4,1,(4,1))
        self.lay4=self.make_layers(Resnet_Block,hiden_size*4,hiden_size*8,1,(4,1))

        #линейные слои
        self.rec_part=nn.LSTM(hiden_size*8,hiden_size*4,num_layers=1,bidirectional=True,batch_first=False)
        self.fin_lin=nn.Linear(hiden_size*8,num_classes+1)

    def make_layers(self,block,input_size,output_size,cnt,stride):
        layers=[]

        layers.append(block(input_size,output_size,stride=stride))

        for i in range(1,cnt):
            layers.append(block(output_size,output_size,stride=1))
        return nn.Sequential(*layers)

    def forward(self,x):
        #print(f'0:{x.shape}')
        initial_out=self.inital_conv(x)
        #print(initial_out.shape)
        initial_out=self.inital_norm(initial_out)
        initial_out=self.relu(initial_out)
        initial_out=self.maxpool(initial_out)
        #print(f'1:{initial_out.shape}')
        out0=self.lay0(initial_out)
        #print(f'2:{out0.shape}')
        out1=self.lay1(out0)
        #print(f'3:{out1.shape}')
        out2=self.lay2(out1)
        #print(f'4:{out2.shape}')

        out3=self.lay3(out2)
        #print(f'5:{out3.shape}')


        out4=self.lay4(out3)
        #print(f'6:{out4.shape}')

        N,C,H,W=out4.shape

        out4=out4.view(N,-1,W)
        #print(out4.shape)

        

        out4=out4.permute(2,0,1)
        #print(out4.shape)

        lstm_out,_=self.rec_part(out4)
        #print(f'lstm:{lstm_out.shape}')
        final_out=self.fin_lin(lstm_out)
        #print(f'final:{final_out.shape}')
        return final_out


        




