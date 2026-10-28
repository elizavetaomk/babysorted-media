# Navy "fold tests" layout: navy bg, product on pink/white/mint rounded panel, white card with test text.
# Used for: One-hand fold (28 Oct 2026). Run from folder with cut/*.png; writes ./out_fold
from playwright.sync_api import sync_playwright
import base64, os
PINK="#F1D3DF"; NAVY="#051F45"; ROSE="#E6B6C9"; MINT="#DDF5E3"
b=lambda f: base64.b64encode(open(f,"rb").read()).decode()
YO=b("cut/yoyo.png"); YF=b("cut/yoyo_fold.png"); MI=b("cut/minu.png"); MF=b("cut/minu_fold.png")
OUT="out_fold"; os.makedirs(OUT,exist_ok=True)
def star(x,y,s,c,o=1): return f'<svg style="position:absolute;left:{x}px;top:{y}px;opacity:{o}" width="{s}" height="{s}" viewBox="0 0 20 20"><path d="M10 0l2.6 7.4L20 10l-7.4 2.6L10 20l-2.6-7.4L0 10l7.4-2.6z" fill="{c}"/></svg>'
CSS=f"""*{{margin:0;padding:0;box-sizing:border-box}} body{{width:1080px;height:1350px;background:{NAVY};font-family:Inter;color:{NAVY};position:relative;overflow:hidden}}
.h{{font-weight:800;letter-spacing:-0.035em;line-height:1.04}}
.tags{{display:flex;gap:14px}} .tag{{font-weight:700;font-size:28px;padding:9px 22px;border-radius:30px}}
.t1{{background:{MINT};color:{NAVY}}} .t2{{background:#fff;box-shadow:inset 0 0 0 3px {NAVY}}}
.card{{position:absolute;left:60px;right:60px;bottom:140px;background:#fff;border-radius:44px;padding:44px 52px}}
.kick{{font-weight:800;font-size:28px;letter-spacing:.06em;opacity:.5}}
.body{{font-size:37px;font-weight:500;line-height:1.4;margin-top:18px}}
.stage{{position:absolute;left:60px;right:60px;top:70px;display:flex}}
.panel{{border-radius:44px;width:100%;height:100%;display:flex;align-items:center;justify-content:center;gap:50px;padding:36px;position:relative}}
.panel img{{max-height:100%;max-width:100%;object-fit:contain;filter:drop-shadow(0 20px 20px rgba(5,31,69,.18))}}
.foot{{position:absolute;left:80px;right:80px;bottom:56px;display:flex;justify-content:space-between;align-items:center;color:#fff}}
.brand{{font-weight:800;font-size:36px;letter-spacing:-0.03em}}
.pill{{display:inline-block;font-weight:800;font-size:30px;padding:12px 22px;border-radius:22px;white-space:nowrap}}"""
def foot(i,n):
    d="".join(f'<div style="width:{40 if j==i else 14}px;height:14px;border-radius:7px;background:#fff;opacity:{1 if j==i else .3}"></div>' for j in range(n))
    return f'<div class="foot"><div class="brand">BabySorted</div><div style="display:flex;gap:12px">{d}</div></div>'
im=lambda s,h=None,st="": f'<img src="data:image/png;base64,{s}" style="{f"height:{h}px;" if h else ""}{st}">'
deco=star(975,32,30,PINK)+star(36,28,22,"#fff",.5)
def stage(inner,bg): return f'<div class="stage" id="st"><div class="panel" style="background:{bg}">{inner}</div></div>'
pills=lambda *ps: '<div style="display:flex;flex-direction:column;align-items:flex-start;gap:18px">'+"".join(f'<span class="pill" style="background:{bg};{"color:#fff" if bg==NAVY else ""}">{t}</span>' for t,bg in ps)+'</div>'
def test(n,title,body,pic,bg,kick=None):
    k=kick or f"FOLD TEST {n} OF 5"
    return deco+stage(pic,bg)+f'<div class="card"><div class="kick">{k}</div><div class="h" style="font-size:64px;margin-top:12px">{title}</div><div class="body">{body}</div></div>'
