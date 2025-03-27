from Detector import Detector
from Dataset import Images_Dataset
from Loop import train_loop
from torch.utils.data import DataLoader
import yaml
import torch.nn as nn 
import os
import torch

import torch.optim as optim












detector_model=Detector(3,64,4)

detector_weigths=torch.load(r'detector_weights.pth',weights_only=True)
detector_model.state_dict(detector_weigths)