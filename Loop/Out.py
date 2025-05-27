import torch
import sys 
sys.path.insert(0, '/home/artemybombastic/ArtemyBombasticGit/OCR_RAZGROM2/Loop')
from torchvision import transforms
import os
from Model import CRNN
import json

def get_text(model,image,int2let):

    if model==None:
        model=CRNN(3,64,33)
        if f'model_weights.pth' in os.listdir('Loop/weights'):
            weights_dict=torch.load(f'Loop/weights/model_weights.pth',weights_only=True)
            model.load_state_dict(weights_dict)
        else:
            print(0)

    if int2let==None:
        json_path='/home/artemybombastic/ArtemyBombasticGit/OCR_RAZGROM2/Data/vocab/vocab.json'
        with open(json_path,'r') as file_option:
            vocab=json.load(file_option)
        int2let=vocab['int2let']

    trans=transforms.Compose([transforms.Resize((256,256)),transforms.ToTensor()])
    image_tensor=trans(image)
    image_tensor=image_tensor.view(-1,3,256,256)
    pred=model(image_tensor)
    pred=torch.log_softmax(pred,dim=2)
    result=[int2let[str(i.item())] for i in pred.max(2)[1].transpose(1,0)[0]]
    result=''.join(result)
    result=result.replace('     ','7&7')
    for i in range(len(result)):
        result=result.replace(' ','')
    result=result.replace('7&7',' ')
    if result[0]==' ':
        result=result[1:]
    return result

