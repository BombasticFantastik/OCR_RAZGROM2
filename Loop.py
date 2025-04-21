from tqdm import tqdm
import torch


def train_loop(model,optimizer,loss_func,dataloader,device):
    for batch in (pbar:=tqdm(dataloader)):
        optimizer.zero_grad()

        
        pred=model(batch['img'].to(device))
        #ctc_loss
        imput_size=pred.shape[0]*pred.shape[1]
        print(pred.shape)
        # #loss=loss_func(pred,batch['label'],input_size,label_size)
        # loss_item=loss.item()
        # loss.backward()

        # optimizer.step()

        # pbar.set_description(f'Loss: {loss_item}')

        # torch.save(model.state_dict(),'weights/detector_weights.pth')

        
