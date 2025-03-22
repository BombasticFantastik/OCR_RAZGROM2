from torch import nn
from torch.nn import Module


class Detector(Module):
    def __init__(self,input_size,output_size)