# Deeper-pink (rose) "pick your changer" buying guide for changing units and dressers (17 Nov 2026).
# Rose bg, navy text, white product cards. Wood/beige products suit rose. Safety line sourced to RoSPA.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css(ROSE,NAVY,NAVY,"#fff")+".t2{background:#fff;box-shadow:none}"
DATE="13 Nov 2026"
deco=star(36,30,26,"#fff")+star(1000,36,30,"#fff")
CT=b("cottop.png",1000); CU=b("changeunit.png",1000); DR=b("dresserchg.png",1000); RA=b("rattan.png",1000)
RS="Source: RoSPA, the UK accident prevention charity"
def card(inner,price=None):
    pr=f'<div style="position:absolute;right:34px;bottom:28px;text-align:right"><div class="h" style="font-size:44px">{price[0]}</div><div style="font-size:21px;font-weight:600;opacity:.7;line-height:1.3">{price[1]}<br>Price on BabySorted, {DATE}</div></div>' if price else ""
    return f'<div style="position:absolute;left:60px;right:60px;top:60px;height:610px;background:#fff;border-radius:44px;overflow:hidden"><div style="position:absolute;inset:40px;display:flex;align-items:center;justify-content:center">{inner}</div>{pr}</div>'
def typ(k,kind,title,body,inner,price):
    return deco+card(inner,price)+f'''<div style="position:absolute;left:92px;top:92px"><span style="background:{NAVY};color:#fff;font-weight:800;font-size:28px;padding:10px 22px;border-radius:20px">TYPE {k} OF 4</span></div>
<div style="position:absolute;left:70px;right:70px;top:712px"><div class="kick">{kind}</div><div class="h" style="font-size:66px;margin-top:8px">{title}</div><div class="b" style="margin-top:14px;font-size:38px">{body}</div></div>'''
img=lambda s,h: f'<img src="{s}" style="height:{h}px;max-width:820px;object-fit:contain;{SH}">'
def big(a,c):return f'<div style="text-align:center"><div class="h" style="font-size:150px;line-height:1">{a}</div><div class="h" style="font-size:44px;margin-top:8px">{c}</div></div>'
cover=hero_cover(baby(33,1080,800,.5,.42,1.0),'<div class="tags"><span class="tag t1">Buying guide</span><span class="tag t2">Kids Furniture</span></div>',"Best changing units and dressers","Change, store and reuse it later.",f'<img src="{DR}" style="height:270px;{SH}">',1,card=ROSE,fg=NAVY,pill_bg=NAVY,pill_fg="#fff",pill="Swipe before you buy",title_fs=66)
s2=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="kick">BUY ONCE</div><div class="h" style="font-size:84px;margin-top:8px">The one you'll still use in 3 years</div></div>
<div style="position:absolute;left:60px;right:60px;top:355px;background:#fff;border-radius:44px;padding:44px 48px">
<div class="b" style="font-size:41px">A dresser-changer is the smart buy. Take the changing top off later and it's a normal chest of drawers your child keeps for years.</div>
<div style="margin-top:28px;display:flex;gap:18px;align-items:center"><div class="h" style="font-size:90px">3-in-1</div><div style="font-size:34px;font-weight:600;line-height:1.3">changer now, drawers later,<br>bedroom storage for good</div></div></div>
<div class="b" style="position:absolute;left:70px;right:70px;top:1030px;font-size:38px">Here are the 4 types, cheapest first.</div>'''
s3=typ(1,"SMALLEST AND CHEAPEST","Cot-top changer","It sits across the top of your cot, so it takes no extra floor space. Check it fits your cot's width and locks on firmly. Great for a small room.",img(CT,330),("£34.95","Puggle Universal Cot Top Changer, white"))
s4=typ(2,"OPEN SHELVES","Open changing unit","Shelves keep nappies and wipes within arm's reach, so you never step away. Lighter and cheaper than a dresser, but less hidden storage.",img(CU,440),("£119.00","Obaby Stamford Open Changing Unit, warm grey"))
s5=typ(3,"THE LONG GAME","Dresser changer","Drawers below, changing top above. Costs more, but take the top off later and it's a chest of drawers for the bedroom. Best value over time.",img(DR,450),("£279.00","Mamas & Papas Atlas Dresser Changer, light oak"))
s6=typ(4,"THE STYLE PICK","Open rattan table","Pretty and airy, with baskets for storage. Check the baskets slide out easily and nothing loose sits where baby can reach. Style costs a little more.",img(RA,470),("£224.10","CuddleCo Aria Rattan Changing Table, natural"))
s7=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="kick">BEFORE YOU CHOOSE</div><div class="h" style="font-size:80px;margin-top:8px">3 things that matter more than the look</div></div>
<div style="position:absolute;left:60px;right:60px;top:355px;display:flex;flex-direction:column;gap:22px">
<div style="background:#fff;border-radius:34px;padding:34px 40px"><div class="h" style="font-size:46px">Match it to your height</div><div class="b" style="font-size:34px;margin-top:8px">A top at your hip height saves your back on every change.</div></div>
<div style="background:#fff;border-radius:34px;padding:34px 40px"><div class="h" style="font-size:46px">Raised edges on all sides</div><div class="b" style="font-size:34px;margin-top:8px">A lip around the top helps, but it's never a substitute for your hands.</div></div>
<div style="background:{NAVY};color:#fff;border-radius:34px;padding:34px 40px"><div class="h" style="font-size:46px">Storage within arm's reach</div><div class="b" style="font-size:34px;margin-top:8px">So everything you need is there and you never leave your baby.</div></div></div>'''
s8=deco+f'''<div style="position:absolute;left:70px;right:70px;top:90px"><div class="kick">THE SAFETY RULE</div><div class="h" style="font-size:80px;margin-top:8px">Never leave your baby on a raised unit</div></div>
<div style="position:absolute;left:60px;right:60px;top:380px;background:#fff;border-radius:44px;padding:50px 50px;text-align:center">{big("0","seconds alone, up high")}</div>
<div class="b" style="position:absolute;left:70px;right:70px;top:800px;font-size:40px">Have everything in reach before you start. Need to turn away? Take your baby with you, or change them on a mat on the floor, where they can't fall.</div>
<div style="position:absolute;left:70px;right:70px;top:1150px;font-size:26px;font-weight:700;opacity:.6">Source: RoSPA, the UK accident prevention charity, and NHS</div>'''
s9=hero_last(baby(36,1080,760,.5,.45,1.0),"Setting up the nursery? Compare changing unit prices first","See changing unit and dresser prices from UK shops in one place.",NAVY,fg=NAVY)
pin=pin_hero(baby(35,1000,680,.5,.42),pin_tags("Buying guide","Kids Furniture"),"Changing units: which type to buy",["Cot-top changer: smallest, cheapest","Open unit: shelves within reach","Dresser changer: best value over time","Rattan table: the style pick","Match the height to save your back","Never leave baby alone up high"],DR,290,ROSE,NAVY,NAVY,"#fff","Safety: RoSPA, the UK accident prevention charity, and NHS.","Compare changing unit prices at babysorted.com",line="#fff",photo_h=680,title_fs=56)
render(ROOT+"/out/p5",[cover,s2,s3,s4,s5,s6,s7,s8,s9],pin,CSS,NAVY)
