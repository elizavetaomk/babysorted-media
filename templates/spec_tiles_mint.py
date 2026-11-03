# Mint "spec tiles" layout: mint bg; cover = product with rising age ladder; pick slides = white panel with whole product,
# three stacked stat tiles, then "Best for" + "Watch out". Price table slide shows label price vs ready-for-a-baby price.
# Used for: Best high chairs that grow with your child (3 Nov 2026). Run from folder with cut/*.png; writes ./out_chairs
from playwright.sync_api import sync_playwright
import base64, os
NAVY="#051F45"; MINT="#DDF5E3"; DMINT="#BFE8CB"
b=lambda f: base64.b64encode(open(f,"rb").read()).decode()
TT=b("cut/tripp.png"); KL=b("cut/klapp.png"); LE=b("cut/lemo.png"); L2=b("cut/lemo2.png"); HA=b("cut/hauck_t.png")
OUT="out_chairs"; os.makedirs(OUT,exist_ok=True)
SH="filter:drop-shadow(0 16px 16px rgba(5,31,69,.16))"
def star(x,y,s,c,o=1): return f'<svg style="position:absolute;left:{x}px;top:{y}px;opacity:{o}" width="{s}" height="{s}" viewBox="0 0 20 20"><path d="M10 0l2.6 7.4L20 10l-7.4 2.6L10 20l-2.6-7.4L0 10l7.4-2.6z" fill="{c}"/></svg>'
CSS=f"""*{{margin:0;padding:0;box-sizing:border-box}} body{{width:1080px;height:1350px;background:{MINT};font-family:Inter;color:{NAVY};position:relative;overflow:hidden}}
.h{{font-weight:800;letter-spacing:-0.035em;line-height:1.05}}
.tags{{display:flex;gap:14px}} .tag{{font-weight:700;font-size:28px;padding:9px 22px;border-radius:30px}}
.t1{{background:{NAVY};color:#fff}} .t2{{background:#fff;box-shadow:inset 0 0 0 3px {NAVY}}}
.kick{{font-weight:800;font-size:28px;letter-spacing:.06em;opacity:.6}}
.foot{{position:absolute;left:70px;right:70px;bottom:50px;display:flex;justify-content:space-between;align-items:center}}
.brand{{font-weight:800;font-size:36px;letter-spacing:-0.03em}}
.pill{{display:inline-block;font-weight:800;font-size:30px;padding:13px 24px;border-radius:24px;white-space:nowrap}}"""
def foot(i,n):
    d="".join(f'<div style="width:{40 if j==i else 14}px;height:14px;border-radius:7px;background:{NAVY};opacity:{1 if j==i else .25}"></div>' for j in range(n))
    return f'<div class="foot"><div class="brand">BabySorted</div><div style="display:flex;gap:12px">{d}</div></div>'
deco=star(36,30,26,"#fff")+star(1000,36,30,"#fff")
im=lambda s,h,x="": f'<img src="data:image/png;base64,{s}" style="height:{h}px;max-width:100%;object-fit:contain;{SH};{x}">'
def tile(k,v):
    return f'<div style="background:{MINT};border-radius:26px;padding:18px 24px"><div style="font-weight:800;font-size:22px;letter-spacing:.06em;opacity:.6">{k}</div><div class="h" style="font-size:42px;margin-top:6px">{v}</div></div>'
def pick(k,name,best,pic,h,tiles,good,watch):
    t="".join(tile(a,c) for a,c in tiles)
    return deco+f'''<div style="position:absolute;left:60px;right:60px;top:60px;height:640px;background:#fff;border-radius:44px;display:flex;align-items:center;padding:30px 36px;gap:26px">
<div style="flex:1;display:flex;justify-content:center;align-items:center;height:100%">{im(pic,h)}</div><div style="flex:none;width:350px;display:flex;flex-direction:column;gap:16px">{t}</div></div>
<div style="position:absolute;left:96px;top:86px;font-weight:800;font-size:26px;background:{NAVY};color:#fff;padding:7px 16px;border-radius:18px">{k} of 4</div>
<div style="position:absolute;left:70px;right:70px;top:726px"><div class="h" style="font-size:74px">{name}</div>
<div style="margin-top:14px"><span class="pill" style="background:{NAVY};color:#fff">{best}</span></div>
<div style="font-size:37px;font-weight:500;line-height:1.36;margin-top:22px">{good}</div>
<div style="font-size:37px;font-weight:500;line-height:1.36;margin-top:12px"><b style="font-weight:800">Watch out:</b> {watch}</div></div>'''
def step(l,bot,h,t,sub):
    return f'<div style="position:absolute;left:{l}px;bottom:{bot}px;width:190px;height:{h}px;background:#fff;border-radius:26px 26px 0 0;padding:16px 18px"><div class="h" style="font-size:33px">{t}</div><div style="font-size:23px;font-weight:600;opacity:.7;margin-top:4px">{sub}</div></div>'
