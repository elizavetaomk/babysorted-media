# Pink "fit checks" layout: pink bg; check slides = product on a white tile + big navy "CHECK n" block; seat slides = white card with spec tiles.
# Used for: Best car seats for small cars (10 Nov 2026). Facts: GOV.UK, RoSPA (childcarseats.org.uk); sizes are makers' figures from listings.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css(PINK,NAVY,NAVY,"#fff")+".t2{background:#fff;box-shadow:none}"
deco=star(36,30,26,"#fff")+star(1000,40,30,"#fff")
IL=b("ilevel.png",1000); IS=b("ispin.png",1000); NO=b("nomad.png",1000)
DATE="9 Nov 2026"
img=lambda s,h,x="": f'<img src="{s}" style="height:{h}px;max-width:100%;object-fit:contain;{SH};{x}">'
def check(k,q,body,pic,h,src,note=""):
    nt=f'<div style="position:absolute;left:30px;right:30px;bottom:24px;text-align:center"><span class="pill" style="background:{PINK};font-size:26px">{note}</span></div>' if note else ""
    return deco+f'''<div style="position:absolute;left:60px;top:60px;width:560px;height:600px;background:#fff;border-radius:44px;display:flex;align-items:center;justify-content:center;overflow:hidden">{img(pic,h)}{nt}</div>
<div style="position:absolute;left:650px;right:60px;top:60px;height:600px;background:{NAVY};color:#fff;border-radius:44px;display:flex;flex-direction:column;align-items:center;justify-content:center"><div style="font-weight:800;font-size:30px;letter-spacing:.08em;opacity:.7">CHECK</div><div class="h" style="font-size:230px;line-height:1">{k}</div><div style="font-weight:700;font-size:28px;opacity:.7">of 4</div></div>
<div style="position:absolute;left:70px;right:70px;top:705px"><div class="h" style="font-size:70px">{q}</div><div class="b" style="margin-top:16px;font-size:40px">{body}</div></div>
<div style="position:absolute;left:70px;right:70px;top:1195px;font-size:26px;font-weight:700;opacity:.6">{src}</div>'''
def seat(k,name,use,pic,h,specs,good,price):
    tiles="".join(f'<div style="flex:1;background:{PINK};border-radius:22px;padding:16px 18px"><div style="font-weight:800;font-size:21px;letter-spacing:.05em;opacity:.65">{a}</div><div class="h" style="font-size:36px;margin-top:4px">{c}</div></div>' for a,c in specs)
    return deco+f'''<div style="position:absolute;left:60px;right:60px;top:60px;height:1150px;background:#fff;border-radius:44px">
<div style="position:absolute;left:40px;top:36px"><span class="pill" style="background:{NAVY};color:#fff;font-size:26px">Seat {k} of 3 · {use}</span></div>
<div style="position:absolute;left:0;right:0;top:110px;height:450px;display:flex;align-items:center;justify-content:center">{img(pic,h)}</div>
<div style="position:absolute;right:40px;top:120px;text-align:right"><div class="h" style="font-size:54px">{price}</div><div style="font-size:21px;font-weight:600;opacity:.65">Price on BabySorted,<br>{DATE}</div></div>
<div style="position:absolute;left:40px;right:40px;top:580px"><div class="h" style="font-size:52px">{name}</div>
<div style="display:flex;gap:14px;margin-top:22px">{tiles}</div>
<div class="b" style="margin-top:22px;font-size:35px"><b style="font-weight:800">Small car tip:</b> {good}</div>
<div style="font-size:24px;font-weight:600;opacity:.55;margin-top:14px">Sizes are the maker's figures. Check yours in the car before you buy.</div></div></div>'''
cover=hero_cover(baby(13,1080,800,.42,.4,1.0),'<div class="tags"><span class="tag t1" style="font-size:28px">Buying guide</span><span class="tag t2" style="box-shadow:inset 0 0 0 3px #051F45;font-size:28px" style="font-size:28px">Car Seats</span></div>',"Best car seats for small cars","4 checks first. Then 3 seats worth a look.",f'<img src="{IS}" style="height:380px;{SH}">',1,card="#fff",title_fs=80)+star(1000,40,30,"#fff")
s2=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="kick">START WITH THE LAW</div><div class="h" style="font-size:80px;margin-top:8px">Plan for rear-facing</div></div>
<div style="position:absolute;left:60px;right:60px;top:320px;height:470px;background:#fff;border-radius:44px;display:flex;flex-direction:column;align-items:center;justify-content:center"><div style="font-weight:800;font-size:34px;opacity:.6">rear-facing until over</div><div class="h" style="font-size:220px;line-height:1">15</div><div class="h" style="font-size:64px">months</div></div>
<div class="b" style="position:absolute;left:70px;right:70px;top:830px;font-size:41px">Height-based (i-Size) seats must face backwards until your child is over 15 months. So in a small car, the real question is room behind the front seat, not just width.</div>
<div style="position:absolute;left:70px;right:70px;top:1150px;font-size:27px;font-weight:700;opacity:.6">Source: GOV.UK</div>'''
s3=check(1,"Is the seat on your car's list?","Many car makers show which seats are approved for each car. Then try the seat in your own car. If it won't fit securely, don't buy it.",IL,430,"Source: RoSPA, the UK accident prevention charity")
s4=check(2,"Is there storage under the floor?","Some seats stand on a support leg. It must not rest on an underfloor storage box: the lid could collapse in a crash. Lift the floor mat and look.",IS,520,"Source: RoSPA, the UK accident prevention charity","Support leg")
s5=check(3,"Does it need a top tether?","If the seat uses a top tether strap, your car needs a tether point for it. Small cars don't always have one in every seat. Check the handbook.",NO,500,"Source: RoSPA, the UK accident prevention charity","Top tether up to 4 years")
s6=check(4,"Thinking of the front seat?","You must turn off the front airbag before you fit a rear-facing seat there. If you can't turn it off, that seat is out.",IL,430,"Source: GOV.UK","Rear-facing")
s7=seat(1,"Joie i-Level Pro Signature","Newborn",IL,420,[("FITS","Birth to 87cm"),("WIDTH","44.5cm"),("FITS WITH","Seat belt or base")],"it fits with the car's 3-point belt, so it still works in a car without ISOFIX. Bases are sold separately.","£137.99")
s8=seat(2,"Joie i-Spin 360 Compact","Next stage",IS,440,[("FITS","61 to 105cm"),("WIDTH","44cm"),("LENGTH","69.4cm")],"it turns to face the door for lifting in. It uses ISOFIX and a support leg, so do check 2 first.","£150.00")
s9=seat(3,"Maxi-Cosi Nomad XL Plus","15 months+",NO,440,[("FITS","15 months to 12 years"),("WIDTH","44cm"),("EXTRA","Folds")],"it folds to swap between cars or to store. Up to 4 years it uses ISOFIX and a top tether, so do check 3.","£152.94")
s10=hero_last(baby(7,1080,760,.36,.5,1.0),"Found one that fits? Compare prices first","Compare car seat prices from UK shops in one place.","#fff")
C=[("On your car's list?","Car makers list approved seats. Try it in your car."),("Storage under the floor?","A support leg must not stand on a storage lid."),("Needs a top tether?","Your car needs a tether point for it."),("Front seat?","Rear-facing only with the airbag turned off.")]
cc="".join(f'<div style="display:flex;align-items:center;gap:20px;padding:15px 0;border-top:{"0" if i==0 else f"3px solid {PINK}"}"><div class="h" style="flex:none;width:58px;height:58px;border-radius:50%;background:{NAVY};color:#fff;font-size:30px;display:flex;align-items:center;justify-content:center">{i+1}</div><div><div class="h" style="font-size:35px">{a}</div><div style="font-size:26px;font-weight:500;opacity:.85;margin-top:2px">{c}</div></div></div>' for i,(a,c) in enumerate(C))
SE=[(IL,"£137.99","Joie i-Level Pro Signature","Birth to 87cm"),(IS,"£150.00","Joie i-Spin 360 Compact","61 to 105cm"),(NO,"£152.94","Maxi-Cosi Nomad XL Plus","15 months+")]
se="".join(f'<div style="flex:1;background:#fff;border-radius:28px;padding:16px 12px;text-align:center"><div style="height:250px;display:flex;align-items:center;justify-content:center">{img(p,240)}</div><div class="h" style="font-size:24px;margin-top:8px;line-height:1.15">{n}</div><div style="font-size:21px;font-weight:600;opacity:.7">{f}</div><div class="h" style="font-size:32px;margin-top:4px">{pr}</div></div>' for p,pr,n,f in SE)
pin=f'''{star(920,44,30,"#fff")}<div style="position:absolute;left:60px;right:60px;top:56px"><div class="tags"><span class="tag t1" style="font-size:24px">Buying guide</span><span class="tag t2" style="font-size:24px">Car Seats</span></div>
<div class="h" style="font-size:64px;margin-top:20px;width:520px">Car seats for small cars: 4 checks first</div></div><img src="{baby(13,330,270,.42,.4,1.1)}" style="position:absolute;right:60px;top:56px;width:330px;height:280px;border-radius:30px;object-fit:cover">
<div style="position:absolute;left:60px;right:60px;top:355px;background:#fff;border-radius:34px;padding:10px 34px 12px">{cc}</div>
<div style="position:absolute;left:60px;right:60px;top:830px;display:flex;gap:16px">{se}</div>
<div style="position:absolute;left:60px;right:60px;top:1290px;font-size:23px;font-weight:600;opacity:.75;line-height:1.3">Prices on BabySorted, {DATE}. Source for checks 1–3: RoSPA, the UK accident prevention charity. Source for check 4: GOV.UK.</div>
<div style="position:absolute;left:60px;right:60px;bottom:30px;display:flex;justify-content:space-between;align-items:center"><div class="brand" style="font-size:34px">BabySorted</div><div style="font-weight:700;font-size:25px">Compare car seat prices at babysorted.com</div></div>'''
render(ROOT+"/out/c",[cover,s2,s3,s4,s5,s6,s7,s8,s9,s10],pin,CSS,NAVY)
