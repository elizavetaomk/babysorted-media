# Pink "two layouts" buying guide for double pushchairs (16 Nov 2026).
# Pink bg, navy text, white product stage cards. No invented widths; numbers only where read from catalog (prices) or a source.
# Facts: pushchair makers (no brand), general buying advice. Products shown as products (real catalog names + prices).
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css(PINK,NAVY,NAVY,"#fff")+".t2{background:#fff;box-shadow:none}"
DATE="13 Nov 2026"
deco=star(36,30,26,"#fff")+star(1000,36,30,"#fff")
AI=b("aire.png",1000); DO=b("donkey.png",1000); PE=b("peach.png",1000)
def stage(inner,price=None,bg="#fff"):
    pr=f'<div style="position:absolute;right:34px;bottom:28px;text-align:right"><div class="h" style="font-size:44px">{price[0]}</div><div style="font-size:21px;font-weight:600;opacity:.7;line-height:1.3">{price[1]}<br>Price on BabySorted, {DATE}</div></div>' if price else ""
    return f'<div style="position:absolute;left:60px;right:60px;top:60px;height:610px;background:{bg};border-radius:44px;overflow:hidden"><div style="position:absolute;inset:40px;display:flex;align-items:center;justify-content:center">{inner}</div>{pr}</div>'
def slide(kick,title,body,inner,price=None,src="",bg="#fff"):
    s=f'<div style="font-size:26px;font-weight:700;opacity:.6;margin-top:14px">{src}</div>' if src else ""
    return deco+stage(inner,price,bg)+f'''<div style="position:absolute;left:70px;right:70px;top:712px"><div class="kick">{kick}</div><div class="h" style="font-size:68px;margin-top:8px">{title}</div><div class="b" style="margin-top:14px;font-size:38px">{body}</div>{s}</div>'''
img=lambda s,h: f'<img src="{s}" style="height:{h}px;max-width:860px;object-fit:contain;{SH}">'
def big(a,c):return f'<div style="text-align:center"><div class="h" style="font-size:150px;line-height:1">{a}</div><div class="h" style="font-size:46px;margin-top:8px">{c}</div></div>'
cover=hero_cover(baby(48,1080,800,.5,.45,1.0),'<div class="tags"><span class="tag t1">Buying guide</span><span class="tag t2">Pushchairs</span></div>',"Best double pushchairs for twins and siblings","Two babies, one door frame. Width is everything.",f'<img src="{DO}" style="width:300px;{SH}">',1,card=PINK,fg=NAVY,pill_bg=NAVY,pill_fg="#fff",pill="Swipe before you buy",title_fs=62)
s2=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="kick">START HERE</div><div class="h" style="font-size:80px;margin-top:8px">Two shapes. Pick the shape first.</div></div>
<div style="position:absolute;left:60px;right:60px;top:330px;display:flex;flex-direction:column;gap:26px">
<div style="background:#fff;border-radius:36px;padding:38px 44px"><div class="h" style="font-size:54px">Side by side</div><div class="b" style="font-size:36px;margin-top:10px">Both seats in a row. Easy to see both babies and often from birth for twins. But wider, so it may not fit narrow doors or lifts.</div></div>
<div style="background:{NAVY};color:#fff;border-radius:36px;padding:38px 44px"><div class="h" style="font-size:54px">Tandem (inline)</div><div class="b" style="font-size:36px;margin-top:10px">One seat behind or above the other. Usually narrower, so it suits narrow doors. But longer, and reaching the back seat can be fiddly.</div></div></div>'''
s3=slide("THE TAPE MEASURE WINS","Measure before you fall in love","Side-by-side doubles vary a lot in width. Measure your front door, your lift and your car boot first, then only look at ones that fit. A pushchair that won't go through the door is no bargain.",big("3","things to measure: door, lift, boot"),bg=MINT)
s4=slide("NEWBORN + TODDLER","Can it take a carrycot or car seat?","For a baby and an older sibling, check one seat takes a carrycot or infant car seat from birth, while the other holds a toddler. Not every double does both.",img(PE,440),("From £1,839.00","iCandy Peach 8 twin, inline"))
s5=slide("TWO NEWBORNS","From birth for both seats","For twins, both seats (or carrycots) must be suitable from birth. Makers set this per model, so check the box, not the brand.",img(DO,440),("£1,436.50","Bugaboo Donkey 6 twin, fern green"))
s6=slide("THE DAILY LIFT","Weight you can actually carry","Doubles are heavy. If you'll lift it into a boot or up steps alone, check the weight and whether it folds in one piece. A lighter twin buggy can be the one you'll really use.",img(AI,420),("£125.00","Joie Aire Twin, shale"))
s7=slide("NAP TIME","Can one lie back while one sits up?","Look for seats that recline on their own. Then one baby can nap while the other looks out.",big("2","seats, 2 separate reclines"),bg=MINT)
s8=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="kick">WHAT YOU'LL PAY</div><div class="h" style="font-size:80px;margin-top:8px">Doubles cost from about £115 to over £2,000</div></div>
<div style="position:absolute;left:60px;right:60px;top:420px;background:#fff;border-radius:40px;padding:44px 48px">
<div class="b" style="font-size:40px">A simple side-by-side twin buggy starts around <b>£115</b>. A premium convertible or inline travel system can pass <b>£2,000</b> once you add two carrycots and car seats.</div>
<div style="margin-top:28px;font-size:34px;font-weight:600;opacity:.8">Shops often price the same model differently. Compare before you pay.</div></div>
<div style="position:absolute;left:70px;right:70px;top:1150px;font-size:25px;font-weight:600;opacity:.6">Prices on BabySorted, {DATE}. Checked across the whole catalogue, not a few models.</div>'''
s9=hero_last(baby(47,1080,760,.5,.45,1.0),"Two seats, one budget? Compare prices first","See double pushchair prices from UK shops in one place.",NAVY,fg=NAVY)
pin=pin_hero(baby(46,1000,680,.5,.4),pin_tags("Buying guide","Pushchairs"),"Double pushchairs: how to choose",["Pick the shape: side-by-side or inline","Measure door, lift and boot first","Check it works from birth for twins","Newborn + toddler? One carrycot, one seat","Weigh it: can you lift it alone?"],DO,300,PINK,NAVY,NAVY,"#fff","From about £115 to over £2,000. Prices on BabySorted, 13 Nov 2026.","Compare double pushchair prices at babysorted.com",line="#fff",photo_h=680,title_fs=56)
render(ROOT+"/out/p3",[cover,s2,s3,s4,s5,s6,s7,s8,s9],pin,CSS,NAVY)
