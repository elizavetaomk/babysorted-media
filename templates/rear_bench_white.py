# White "rear bench" layout (21 Nov 2026): white bg, a top-down drawing of the back seat (3 seats) in a pink panel,
# highlighted seats in navy/deeper pink, title + body below, source line. Photo-led cover and last slide.
# Used for: #52 Two car seats in one car. Facts: GOV.UK child car seat rules, RoSPA (childcarseats.org.uk).
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css("#fff",NAVY,NAVY,"#fff")+f".t2{{background:{PINK};box-shadow:none}}"
IS=b("isnug.png",800); EL=b("elevate.png",800); DATE="20 Nov 2026"
RO="Source: RoSPA, the UK accident prevention charity"; GV="Source: GOV.UK"
def seat(label,state,mark=""):
    bg={"on":NAVY,"hot":ROSE,"off":"#fff"}[state]; fg="#fff" if state=="on" else NAVY
    return f'''<div style="flex:1;height:250px;background:{bg};color:{fg};border-radius:34px 34px 20px 20px;box-shadow:inset 0 0 0 4px {NAVY};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;position:relative">
<div class="h" style="font-size:30px">{label}</div><div style="font-weight:800;font-size:26px;opacity:.85">{mark}</div></div>'''
def bench(states,marks=("","",""),note=""):
    labs=("Left","Middle","Right")
    seats="".join(seat(labs[i],states[i],marks[i]) for i in range(3))
    return f'''<div style="position:absolute;left:60px;right:60px;top:70px;height:470px;background:{PINK};border-radius:44px;padding:40px 46px">
<div style="font-weight:800;font-size:24px;letter-spacing:.08em;opacity:.6">BACK SEAT, FROM ABOVE</div>
<div style="display:flex;gap:22px;margin-top:24px">{seats}</div>
<div style="margin-top:22px;font-weight:700;font-size:26px;text-align:center">{note}</div></div>'''
def sl(kick,title,body,top,src=None):
    s=f'<div style="position:absolute;left:70px;right:70px;top:1100px;font-size:23px;font-weight:700;opacity:.65">{src}</div>' if src else ""
    return f'''{top}<div style="position:absolute;left:70px;right:70px;top:590px"><div class="kick">{kick}</div><div class="h" style="font-size:66px;margin-top:6px">{title}</div><div class="b" style="margin-top:14px;font-size:36px">{body}</div></div>{s}'''
def bigp(a,c): return f'<div style="position:absolute;left:60px;right:60px;top:70px;height:470px;background:{PINK};border-radius:44px;display:flex;flex-direction:column;align-items:center;justify-content:center"><div class="h" style="font-size:150px;line-height:1">{a}</div><div class="h" style="font-size:40px;margin-top:16px">{c}</div></div>'
prods=f'<div style="display:flex;gap:8px;align-items:flex-end;justify-content:center"><img src="{IS}" style="height:128px;{SH}"><img src="{EL}" style="height:175px;{SH}"></div>'
cover=hero_cover(baby(6,1080,800,.5,.62,1.25),'<div class="tags"><span class="tag t1">Buying guide</span><span class="tag t2">Car Seats</span></div>',"Two car seats in one car: what really fits","Measure first. It saves a return trip.",prods,1,card="#fff",fg=NAVY,pill_bg=NAVY,pill_fg="#fff",title_fs=62)
s2=sl("START HERE","Every car is different","The shape of car seats, the length of seat belts and where the anchor points sit all differ between cars. Check a seat fits every position you plan to use, before you buy.",bench(("on","off","on"),("Seat 1","?","Seat 2"),"Measure the seats you'll actually use"),RO+".")
s3=sl("THE LAW","Who needs a child seat","Children must normally use a child car seat until they're 12 years old or 135cm tall, whichever comes first. So plan for years, not months.",bigp("135cm","or 12 years old"),GV+".")
s4=sl("ISOFIX","Which seats have ISOFIX?","Open your car handbook before you buy. An ISOFIX seat can only go in the middle if your car has ISOFIX points there.",bench(("on","off","on"),("ISOFIX?","ISOFIX?","ISOFIX?"),"Check the handbook, seat by seat"),RO+".")
s5=sl("THE MIDDLE SEAT","Safest, if the belt allows","With a 3-point belt, the middle rear seat is the safest place for a child seat. If it only has a lap belt, check your seat allows that. Most need a 3-point belt.",bench(("off","on","off"),("","3-point belt?","")),RO+".")
s6=sl("SIDE BY SIDE","Two checks people miss","Buckle crunch: the belt buckle must not rest on the child seat frame. Support legs: the foot must not stand on an under-floor storage lid.",bench(("hot","off","hot"),("buckle clear?","","leg on a lid?"),"Squeezed seats push buckles out of place"),RO+".")
s7=sl("THE FRONT SEAT","Rear-facing in the front?","Only if you switch off the front airbag first. Never fit a rear-facing seat in front of an active airbag.",bigp("Airbag OFF","before a rear-facing seat goes in"),"Sources: GOV.UK; RoSPA, the UK accident prevention charity.")
s8=sl("THREE CHILDREN","No room for a third seat?","Children under 3 must travel in the front with the correct child car seat. Children aged 3 or older can sit in the back using an adult belt.",bench(("on","hot","on"),("Seat","age 3+? adult belt","Seat")),GV+".")
pp=f'''<div style="position:absolute;left:60px;right:60px;top:70px;height:470px;background:{PINK};border-radius:44px;display:flex;align-items:center;justify-content:space-around;padding:0 30px">
<div style="text-align:center"><img src="{IS}" style="height:270px;{SH}"><div class="h" style="font-size:46px;margin-top:10px">£89.95</div><div style="font-size:21px;font-weight:600;opacity:.75">Joie i-Snug 2, Shale</div></div>
<div style="text-align:center"><img src="{EL}" style="height:300px;{SH}"><div class="h" style="font-size:46px;margin-top:10px">£49.99</div><div style="font-size:21px;font-weight:600;opacity:.75">Joie Elevate R129, Shale</div></div></div>'''
s9=sl("PRICES","Same seat, different price","On BabySorted today the same Elevate costs from £49.99 to £65.00, depending on the shop. Two seats means the gap counts twice.",pp,f"Prices on BabySorted, {DATE}.")
s10=hero_last(baby(11,1080,700,.5,.3),"Buying two seats? Compare prices first","Compare car seat prices from UK shops in one place.",PINK,fg=NAVY,photo_h=700)
pin=pin_hero(baby(1,1000,680,.42,.45,1.1),pin_tags("Buying guide","Car Seats"),"Two car seats in one car",
 ["Check every seat you plan to use","Child seat until 12 or 135cm","ISOFIX in the middle? Check","Middle seat: 3-point belt?","No buckle crunch side by side","Rear-facing in front: airbag off"],
 IS,180,"#fff",NAVY,NAVY,"#fff","Sources: GOV.UK; RoSPA, the UK accident prevention charity.","Compare car seat prices at babysorted.com",line=PINK,photo_h=680,title_fs=56)
render(ROOT+"/out/c",[cover,s2,s3,s4,s5,s6,s7,s8,s9,s10],pin,CSS,NAVY)