cover=deco+f'''<div style="position:absolute;left:60px;right:60px;top:60px;bottom:140px;border-radius:44px;background:{PINK};overflow:hidden">
{star(70,560,30,"#fff")}{star(840,520,22,"#fff")}
<img src="data:image/png;base64,{YO}" style="position:absolute;left:190px;top:520px;height:960px;filter:drop-shadow(0 24px 24px rgba(5,31,69,.22))"></div>
<div style="position:absolute;left:100px;right:100px;top:100px;background:#fff;border-radius:40px;padding:40px 46px;box-shadow:0 20px 40px rgba(5,31,69,.15)">
<div class="tags"><span class="tag t1">Tips</span><span class="tag t2">Pushchairs</span></div>
<div class="h" style="font-size:74px;margin-top:22px">One-hand fold: why it matters more than you think</div>
<div style="margin-top:22px;display:inline-block;background:{NAVY};color:#fff;font-weight:700;font-size:30px;padding:14px 28px;border-radius:40px">Swipe before you buy</div></div>'''
s2=test(0,"Picture the bus stop","Baby in one arm, bag on your shoulder. On London buses, wheelchair users have priority for the space by law. If one needs it, you share the space, fold your buggy or move.",
  f'<div style="display:flex;align-items:center;gap:50px;height:100%">{im(YF,420)}{pills(("1 hand free",NAVY),("Baby in the other arm",PINK))}</div>',MINT,"WHY IT MATTERS")
s3=test(1,"Fold it holding a bag","\"One-hand\" on the box doesn't always mean easy. Which? testers find some folds need a knack. In the shop, hold your bag in one arm, then fold and unfold.",
  f'<div style="display:flex;align-items:center;gap:50px;height:100%">{im(YO,440)}{pills(("Fold ✓",MINT),("Unfold ✓",MINT),("One arm only",NAVY))}</div>',PINK)
s4=test(2,"Check which way the seat faces","Some pushchairs only fold with the seat facing forward, or once the carrycot is off. If your baby will face you, ask the shop to show that fold.",
  f'<div style="display:flex;align-items:center;gap:50px;height:100%">{im(MI,440)}{pills(("Facing you?",PINK),("Facing out?",MINT),("Carrycot on?",NAVY))}</div>',"#fff")
s5=test(3,"Does it stand on its own?","A fold that stands up frees your hand at the car or in a small hallway. It also keeps the seat fabric off a wet floor.",
  f'<div style="display:flex;align-items:center;gap:50px;height:100%">{im(MF,440)}{pills(("Stands up",MINT),("Hands free",NAVY))}</div>',PINK)
s6=test(4,"Lock, strap, lift","Look for a lock that keeps it shut and a strap or handle. Then lift it with one arm. That's how you'll carry it up stairs and onto trains.",
  f'<div style="display:flex;align-items:center;gap:50px;height:100%">{im(YF,430)}{pills(("Locks shut?",PINK),("Strap or handle?",MINT),("One-arm lift?",NAVY))}</div>',"#fff")
ticks="".join(f'<div style="position:absolute;left:6px;top:{k*5}%;width:{60 if k%5==0 else 32}px;height:4px;background:{NAVY};opacity:.7"></div>' for k in range(21))
RULER=(f'<div style="display:flex;align-items:center;gap:18px;height:100%"><div class="h" style="font-size:52px">cm</div>'
       f'<div style="position:relative;width:70px;height:420px"><div style="position:absolute;left:0;top:0;bottom:0;width:6px;background:{NAVY};border-radius:3px"></div>{ticks}</div></div>')
s7=test(5,"Measure your boot","Which? puts every folded pushchair in a car boot to see how much room is left. Measure yours and check the shopping still fits beside it.",
  f'<div style="display:flex;align-items:center;gap:50px;height:100%">{RULER}{im(MF,420)}</div>',MINT)
