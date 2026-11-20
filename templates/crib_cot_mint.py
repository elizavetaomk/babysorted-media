# Mint "sign card" layout (20 Nov 2026): mint bg, white visual card with a navy tab, title + body below, source chip.
# Used for: #48 When to move baby from crib to cot. Facts: The Lullaby Trust, NHS; crib standard scope from BSI listing.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css(MINT,NAVY,NAVY,"#fff")+".t2{background:#fff;box-shadow:none}"
COT=b("cot.png",1000); CRIB=b("crib.png",1000); DATE="20 Nov 2026"
LT="Source: The Lullaby Trust, the UK safer baby sleep charity"
deco=star(40,36,24,"#fff")+star(1010,48,30,"#fff")
def card(tab,title,body,inner,src=None,kick=""):
    s=f'<div style="position:absolute;left:70px;right:70px;top:1088px;font-size:23px;font-weight:700;opacity:.7">{src}</div>' if src else ""
    return deco+f'''<div style="position:absolute;left:60px;right:60px;top:80px;height:500px;background:#fff;border-radius:44px;display:flex;align-items:center;justify-content:center;overflow:hidden">{inner}</div>
<div style="position:absolute;left:96px;top:56px;background:{NAVY};color:#fff;font-weight:800;font-size:28px;padding:12px 26px;border-radius:22px;letter-spacing:.04em">{tab}</div>
<div style="position:absolute;left:70px;right:70px;top:620px"><div class="kick">{kick}</div><div class="h" style="font-size:64px;margin-top:6px">{title}</div><div class="b" style="margin-top:14px;font-size:36px">{body}</div></div>{s}'''
def big(a,c): return f'<div style="text-align:center;padding:0 40px"><div class="h" style="font-size:132px;line-height:1">{a}</div><div class="h" style="font-size:40px;margin-top:16px">{c}</div></div>'
def rail(k):
    dots="".join(f'<div style="display:flex;align-items:center;gap:18px"><div class="h" style="width:116px;height:116px;border-radius:50%;background:{NAVY if i==k else MINT};color:{"#fff" if i==k else NAVY};font-size:60px;display:flex;align-items:center;justify-content:center">{i}</div><div class="h" style="font-size:50px;opacity:{1 if i==k else .35}">{t}</div></div>' for i,t in [(1,"Sits up alone"),(2,"Hands and knees"),(3,"Weight limit")])
    return f'<div style="display:flex;flex-direction:column;gap:30px">{dots}</div>'
cover=hero_cover(baby(35,1080,800,.5,.32,1.1),'<div class="tags"><span class="tag t1">Tips</span><span class="tag t2">Kids Furniture</span></div>',"Crib to cot: when to move up","Watch what your baby can do, not the calendar.",f'<img src="{COT}" style="width:280px;{SH}">',1,card=MINT,fg=NAVY,pill_bg=NAVY,pill_fg="#fff",title_fs=70)
s2=card("THE RULE","A bedside crib has a stage, not an age","Bedside cribs should meet BS EN 1130:2019. That standard covers babies until they can sit up unaided or push up onto their hands and knees.",
  f'<img src="{CRIB}" style="height:400px;{SH}">',LT+".",kick="START HERE")
s3=card("SIGN 1",'Your baby sits up on their own',"Once they can sit unaided, they've moved past what a bedside crib is made for. Time to move to the cot.",rail(1),kick="3 SIGNS IT'S TIME")
s4=card("SIGN 2","They push up onto hands and knees","Getting up on all fours, or pulling up on the sides, is the second sign. Don't wait for the third.",rail(2),kick="3 SIGNS IT'S TIME")
s5=card("SIGN 3","They reach the weight limit","Every crib has a weight limit in its instructions. Check yours today, and stop at the limit even if they still seem to fit.",rail(3),kick="3 SIGNS IT'S TIME")
s6=card("KEEP THIS","New cot, same room",'Moving to a cot doesn\'t mean moving out. The safest place for your baby to sleep is in the same room as you for the first 6 months, day and night.',big("6 months","same room, naps too"),LT+".",kick="DON'T MISS")
cotp=f'''<div style="display:flex;align-items:center;gap:34px"><img src="{COT}" style="width:470px;{SH}"><div><div class="h" style="font-size:60px">£199.00</div><div style="font-size:22px;font-weight:600;opacity:.7;line-height:1.3;margin-top:6px">Tutti Bambini Modena<br>3 in 1 Cot Bed, white/oak<br>Price on BabySorted, {DATE}</div></div></div>'''
s7=card("BUYING","Check two labels","Cot: BS EN 716-1:2017. Mattress: BS EN 16890. It should fit with no gaps, and your baby's head should sink no more than a few millimetres.",cotp,LT+".",kick="BEFORE THE FIRST NIGHT")
s8=card("SET UP","Clear cot, feet to foot","No bumpers, pillows, duvets or soft toys. Feet right at the bottom of the cot. Tuck blankets in firmly, no higher than the shoulders.",big("Clear","nothing but a fitted sheet"),"Sources: The Lullaby Trust, the UK safer baby sleep charity; NHS.",kick="BEFORE THE FIRST NIGHT")
s9=card("NEXT","Lower the base in time","Cot makers say: move the base to its lowest level before your baby can pull up to stand. Pick vertical bars: horizontal ones can work like a ladder.",big("Lowest","before they stand"),kick="DON'T FORGET")
s10=hero_last(baby(24,1080,700,.5,.45),"Ready for the cot? Compare prices first","Compare cot and cot bed prices from UK shops in one place.",PINK,fg=NAVY,photo_h=700)
pin=pin_hero(baby(32,1000,680,.5,.12),pin_tags("Tips","Kids Furniture"),"Crib to cot: when to move up",
 ["Sits up alone? Time for the cot","On hands and knees? Move up","Check the crib's weight limit","Same room for the first 6 months","Cot to BS EN 716, no mattress gaps","Clear cot, feet to foot"],
 COT,200,MINT,NAVY,NAVY,"#fff",LT+".","Compare cot prices at babysorted.com",line="#fff",photo_h=680,title_fs=56)
render(ROOT+"/out/a",[cover,s2,s3,s4,s5,s6,s7,s8,s9,s10],pin,CSS,NAVY)
