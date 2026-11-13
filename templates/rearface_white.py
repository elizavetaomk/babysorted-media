# White "rear-facing" Tips post (16 Nov 2026): white bg, navy stage cards, a pink rear-facing arrow motif.
# Facts: RoSPA (childcarseats.org.uk) and gov.uk. Black/grey seats on white/navy. Source labels on safety claims.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css("#fff",NAVY,NAVY,"#fff")
DATE="13 Nov 2026"
deco=star(36,30,26,PINK)+star(1000,36,30,PINK)
MK=b("minikid.png",1000); PF=b("perform.png",1000); BE=b("beyond.png",1000)
RS="Source: RoSPA, the UK accident prevention charity"
def rfarrow(h=300):
    return f'<svg width="{int(h*1.4)}" height="{h}" viewBox="0 0 140 100"><path d="M130 50 H40 M70 20 L30 50 L70 80" fill="none" stroke="{PINK}" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def stage(inner,price=None,bg=NAVY):
    pr=f'<div style="position:absolute;right:34px;top:28px;text-align:right;color:#fff"><div class="h" style="font-size:44px">{price[0]}</div><div style="font-size:21px;font-weight:600;opacity:.8;line-height:1.3">{price[1]}<br>Price on BabySorted, {DATE}</div></div>' if price else ""
    return f'<div style="position:absolute;left:60px;right:60px;top:60px;height:610px;background:{bg};border-radius:44px;overflow:hidden"><div style="position:absolute;inset:40px;display:flex;align-items:center;justify-content:center;gap:40px">{inner}</div>{pr}</div>'
def slide(kick,title,body,inner,price=None,src="",bg=NAVY):
    s=f'<div style="font-size:26px;font-weight:700;opacity:.6;margin-top:14px">{src}</div>' if src else ""
    return deco+stage(inner,price,bg)+f'''<div style="position:absolute;left:70px;right:70px;top:712px"><div class="kick">{kick}</div><div class="h" style="font-size:68px;margin-top:8px">{title}</div><div class="b" style="margin-top:14px;font-size:38px">{body}</div>{s}</div>'''
img=lambda s,h: f'<img src="{s}" style="height:{h}px;max-width:620px;object-fit:contain;filter:drop-shadow(0 18px 24px rgba(0,0,0,.35))">'
def statw(a,c):return f'<div style="text-align:center;color:#fff"><div class="h" style="font-size:170px;line-height:1">{a}</div><div class="h" style="font-size:46px;margin-top:6px">{c}</div></div>'
cover=hero_cover(baby(32,1080,800,.5,.32,1.0),'<div class="tags"><span class="tag t1">Tips</span><span class="tag t2">Car Seats</span></div>',"Rear-facing for longer: why experts say so","The simple reason most safety groups say face backwards.",f'<img src="{MK}" style="height:250px;filter:drop-shadow(0 14px 16px rgba(5,31,69,.2))">',1,card="#fff",fg=NAVY,pill_bg=PINK,pill_fg=NAVY,pill="Swipe for the reasons",title_fs=60)
s2=slide("REASON 1","A baby's head is heavy","A baby's head is about a quarter of their body weight. For an adult it's only a small part. In a crash, that heavy head pulls hard on a tiny neck.",'<div style="display:flex;align-items:flex-end;gap:50px">'+statw("25%","baby's head")+statw("6%","adult's head")+'</div>',src=RS)
s3=slide("REASON 2","Facing back spreads the force","Hit from the front, a rear-facing seat spreads the force across the whole back, neck and head. Frontal crash tests show the strain on the neck is five times greater facing forward.",'<div style="display:flex;align-items:center;gap:30px">'+rfarrow(260)+statw("5×","less neck strain, rear-facing")+'</div>',src=RS)
s4=slide("THE LAW, THE FLOOR NOT THE GOAL","Rear-facing to at least 15 months","By law, height-based (R129) seats must stay rear-facing until your child is over 15 months. That's the minimum. RoSPA says keep them rear-facing as long as the seat allows.",statw("15","months, by law, at least"),price=("£295.00","Axkid Minikid 4 Pro, coastal storm black"),src="Source: RoSPA and GOV.UK")
s5=slide("HOW LONG YOU CAN GO","Many seats go rear-facing to about 4","Extended rear-facing seats take a child rear-facing up to around 18kg, about four years old. Some go further, to 25kg. Look at the seat's own height and weight limits.",img(PF,440),price=("£325.00","Silver Cross Perform ERF, iconic black"),src=RS)
s6=slide("THE WORRY YOU CAN DROP","Bent legs are fine","Children get comfy by bending their knees, crossing their legs or resting them on the seat back. It isn't a reason to turn them forward.",statw("OK","crossed or bent legs"),bg=MINT)
s6=s6.replace('color:#fff"><div class="h" style="font-size:170px;line-height:1">OK','color:'+NAVY+'"><div class="h" style="font-size:170px;line-height:1">OK').replace('</div><div class="h" style="font-size:46px;margin-top:6px">crossed','</div><div class="h" style="font-size:46px;margin-top:6px;color:'+NAVY+'">crossed')
s7=slide("NEVER","Not in front of an active airbag","Never fit a rear-facing seat in a front seat with the airbag on. Turn the airbag off first, or fit the seat in the back.",statw("0","rear-facing seats on a live airbag"),bg=NAVY,src="Source: RoSPA and GOV.UK")
s8=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="kick">THE QUICK VERSION</div><div class="h" style="font-size:84px;margin-top:8px">Rear-facing, in 3 lines</div></div>
<div style="position:absolute;left:60px;right:60px;top:360px;display:flex;flex-direction:column;gap:24px">
<div style="background:{PINK};border-radius:34px;padding:34px 40px"><div class="h" style="font-size:48px">Rear-facing is safer for the head and neck</div></div>
<div style="background:{MINT};border-radius:34px;padding:34px 40px"><div class="h" style="font-size:48px">By law to 15 months, but keep going if you can</div></div>
<div style="background:{NAVY};color:#fff;border-radius:34px;padding:34px 40px"><div class="h" style="font-size:48px">Never on a live front airbag</div></div></div>
<div style="position:absolute;left:70px;right:70px;top:1150px;font-size:25px;font-weight:700;opacity:.6">{RS}, and GOV.UK</div>'''
s9=hero_last(baby(27,1080,760,.42,.45,1.0),"Choosing an extended rear-facing seat? Compare prices first","See rear-facing car seat prices from UK shops in one place.",PINK,fg=NAVY)
pin=pin_hero(baby(40,1000,680,.5,.34),pin_tags("Tips","Car Seats"),"Rear-facing for longer: why it's safer",["A baby's head is 25% of their weight","Facing back: 5× less neck strain","Rear-facing to 15 months by law","Many seats go rear-facing to about 4","Bent legs are fine","Never on a live front airbag"],MK,290,"#fff",NAVY,NAVY,"#fff","Source: RoSPA, the UK accident prevention charity, and GOV.UK.","Compare car seat prices at babysorted.com",line=PINK,photo_h=680,title_fs=56)
render(ROOT+"/out/p4",[cover,s2,s3,s4,s5,s6,s7,s8,s9],pin,CSS,NAVY)
