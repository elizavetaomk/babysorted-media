# Mint "turn the seat" layout: mint bg, white circle with a turning arc around the product, three stat chips in a row; weight bars; checks.
# Used for: Best rotating car seats for easy lifting (Nov 2026). Beige/taupe seats on mint.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from slide_lib import *
MO=b("motion.png"); SI=b("sirona.png"); PE=b("pebble.png"); SP_=b("spinkid.png")
CSS=css(MINT,NAVY,NAVY,"#fff")+".t2{background:#fff}"
deco=star(36,30,26,"#fff")+star(1000,36,30,"#fff")
SH="filter:drop-shadow(0 16px 16px rgba(5,31,69,.18))"
im=lambda s,h,x="": f'<img src="{s}" style="height:{h}px;max-width:100%;object-fit:contain;{SH};{x}">'
def arc(deg,size):
    # circular arrow: deg=360 near-full ring, deg=180 half ring
    import math
    r=size/2-14; c=size/2
    a0=math.radians(-60); a1=a0+math.radians(deg-28 if deg==360 else deg)
    x0,y0=c+r*math.cos(a0),c+r*math.sin(a0); x1,y1=c+r*math.cos(a1),c+r*math.sin(a1)
    large=1 if deg>180 else 0
    t=a1+math.pi/2; L=34
    p1=(x1-L*math.cos(t-0.55),y1-L*math.sin(t-0.55)); p2=(x1-L*math.cos(t+0.55),y1-L*math.sin(t+0.55))
    return f'<svg style="position:absolute;left:0;top:0" width="{size}" height="{size}" viewBox="0 0 {size} {size}"><path d="M{x0:.1f} {y0:.1f} A{r} {r} 0 {large} 1 {x1:.1f} {y1:.1f}" fill="none" stroke="{NAVY}" stroke-width="9" stroke-linecap="round"/><path d="M{p1[0]:.1f} {p1[1]:.1f} L{x1:.1f} {y1:.1f} L{p2[0]:.1f} {p2[1]:.1f}" fill="none" stroke="{NAVY}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def ring(pic,h,deg,size=600,x=""):
    return f'<div style="position:relative;width:{size}px;height:{size}px;background:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center">{im(pic,h,x)}{arc(deg,size)}</div>'
cover=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="tags"><span class="tag t1">Buying guide</span><span class="tag t2">Car Seats</span></div>
<div class="h" style="font-size:98px;margin-top:26px">Best rotating car seats for easy lifting</div>
<div style="font-size:39px;font-weight:600;opacity:.75;margin-top:16px;white-space:nowrap">Save your back. Turn the seat, not the baby.</div></div>
<div style="position:absolute;left:180px;top:510px">{ring(MO,600,360,720)}</div>
<div style="position:absolute;right:50px;top:1160px;background:{NAVY};color:#fff;font-weight:700;font-size:30px;padding:14px 28px;border-radius:40px">Swipe before you buy</div>'''
def kind(deg,t,c,pic):
    return f'''<div style="flex:1;background:#fff;border-radius:38px;padding:34px 34px 30px"><div style="position:relative;width:250px;height:250px;margin:0 auto">{arc(deg,250)}<div class="h" style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:66px">{deg}°</div></div>
<div class="h" style="font-size:47px;margin-top:22px">{t}</div><div class="b" style="font-size:35px;margin-top:12px">{c}</div></div>'''
s2=deco+f'''<div style="position:absolute;left:70px;right:70px;top:70px"><div class="kick">FIRST, THE BASICS</div><div class="h" style="font-size:84px;margin-top:8px">360 and 180 aren't the same</div></div>
<div style="position:absolute;left:60px;right:60px;top:340px;display:flex;gap:22px">{kind(360,"Full turn","Turns to the door, and also lets you pick rear or forward-facing without refitting.",0)}{kind(180,"Half turn","Mainly turns to the door to make strapping in easier.",0)}</div>
<div style="position:absolute;left:70px;right:70px;top:960px;font-size:35px;font-weight:600;opacity:.8;line-height:1.35">Which? says most swivel seats cost about £200 to £400, and most weigh over 10 kg.</div>'''
def pick(k,name,best,pic,h,deg,chips,good,watch):
    ch="".join(f'<div style="flex:1;background:#fff;border-radius:22px;padding:13px 18px"><div style="font-weight:800;font-size:20px;letter-spacing:.05em;opacity:.6">{a}</div><div class="h" style="font-size:33px;margin-top:4px;white-space:nowrap">{c}</div></div>' for a,c in chips)
    return deco+f'''<div style="position:absolute;left:50%;top:48px;transform:translateX(-50%)">{ring(pic,h,deg,540)}</div>
