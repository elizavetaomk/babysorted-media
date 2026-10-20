from playwright.sync_api import sync_playwright
import base64
from stagehelpers import stage,pic,RULER_I,ARR_I,I_SIZE
PINK="#F1D3DF"; NAVY="#051F45"; ROSE="#E6B6C9"; MINT="#DDF5E3"
b=lambda f: base64.b64encode(open(f,"rb").read()).decode()
SEAT=b("seat_cut.png"); CARR=b("carrier_cut.png"); BASE=b("base_cut.png")
def star(x,y,s,c,o=1): return f'<svg style="position:absolute;left:{x}px;top:{y}px;opacity:{o}" width="{s}" height="{s}" viewBox="0 0 20 20"><path d="M10 0l2.6 7.4L20 10l-7.4 2.6L10 20l-2.6-7.4L0 10l7.4-2.6z" fill="{c}"/></svg>'
CSS=f"""*{{margin:0;padding:0;box-sizing:border-box}} body{{width:1080px;height:1350px;background:{PINK};font-family:Inter;color:{NAVY};position:relative;overflow:hidden}}
.h{{font-weight:800;letter-spacing:-0.035em;line-height:1.04}}
.tags{{display:flex;gap:14px}} .tag{{font-weight:700;font-size:26px;padding:8px 20px;border-radius:30px}}
.t1{{background:{MINT}}} .t2{{background:#fff;box-shadow:inset 0 0 0 3px {NAVY}}}
.card{{position:absolute;left:50px;right:50px;bottom:130px;background:#fff;border-radius:44px;padding:46px 54px;box-shadow:0 20px 40px rgba(5,31,69,.12)}}
.kick{{font-weight:800;font-size:28px;letter-spacing:.06em;opacity:.5}}
.body{{font-size:38px;font-weight:500;line-height:1.4;margin-top:20px}}
.img{{position:absolute;filter:drop-shadow(0 24px 24px rgba(5,31,69,.18))}}
.foot{{position:absolute;left:70px;right:70px;bottom:52px;display:flex;justify-content:space-between;align-items:center}}
.brand{{font-weight:800;font-size:36px;letter-spacing:-0.03em}}"""
def foot(i,n):
    d="".join(f'<div style="width:{40 if j==i else 14}px;height:14px;border-radius:7px;background:{NAVY};opacity:{1 if j==i else .25}"></div>' for j in range(n))
    return f'<div style="position:absolute;left:0;right:0;bottom:0;height:118px;background:{PINK}"></div><div class="foot"><div class="brand">BabySorted</div><div style="display:flex;gap:12px">{d}</div></div>'
img=lambda src,l,t,h: f'<img class="img" src="data:image/png;base64,{src}" style="left:{l}px;top:{t}px;height:{h}px">'

RULER="".join(f'<div style="position:absolute;left:{300 if k%5 else 270}px;top:{80+k*26}px;width:{40 if k%5 else 70}px;height:4px;background:{NAVY};opacity:.7"></div>' for k in range(21))+f'<div style="position:absolute;left:250px;top:70px;width:6px;height:530px;background:{NAVY};border-radius:3px"></div><div class="h" style="position:absolute;left:150px;top:300px;font-size:56px">cm</div>'
ARR=lambda x,flip: f'<svg style="position:absolute;left:{x}px;top:260px;transform:scaleX({-1 if flip else 1})" width="150" height="120" viewBox="0 0 150 120"><path d="M10 60 H110 M80 25 L120 60 L80 95" fill="none" stroke="{NAVY}" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARROWS=ARR(200,False)+ARR(745,True)
def card(inner): return f'<div class="card">{inner}</div>'
def rule(n,title,body,pic):
    return pic+card(f'<div class="kick">RULE {n} OF 4</div><div class="h" style="font-size:70px;margin-top:14px">{title}</div><div class="body">{body}</div>')
