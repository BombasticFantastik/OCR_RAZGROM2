from tqdm import tqdm


def train_loop(model,optimizer,loss_func,dataloader):
    for batch in (pbar:=tqdm(dataloader)):
        optimizer.zero_grad()


        pred=model(batch['data'])
        loss=loss_func(pred,batch['label'])
        loss_item=loss.item()
        loss.backward()

        optimizer.step()

        pbar.set_description(f'Loss: {loss_item}')

        
