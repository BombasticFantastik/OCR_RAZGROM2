from PIL import Image,ImageDraw,ImageFont
from random import randint,choice
import yaml


option_path='config.yml'
with open('config.yml','r') as file_option:
    option=yaml.safe_load(file_option)


#получаем список шрифтов для того что бы выбирать случайный из них
fonts=[option['fonts'][font] for font in option['fonts']]




#class Text_Creat


def create_images():
    
    alphabet='abcdefgh'
    back_img=Image.open('white.png')
    
    max_widh,max_height=back_img.size
    

    word='aaa'

    
   

    for i1 in range(len(alphabet)):
        for i2 in range(len(alphabet)):
            for i3 in range(len(alphabet)):
                word=alphabet[i1]+alphabet[i2]+alphabet[i3]

                #копируем новую фотку и начинаем писать на фотке
                img=back_img.copy()
                img_draw=ImageDraw.Draw(img)

                img_size=(randint(0,max_widh-200),randint(0,max_height-200))

                #выбираем случайный шрифт из конфига
                selected_font=ImageFont.truetype(choice(fonts),65)

                img_draw.text(xy=img_size,text=word,font=selected_font,fill=(255,0,0))
                img.save(f'images/white_with_text{i1}{i2}{i3}.png')
                print(word)


create_images()
   
    
    