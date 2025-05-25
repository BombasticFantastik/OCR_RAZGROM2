
import PIL.Image
from Dataset import Images_Dataset,TestImages_Dataset
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
#trans=transforms=transforms.Compose([transforms.Resize((256,512)),transforms.ToTensor()])

test_dataset=TestImages_Dataset('Test')
test_dataloader=DataLoader(dataset=test_dataset,batch_size=16,shuffle=False,drop_last=False)

    
loss_func=nn.CTCLoss()

model=CRNN(3,64,33).to(device)
#model=model.eval()

if f'model_weights.pth' in os.listdir('weights'):
    weights_dict=torch.load(f'weights/model_weights.pth',weights_only=True)
    model.load_state_dict(weights_dict)
else:
    print(1)

#model.eval()

for batch in test_dataloader:
    pred=model(batch['img'])
    pred=torch.log_softmax(pred,dim=2)
    T = pred.size(0)
    N = pred.size(1)
    input_lengths = torch.full(size=(N,), fill_value=T, dtype=torch.int32)
    target_lengths = torch.full(size=(N,), fill_value=5, dtype=torch.int32)
    loss=loss_func(pred,batch['label'],input_lengths,target_lengths)
    result=[int2let[str(i.item())] for i in pred.max(2)[1].transpose(1,0)[0]]
    result_label=[int2let[str(i.item())] for i in batch['label'][0]]

    #print(''.join(result))
    #result=[int2let[str(i.item())] for i in pred.max(2)[1].max(1)[1]]
    
    #print(result_label)
    print(f'{''.join(result).replace('а','')}-----{''.join(result_label)}')
    #print(f'{[i.item() for i in pred.argmax(0)[0]]}-----{batch['label'][0]}')



#print(get_normal_word(''.join(a)))



