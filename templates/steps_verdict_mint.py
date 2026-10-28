# Mint "steps + verdict" layout: mint bg, cover = 3 products on rising steps; inner = white card with colour band,
# product, headline and a verdict pill (Move up / Not yet). Used for: When to move to the next car seat (29 Oct 2026).
from playwright.sync_api import sync_playwright
import base64, os
PINK="#F1D3DF"; NAVY="#051F45"; ROSE="#E6B6C9"; MINT="#DDF5E3"; DMINT="#BFE8CB"; GREY="#EEF0F3"
b=lambda f: base64.b64encode(open(f,"rb").read()).decode()
MA=b("cut/maple.png"); EL=b("cut/elm.png"); E0=b("cut/elm0.png"); PA=b("cut/palm.png")
OUT="out_seat"; os.makedirs(OUT,exist_ok=True)
SH="filter:drop-shadow(0 18px 16px rgba(5,31,69,.18))"
def star(x,y,s,c,o=1): return f'<svg style="position:absolute;left:{x}px;top:{y}px;opacity:{o}" width="{s}" height="{s}" viewBox="0 0 20 20"><path d="M10 0l2.6 7.4L20 10l-7.4 2.6L10 20l-2.6-7.4L0 10l7.4-2.6z" fill="{c}"/></svg>'
CSS=f"""*{{margin:0;padding:0;box-sizing:border-box}} body{{width:1080px;height:1350px;background:{MINT};font-family:Inter;color:{NAVY};position:relative;overflow:hidden}}
.h{{font-weight:800;letter-spacing:-0.035em;line-height:1.04}}
.tags{{display:flex;gap:14px}} .tag{{font-weight:700;font-size:28px;padding:9px 22px;border-radius:30px}}
.t1{{background:{NAVY};color:#fff}} .t2{{background:#fff;box-shadow:inset 0 0 0 3px {NAVY}}}
.card{{position:absolute;left:70px;right:70px;top:80px;bottom:150px;background:#fff;border-radius:44px;overflow:hidden}}
.kick{{font-weight:800;font-size:28px;letter-spacing:.06em;opacity:.55}}
.foot{{position:absolute;left:90px;right:90px;bottom:58px;display:flex;justify-content:space-between;align-items:center}}
.brand{{font-weight:800;font-size:38px;letter-spacing:-0.03em}}
.pill{{display:inline-block;font-weight:800;font-size:32px;padding:14px 26px;border-radius:26px;white-space:nowrap}}"""
deco=star(30,26,34,"#fff")+star(1010,30,26,NAVY,.25)+star(1012,1196,30,"#fff")
def foot(i,n):
    d="".join(f'<div style="width:{40 if j==i else 14}px;height:14px;border-radius:7px;background:{NAVY};opacity:{1 if j==i else .25}"></div>' for j in range(n))
    return f'<div class="foot"><div class="brand">BabySorted</div><div style="display:flex;gap:12px">{d}</div></div>'
