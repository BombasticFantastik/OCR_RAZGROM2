from Loop.Dataset import Images_Dataset,TestImages_Dataset
from Loop.Model import CRNN,Resnet50_CRNN,Resnet_Block
from Loop.Loop import train_loop

from torch.utils.data import DataLoader
import yaml
import torch.nn as nn 
import os
import torch

import torch.optim as optim

option_path='config.yml'
with open(option_path,'r') as file_option:
    option=yaml.safe_load(file_option)

device=option['device']

train_dataset=Images_Dataset(option['path'])

train_dataloader=DataLoader(dataset=train_dataset,batch_size=16,shuffle=True,drop_last=True)


model=Resnet50_CRNN(3,64,33).to(device)

if f'model_weights.pth' in os.listdir('Loop/weights'):
    weights_dict=torch.load(f'Loop/weights/model_weights.pth',weights_only=True)
    model.load_state_dict(weights_dict)
else:
    print('Весов нет, инициализируются новые')

detector_optimizer=optim.Adam(model.parameters())
loss_func=nn.CTCLoss()


train_loop(8,model=model,optimizer=detector_optimizer,loss_func=loss_func,dataloader=train_dataloader,device=device)