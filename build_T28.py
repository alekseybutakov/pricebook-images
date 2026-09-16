# T28: квадраты 1200 на белом. Запуск из images/: python3 T28/build_T28.py
import os
from PIL import Image
SRC="T28"; OUT="upload/photos_05"; os.makedirs(OUT,exist_ok=True)
def white(im):
    im=im.convert("RGBA"); bg=Image.new("RGBA",im.size,"white"); return Image.alpha_composite(bg,im).convert("RGB")
def square(src,dst,size=1200,margin=0.08):
    im=white(Image.open(src)); box=int(size*(1-2*margin)); k=min(box/im.width,box/im.height)
    im=im.resize((max(1,int(im.width*k)),max(1,int(im.height*k))),Image.LANCZOS)
    c=Image.new("RGB",(size,size),"white"); c.paste(im,((size-im.width)//2,(size-im.height)//2)); c.save(dst,quality=90)
SQ={"MXZ-2D20NL.png":"MXZ-2D20NL.jpg","SLZ-AF12NL.png":"SLZ-AF12NL.jpg","SLP-18FAU.png":"SLP-18FAU.jpg",
    "MHK2.jpg":"MHK2.jpg","YN020GLSI24M2G.jpg":"YN020GLSI24M2G.jpg","CT012GLSILCFHG.jpg":"CT012GLSILCFHG.jpg",
    "SUZ-AA-series.png":"SUZ-AA12NL.jpg","YN012GLSI24RPG.jpg":"YN012GLSI24RPG.jpg"}
for s,d in SQ.items():
    p=os.path.join(SRC,s)
    if not os.path.exists(p): print("НЕТ ИСХОДНИКА",s); continue
    square(p,os.path.join(OUT,d)); print("OK",d)
# панель Pioneer отдельного фото не имеет — используем фото кассеты (панель видна)
import shutil
src=os.path.join(OUT,"CT012GLSILCFHG.jpg")
if os.path.exists(src): shutil.copyfile(src,os.path.join(OUT,"CT0918DPNL.jpg")); print("OK CT0918DPNL.jpg (reuse)")
# проход 2: серийные фото — один файл на серию
for code in ["SUZ-AA09NL","SUZ-AA15NL","SUZ-AA18NL"]:
    a=os.path.join(OUT,"SUZ-AA12NL.jpg")
    if os.path.exists(a): shutil.copyfile(a,os.path.join(OUT,code+".jpg")); print("OK",code+".jpg (series photo)")
for code in ["SLZ-AF09NL","SLZ-AF15NL","SLZ-AF18NL"]:
    a=os.path.join(OUT,"SLZ-AF12NL.jpg")
    if os.path.exists(a): shutil.copyfile(a,os.path.join(OUT,code+".jpg")); print("OK",code+".jpg (series photo)")
