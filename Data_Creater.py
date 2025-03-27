from PIL import Image,ImageDraw,ImageFont
from random import randint,choice
import yaml
from tqdm import tqdm


option_path='config.yml'
with open('config.yml','r') as file_option:
    option=yaml.safe_load(file_option)






#class Text_Creat


def create_sans_images(alphabet,image_path,lenght,count):
    for cnt in tqdm(range(count)):
        word=''
        while len(word)<lenght:
            word+=choice(alphabet)

        back_img=Image.open(image_path)        
        max_widh,max_height=back_img.size
        #копируем новую фотку и начинаем писать на фотке
        img=back_img.copy()
        img_draw=ImageDraw.Draw(img)
        
        
        widh,height=randint(5,max_widh-150),randint(5,max_height-150)
        img_size=(widh,height)
        #выбираем случайный шрифт из конфига
        selected_font=ImageFont.truetype(option['fonts']['comic_sans'],65)
        #сохраняем изображение
        img_draw.text(xy=img_size,text=word,font=selected_font,fill=(255,0,0))
        img.save(f'images/comic_sans/data/{word}.png')
        #сохраняем обрезанное изображение
        
        img_crop=img.crop((widh,height+20,widh+len(word)*36,height+100))
        img_crop.save(f'images/comic_sans/croped_images/{word}.png')
        #сохраняем метки классов
        label_file=open(f'images/comic_sans/labels/{word}.txt','w+')#w+ означает создание нового файла
        label_file.write(f'{widh},{height+20},{widh+len(word)*36},{height+100}')
        label_file.close()

        
alphabet=[symb for symb in 'abcdefghijklmnopqrstuvwxyz']


create_sans_images(alphabet,'white.png',3,1500)
create_sans_images(alphabet,'white.png',5,1500)
create_sans_images(alphabet,'white.png',6,1500)
   
    
    