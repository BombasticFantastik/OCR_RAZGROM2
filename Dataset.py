from torch.utils.data import Dataset
from os import listdir
from os.path import join
from PIL import Image
from torchvision import transforms


class Images_Dataset(Dataset):
    def __init__(self,
                 path,
                 transforms=transforms.Compose([
        transforms.Resize((256,256))
        ,transforms.ToTensor()
        ])
        
        ):
        super(Images_Dataset,self).__init__()
        self.data_path=f'{path}/data'
        self.label_path=f'{path}/labels'
        self.image_transforms=transforms

        #self.data_dirs=listdir(self.data_path)
        #self.data_dirs=listdir(self.label_path)
        self.all_data=[join(self.data_path,item) for item in listdir(self.data_path)]
        self.all_labels=[join(self.label_path,item) for item in listdir(self.label_path)]

    def __len__(self):
        return len(self.all_data)

    def __getitem__(self, idx):
        return {
            'data':self.image_transforms(Image.open(self.all_data[idx])),
            'label':self.image_transforms(Image.open(self.all_labels[idx]))
        }
    


dataset=Images_Dataset('/home/artemybombastic/ArtemyBombasticGit/OCR_RAZGROM2/images/comic_sans/')


