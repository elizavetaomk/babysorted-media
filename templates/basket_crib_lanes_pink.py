# Pink "two lanes" layout (24 Nov 2026): pink bg, two white lanes side by side (Moses basket | bedside crib),
# each lane with a navy verdict chip, then a navy title + body below. Used for: #53 Moses basket or bedside crib.
# Facts: The Lullaby Trust product guide (mattress, British Standards label check, room-sharing day and night), NHS (same room 6 months),
# BSI catalogue (BS EN 1466 carry cots and stands; BS EN 1130 cribs). Maker instructions for stands and crib straps ("makers say").
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css(PINK,NAVY,NAVY,"#fff")+".t2{background:#fff;box-shadow:none}"
MO=b("moses.png",900); CR=b("crib.png",900); DATE="22 Nov 2026"
LT="Source: The Lullaby Trust, the UK safer baby sleep charity"
deco=star(46,40,24,"#fff")+star(1000,60,30,"#fff",.9)
def lane(img,h,label,chip):
    return f'''<div style="flex:1;background:#fff;border-radius:40px;position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:70px 24px 30px">
<div style="position:absolute;left:28px;top:26px;font-weight:800;font-size:26px;letter-spacing:.05em;opacity:.6">{label}</div>
{f'<img src="{img}" style="max-height:{h}px;max-width:92%;object-fit:contain;{SH}">' if img else ''}
<div class="h" style="margin-top:22px;background:{NAVY};color:#fff;font-size:30px;padding:12px 22px;border-radius:20px;text-align:center;line-height:1.15">{chip}</div></div>'''
def slide(kick,title,body,a,c,src=None,h=260,ia=MO,ic=CR):
    s=f'<div style="position:absolute;left:70px;right:70px;top:1170px;font-size:23px;font-weight:700;opacity:.75">{src}</div>' if src else ""
    return deco+f'''<div style="position:absolute;left:50px;right:50px;top:90px;height:600px;display:flex;gap:24px">{lane(ia,h,"MOSES BASKET",a)}{lane(ic,int(h*1.3),"BEDSIDE CRIB",c)}</div>
<div style="position:absolute;left:70px;right:70px;top:740px"><div class="kick">{kick}</div><div class="h" style="font-size:62px;margin-top:6px">{title}</div><div class="b" style="margin-top:14px;font-size:35px">{body}</div></div>{s}'''
def price(img,h,p,name):
    return f'<div style="text-align:center"><img src="{img}" style="max-height:{h}px;max-width:100%;object-fit:contain;{SH}"><div class="h" style="font-size:54px;margin-top:10px">{p}</div><div style="font-size:21px;font-weight:600;opacity:.7;line-height:1.25">{name}</div></div>'
