# Pink "scorecard rounds" layout: pink bg; cover = two products on a white arch; rounds = two white cards side by side
# with a navy result bar; traps = product in the open, white text card below.
# Used for: ISOFIX vs seat belt fitting (2 Nov 2026). Run from folder with cut/*.png; writes ./out_isofix
from playwright.sync_api import sync_playwright
import base64, os
PINK="#F1D3DF"; NAVY="#051F45"; ROSE="#E6B6C9"; MINT="#DDF5E3"
b=lambda f: base64.b64encode(open(f,"rb").read()).decode()
IS=b("cut/ispin.png"); ST=b("cut/steadi.png"); BA=b("cut/base.png"); SN=b("cut/isnug.png")
OUT="out_isofix"; os.makedirs(OUT,exist_ok=True)
SH="filter:drop-shadow(0 18px 18px rgba(5,31,69,.20))"
def star(x,y,s,c,o=1): return f'<svg style="position:absolute;left:{x}px;top:{y}px;opacity:{o}" width="{s}" height="{s}" viewBox="0 0 20 20"><path d="M10 0l2.6 7.4L20 10l-7.4 2.6L10 20l-2.6-7.4L0 10l7.4-2.6z" fill="{c}"/></svg>'
CSS=f"""*{{margin:0;padding:0;box-sizing:border-box}} body{{width:1080px;height:1350px;background:{PINK};font-family:Inter;color:{NAVY};position:relative;overflow:hidden}}
.h{{font-weight:800;letter-spacing:-0.035em;line-height:1.05}}
.tags{{display:flex;gap:14px}} .tag{{font-weight:700;font-size:28px;padding:9px 22px;border-radius:30px}}
.t1{{background:{NAVY};color:#fff}} .t2{{background:#fff;box-shadow:inset 0 0 0 3px {NAVY}}}
.kick{{font-weight:800;font-size:28px;letter-spacing:.06em;opacity:.6}}
.foot{{position:absolute;left:70px;right:70px;bottom:50px;display:flex;justify-content:space-between;align-items:center}}
.brand{{font-weight:800;font-size:36px;letter-spacing:-0.03em}}
.res{{position:absolute;left:60px;right:60px;bottom:126px;height:130px;display:flex;flex-direction:column;justify-content:center;background:{NAVY};color:#fff;border-radius:26px;padding:0 34px;font-weight:700;font-size:34px;line-height:1.22}}
.res b{{font-weight:800;color:{PINK}}}
.txt{{position:absolute;left:60px;right:60px;bottom:126px;background:#fff;border-radius:40px;padding:44px 50px}}
.pill{{display:inline-block;font-weight:800;font-size:30px;padding:13px 24px;border-radius:24px;white-space:nowrap}}
.chip{{position:absolute;background:{NAVY};color:#fff;font-weight:800;font-size:28px;padding:12px 22px;border-radius:22px;white-space:nowrap}}"""
def foot(i,n):
    d="".join(f'<div style="width:{40 if j==i else 14}px;height:14px;border-radius:7px;background:{NAVY};opacity:{1 if j==i else .25}"></div>' for j in range(n))
    return f'<div class="foot"><div class="brand">BabySorted</div><div style="display:flex;gap:12px">{d}</div></div>'
