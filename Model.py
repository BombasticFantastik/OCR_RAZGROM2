from torch import nn
from torch.nn import Module

class CRNN(Module):
    def __init__(self,input_size,hidden_dim,num_classes):
        super().__init__()
        self.cnn_lay0=nn.Sequential(
            nn.Conv2d(input_size,hidden_dim,3),
            nn.ReLU(),
            nn.BatchNorm2d(hidden_dim),
            nn.MaxPool2d(2,2)
        )
    def forward(self,x):
        out0=self.cnn_lay0(x)
        return out0

model=CRNN(3,64,32)