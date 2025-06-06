from tqdm import tqdm
import torch
import json

json_path=r'D:\Code\OCR_RAZGROM2\Data\vocab\vocab.json'
with open(json_path,'r') as file_option:
    vocab=json.load(file_option)
let2int=vocab['let2int']
int2let=vocab['int2let']


def train_loop(epochs,model,optimizer,loss_func,dataloader,device):
    for epoch in range(epochs):
        losses=[]
        for batch in (pbar:=tqdm(dataloader)):
            optimizer.zero_grad()
            pred=model(batch['img'].to(device))        
            T = pred.size(0)
            N = pred.size(1)
            input_lengths = torch.full(size=(N,), fill_value=T, dtype=torch.int32)
            target_lengths = torch.full(size=(N,), fill_value=7, dtype=torch.int32)
            loss=loss_func(torch.log_softmax(pred,dim=2),batch['label'],input_lengths,target_lengths)
            loss_item=loss.item()
            losses.append(loss)
            loss.backward()
            optimizer.step()
            pbar.set_description(f'Loss: {loss_item}')
            try:
                torch.save(model.state_dict(),r'D:\Code\OCR_RAZGROM2\Loop\weights\model_weights.pth')
            except:
                print('Ошибка загрузки')
        print(f'mean loss:{sum(losses)/len(losses)}')


        
