# T23: квадраты 1200 на белом + комбо конденсер+фанкойл. Запуск из images/: python3 T23/build_T23.py
import os
from PIL import Image
SRC="T23"; OUT="upload/T23_01"; os.makedirs(OUT,exist_ok=True)
def white(im):
    im=im.convert("RGBA"); bg=Image.new("RGBA",im.size,"white"); return Image.alpha_composite(bg,im).convert("RGB")
def square(src,dst,size=1200,margin=0.08):
    im=white(Image.open(src)); box=int(size*(1-2*margin)); k=min(box/im.width,box/im.height)
    im=im.resize((max(1,int(im.width*k)),max(1,int(im.height*k))),Image.LANCZOS)
    c=Image.new("RGB",(size,size),"white"); c.paste(im,((size-im.width)//2,(size-im.height)//2)); c.save(dst,quality=90)
def combo(a,b,dst):
    def fit(p,box):
        im=white(Image.open(p)); k=min(box[0]/im.width,box[1]/im.height); return im.resize((int(im.width*k),int(im.height*k)),Image.LANCZOS)
    c=Image.new("RGB",(1200,800),"white"); x=fit(a,(560,700)); y=fit(b,(560,700))
    c.paste(x,(40+(560-x.width)//2,(800-x.height)//2)); c.paste(y,(600+(560-y.width)//2,(800-y.height)//2)); c.save(dst,quality=90)
SQ={"SCT030AG-L.png":"SCT030AG-L.jpg","36CDXQ201UZP050AAF.png":"36CDXQ201UZP050AAF.jpg","36HCXW.png":"36HCXW.jpg",
    "9EVR32-1A.webp":"9EVR32-1A.jpg","9EVR454B-1A.webp":"9EVR454B-1A.jpg","400-4.jpg":"TACO-400-4.jpg","MP-4E.jpg":"MP-4E.jpg",
    "0230K00044.jpg":"0230K00044.jpg","KDDQ44XA60.jpg":"KDDQ44XA60.jpg","KER087A41.png":"KER087A41.jpg","KKP937A4.jpg":"KKP937A4.jpg"}
for s,d in SQ.items(): square(os.path.join(SRC,s),os.path.join(OUT,d)); print("OK",d)
for cond in ["GLXS4BA1810A","37MURAQ18AA3","5A6H7024A1","DC7TCA2410A"]:
    for fc in ["36HCXW","36CDXQ201UZP050AAF"]:
        d=f"{cond}+{fc}.jpg"; combo(f"{cond}.jpg", os.path.join(SRC,fc+".png"), os.path.join(OUT,d)); print("OK",d)
