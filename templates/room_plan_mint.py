# Mint "room plan" layout: mint bg, white card drawn like a floor plan (dashed walls, door arc) with the product inside,
# a navy map-pin number, text below. Used for: How to set up a small nursery (13 Nov 2026).
# Facts: The Lullaby Trust, RoSPA, NHS. Wood/beige products on mint, navy accents only.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css(MINT,NAVY,NAVY,"#fff")+".t2{background:#fff;box-shadow:none}"
DATE="13 Nov 2026"
deco=star(36,30,26,"#fff")+star(1000,36,30,"#fff")
CZ=b("cozee.png",1000); MY=b("maya.png",1000); MT=b("mat.png",800)
LT="Source: The Lullaby Trust, the UK safer baby sleep charity"
RS="Source: RoSPA, the UK accident prevention charity"
def plan(inner,price=None):
    pr=f'<div style="position:absolute;right:34px;bottom:30px;text-align:right"><div class="h" style="font-size:46px">{price[0]}</div><div style="font-size:21px;font-weight:600;opacity:.7;line-height:1.3">{price[1]}<br>Price on BabySorted, {DATE}</div></div>' if price else ""
    return f'''<div style="position:absolute;left:60px;right:60px;top:60px;height:610px;background:#fff;border-radius:44px;overflow:hidden">
<div style="position:absolute;inset:34px;border:5px dashed {MINT};border-radius:18px"></div>
<svg style="position:absolute;right:34px;top:34px" width="150" height="150" viewBox="0 0 150 150"><path d="M150 0 A150 150 0 0 0 0 150" fill="none" stroke="{MINT}" stroke-width="5" stroke-dasharray="12 10"/><line x1="0" y1="0" x2="0" y2="150" stroke="{MINT}" stroke-width="5"/></svg>
<div style="position:absolute;inset:40px 40px 40px 40px;display:flex;align-items:center;justify-content:center">{inner}</div>{pr}</div>'''
def pinmark(k):
    return f'''<div style="position:absolute;left:44px;top:40px;width:150px;height:190px"><svg width="150" height="190" viewBox="0 0 150 190"><path d="M75 186 C 40 130 6 104 6 70 A69 69 0 1 1 144 70 C144 104 110 130 75 186Z" fill="{NAVY}"/></svg>
<div class="h" style="position:absolute;left:0;right:0;top:22px;text-align:center;color:#fff;font-size:84px">{k}</div></div>'''
def move(k,title,body,inner,src,price=None):
    return deco+plan(inner,price)+pinmark(k)+f'''<div style="position:absolute;left:70px;right:70px;top:712px"><div class="kick">MOVE {k} OF 7</div><div class="h" style="font-size:70px;margin-top:8px">{title}</div><div class="b" style="margin-top:14px;font-size:38px">{body}</div>
<div style="font-size:26px;font-weight:700;opacity:.6;margin-top:14px">{src}</div></div>'''
img=lambda s,h,x="": f'<img src="{s}" style="height:{h}px;max-width:820px;object-fit:contain;{SH};{x}">'
big=lambda a,c: f'<div style="text-align:center"><div class="h" style="font-size:180px;line-height:1">{a}</div><div class="h" style="font-size:48px;margin-top:8px">{c}</div></div>'
def nolist(items):
    return '<div style="display:flex;flex-direction:column;gap:22px">'+"".join(f'<div style="display:flex;align-items:center;gap:24px"><div class="h" style="flex:none;width:76px;height:76px;border-radius:50%;background:{NAVY};color:#fff;font-size:46px;display:flex;align-items:center;justify-content:center">✕</div><div class="h" style="font-size:52px">{t}</div></div>' for t in items)+'</div>'
cover=hero_cover(baby(31,1080,800,.5,.36,1.0),'<div class="tags"><span class="tag t1">Tips</span><span class="tag t2">Kids Furniture</span></div>',"No spare room? Set up a small nursery","7 space-saving moves that stay safe.",f'<img src="{CZ}" style="width:280px;{SH}">',1,card=MINT,fg=NAVY,pill_bg=NAVY,pill_fg="#fff",pill="Swipe for the 7 moves",title_fs=72)+star(1000,40,30,"#fff")
s2=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="kick">GOOD NEWS FIRST</div><div class="h" style="font-size:84px;margin-top:8px">You don't need a nursery yet</div></div>
<div style="position:absolute;left:60px;right:60px;top:345px;height:440px;background:#fff;border-radius:44px;display:flex;flex-direction:column;align-items:center;justify-content:center"><div class="h" style="font-size:210px;line-height:1">6</div><div class="h" style="font-size:56px">months in your room</div></div>
<div class="b" style="position:absolute;left:70px;right:70px;top:830px;font-size:40px">Your baby should sleep in the same room as you for at least the first six months, day and night. So the first "nursery" is a safe sleep space by your bed.</div>
<div style="position:absolute;left:70px;right:70px;top:1150px;font-size:26px;font-weight:700;opacity:.6">{LT}</div>'''
s3=move(1,"Start with a bedside crib","It sits flush with your bed and takes little floor space. Look for the crib safety standard BS EN 1130:2019 on the label.",img(CZ,430),LT,("£189.00","Tutti Bambini Cozee Air 2, toasted oak"))
s4=move(2,"Or a mini cot, with its own mattress","Mini cots are smaller than standard cots, so buy the mattress size made for yours. It should fit with no gaps. Cots should meet BS EN 716.",img(MY,400),LT,("£209.00","Obaby Maya mini cot bed, slate/natural"))
s5=move(3,"Pick the right wall",'Keep the cot away from radiators, direct sunlight and blind cords. And away from the window.','<div style="display:flex;gap:46px">'+nolist(["Radiators","Sunlight","Blind cords"])+'</div>',"Source: The Lullaby Trust and RoSPA")
s6=move(4,"Skip the changing table","It saves floor space, and it's the safer choice: change your baby's nappy on a changing mat on the floor.",img(MT,450,"transform:rotate(-90deg)"),"Source: NHS",("£12.00","Mama Shack changing mat, linear leaf/sage"))
s7=move(5,"Fix tall furniture to the wall","Small rooms mean tall storage. Drawers and wardrobes that could be pulled over should be secured to the wall.",big("Fix it","to the wall, not just the floor"),RS)
s8=move(6,"Keep it 16 to 20°C","That's the range to aim for, day and night. A simple room thermometer near the cot takes the guesswork out of it.",big("16–20°C","room temperature"),LT)
s9=move(7,"Store around the cot, not in it","No baskets, toys or pillows inside. The safest cot for a baby is a clear cot.",big("Clear","cot, every sleep"),LT)
s10=hero_last(baby(16,1080,760,.5,.5,1.0),"Short on space? Compare crib prices first","See bedside crib and mini cot prices from UK shops in one place.","#fff",fg=NAVY)
pin=pin_hero(baby(24,1000,700,.5,.5),pin_tags("Tips","Kids Furniture"),"Small nursery? 7 space-saving moves",["Your room first: 6 months","Bedside crib or mini cot","Mattress that fits, no gaps","Away from radiators and blinds","Change nappies on the floor","Fix tall furniture to the wall","Keep it 16–20°C and clear"],CZ,300,MINT,NAVY,NAVY,"#fff","Source: The Lullaby Trust, the UK safer baby sleep charity, RoSPA, the UK accident prevention charity, and NHS.","Compare crib prices at babysorted.com",line="#fff",title_fs=56,photo_h=590)
render(ROOT+"/out/p1",[cover,s2,s3,s4,s5,s6,s7,s8,s9,s10],pin,CSS,NAVY)
