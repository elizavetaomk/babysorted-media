# White "tog scale" layout (27 Nov 2026): white bg, product on a soft pink disc at the top, a tog scale strip with the
# current value highlighted, navy text below. Used for: #58 Tog ratings explained. No prices.
# Facts: The Lullaby Trust "Dress your baby for sleep" (higher tog = warmer; no tog-for-temperature table, follow the maker;
# 16-20°C; fitted by weight; well fitted round neck and shoulders; no blankets on top; hats off indoors; feel chest or back of
# neck; weighted bags not recommended under 1; BS EN 16781:2018; don't wrap an unwell baby up more than usual).
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css("#fff",NAVY,PINK,NAVY)+".t2{background:#fff}"
LT="Source: The Lullaby Trust, the UK safer baby sleep charity"
SN=b("snuz.png",700); MO=b("mori.png",700); LD=b("ltd.png",700); JO=b("jollein.png",700)
TOGS=["0.5","1.0","1.5","2.5","3.5"]
def scale(on=None):
    cells="".join(f'<div class="h" style="flex:1;text-align:center;padding:14px 0;border-radius:18px;font-size:34px;background:{NAVY if t==on else PINK};color:{"#fff" if t==on else NAVY}">{t}</div>' for t in TOGS)
    return f'<div style="display:flex;gap:10px;align-items:center"><div style="font-weight:800;font-size:24px;letter-spacing:.06em;opacity:.6;width:70px">TOG</div>{cells}</div>'
def top(inner):
    return f'''<div style="position:absolute;left:270px;top:60px;width:540px;height:540px;border-radius:50%;background:{PINK}"></div>
<div style="position:absolute;left:0;right:0;top:50px;height:580px;display:flex;align-items:center;justify-content:center">{inner}</div>'''
def slide(inner,kick,title,body,on=None,src=LT):
    s=f'<div style="position:absolute;left:70px;right:70px;top:1190px;font-size:23px;font-weight:700;opacity:.7">{src}</div>' if src else ""
    return top(inner)+f'''<div style="position:absolute;left:70px;right:70px;top:665px">{scale(on)}
<div class="kick" style="margin-top:30px">{kick}</div><div class="h" style="font-size:66px;margin-top:8px">{title}</div>
<div class="b" style="margin-top:16px;font-size:38px">{body}</div></div>{s}'''
pimg=lambda s,h: f'<img src="{s}" style="height:{h}px;object-fit:contain;{SH}">'
big=lambda a,c: f'<div style="text-align:center;position:relative"><div class="h" style="font-size:150px">{a}</div><div style="font-weight:700;font-size:32px;opacity:.75;margin-top:6px">{c}</div></div>'
cover=hero_cover(baby(24,1080,800,.5,.45,1.0),'<div class="tags"><span class="tag t1">Tips</span><span class="tag t2" style="box-shadow:inset 0 0 0 3px #051F45">Kids Furniture</span></div>',
 "Tog ratings explained","What the numbers really mean on a cold night.",f'<img src="{LD}" style="height:430px;{SH}">',1,card="#fff",title_fs=78,pill="Swipe for 8 checks")
s2=slide(f'<div style="display:flex;align-items:flex-end;gap:26px">{pimg(JO,300)}{pimg(SN,360)}{pimg(MO,400)}{pimg(LD,450)}</div>',"THE NUMBER","Higher tog = warmer bag","Tog only tells you how warm the fabric is. It doesn’t tell you the size, the fit or the right room for it.","1.0")
s3=slide(big("16–20°C","the room a baby sleeps in"),"START WITH THE ROOM","Check the room, not the season","At 16–20°C a lightweight, well-fitting sleep bag or light bedding is comfortable. A cheap room thermometer stops the guessing.")
s4=slide(f'<div style="display:flex;align-items:flex-end;gap:40px">{pimg(SN,400)}{pimg(LD,450)}</div>',"NO OFFICIAL CHART","There’s no national tog chart","The Lullaby Trust doesn’t give a tog-for-temperature table. Follow the guide that comes with your bag, for your room.","2.5")
s5=slide(pimg(MO,470),"FIT","Size by weight, not age","Most sleep bags are fitted by weight. It should fit well around the neck and shoulders, so your baby can’t slip down inside.","1.5")
s6=slide(big("BS EN<br>16781","the sleep bag safety standard"),"LABEL","Look for the safety standard","The UK safety standard for baby sleep bags is BS EN 16781:2018. Check the label or the listing before you buy.")
s7=slide(big("Chest","or back of the neck"),"CHECK","Feel the chest, not the hands","Cool hands and feet are normal. If the skin on the chest feels hot or sweaty, your baby is too hot: take a layer off.")
s8=slide(pimg(JO,470),"KEEP IT SIMPLE","No blankets on top, no hats","With a sleep bag, don’t add blankets. Take hats off indoors. Weighted sleep bags aren’t recommended for babies under one.","0.5")
s9=slide(big("Unwell?","dress for the room"),"WHEN POORLY","Don’t wrap a poorly baby up","Dress them for the room, not more than usual. Worried? Call your GP or NHS 111 (free from landlines and mobiles in England, Scotland and Wales).")
s10=hero_last(baby(4,1080,760,.45,.5),"Right tog, right fit, right room","Compare sleeping bag prices from UK shops in one place.",PINK)
pin=pin_hero(baby(16,1000,700,.5,.62,1.0),pin_tags("Tips","Kids Furniture"),"Tog ratings: 6 things to check",
 ["Higher tog = warmer fabric","Aim for a room of 16–20°C","Use the maker’s tog chart","Fit by weight, snug at the neck","No blankets on top, no hats","Feel the chest, not the hands"],
 SN,330,"#fff",NAVY,PINK,NAVY,LT+".","Compare sleeping bag prices at babysorted.com",line=PINK,photo_h=700,title_fs=58)
render(ROOT+"/out/a",[cover,s2,s3,s4,s5,s6,s7,s8,s9,s10],pin,CSS,NAVY)
