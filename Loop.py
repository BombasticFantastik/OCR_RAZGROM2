from tqdm import tqdm
import torch


def train_loop(model,optimizer,loss_func,dataloader,device):
    for batch in (pbar:=tqdm(dataloader)):
        optimizer.zero_grad()

        
        pred=model(batch['img'].to(device))
        loss=loss_func(pred,batch['label'].to(device))
        loss_item=loss.item()
        loss.backward()

        optimizer.step()

        pbar.set_description(f'Loss: {loss_item}')

        torch.save(model.state_dict(),'weights/detector_weights.pth')

        
