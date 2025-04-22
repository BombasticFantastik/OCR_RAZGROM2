from tqdm import tqdm
import torch
import json

json_path='vocab/vocab.json'
with open(json_path,'r') as file_option:
    vocab=json.load(file_option)
let2int=vocab['let2int']
int2let=vocab['int2let']


def train_loop(model,optimizer,loss_func,dataloader,device):
    for batch in (pbar:=tqdm(dataloader)):
        optimizer.zero_grad()

        
        pred=model(batch['img'].to(device))
        #ctc_loss
        
        T = pred.size(0)
        N = pred.size(1)
        #input_size=pred.shape[0]*pred.shape[1]
        #target_size=torch.tensor([len(i) for i in batch['label']])
        input_lengths = torch.full(size=(N,), fill_value=T, dtype=torch.int32)
        target_lengths = torch.full(size=(N,), fill_value=8, dtype=torch.int32)
        loss=loss_func(pred,batch['label'],input_lengths,target_lengths)
        loss_item=loss.item()
        loss.backward()
        optimizer.step()

        #acc_item=pred[0:8]-batch['label']
        pbar.set_description(f'Loss: {loss_item}; Accuracy: {[int2let[str(i)] for i in [let.tolist() for let in pred[0:8].argmax(dim=1)][0]]}')
        torch.save(model.state_dict(),'weights/detector_weights.pth')

        
