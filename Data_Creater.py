from PIL import Image,ImageDraw,ImageFont
from random import randint


#class Text_Creat


def create_images():
    #alphabet='abcdefghijklmnopqrstuvwxyz'
    alphabet='abcdefgh'
    back_img=Image.open('white.png')
    
    max_widh,max_height=back_img.size
    

    word='aaa'

    selected_font=ImageFont.truetype('fonts/Comic Sans MS.ttf',65)
    #font=ImageFont.load("arial.pil")

    for i1 in range(len(alphabet)):
        for i2 in range(len(alphabet)):
            for i3 in range(len(alphabet)):
                word=alphabet[i1]+alphabet[i2]+alphabet[i3]
                img=back_img.copy()
                img_draw=ImageDraw.Draw(img)

                img_size=(randint(0,max_widh-200),randint(0,max_height-200))

                img_draw.text(img_size,word,font=selected_font,fill=(255,0,0))
                img.save(f'images/white_with_text{i1}{i2}{i3}.png')
                print(word)


create_images()
   
    
    