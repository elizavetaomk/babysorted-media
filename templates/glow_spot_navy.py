# Navy "glow spot" layout (27 Nov 2026): navy bg like a dark nursery, product on a soft pink radial glow at the top,
# small pink kicker pill, white text below. Used for: #63 Night lights that help at 3am. No prices.
# Buying advice is ours (no label). Labelled facts: NHS "Helping your baby to sleep" (night different from day; lights down
# low, voice quiet, don't play at night); GOV.UK OPSS button battery leaflet (night lights listed; if the battery compartment
# isn't secured by a screw, move out of reach); The Lullaby Trust baby monitors page (keep the unit out of reach; higher risk
# of accidents with wires with an active baby) and "Dress your baby for sleep" (room 16-20°C).
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css(NAVY,"#fff",PINK,NAVY)+".t2{background:transparent;box-shadow:inset 0 0 0 3px #fff;color:#fff}"
YU=b("yuki.png",700); PA=b("panda.png",700); CO=b("cow.png",700); BE=b("bear.png",700)
GLOW=f"radial-gradient(circle, rgba(241,211,223,.95) 0%, rgba(241,211,223,.55) 35%, rgba(241,211,223,0) 68%)"
def slide(inner,kick,title,body,src=""):
    s=f'<div style="position:absolute;left:70px;right:70px;top:1190px;font-size:23px;font-weight:700;opacity:.75">{src}</div>' if src else ""
    return f'''<div style="position:absolute;left:140px;top:-60px;width:800px;height:800px;border-radius:50%;background:{GLOW}"></div>
<div style="position:absolute;left:0;right:0;top:60px;height:540px;display:flex;align-items:center;justify-content:center;gap:40px;color:{NAVY}">{inner}</div>
<div style="position:absolute;left:70px;right:70px;top:650px"><span class="h" style="background:{PINK};color:{NAVY};font-size:28px;padding:10px 22px;border-radius:30px">{kick}</span>
<div class="h" style="font-size:66px;margin-top:26px">{title}</div><div class="b" style="margin-top:16px;font-size:38px;opacity:.92">{body}</div></div>{s}'''
pimg=lambda s,h: f'<img src="{s}" style="height:{h}px;object-fit:contain;filter:drop-shadow(0 20px 22px rgba(0,0,0,.35))">'
word=lambda a,c,fs=150: f'<div style="text-align:center"><div class="h" style="font-size:{fs}px">{a}</div><div style="font-weight:700;font-size:34px;opacity:.75;margin-top:6px">{c}</div></div>'
cover=hero_cover(baby(29,1080,800,.5,.55,1.0),'<div class="tags"><span class="tag t1">Buying guide</span><span class="tag t2">Kids Furniture</span></div>',
 "Night lights that help at 3am","Bright enough to feed. Soft enough to sleep.",f'<img src="{PA}" style="height:330px;filter:drop-shadow(0 18px 20px rgba(0,0,0,.35))">',1,card=NAVY,fg="#fff",pill_bg=PINK,pill_fg=NAVY,title_fs=74,pill="Swipe for 7 checks")
s2=slide(word("Low &amp; quiet","the night-feed rule",120),"WHY IT MATTERS","Night feeds: dim, quiet, boring","The NHS suggests keeping lights down low, voices quiet and no play at night, so your baby learns night is different from day.","Source: NHS")
s3=slide(pimg(YU,400),"CHECK 1","Pick a dimmer, not just on/off","You need enough light to see a latch or a bottle, then less. Several brightness levels beat one bright setting.")
s4=slide(pimg(BE,440),"CHECK 2","Tap, touch or timer","One arm will be holding your baby. A light you can tap on, or one that switches off by itself, is easier at 3am.")
s5=slide(pimg(CO,420),"CHECK 3","Rechargeable or plug-in?","Rechargeable lights move with you to the feeding chair. Plug-ins never go flat. Check how many hours a charge really lasts.")
s6=slide(word("Screw?","on the battery lid",150),"CHECK 4","Button batteries: check the lid","Some small night lights run on button batteries. If the battery lid isn’t secured by a screw, keep the light out of reach.","Source: GOV.UK")
s7=slide(pimg(PA,420),"CHECK 5","Out of reach, cables too","Keep the light and any cable well away from the cot. Wires are a bigger risk once your baby is on the move.","Source: The Lullaby Trust, the UK safer baby sleep charity")
s8=slide(word("16–20°C","a handy extra",150),"BONUS","A thermometer helps too","Some lights show the room temperature. For sleep, aim for a room of 16–20°C.","Source: The Lullaby Trust, the UK safer baby sleep charity")
s9=hero_last(baby(34,1080,760,.5,.35,1.0),"Soft light, calm nights","Compare night light prices from UK shops in one place.",PINK,fg="#fff")
pin=pin_hero(baby(23,1000,660,.5,.3,1.0),pin_tags("Buying guide","Kids Furniture"),"Night lights: 6 checks for 3am feeds",
 ["Lights low, voices quiet","Choose a dimmer, not on/off","Tap control or a timer","Rechargeable or plug-in?","Button battery lid with a screw","Keep it and cables out of reach"],
 YU,230,NAVY,"#fff",PINK,NAVY,"Sources: NHS; GOV.UK; The Lullaby Trust, the UK safer baby sleep charity.","Compare night light prices at babysorted.com",line="rgba(255,255,255,.2)",photo_h=660,title_fs=54)
render(ROOT+"/out/f",[cover,s2,s3,s4,s5,s6,s7,s8,s9],pin,CSS,"#fff")
