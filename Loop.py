def train_loop(model,optimizer,loss_func,dataloader):
    for batch in loss_func:
        optimizer.zero_grad()
