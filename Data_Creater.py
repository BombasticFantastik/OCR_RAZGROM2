from PIL import Image,ImageDraw,ImageFont
from random import randint,choice
import yaml
from tqdm import tqdm


option_path='config.yml'
with open('config.yml','r') as file_option:
    option=yaml.safe_load(file_option)

def create_sans_images(alphabet,image_path,lenght,count):
    for cnt in tqdm(range(count)):
        alphabet_with_no_space=[i for i in alphabet if i!=' ']
        word=choice(alphabet_with_no_space)
        while len(word)<lenght+1:
            word+=choice(alphabet)
        word+=choice(alphabet_with_no_space)

        

        back_img=Image.open(image_path)        
        max_widh,max_height=back_img.size
        #копируем новую фотку и начинаем писать на фотке
        img=back_img.copy()
        img_draw=ImageDraw.Draw(img)
        
        
        widh,height=randint(5,max_widh-1700),randint(5,max_height-200)
        img_size=(widh,height)
        #выбираем случайный шрифт из конфига
        selected_font_name=choice(list(option['fonts']))
        selected_font=ImageFont.truetype(option['fonts'][selected_font_name],250)

        
        #сохраняем изображение
        img_draw.text(xy=img_size,text=word,font=selected_font,fill=(255,0,0))
        img.save(f'data/{word}_{selected_font_name}.png')
        
alphabet=[symb for symb in ' абвгдеёжзийклмнопрстуфхцчшщъыьэюя']


create_sans_images(alphabet,'white.png',5,9000)
   
    
    