YES=lambda t="Time to move up": f'<span class="pill" style="background:{NAVY};color:#fff">✓ {t}</span>'
NO=lambda t="Not a reason to move": f'<span class="pill" style="background:{PINK}">✕ {t}</span>'
def sign(k,title,body,pic,band,verdict,big=None):
    vis=f'<img src="data:image/png;base64,{pic}" style="position:absolute;right:60px;bottom:30px;height:470px;max-width:470px;object-fit:contain;{SH}">' if pic else ''
    bigt=f'<div class="h" style="position:absolute;left:60px;bottom:60px;font-size:{big[1]}px;width:{big[2]}px;white-space:nowrap">{big[0]}</div>' if big else ''
    return deco+f'''<div class="card"><div style="position:relative;height:540px;background:{band}">{bigt}{vis}
<div style="position:absolute;left:60px;top:50px;font-weight:800;font-size:28px;background:#fff;padding:8px 18px;border-radius:20px">{k}</div></div>
<div style="padding:44px 60px 0"><div class="h" style="font-size:66px">{title}</div>
<div style="font-size:37px;font-weight:500;line-height:1.4;margin-top:20px">{body}</div>
<div style="margin-top:30px">{verdict}</div></div></div>'''
stepimg=lambda s,l,bot,h: f'<img src="data:image/png;base64,{s}" style="position:absolute;left:{l}px;bottom:{bot}px;height:{h}px;{SH}">'
cover=deco+f'''<div style="position:absolute;left:90px;right:90px;top:90px">
<div class="tags"><span class="tag t1">Tips</span><span class="tag t2">Car Seats</span></div>
<div class="h" style="font-size:88px;margin-top:28px">When to move your child to the next car seat</div>
<div style="font-size:40px;font-weight:600;opacity:.75;margin-top:20px">Not by age. By height and fit.</div><div style="margin-top:28px;display:inline-block;background:#fff;font-weight:700;font-size:30px;padding:14px 28px;border-radius:40px">Swipe before you buy</div></div>
<div style="position:absolute;left:70px;width:300px;bottom:150px;height:150px;background:#fff;border-radius:30px 30px 0 0"></div>
<div style="position:absolute;left:390px;width:300px;bottom:150px;height:260px;background:{PINK};border-radius:30px 30px 0 0"></div>
<div style="position:absolute;left:710px;width:300px;bottom:150px;height:370px;background:{ROSE};border-radius:30px 30px 0 0"></div>
{stepimg(MA,95,290,250)}{stepimg(EL,405,400,270)}{stepimg(PA,735,510,300)}
<div style="position:absolute;left:0;right:0;bottom:150px;height:6px;background:{NAVY};opacity:.12"></div>
<div style="position:absolute;left:100px;bottom:180px;font-weight:800;font-size:28px">Baby seat</div>
<div style="position:absolute;left:420px;bottom:180px;font-weight:800;font-size:28px">Toddler seat</div>
<div style="position:absolute;left:740px;bottom:180px;font-weight:800;font-size:28px">Booster</div>'''
s2=sign("THE RULE","Move up when the seat is outgrown",
 "Not on a birthday. Which? says keep your child in their seat until they go over its weight or height limit. Moving up too soon is a common mistake.",
 None,PINK,YES("Over the limit? Move up"),("Limit, not age",118,900))
s3=sign("BABY SEAT","Head above the top of the shell",
 "RoSPA: a baby seat is outgrown when your baby goes over its weight limit, or when the top of their head is above the top of the seat.",
 MA,ROSE,YES())
s4=sign("COMMON MYTH","Feet touching the back seat",
 "Bent legs are fine. UK road safety teams say feet reaching the end of the seat is not a sign to move. Rear-facing still protects the head, neck and spine.",
 EL,GREY,NO())
s5=sign("HARNESS SEATS","Shoulders at the top harness slot",
 "Move the headrest up as they grow. When the shoulders are level with the highest harness position, or the harness no longer fits, it's time for the next seat.",
 E0,MINT,YES())
s6=sign("I-SIZE SEATS","Read the cm on the label",
 "i-Size seats show a height range in cm. They must stay rear-facing until at least 15 months. That's the minimum, not the target.",
 None,PINK,f'<span class="pill" style="background:{MINT}">Measure your child, then check the label</span>',("cm, not age",150,900))
s7=sign("OLDER R44 SEATS","Not into a booster before 15 kg",
 "Group 1 harness seats go up to 18 kg. Road safety teams advise: keep the harness until at least 15 kg, the start of group 2.",
 None,ROSE,NO("Under 15 kg? Not yet"),("15 kg",200,900))
s8=sign("BOOSTERS","Keep the high back",
 "New backless booster cushions are only approved for children over 125 cm and 22 kg. RoSPA advises against taking the back off: it protects the head in a side crash.",
 PA,GREY,f'<span class="pill" style="background:{NAVY};color:#fff">High back + side wings</span>')
s9=sign("OUT OF THE BOOSTER","12 years or 135 cm, then check the belt",
 "UK law: a car seat until 12 years or 135 cm, whichever comes first. The lap belt should sit on the hips, not the tummy. The diagonal belt on the shoulder, not the neck.",
 None,MINT,f'<span class="pill" style="background:{PINK}">Belt doesn\'t fit yet? Keep the booster</span>',("135 cm",200,900))