<div style="position:absolute;left:60px;top:66px;font-weight:800;font-size:26px;background:{NAVY};color:#fff;padding:7px 16px;border-radius:18px">{k} of 4</div>
<div style="position:absolute;left:60px;right:60px;top:606px"><div class="h" style="font-size:66px">{name}</div>
<div style="margin-top:12px"><span class="pill" style="background:{NAVY};color:#fff;font-size:28px">{best}</span></div>
<div style="display:flex;gap:12px;margin-top:18px">{ch}</div>
<div class="b" style="font-size:36px;margin-top:20px">{good}</div><div class="b" style="font-size:36px;margin-top:10px"><b style="font-weight:800">Watch out:</b> {watch}</div></div>'''
s3=pick(1,"Silver Cross Motion 3","Best one-seat-for-years",MO,440,360,[("SIZE","40 to 145 cm"),("SEAT WEIGHT","14.4 kg"),("PRICE","£275")],"One seat from birth to about 12 years. Rear-facing up to 105 cm or 18 kg.","it stays in the car, so you can't lift it out with baby in it. A Mumsnet reviewer lost front legroom in a small car.")
s4=pick(2,"Maxi-Cosi Pebble 360 Pro²","Best to lift out",PE,340,360,[("SIZE","40 to 87 cm"),("TURN","On the base"),("WITH BASE","£399.95")],"Lift the carrier out, baby and all. On the FamilyFix 360 Pro base it turns and slides towards you.","the base is sold separately, and it's outgrown by about 18 months. It's for travel, not long sleeps.")
s5=pick(3,"Cybex Sirona G3","Best if you swap cars",SI,450,360,[("SIZE","61 to 105 cm"),("SEAT ONLY","6 kg"),("WITH BASE","£324.90")],"Clips off its base, so the seat alone moves between cars. With the base it's 13 kg.","starts at 61 cm, about 3 months. Budget for a baby seat first, and buy the base separately.")
s6=pick(4,"Axkid Spinkid 2","Best for rear-facing fans",SP_,360,180,[("SIZE","40 to 105 cm"),("SEAT WEIGHT","15 kg"),("PRICE","£224")],"A 180° turn to the door. Listed as rear-facing, so nothing to turn round too early.","it's heavy, so treat it as a one-car seat. Check the fit list for your car.")
BW=[("Sirona G3, seat only",6),("Sirona G3 with base",13),("Motion 3",14.4),("Spinkid 2",15)]
bw="".join(f'''<div style="margin-top:34px"><div style="display:flex;justify-content:space-between;font-weight:800;font-size:36px"><div>{a}</div><div>{v} kg</div></div><div style="height:34px;background:{MINT};border-radius:17px;margin-top:10px"><div style="height:34px;width:{v/15*100:.0f}%;background:{NAVY};border-radius:17px"></div></div></div>''' for a,v in BW)
s7=deco+f'''<div style="position:absolute;left:70px;right:70px;top:70px"><div class="kick">THE TRADE-OFF</div><div class="h" style="font-size:84px;margin-top:8px">Easy on your back, heavy to move</div></div>
<div style="position:absolute;left:60px;right:60px;top:340px;background:#fff;border-radius:40px;padding:14px 44px 40px">{bw}</div>
<div class="b" style="position:absolute;left:70px;right:70px;top:960px">Two cars in the family? Weigh this up first. A 15 kg seat is not one you'll want to move every week.</div>'''
CK=[("Does it stop you turning too early?","Which? marks down seats with no way to stop early forward-facing."),("Does it turn on the base?","Some must be unclipped from the base to go forward-facing. Try it in the shop."),("Does it fit your car?","Most bases use ISOFIX. Check the seat's car fit list, and sit in the front with it fitted.")]
ck="".join(f'''<div style="display:flex;gap:24px;padding:46px 0;border-top:{"0" if i==0 else f"3px solid {MINT}"}"><div style="flex:none;width:60px;height:60px;border-radius:18px;background:{NAVY};color:#fff;font-weight:800;font-size:32px;display:flex;align-items:center;justify-content:center">{i+1}</div><div><div class="h" style="font-size:47px">{a}</div><div style="font-size:37px;font-weight:500;line-height:1.32;margin-top:10px">{c}</div></div></div>''' for i,(a,c) in enumerate(CK))
s8=deco+f'''<div style="position:absolute;left:70px;right:70px;top:70px"><div class="kick">IN THE SHOP</div><div class="h" style="font-size:80px;margin-top:8px">Ask these 3 things</div></div>
<div style="position:absolute;left:60px;right:60px;top:230px;background:#fff;border-radius:40px;padding:18px 44px 22px">{ck}</div>'''
US=[("Lock it before you drive","Turning is only for getting in and out. Cybex's Sirona T manual says check the seat is locked and the indicator is green."),("Stay rear-facing longer","On height-based i-Size seats the law says rear-facing until over 15 months. Which? recommends longer, ideally until about 4."),("Fit still matters most","A seat is only safe if it's fitted right. Follow your seat's own manual.")]
us="".join(f'''<div style="padding:40px 0;border-top:{"0" if i==0 else f"3px solid {MINT}"}"><div class="h" style="font-size:47px">{a}</div><div style="font-size:36px;font-weight:500;line-height:1.33;margin-top:10px">{c}</div></div>''' for i,(a,c) in enumerate(US))
s9=deco+f'''<div style="position:absolute;left:70px;right:70px;top:70px"><div class="kick">EVERY JOURNEY</div><div class="h" style="font-size:80px;margin-top:8px">Before you pull away</div></div>
<div style="position:absolute;left:60px;right:60px;top:230px;background:#fff;border-radius:40px;padding:14px 44px 24px">{us}</div>'''
s10=deco+f'''<div style="position:absolute;left:60px;right:60px;top:60px;height:560px;background:#fff;border-radius:44px;display:flex;align-items:center;justify-content:center;gap:10px;padding:30px">{im(SP_,330,"flex:none")}{im(MO,450,"flex:none")}</div>
<div style="position:absolute;left:70px;right:70px;top:660px"><div class="h" style="font-size:80px">Found your seat? Compare prices first</div>
<div class="b" style="margin-top:18px;font-size:38px">Compare car seat prices from UK shops in one place.</div>
<div style="margin-top:30px;display:flex;align-items:center;gap:16px"><div class="h" style="font-size:46px;background:#fff;padding:22px 32px;border-radius:24px">babysorted.com/links</div>
<div style="background:{NAVY};color:#fff;font-weight:800;font-size:32px;padding:22px 26px;border-radius:24px;white-space:nowrap">Link in bio ↑</div></div>
<div style="margin-top:22px;font-size:32px;font-weight:700;opacity:.55">Save this post for later</div></div>'''
PN=[(MO,"Silver Cross Motion 3","One seat for years. 360°, 40 to 145 cm.","£275"),(PE,"Maxi-Cosi Pebble 360 Pro²","Lift out with baby. With base.","£399.95"),(SI,"Cybex Sirona G3","Seat only 6 kg. With base.","£324.90"),(SP_,"Axkid Spinkid 2","180° turn. Rear-facing, 40 to 105 cm.","£224")]
pn="".join(f'''<div style="display:flex;align-items:center;gap:20px;background:#fff;border-radius:28px;padding:12px 26px 12px 14px;margin-top:14px"><div style="flex:none;width:170px;height:150px;display:flex;align-items:center;justify-content:center"><img src="{s}" style="max-width:164px;max-height:146px"></div><div style="flex:1"><div class="h" style="font-size:36px">{a}</div><div style="font-size:26px;font-weight:600;opacity:.75;margin-top:6px;line-height:1.25">{c}</div></div><div class="h" style="font-size:36px;white-space:nowrap">{e}</div></div>''' for s,a,c,e in PN)
pin=f'''{star(910,50,32,"#fff")}<div style="position:absolute;left:60px;right:60px;top:60px"><div class="tags"><span class="tag t1" style="font-size:24px">Buying guide</span><span class="tag t2" style="font-size:24px">Car Seats</span></div>
<div class="h" style="font-size:80px;margin-top:20px">Best rotating car seats for easy lifting</div>
<div style="font-size:31px;font-weight:600;opacity:.75;margin-top:12px">Save your back. Turn the seat, not the baby.</div></div>
<div style="position:absolute;left:60px;right:60px;top:368px">{pn}</div>
<div style="position:absolute;left:60px;right:60px;top:1136px;background:{NAVY};color:#fff;border-radius:26px;padding:22px 28px"><div style="font-weight:800;font-size:22px;opacity:.7;letter-spacing:.06em">3 CHECKS BEFORE YOU BUY</div><div style="font-size:28px;font-weight:600;margin-top:4px;line-height:1.3">Does it stop early forward-facing? Does it turn without unclipping? Does it fit your car? Most swivel seats weigh over 10 kg.</div></div>
<div style="position:absolute;left:60px;right:60px;top:1336px;font-size:23px;font-weight:600;opacity:.65">Prices from the BabySorted catalog on 4 Nov. Prices can change.</div>
<div style="position:absolute;left:60px;right:60px;bottom:40px;display:flex;justify-content:space-between;align-items:center"><div class="brand" style="font-size:34px">BabySorted</div><div style="font-weight:700;font-size:25px">Compare car seat prices at babysorted.com</div></div>'''
render(ROOT+"/out/p4",[cover,s2,s3,s4,s5,s6,s7,s8,s9,s10],pin,CSS,NAVY)
