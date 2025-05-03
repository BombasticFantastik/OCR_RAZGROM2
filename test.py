
import PIL.Image
from Dataset import Images_Dataset
from Loop import train_loop
from torch.utils.data import DataLoader
import yaml
import torch.nn as nn 
import os
import torch
import PIL
import json
import torch.optim as optim
from Utils import get_normal_word


json_path='vocab/vocab.json'
with open(json_path,'r') as file_option:
    vocab=json.load(file_option)
let2int=vocab['let2int']
int2let=vocab['int2let']



from Dataset import Images_Dataset
from Model import CRNN
from Loop import train_loop
from torch.utils.data import DataLoader
import yaml
import torch.nn as nn 
import os
import torch
from torchvision import transforms
import torch.optim as optim

option_path='config.yml'
with open(option_path,'r') as file_option:
    option=yaml.safe_load(file_option)

device=option['device']
trans=transforms=transforms.Compose([transforms.Resize((256,512)),transforms.ToTensor()])

test_image=trans(PIL.Image.open('/home/artemybombastic/ArtemyBombasticGit/OCR_RAZGROM2/Test/а тючкялбф_comic_sans.png'))
#print(test_image.view(-1,3,32,128))


    


model=CRNN(3,64,33).to(device)

if f'model_weights.pth' in os.listdir('weights'):
    weights_dict=torch.load(f'weights/model_weights.pth',weights_only=True)
    model.load_state_dict(weights_dict)
else:
    print(1)

out=model(test_image.view(-1,3,256,512).to(device))

a=[int2let[str(let.item())] for let in torch.log_softmax(out,dim=2).argmax(2)]
print(get_normal_word(''.join(a)))



