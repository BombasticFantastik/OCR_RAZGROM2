from Detector import Detector
from Dataset import Images_Dataset
from Loop import train_loop
from torch.utils.data import DataLoader
import yaml
import torch.nn as nn 
import os
import torch

import torch.optim as optim

option_path='config.yml'
with open(option_path,'r') as file_option:
    option=yaml.safe_load(file_option)


train_dataset=Images_Dataset(option['paths']['comic_sans'])

train_dataloader=DataLoader(dataset=train_dataset,batch_size=16,shuffle=True,drop_last=True)

detector_model=Detector(3,64,4).to(option['device'])

if 'detector_weights.pth' in os.listdir('.'):
    detector_weigths=torch.load('detector_weights.pth',weights_only=True)
    detector_model.state_dict(detector_weigths)

detector_optimizer=optim.Adam(detector_model.parameters())
loss_func=nn.CrossEntropyLoss()


train_loop(model=detector_model,optimizer=detector_optimizer,loss_func=loss_func,dataloader=train_dataloader,device=option['device'])