deco=star(990,40,30,"#fff")+star(36,30,24,"#fff")
im=lambda s,h,x="": f'<img src="data:image/png;base64,{s}" style="height:{h}px;max-width:100%;object-fit:contain;{SH};{x}">'
def card(name,model,pic,h,txt):
    return f'''<div style="flex:1;background:#fff;border-radius:38px;padding:30px 34px;display:flex;flex-direction:column">
<div style="height:320px;display:flex;align-items:center;justify-content:center">{im(pic,h)}</div>
<div class="h" style="font-size:46px;margin-top:16px">{name}</div><div style="font-size:24px;font-weight:600;opacity:.55;margin-top:4px">{model}</div>
<div style="font-size:37px;font-weight:500;line-height:1.34;margin-top:18px">{txt}</div></div>'''
def rnd(k,title,a,bt,res):
    return deco+f'''<div style="position:absolute;left:70px;right:70px;top:66px"><div class="kick">ROUND {k} OF 3</div><div class="h" style="font-size:76px;margin-top:8px">{title}</div></div>
<div style="position:absolute;left:60px;right:60px;top:226px;bottom:278px;display:flex;gap:22px">{card("ISOFIX","e.g. Joie i-Spin 360 Max",IS,300,a)}{card("Seat belt","e.g. Joie Steadi R129",ST,290,bt)}</div>
<div class="res">{res}</div>'''
def trap(kick,title,body,vis,extra=""):
    return deco+f'''<div style="position:absolute;left:60px;right:60px;top:60px;height:520px;display:flex;align-items:center;justify-content:center;gap:50px">{vis}</div>
<div class="txt" style="top:590px"><div class="kick">{kick}</div><div class="h" style="font-size:63px;margin-top:8px;white-space:nowrap">{title}</div>
<div style="font-size:39px;font-weight:500;line-height:1.36;margin-top:20px">{body}</div>{extra}</div>'''
cover=star(980,60,40,"#fff")+star(50,560,24,"#fff")+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="tags"><span class="tag t1">Comparison</span><span class="tag t2">Car Seats</span></div>
<div class="h" style="font-size:100px;margin-top:28px">ISOFIX or seat belt:<br>which is safer<br>for you?</div>
<div style="font-size:39px;font-weight:600;opacity:.75;margin-top:20px">Both can be safe. One is much easier to get right.</div></div>
<div style="position:absolute;left:60px;right:60px;top:590px;bottom:126px;background:#fff;border-radius:440px 440px 44px 44px"></div>
<div style="position:absolute;left:0;right:0;top:610px;display:flex;justify-content:center;gap:40px;align-items:flex-end;height:500px">{im(IS,490)}{im(ST,450)}</div>
<div style="position:absolute;left:120px;top:1136px;background:{PINK};font-weight:800;font-size:30px;padding:10px 24px;border-radius:22px">ISOFIX</div>
<div style="position:absolute;right:120px;top:1136px;background:{PINK};font-weight:800;font-size:30px;padding:10px 24px;border-radius:22px">Seat belt</div>
<div style="position:absolute;left:0;right:0;top:1134px;text-align:center"><span style="display:inline-block;background:{NAVY};color:#fff;font-weight:700;font-size:28px;padding:12px 26px;border-radius:40px">Swipe before you buy</span></div>'''
s2=trap("THE SHORT ANSWER","ISOFIX is harder to get wrong",
 "RoSPA calls it a more secure and easier way to fit a seat. Which? recommends it if your car has the points. But the real test is the same for both: is this seat right for your car, and fitted right every time?",
 im(IS,500),f'<div style="margin-top:26px"><span class="pill" style="background:{NAVY};color:#fff">Right seat. Right car. Right fit.</span></div>')
s3=rnd(1,"Getting it in","Push the connectors into the car's points until it clicks or the indicator shows green.",
 "Thread the belt through every guide. Press your weight in, pull tight. No slack.",
 "<b>Round 1: ISOFIX.</b> Fewer steps to get wrong.")
s4=rnd(2,"Fitting your car","Having the points isn't enough. Not every ISOFIX seat fits every car with points.",
 "Belts vary. One that's too short lifts the seat, so it won't sit flat.",
 "<b>Round 2: a draw.</b> Check the fit list. Try it in your car first.")
s5=trap("THE ISOFIX TRAP","Two clicks are only half the job",
 "It also needs a support leg or top tether to stop the seat tilting or rotating in a crash. The leg must stand on solid floor: an underfloor storage lid may collapse. A tether only goes on the car's own anchor, never a luggage hook.",
 im(BA,500)+f'<div style="display:flex;flex-direction:column;gap:18px"><span class="pill" style="background:{NAVY};color:#fff">Support leg</span><span class="pill" style="background:#fff">Solid floor only</span></div>')
COL=lambda c,t: f'<div style="display:flex;align-items:center;gap:16px;font-weight:800;font-size:32px"><span style="width:44px;height:44px;border-radius:50%;background:{c}"></span>{t}</div>'
s6=trap("THE SEAT BELT TRAP","Watch for buckle crunch",
 "If the belt's buckle presses on the seat frame, it can fail in a crash or under hard braking. Only the webbing should touch the frame. So try the seat in your own car before you buy.",
 im(ST,500)+f'<div style="display:flex;flex-direction:column;gap:18px;background:#fff;border-radius:30px;padding:28px 30px"><div style="font-weight:800;font-size:24px;letter-spacing:.06em;opacity:.55">BELT GUIDES</div>{COL("#2F6FD0","Rear-facing")}{COL("#D0342C","Forward-facing")}{COL("#2E9E5B","i-Size")}</div>',f'<div style="margin-top:26px"><span class="pill" style="background:{NAVY};color:#fff">Follow the colour for your seat</span></div>')
s7=rnd(3,"Swapping cars","Older cars may not have points. Look for the labels between the seat base and back.",
 "Uses the car's own 3-point belt, so it can suit a second car. Refit it properly every time.",
 "<b>Round 3: seat belt.</b> Handy for a second car, if the belt reaches.")
s8=trap("WANT BOTH?","Some seats do both",
 "Some baby seats fit with the belt alone, or on an ISOFIX base bought separately. So one seat can suit two cars. Read the manual first: some seats must use their base, and a base only fits its own matching seats.",
 im(SN,400)+im(BA,500),f'<div style="margin-top:26px"><span class="pill" style="background:{NAVY};color:#fff">One seat, two cars</span></div>')
def col(t,items,bg):
    li="".join(f'<div style="display:flex;gap:14px;margin-top:22px"><span style="flex:none;width:40px;height:40px;border-radius:50%;background:{NAVY};color:#fff;font-size:22px;font-weight:800;display:flex;align-items:center;justify-content:center">✓</span><span style="font-size:37px;font-weight:600;line-height:1.26">{x}</span></div>' for x in items)
    return f'<div style="flex:1;background:{bg};border-radius:36px;padding:32px 30px"><div class="h" style="font-size:48px">{t}</div>{li}</div>'
s9=deco+f'''<div style="position:absolute;left:70px;right:70px;top:66px"><div class="kick">THE VERDICT</div><div class="h" style="font-size:84px;margin-top:8px">Which one is for you?</div></div>
<div style="position:absolute;left:60px;right:60px;top:236px;height:590px;display:flex;gap:22px">{col("Choose ISOFIX if",["Your car has the points","The seat is on the maker's fit list","It stays in one car"],"#fff")}{col("Choose belt if",["Your car has no points","It moves between cars","It sits flat and tight in your car"],"#fff")}</div>
<div class="res" style="top:850px;bottom:auto;height:auto;padding:34px 40px"><div style="font-weight:800;font-size:26px;letter-spacing:.06em;opacity:.7">EITHER WAY, DO THIS TEST</div>
<div style="font-size:40px;font-weight:600;line-height:1.3;margin-top:10px">Rear-facing seat? Push down where your baby's head would sit. The seat shouldn't move.</div></div>'''
s10=deco+f'''<div style="position:absolute;left:60px;right:60px;top:60px;height:560px;display:flex;align-items:center;justify-content:center;gap:50px">{im(IS,510)}{im(ST,470)}</div>
<div class="txt" style="top:650px"><div class="h" style="font-size:72px">Picked your fit? Compare prices first</div>
<div style="font-size:37px;font-weight:500;margin-top:16px">Compare car seat prices from UK shops in one place.</div>
<div style="margin-top:28px;display:flex;align-items:center;gap:16px"><div class="h" style="font-size:44px;background:{PINK};padding:20px 28px;border-radius:24px">babysorted.com/links</div>
<div style="background:{NAVY};color:#fff;font-weight:800;font-size:30px;padding:20px 24px;border-radius:24px;white-space:nowrap">Link in bio ↑</div></div>
<div style="margin-top:20px;font-size:30px;font-weight:700;opacity:.55">Save this post for later</div></div>'''
bodies=[cover,s2,s3,s4,s5,s6,s7,s8,s9,s10]; n=len(bodies)
rows=[("Getting it in","Push and click","Thread, press, tighten","ISOFIX"),("Fitting your car","Check the fit list","Check the belt length","Draw"),("Swapping cars","Needs points in each car","The car's 3-point belt","Belt")]
tb="".join(f'''<div style="display:flex;align-items:center;gap:12px;padding:14px 0;border-top:{"0" if i==0 else "2px solid #F4E3EA"}"><div style="flex:1.1;font-weight:800;font-size:29px;letter-spacing:-.02em">{a}</div><div style="flex:1;font-size:25px;font-weight:500">{c}</div><div style="flex:1;font-size:25px;font-weight:500">{d}</div><div style="flex:none;width:112px;text-align:center;background:{NAVY if e!="Draw" else PINK};color:{"#fff" if e!="Draw" else NAVY};font-weight:800;font-size:23px;padding:8px 0;border-radius:18px">{e}</div></div>''' for i,(a,c,d,e) in enumerate(rows))
traps=[("ISOFIX trap","Add the support leg or tether. Leg on solid floor, tether on the car's anchor."),("Belt trap","Buckle crunch: only the webbing should touch the seat frame."),("Either way","Push down where baby's head sits. The seat shouldn't move.")]
tr="".join(f'<div style="flex:1;background:#fff;border-radius:24px;padding:18px 20px;height:262px"><div class="h" style="font-size:27px">{a}</div><div style="font-size:26px;font-weight:500;line-height:1.28;margin-top:8px">{c}</div></div>' for a,c in traps)
pin=f'''{star(900,50,34,"#fff")}<div style="position:absolute;left:60px;right:60px;top:60px"><div class="tags"><span class="tag t1" style="font-size:24px">Comparison</span><span class="tag t2" style="font-size:24px">Car Seats</span></div>
<div class="h" style="font-size:78px;margin-top:20px">ISOFIX or seat belt: which is safer for you?</div></div>
<div style="position:absolute;left:60px;right:60px;top:300px;height:440px;background:#fff;border-radius:220px 220px 36px 36px"></div>
<div style="position:absolute;left:60px;right:60px;top:330px;height:390px;display:flex;justify-content:center;gap:60px;align-items:flex-end">{im(IS,380)}{im(ST,350)}</div>
<div style="position:absolute;left:60px;right:60px;top:752px;background:#fff;border-radius:36px;padding:12px 32px"><div style="display:flex;gap:12px;font-weight:800;font-size:22px;letter-spacing:.05em;opacity:.55;padding-top:8px"><div style="flex:1.1"></div><div style="flex:1">ISOFIX</div><div style="flex:1">SEAT BELT</div><div style="flex:none;width:112px;text-align:center">WINS</div></div>{tb}</div>
<div style="position:absolute;left:60px;right:60px;top:1110px;display:flex;gap:14px">{tr}</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:100px;background:{NAVY};color:#fff;display:flex;justify-content:space-between;align-items:center;padding:0 60px"><div class="brand" style="font-size:34px">BabySorted</div><div style="font-weight:700;font-size:26px">Compare car seat prices at babysorted.com</div></div>'''
with sync_playwright() as p:
    br=p.chromium.launch(); pg=br.new_page(viewport=dict(width=1080,height=1350))
    for i,bd in enumerate(bodies):
        pg.set_content(f"<html><head><style>{CSS}</style></head><body>{bd}{foot(i,n)}</body></html>"); pg.wait_for_timeout(250)
        pg.screenshot(path=f"{OUT}/slide_{i+1}.png")
    pg2=br.new_page(viewport=dict(width=1000,height=1500),device_scale_factor=2)
    pg2.set_content(f"<html><head><style>{CSS.replace('width:1080px;height:1350px','width:1000px;height:1500px')}</style></head><body>{pin}</body></html>"); pg2.wait_for_timeout(250)
    pg2.screenshot(path=f"{OUT}/pin.png"); br.close()
from PIL import Image
W=Image.new('RGB',(1800,1000),'#bbb')
for k in range(n): W.paste(Image.open(f'{OUT}/slide_{k+1}.png').resize((352,440)),((k%5)*360,(k//5)*460))
W.save(f'{OUT}/preview.png')
Image.open(f'{OUT}/pin.png').resize((667,1000)).save(f'{OUT}/pinp.png')
