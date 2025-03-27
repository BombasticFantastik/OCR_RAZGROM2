from torch import nn
from torch.nn import Module


class Detector(Module):
    def __init__(self,input_size,hidden_size,output_size):
        super(Detector,self).__init__()
        self.initial_lay=nn.Sequential(
            nn.Conv2d(in_channels=input_size,out_channels=hidden_size,kernel_size=3),
            nn.ReLU(),
            nn.MaxPool2d(2,2)
            )
        self.lay0=nn.Sequential(
            nn.Conv2d(hidden_size,hidden_size*2,3),
            nn.ReLU(),
            nn.MaxPool2d(2,2)
        )
        self.lay1=nn.Sequential(
            nn.Conv2d(hidden_size*2,hidden_size*4,3),
            nn.ReLU(),
            nn.MaxPool2d(2,2)
        )
        self.lay2=nn.Sequential(
            nn.Conv2d(hidden_size*4,hidden_size*4,3),
            nn.ReLU(),
            nn.MaxPool2d(2,2)
        )
        self.final_lay=nn.Sequential(
            nn.Flatten(),
            nn.Linear(50176,output_size)
            
            
        )
    def forward(self,x):
        initial_out=self.initial_lay(x)
        out0=self.lay0(initial_out)
        out1=self.lay1(out0)
        out2=self.lay2(out1)

        fin_out=self.final_lay(out2)
        return fin_out
    
model=Detector(3,64,4)