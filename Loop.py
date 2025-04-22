from tqdm import tqdm
import torch
import json

json_path='vocab/vocab.json'
with open(json_path,'r') as file_option:
    vocab=json.load(file_option)
let2int=vocab['let2int']
int2let=vocab['int2let']


def train_loop(epochs,model,optimizer,loss_func,dataloader,device):
    for epoch in range(epochs):
        for batch in (pbar:=tqdm(dataloader)):
            optimizer.zero_grad()
            pred=model(batch['img'].to(device))        
            T = pred.size(0)
            N = pred.size(1)
            input_lengths = torch.full(size=(N,), fill_value=T, dtype=torch.int32)
            target_lengths = torch.full(size=(N,), fill_value=8, dtype=torch.int32)
            loss=loss_func(pred,batch['label'],input_lengths,target_lengths)
            loss_item=loss.item()
            loss.backward()
            optimizer.step()
            pbar.set_description(f'Loss: {loss_item}')
            torch.save(model.state_dict(),'weights/model_weights.pth')

        