cover=hero_cover(baby(38,1080,800,.5,.42,1.05),'<div class="tags"><span class="tag t1">Buying guide</span><span class="tag t2" style="box-shadow:inset 0 0 0 3px #051F45">Kids Furniture</span></div>',"Moses basket or bedside crib?","Same job, very different nights.",f'<img src="{MO}" style="width:290px;{SH}">',1,card=PINK,fg=NAVY,title_fs=72)
s2=deco+f'''<div style="position:absolute;left:50px;right:50px;top:90px;height:640px;display:flex;gap:24px">
<div style="flex:1;background:#fff;border-radius:40px;display:flex;align-items:center;justify-content:center;padding:30px">{price(MO,250,"£125.00","Little Green Sheep Organic Knitted<br>Moses Basket &amp; Mattress, Juniper")}</div>
<div style="flex:1;background:#fff;border-radius:40px;display:flex;align-items:center;justify-content:center;padding:30px">{price(CR,320,"£145.00","Silver Cross Lunar<br>Bedside Crib, Oatmeal")}</div></div>
<div style="position:absolute;left:70px;right:70px;top:770px"><div class="kick">THE SHORT ANSWER</div><div class="h" style="font-size:62px;margin-top:6px">Light and portable, or fixed and longer-lasting</div><div class="b" style="margin-top:14px;font-size:35px">A basket moves with you. A crib stays by your bed.</div></div>
<div style="position:absolute;left:70px;right:70px;top:1180px;font-size:22px;font-weight:700;opacity:.75">Prices on BabySorted, {DATE}.</div>'''
s3=slide("1 · HOW LONG IT LASTS","Check the limit before you buy","Basket: stop at the limit in its instructions, often within months. Crib: until your baby can sit up alone or push up onto hands and knees.","Shorter","Longer")
s4=slide("2 · DAY NAPS","Naps count too","Babies should sleep in the same room as you, day and night, for the first 6 months. A basket you can carry makes daytime naps near you easy.","Room to room","Stays in the bedroom","Sources: The Lullaby Trust, the UK safer baby sleep charity; NHS.")
s5=slide("3 · NIGHT FEEDS","Reach without getting up","A bedside crib sits level with your bed, so you can see and reach your baby at 3am. A basket on a stand is lower and a step away.","A step away","Within reach")
s6=slide("4 · SET UP","Where it stands matters","Basket makers say: use it on the floor or on the stand made for it, never on a bed, sofa or table. Crib makers say: fix the straps tight, with no gap to your bed.","Floor or its stand","Strapped, no gap")
mat=f'''<div style="text-align:center;padding:0 30px"><div class="h" style="font-size:118px;line-height:1">Firm, flat</div><div class="h" style="font-size:44px;margin-top:14px">waterproof, fits with no gaps</div><div style="font-size:30px;font-weight:600;margin-top:12px;opacity:.75">head sinks no more than a few mm</div></div>'''
s7=deco+f'''<div style="position:absolute;left:50px;right:50px;top:90px;height:600px;background:#fff;border-radius:40px;display:flex;align-items:center;justify-content:center">{mat}</div>
<div style="position:absolute;left:70px;right:70px;top:740px"><div class="kick">5 · BOTH NEED THIS</div><div class="h" style="font-size:62px;margin-top:6px">The mattress rule is the same</div><div class="b" style="margin-top:14px;font-size:35px">Use the mattress made for it. No extra padding, pillows or bumpers, even if it looks hard.</div></div>
<div style="position:absolute;left:70px;right:70px;top:1170px;font-size:23px;font-weight:700;opacity:.75">{LT}.</div>'''
lab=lambda a: f'<div class="h" style="font-size:64px;line-height:1;text-align:center">{a}</div>'
s8=slide("6 · CHECK THE LABEL","Look for the British Standard","It should be on the product, box, instructions or shop page. No standard listed? Ask before you buy.",'BS EN 1466<br><span style="font-size:22px;font-weight:600">carry cots and stands</span>','BS EN 1130<br><span style="font-size:22px;font-weight:600">cribs</span>',LT+".",h=220)
s9=hero_last(baby(24,1080,720,.5,.5),"Basket or crib? Compare prices first","Compare Moses basket and bedside crib prices from UK shops in one place.","#fff",fg=NAVY,photo_h=720)
pin=pin_hero(baby(39,1000,660,.5,.22,1.6),pin_tags("Buying guide","Kids Furniture"),"Moses basket or bedside crib?",
 ["Basket: light, moves room to room","Crib: level with your bed, lasts longer","Check the limit in the instructions","Same room for naps too, 6 months","Firm, flat mattress, no gaps","Basket on the floor or its own stand"],
 MO,170,PINK,NAVY,NAVY,"#fff","Sources: The Lullaby Trust, the UK safer baby sleep charity; NHS.","Compare crib prices at babysorted.com",line="#fff",photo_h=660,title_fs=56)
render(ROOT+"/out/a",[cover,s2,s3,s4,s5,s6,s7,s8,s9],pin,CSS,NAVY)
