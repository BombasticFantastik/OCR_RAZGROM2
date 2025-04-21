from torch.utils.data import Dataset
from os import listdir
from os.path import join
from PIL import Image
from torchvision import transforms
from torch import tensor


class Images_Dataset(Dataset):
    def __init__(self,
                path,
                transforms=transforms.Compose([
        transforms.Resize((256,256))
        ,transforms.ToTensor()
        ])
        
        ):
        super(Images_Dataset,self).__init__()
        self.data_path=path
        self.image_transforms=transforms

        self.all_data=[join(self.data_path,item) for item in listdir(self.data_path)]


    def __len__(self):
        return len(self.all_data)

    def __getitem__(self, idx):
        
        #with open(self.all_labels[idx],'r') as f: label=f.read().split(',')
        return {
            "img":self.image_transforms(Image.open(self.all_data[idx])),
            'label':[self.all_data[idx].split('_')[0].replace('data/','')]
        }
        
df=Images_Dataset('data')
print(df[0])


