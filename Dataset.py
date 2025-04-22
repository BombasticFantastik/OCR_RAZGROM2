from torch.utils.data import Dataset
from os import listdir
from os.path import join
from PIL import Image
from torchvision import transforms
from torch import tensor
import json




class Images_Dataset(Dataset):
    def __init__(self,
                path,
                transforms=transforms.Compose([
        transforms.Resize((32,128))
        ,transforms.ToTensor()
        ])
        
        ):
        super(Images_Dataset,self).__init__()
        self.data_path=path
        self.image_transforms=transforms

        self.all_data=[join(self.data_path,item) for item in listdir(self.data_path)]


        json_path='vocab/vocab.json'
        with open(json_path,'r') as file_option:
            vocab=json.load(file_option)
        self.let2int=vocab['let2int']
        self.int2let=vocab['int2let']


    def __len__(self):
        return len(self.all_data)

    def __getitem__(self, idx):
        
        #with open(self.all_labels[idx],'r') as f: label=f.read().split(',')
        return {
            "img":self.image_transforms(Image.open(self.all_data[idx])),
            'label':tensor([self.let2int[let] for let in self.all_data[idx].split('_')[0].replace('data/','')])
        }
        
df=Images_Dataset('data')



