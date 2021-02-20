from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from os import mkdir

def split_text(text: str, line_length: int):
    text = text.split(' ')
    tmp = ""
    word_count = 0
    for i in range(len(text)):

        if ',' in text[i]:
            tmp += text[i].replace(',',',\n')
            word_count=0
        else:
            tmp += text[i]+' '
            word_count+=1

        if word_count == line_length:
            tmp+='\n'
            word_count = 0

    return tmp


def create_imaged_caption(caption: str,save_name: str,bg_color=(255,255,255),fg_color=(0,0,0),size=(1080,1080),font_path='assets/font/AbrilFatface-Regular.ttf',font_size=48):
    words = 6
    caption_text = txt = split_text(caption,words)
    W,H = (size[0],size[1])
    img = Image.new('RGB',(W,H),color=bg_color)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path,font_size)
    w,h = draw.textsize(caption_text, font=font,)
    print(w,h)
    while w>950:
        words-=1
        caption_text = split_text(caption,words)
        w,h = draw.textsize(caption_text, font=font,)
    draw.multiline_text(((W-w)/2,(H-h)/2), caption_text, fg_color, font=font, align='left')
    img.save(save_name)

def create_all(caption_file: str,bg_color=(255,255,255),fg_color=(0,0,0),size=(1080,1080),font_path='assets/font/AbrilFatface-Regular.ttf',font_size=48):
    try:
        mkdir('./caption_images/unused')
    except:
        pass
    with open(caption_file,'r') as f:
        captions=f.readlines()
        f.close()
    
    for i,caption in enumerate(captions):
        fname = "./caption_images/unused/caption_{:03}.jpg".format(i)
        create_imaged_caption(caption,fname,bg_color=bg_color,fg_color=fg_color,size=size,font_path=font_path,font_size=font_size)


create_all('./db_edited.txt',bg_color=(241,234,223),fg_color=(18,69,89))

# with open('./db_edited.txt','r') as f:
#     captions=f.readlines()
#     for s in captions:
#         print(split_text(s,5))
#     f.close()
# print(split_text("Pour arriver au bonheur, il faut commencer par se lever.",6))