cover=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="tags"><span class="tag t1">Buying guide</span><span class="tag t2">Kids Furniture</span></div>
<div class="h" style="font-size:96px;margin-top:28px;width:800px">Best high chairs that grow with your child</div>
<div style="font-size:40px;font-weight:600;opacity:.75;margin-top:20px">Buy once. Use it for years.</div>
<div style="margin-top:24px;display:inline-block;background:{NAVY};color:#fff;font-weight:700;font-size:30px;padding:14px 28px;border-radius:40px">Swipe before you buy</div></div>
<div style="position:absolute;left:60px;right:60px;bottom:126px;height:6px;background:{NAVY};opacity:.12"></div>
{step(60,132,120,"6 months","Baby set on")}{step(260,132,210,"3 years","Baby set off")}{step(460,132,300,"Adult","Still a chair")}
<img src="data:image/png;base64,{TT}" style="position:absolute;right:24px;bottom:132px;height:670px;{SH}">'''
s2=deco+f'''<div style="position:absolute;left:70px;right:70px;top:70px"><div class="kick">FIRST, THE BASICS</div><div class="h" style="font-size:84px;margin-top:8px">“Grows with your child” means two things</div></div>
<div style="position:absolute;left:60px;right:60px;top:380px;bottom:150px;display:flex;gap:22px">
<div style="flex:1;background:#fff;border-radius:40px;padding:36px"><div style="height:330px;display:flex;align-items:center;justify-content:center;background:{MINT};border-radius:28px;font-weight:800;font-size:96px;letter-spacing:-.04em">6-in-1</div><div class="h" style="font-size:50px;margin-top:26px">Multi-mode</div><div style="font-size:35px;font-weight:500;line-height:1.36;margin-top:14px">Changes shape. Which? says many of these last as furniture up to age 5.</div></div>
<div style="flex:1;background:#fff;border-radius:40px;padding:36px"><div style="height:330px;display:flex;align-items:center;justify-content:center;background:{MINT};border-radius:28px">{im(KL,300)}</div><div class="h" style="font-size:50px;margin-top:26px">Growing chair</div><div style="font-size:35px;font-weight:500;line-height:1.36;margin-top:14px">Stays one chair, made to last into adult years. These are our four picks.</div></div></div>'''
PR=[("Stokke Tripp Trapp","£219","£299","Baby Set + tray"),("Cybex Lemo","£209.95","from £211","3-in-1 set"),("KAOS Klapp beech","£191.20","about £297","Rail + tray"),("Hauck Alpha+","£69.95","£109.90","Plus tray")]
pr="".join(f'''<div style="display:flex;align-items:center;padding:24px 0;border-top:{"0" if i==0 else f"3px solid {MINT}"}"><div style="flex:1"><div class="h" style="font-size:40px">{a}</div><div style="font-size:27px;font-weight:600;opacity:.6;margin-top:4px">{d}</div></div><div style="width:170px;text-align:right;font-size:36px;font-weight:600;opacity:.6">{c}</div><div style="width:270px;text-align:right;white-space:nowrap" class="h"><span style="font-size:44px">{e}</span></div></div>''' for i,(a,c,e,d) in enumerate(PR))
s3=deco+f'''<div style="position:absolute;left:70px;right:70px;top:70px"><div class="kick">THE CATCH</div><div class="h" style="font-size:84px;margin-top:8px">The label price isn't the baby price</div>
<div style="font-size:37px;font-weight:500;line-height:1.36;margin-top:16px">The chair alone often isn't ready for a baby. Add up the extras before you compare.</div></div>
<div style="position:absolute;left:60px;right:60px;top:470px;background:#fff;border-radius:40px;padding:24px 44px 26px"><div style="display:flex;font-weight:800;font-size:24px;letter-spacing:.05em;opacity:.55;padding:10px 0"><div style="flex:1"></div><div style="width:170px;text-align:right">CHAIR</div><div style="width:270px;text-align:right">BABY-READY</div></div>{pr}</div>
<div style="position:absolute;left:74px;right:70px;top:1136px;font-size:27px;font-weight:600;opacity:.65">Prices from the BabySorted catalog on 2 Nov. Best price varies by shop and colour.</div>'''
s4=pick(1,"Stokke Tripp Trapp","Best for keeping for life",TT,540,[("START","6 months"),("SEAT","Footplate moves too"),("TAKES UP TO","136 kg")],
 "Seat and footplate both adjust. NHS feeding advice says a footrest keeps feet flat and helps stop slouching.","the Baby Set and tray cost extra on the basic chair.")
s5=pick(2,"Cybex Lemo","Best for quick changes",LE,380,[("START","6 months"),("ADJUST","One-handed, no tools"),("TAKES UP TO","120 kg")],
 "The chair alone starts at 3 years, so a baby needs the 3-in-1 set: chair, Baby Set and tray.","the sets we checked don't list a harness. Ask the shop.")
s6=pick(3,"KAOS Klapp","Best for small kitchens",KL,540,[("FOLDED DEPTH","13 cm"),("WEIGHT","About 5 kg"),("TAKES UP TO","110 kg")],
 "Arrives built and folds flat in seconds, even with the rail and tray on. Handy in a small kitchen.","fixed steps, so nothing adjusts. The rail is for up to 3 years or 15 kg.")
s7=pick(4,"Hauck Alpha+","Best on a budget",HA,520,[("START","6 months"),("HARNESS","5-point listed"),("TAKES UP TO","90 kg")],
 "A wooden step chair for £69.95. Seat and footplate both adjust, like the big names.","the tray costs extra. Check what your shop includes.")
CK=[("Harness in the box","RoSPA says always use one, five-point if you can. On some chairs it's a separate buy."),("A fixed post between the legs","It stops a child sliding down and getting trapped under the tray."),("BS EN 14988:2017 on the label","Trading Standards says to check for this safety standard's number on the chair."),]
ck="".join(f'''<div style="display:flex;gap:24px;padding:34px 0;border-top:{"0" if i==0 else f"3px solid {MINT}"}"><div style="flex:none;width:60px;height:60px;border-radius:18px;background:{NAVY};color:#fff;font-weight:800;font-size:32px;display:flex;align-items:center;justify-content:center">✓</div><div><div class="h" style="font-size:47px">{a}</div><div style="font-size:37px;font-weight:500;line-height:1.34;margin-top:10px">{c}</div></div></div>''' for i,(a,c) in enumerate(CK))
s8=deco+f'''<div style="position:absolute;left:70px;right:70px;top:70px"><div class="kick">BEFORE YOU PAY</div><div class="h" style="font-size:72px;margin-top:8px;white-space:nowrap">3 safety checks on any chair</div></div>
<div style="position:absolute;left:60px;right:60px;top:220px;background:#fff;border-radius:40px;padding:28px 44px 34px">{ck}</div>'''
US=[("Start when they sit unaided","Head steady, around 6 months. The NHS says sat upright and strapped in, so they can swallow properly."),("Never rely on the tray","Trading Standards: a tray won't hold a child in. Use the harness every meal."),("Mind the push-off","Use a level, non-slip floor. Children can push against tables and walls, so check the chair stays stable.")]
us="".join(f'''<div style="padding:26px 0;border-top:{"0" if i==0 else f"3px solid {MINT}"}"><div class="h" style="font-size:47px">{a}</div><div style="font-size:36px;font-weight:500;line-height:1.34;margin-top:8px">{c}</div></div>''' for i,(a,c) in enumerate(US))
s9=deco+f'''<div style="position:absolute;left:70px;right:70px;top:70px"><div class="kick">ONCE IT'S HOME</div><div class="h" style="font-size:84px;margin-top:8px">Use it the safe way</div></div>
<div style="position:absolute;left:60px;right:60px;top:210px;background:#fff;border-radius:40px;padding:22px 44px 30px">{us}<div style="margin-top:10px"><span class="pill" style="background:{NAVY};color:#fff">Never leave them alone in it</span></div></div>'''
s10=deco+f'''<div style="position:absolute;left:60px;right:60px;top:60px;height:560px;background:#fff;border-radius:44px;display:flex;align-items:flex-end;justify-content:center;gap:26px;padding:36px">{im(HA,370,"flex:none")}{im(TT,450,"flex:none")}{im(KL,420,"flex:none")}</div>
<div style="position:absolute;left:70px;right:70px;top:660px"><div class="h" style="font-size:80px">Found your chair? Compare prices first</div>
<div style="font-size:38px;font-weight:500;margin-top:18px">Compare high chair prices from UK shops in one place.</div>
<div style="margin-top:30px;display:flex;align-items:center;gap:16px"><div class="h" style="font-size:46px;background:#fff;padding:22px 32px;border-radius:24px">babysorted.com/links</div>
<div style="background:{NAVY};color:#fff;font-weight:800;font-size:32px;padding:22px 26px;border-radius:24px;white-space:nowrap">Link in bio ↑</div></div>
<div style="margin-top:22px;font-size:32px;font-weight:700;opacity:.55">Save this post for later</div></div>'''
bodies=[cover,s2,s3,s4,s5,s6,s7,s8,s9,s10]; n=len(bodies)
PN=[(TT,"Stokke Tripp Trapp","Best for keeping for life","£299","with Baby Set + tray"),(L2,"Cybex Lemo","Best for quick changes","from £211","3-in-1 set"),(KL,"KAOS Klapp","Best for small kitchens","about £297","with rail + tray"),(HA,"Hauck Alpha+","Best on a budget","£109.90","with tray")]
pn="".join(f'''<div style="display:flex;align-items:center;gap:20px;background:#fff;border-radius:28px;padding:14px 26px 14px 16px;margin-top:14px"><div style="flex:none;width:130px;height:150px;display:flex;align-items:center;justify-content:center"><img src="data:image/png;base64,{s}" style="max-width:124px;max-height:146px"></div><div style="flex:1"><div class="h" style="font-size:38px">{a}</div><div style="font-size:26px;font-weight:600;opacity:.75;margin-top:6px">{c}</div></div><div style="text-align:right"><div class="h" style="font-size:36px">{e}</div><div style="font-size:21px;font-weight:600;opacity:.6;margin-top:4px">{f}</div></div></div>''' for s,a,c,e,f in PN)
pin=f'''{star(910,50,32,"#fff")}<div style="position:absolute;left:60px;right:60px;top:60px"><div class="tags"><span class="tag t1" style="font-size:24px">Buying guide</span><span class="tag t2" style="font-size:24px">Kids Furniture</span></div>
<div class="h" style="font-size:76px;margin-top:20px">Best high chairs that grow with your child</div>
<div style="font-size:31px;font-weight:600;opacity:.75;margin-top:12px">The label price isn't the baby price. Add the extras first.</div></div>
<div style="position:absolute;left:60px;right:60px;top:368px">{pn}</div>
<div style="position:absolute;left:60px;right:60px;top:1168px;background:{NAVY};color:#fff;border-radius:26px;padding:22px 28px"><div style="font-weight:800;font-size:22px;opacity:.7;letter-spacing:.06em">BEFORE YOU PAY</div><div style="font-size:28px;font-weight:600;margin-top:4px;line-height:1.3">Check for a 5-point harness, a fixed post between the legs and BS EN 14988:2017 on the label.</div></div>
<div style="position:absolute;left:60px;right:60px;bottom:40px;display:flex;justify-content:space-between;align-items:center"><div class="brand" style="font-size:34px">BabySorted</div><div style="font-weight:700;font-size:25px">Compare high chair prices at babysorted.com</div></div>'''
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
