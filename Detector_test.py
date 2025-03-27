from Detector import Detector
from Dataset import Images_Dataset
from Loop import train_loop
from torch.utils.data import DataLoader
import yaml
import torch.nn as nn 
import os
import torch

import torch.optim as optim
import torchvision.transforms.functional as F


def test_detector(model,batch):
    pred=model(batch['data'])
    pred=pred[0]
    img_crop=F.to_pil_image(batch['data'][0]).crop((pred[0],pred[1],pred[2],pred[3]))
    img_crop.save(f'images/comic_sans/predicted/test.png')



option_path='config.yml'
with open(option_path,'r') as file_option:
    option=yaml.safe_load(file_option)











dataset=Images_Dataset(option['paths']['comic_sans'])

dataloader=DataLoader(dataset=dataset,batch_size=16,shuffle=True,drop_last=True)


model=Detector(3,64,4)

if 'detector_weights.pth' in os.listdir('.'):
    detector_weigths=torch.load('detector_weights.pth',weights_only=True)
    model.state_dict(detector_weigths)


for batch in dataloader:
    test_detector(model,batch)
    break