s8=deco+stage(f'<div style="text-align:center"><div class="h" style="font-size:120px">Click.</div><div class="pill" style="background:{NAVY};color:#fff;font-size:38px;margin-top:20px;padding:14px 30px;border-radius:40px">Locked open before baby goes in</div></div>',PINK)+f'''<div class="card"><div class="kick">FOLD SAFELY</div><div class="h" style="font-size:60px;margin-top:12px">Little fingers away</div>
<div class="body" style="font-size:34px">RoSPA lists trapped fingers as a pushchair injury. Keep your child away from moving parts as you fold. Take bags off the handle first. After unfolding, check it's locked.</div></div>'''
s9=deco+stage(im(YO,420)+im(MF,360),PINK)+f'''<div class="card" style="top:640px"><div class="h" style="font-size:70px">Found a fold that works? Check the price first</div>
<div class="body">Compare pushchair prices from UK shops in one place.</div>
<div style="margin-top:30px;display:flex;align-items:center;gap:16px"><div class="h" style="font-size:44px;background:{PINK};padding:20px 30px;border-radius:24px">babysorted.com/links</div>
<div style="background:{NAVY};color:#fff;font-weight:800;font-size:30px;padding:20px 24px;border-radius:24px;white-space:nowrap">Link in bio ↑</div></div>
<div style="margin-top:20px;font-size:30px;font-weight:700;opacity:.55">Save this post for your shop visit</div></div>'''
bodies=[cover,s2,s3,s4,s5,s6,s7,s8,s9]; n=len(bodies)
tests=[("Fold it holding a bag","Fold and unfold with one arm full."),("Check the seat direction","Some only fold facing forward or with the carrycot off."),("Does it stand on its own?","Frees your hand, keeps fabric off wet floors."),("Lock, strap, lift","Locks shut? Strap? Lift it with one arm."),("Measure your boot","Leave room for the shopping too.")]
rr="".join(f'<div style="display:flex;gap:20px;align-items:center;padding:13px 0;border-top:{"0" if i==0 else "2px solid #EEF0F3"}"><div style="flex:none;width:52px;height:52px;border-radius:50%;background:{MINT};display:flex;align-items:center;justify-content:center;font-weight:800;font-size:26px">{i+1}</div><div><div class="h" style="font-size:33px">{t}</div><div style="font-size:24px;font-weight:500;opacity:.85;margin-top:3px">{d}</div></div></div>' for i,(t,d) in enumerate(tests))
pin=f'''{star(920,40,30,PINK)}{star(40,36,22,"#fff",.5)}
<div style="position:absolute;left:44px;right:44px;top:60px;height:520px;border-radius:40px;background:{PINK};overflow:hidden">{star(60,60,28,"#fff")}{star(830,90,22,"#fff")}
<img src="data:image/png;base64,{YO}" style="position:absolute;left:190px;top:22px;height:440px;filter:drop-shadow(0 20px 20px rgba(5,31,69,.2))">
<img src="data:image/png;base64,{YF}" style="position:absolute;left:590px;top:165px;height:295px;filter:drop-shadow(0 20px 20px rgba(5,31,69,.2))"></div>
<div style="position:absolute;left:44px;right:44px;top:540px;background:#fff;border-radius:40px;padding:36px 44px;box-shadow:0 -10px 30px rgba(5,31,69,.12)">
<div class="tags"><span class="tag t1" style="font-size:22px">Tips</span><span class="tag t2" style="font-size:22px">Pushchairs</span></div>
<div class="h" style="font-size:56px;margin-top:16px">One-hand fold: 5 tests to do in the shop</div>
<div style="margin-top:10px">{rr}</div>
<div style="margin-top:12px;background:{NAVY};color:#fff;border-radius:22px;padding:18px 24px;font-size:23px;font-weight:600;line-height:1.35"><b>Fold safely:</b> keep little fingers away from moving parts, and check it's locked open before baby goes in.</div></div>
<div style="position:absolute;left:50px;right:50px;bottom:34px;display:flex;justify-content:space-between;align-items:center;color:#fff"><div class="brand" style="font-size:30px">BabySorted</div><div style="font-weight:700;font-size:24px">Compare pushchair prices from UK shops at babysorted.com</div></div>'''
with sync_playwright() as p:
    br=p.chromium.launch(); pg=br.new_page(viewport=dict(width=1080,height=1350))
    for i,bd in enumerate(bodies):
        pg.set_content(f"<html><head><style>{CSS}</style></head><body>{bd}{foot(i,n)}</body></html>"); pg.wait_for_timeout(250)
        pg.evaluate("""()=>{const c=document.querySelector('.card');const s=document.getElementById('st');if(c&&s){s.style.height=(c.getBoundingClientRect().top-40-70)+'px'}}""")
        pg.screenshot(path=f"{OUT}/slide_{i+1}.png")
    pg2=br.new_page(viewport=dict(width=1000,height=1500),device_scale_factor=2)
    pg2.set_content(f"<html><head><style>{CSS.replace('width:1080px;height:1350px','width:1000px;height:1500px')}</style></head><body>{pin}</body></html>"); pg2.wait_for_timeout(250)
    pg2.screenshot(path=f"{OUT}/pin.png"); br.close()
from PIL import Image
W=Image.new('RGB',(1500,1250),'white')
for k in range(n): W.paste(Image.open(f'{OUT}/slide_{k+1}.png').resize((288,360)),((k%5)*300,(k//5)*380))
W.paste(Image.open(f'{OUT}/pin.png').resize((300,450)),(1200,780)); W.save(f'{OUT}/preview.png')
