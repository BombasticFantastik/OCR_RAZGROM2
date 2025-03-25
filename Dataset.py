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
        self.croped_images_path=f'{path}/croped_images'
        self.image_transforms=transforms

        #self.data_dirs=listdir(self.data_path)
        #self.data_dirs=listdir(self.label_path)
        self.all_data=[join(self.data_path,item) for item in listdir(self.data_path)]
        self.all_croped_images=[join(self.croped_images_path,item) for item in listdir(self.croped_images_path)]
        self.all_labels=[join(self.label_path,item) for item in listdir(self.label_path)]

    def __len__(self):
        return len(self.all_data)

    def __getitem__(self, idx):
        
        with open(self.all_labels[idx],'r') as f: label=f.read().split(',')
        return {
            'data':self.image_transforms(Image.open(self.all_data[idx])),
            'crop_image':self.image_transforms(Image.open(self.all_croped_images[idx])),
            'label': label
        }
        


dataset=Images_Dataset('/home/artemybombastic/ArtemyBombasticGit/OCR_RAZGROM2/images/comic_sans/')
print(dataset[0])