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
        self.dropaut=nn.Dropout(0.1)
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

