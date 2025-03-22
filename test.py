from PIL import Image,ImageDraw,ImageFont
from random import randint,choice
import yaml


option_path='config.yml'
with open('config.yml','r') as file_option:
    option=yaml.safe_load(file_option)


#получаем список шрифтов для того что бы выбирать случайный из них
selected_font=option['fonts']['comic_sans']




#class Text_Creat



    
alphabet='abcdefgh'
back_img=Image.open('white.png')
    
max_widh,max_height=back_img.size
widh,height=randint(0,max_widh-200),randint(0,max_height-200)
    

word='Привет'


#копируем новую фотку и начинаем писать на фотке
img=back_img.copy()
img_draw=ImageDraw.Draw(img)

img_size=(widh,height)


selected_font=ImageFont.truetype(selected_font,65)

img_draw.text(xy=img_size,text=word,font=selected_font,fill=(255,0,0))
img.save(f'white_with_text.png')
img=img.crop((widh,height,widh+300,height+100))
img.save(f'white_with_text2.png')




   
    
    