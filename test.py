from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from random import randint


#class Text_Creat


def create_images():
    #alphabet='abcdefghijklmnopqrstuvwxyz'
    alphabet='abcdefgh'
    back_img=Image.open('white.png')
    
    

    word='aaa'

    max_width,max_height=back_img.size

    selected_font=ImageFont.truetype('Comic Sans MS/Comic Sans MS.ttf',65)
    #font=ImageFont.load("arial.pil")
    
    for i1 in range(len(alphabet)):
        for i2 in range(len(alphabet)):
            for i3 in range(len(alphabet)):
                word=alphabet[i1]+alphabet[i2]+alphabet[i3]

                print(randint(0,max_width),randint(0,max_height))
                
                #img=back_img.copy()
                #img_draw=ImageDraw.Draw(img)
                #img_draw.text((28,28),word,font=selected_font,fill=(255,0,0))
                #img.save(f'images/white_with_text{i1}{i2}{i3}.png')
                #print(word)


create_images()
   
    
    