bodies=[
 star(70,80,44,"#fff")+star(960,140,30,"#fff")+img(SEAT,150,-10,1420)+card(f'<div class="tags"><span class="tag t1">Buying guide</span><span class="tag t2">Car Seats</span></div><div class="h" style="font-size:76px;margin-top:22px">i-Size explained: UK car seat rules made simple</div><div style="margin-top:26px;display:inline-block;background:{NAVY};color:#fff;font-weight:700;font-size:30px;padding:14px 28px;border-radius:40px">Swipe for the 4 rules</div>'),
 star(90,90,44,"#fff")+star(930,140,30,"#fff")+star(150,520,24,NAVY,.25)+stage(I_SIZE)+card('<div class="kick">WHAT IS I-SIZE?</div><div class="h" style="font-size:70px;margin-top:14px">The newer safety standard for car seats</div><div class="body">It has stricter rules than the older R44 standard. Here are the 4 that matter most.</div>'),
 rule(1,"Height, not weight","Measure your child in cm. Then check the height range on the seat label. It's easier than guessing their weight.",star(90,90,40,"#fff")+stage(RULER_I+pic(SEAT,520),50)),
 rule(2,"Rear-facing until at least 15 months","Facing backwards protects your baby's head, neck and spine. Keep going for longer if your seat allows.",star(90,90,40,"#fff")+star(930,120,30,"#fff")+stage(pic(CARR,520))),
 rule(3,"Tested for side impacts","i-Size seats must pass side crash tests. Older R44 seats did not have to.",star(930,90,34,"#fff")+stage(ARR_I(False)+pic(SEAT,520)+ARR_I(True),30)),
 rule(4,"Fits with ISOFIX","The seat clicks into fixed points in your car. There's less room for fitting mistakes than with a seat belt. Check your car's fit list first.",star(90,90,40,"#fff")+star(940,110,30,"#fff")+stage(pic(BASE,560))),
 star(80,90,44,"#fff")+star(940,170,34,"#fff")+f'''<div style="position:absolute;left:0;right:0;top:120px;text-align:center"><div class="kick">UK LAW</div>
<div class="h" style="font-size:150px;margin-top:20px">12 years</div><div style="font-size:44px;font-weight:700;margin:6px 0">or</div><div class="h" style="font-size:150px">135 cm</div></div>'''+card('<div class="h" style="font-size:52px">A car seat until 12 years old or 135 cm tall, whichever comes first.</div><div class="body">Got an older R44 seat? It is still legal to use. Check the label on the seat. Breaking the rules can mean a fine of up to £500.</div>'),
 star(80,90,44,"#fff")+star(940,150,34,"#fff")+stage(pic(CARR,500))+card(f'''<div class="h" style="font-size:70px">Looking for an i-Size seat? Check the price first</div><div class="body">Compare car seat prices from UK shops in one place.</div>
<div style="margin-top:30px;display:flex;align-items:center;gap:16px"><div class="h" style="font-size:44px;background:{PINK};padding:20px 30px;border-radius:24px">babysorted.com/links</div>
<div style="background:{NAVY};color:#fff;font-weight:800;font-size:30px;padding:20px 24px;border-radius:24px;white-space:nowrap">Link in bio ↑</div></div>
<div style="margin-top:20px;font-size:30px;font-weight:700;opacity:.55">Save this post for later</div>''')]
n=len(bodies)
rules=[("Height, not weight","Choose the seat by your child's height in cm."),("Rear-facing to 15 months+","Protects head, neck and spine."),("Side impact tested","Older R44 seats did not have to be."),("Fits with ISOFIX","Fewer fitting mistakes. Check your car first.")]
rr="".join(f'''<div style="display:flex;gap:22px;align-items:center;padding:16px 0;border-top:{"0" if i==0 else "2px solid #F3E4EA"}"><div style="flex:none;width:58px;height:58px;border-radius:50%;background:{PINK};display:flex;align-items:center;justify-content:center;font-weight:800;font-size:30px">{i+1}</div>
<div><div class="h" style="font-size:34px">{t}</div><div style="font-size:25px;font-weight:500;opacity:.85;margin-top:4px">{d}</div></div></div>''' for i,(t,d) in enumerate(rules))
pin=f'''{star(70,70,40,"#fff")}{star(880,120,30,"#fff")}{img(SEAT,195,-40,1150)}
<div style="position:absolute;left:44px;right:44px;bottom:44px;background:#fff;border-radius:44px;padding:44px 50px;box-shadow:0 20px 40px rgba(5,31,69,.12)">
<div class="tags"><span class="tag t1" style="font-size:22px">Buying guide</span><span class="tag t2" style="font-size:22px">Car Seats</span></div>
<div class="h" style="font-size:60px;margin-top:18px">i-Size explained: 4 UK car seat rules</div>
<div style="margin-top:14px">{rr}</div>
<div style="margin-top:16px;background:{NAVY};color:#fff;border-radius:22px;padding:20px 26px;font-size:25px;font-weight:600;line-height:1.35"><b>UK law:</b> a car seat until 12 years old or 135 cm, whichever comes first.</div>
<div style="margin-top:20px;display:flex;justify-content:space-between;align-items:center"><div class="brand" style="font-size:32px">BabySorted</div><div style="font-weight:700;font-size:26px">Compare prices at babysorted.com</div></div></div>'''
with sync_playwright() as p:
    br=p.chromium.launch(); pg=br.new_page(viewport=dict(width=1080,height=1350))
    for i,bd in enumerate(bodies):
        pg.set_content(f"<html><head><style>{CSS}</style></head><body>{bd}{foot(i,n)}</body></html>"); pg.wait_for_timeout(200)
        pg.evaluate("""()=>{const c=document.querySelector('.card');document.querySelectorAll('.stage').forEach(s=>{s.style.height=c.getBoundingClientRect().top+'px'})}""")
        pg.screenshot(path=f"/mnt/user-data/outputs/isize/slide_{i+1}.png")
    pg2=br.new_page(viewport=dict(width=1000,height=1500),device_scale_factor=2)
    pg2.set_content(f"<html><head><style>{CSS.replace('width:1080px;height:1350px','width:1000px;height:1500px')}</style></head><body>{pin}</body></html>"); pg2.wait_for_timeout(200)
    pg2.screenshot(path="/mnt/user-data/outputs/isize/pinterest_isize_explained.png"); br.close()
from PIL import Image
W=Image.new('RGB',(1440,900),'white')
for k in range(8): W.paste(Image.open(f'/mnt/user-data/outputs/isize/slide_{k+1}.png').resize((288,360)),((k%5)*288,(k//5)*450))
W.paste(Image.open('/mnt/user-data/outputs/isize/pinterest_isize_explained.png').resize((300,450)),(1140,450))
W.save('/home/claude/preview.png')