s10=deco+f'''<div class="card"><div style="position:relative;height:470px;background:{PINK}">
<img src="data:image/png;base64,{MA}" style="position:absolute;left:70px;bottom:40px;height:270px;{SH}">
<img src="data:image/png;base64,{EL}" style="position:absolute;left:340px;bottom:40px;height:320px;{SH}">
<img src="data:image/png;base64,{PA}" style="position:absolute;left:640px;bottom:40px;height:370px;{SH}"></div>
<div style="padding:44px 60px 0"><div class="h" style="font-size:72px">Ready for the next seat? Check the price first</div>
<div style="font-size:38px;font-weight:500;margin-top:20px">Compare car seat prices from UK shops in one place.</div>
<div style="margin-top:34px;display:flex;align-items:center;gap:16px"><div class="h" style="font-size:44px;background:{MINT};padding:20px 30px;border-radius:24px">babysorted.com/links</div>
<div style="background:{NAVY};color:#fff;font-weight:800;font-size:30px;padding:20px 24px;border-radius:24px;white-space:nowrap">Link in bio ↑</div></div>
<div style="margin-top:22px;font-size:30px;font-weight:700;opacity:.55">Save this post for later</div></div></div>'''
bodies=[cover,s2,s3,s4,s5,s6,s7,s8,s9,s10]; n=len(bodies)
rows=[("✓","Over the seat's weight or height limit","Not a birthday."),("✓","Baby seat: head above the top of the shell",""),("✕","Feet touching the back seat","Bent legs are fine."),
      ("✓","Shoulders at the top harness slot",""),("✕","Under 15 kg in an R44 seat","Keep the harness."),("i","Booster cushions: 125 cm and 22 kg+","Keep the high back."),("i","Law: 12 years or 135 cm","Then check the belt fits.")]
rr="".join(f'''<div style="display:flex;gap:18px;align-items:center;padding:12px 0;border-top:{"0" if i==0 else "2px solid #EEF0F3"}"><div style="flex:none;width:50px;height:50px;border-radius:50%;background:{NAVY if s=="✓" else (PINK if s=="✕" else MINT)};color:{"#fff" if s=="✓" else NAVY};display:flex;align-items:center;justify-content:center;font-weight:800;font-size:26px">{s}</div>
<div><div class="h" style="font-size:32px">{t}</div>{"<div style='font-size:25px;font-weight:500;opacity:.8;margin-top:3px'>"+d+"</div>" if d else ""}</div></div>''' for i,(s,t,d) in enumerate(rows))
pin=f'''{star(30,26,30,"#fff")}{star(940,30,24,NAVY,.25)}
<div style="position:absolute;left:50px;right:50px;top:50px">
<div class="tags"><span class="tag t1" style="font-size:24px">Tips</span><span class="tag t2" style="font-size:24px">Car Seats</span></div>
<div class="h" style="font-size:70px;margin-top:20px">When to move to the next car seat</div>
<div style="font-size:30px;font-weight:600;opacity:.75;margin-top:12px">Not by age. By height and fit.</div></div>
<div style="position:absolute;left:50px;width:290px;top:600px;height:90px;background:#fff;border-radius:26px 26px 0 0"></div>
<div style="position:absolute;left:355px;width:290px;top:530px;height:160px;background:{PINK};border-radius:26px 26px 0 0"></div>
<div style="position:absolute;left:660px;width:290px;top:460px;height:230px;background:{ROSE};border-radius:26px 26px 0 0"></div>
<img src="data:image/png;base64,{MA}" style="position:absolute;left:85px;top:400px;height:200px;{SH}">
<img src="data:image/png;base64,{EL}" style="position:absolute;left:385px;top:310px;height:220px;{SH}">
<img src="data:image/png;base64,{PA}" style="position:absolute;left:690px;top:215px;height:245px;{SH}">
<div style="position:absolute;left:50px;right:50px;top:690px;background:#fff;border-radius:0 0 36px 36px;padding:20px 40px 26px">{rr}</div>
<div style="position:absolute;left:50px;right:50px;bottom:40px;display:flex;justify-content:space-between;align-items:center"><div class="brand" style="font-size:32px">BabySorted</div><div style="font-weight:700;font-size:24px">Compare car seat prices from UK shops at babysorted.com</div></div>'''
with sync_playwright() as p:
    br=p.chromium.launch(); pg=br.new_page(viewport=dict(width=1080,height=1350))
    for i,bd in enumerate(bodies):
        pg.set_content(f"<html><head><style>{CSS}</style></head><body>{bd}{foot(i,n)}</body></html>"); pg.wait_for_timeout(250)
        pg.screenshot(path=f"{OUT}/slide_{i+1}.png")
    pg2=br.new_page(viewport=dict(width=1000,height=1500),device_scale_factor=2)
    pg2.set_content(f"<html><head><style>{CSS.replace('width:1080px;height:1350px','width:1000px;height:1500px')}</style></head><body>{pin}</body></html>"); pg2.wait_for_timeout(250)
    pg2.screenshot(path=f"{OUT}/pin.png"); br.close()
from PIL import Image
W=Image.new('RGB',(1500,1250),'white')
for k in range(n): W.paste(Image.open(f'{OUT}/slide_{k+1}.png').resize((288,360)),((k%5)*300,(k//5)*380))
W.paste(Image.open(f'{OUT}/pin.png').resize((300,450)),(1200,780)); W.save(f'{OUT}/preview.png')
