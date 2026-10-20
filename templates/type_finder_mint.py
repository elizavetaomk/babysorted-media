from playwright.sync_api import sync_playwright
import base64
PUMP=base64.b64encode(open("/home/claude/pump/pump_cut.png","rb").read()).decode()
IMG={k:base64.b64encode(open(f"/home/claude/pump/{k}_cut.png","rb").read()).decode() for k in ["single","double","wear"]}
IMG["manual"]=PUMP
SH="filter:drop-shadow(0 16px 14px rgba(5,31,69,.18))"
PINK="#F1D3DF"; NAVY="#051F45"; ROSE="#E6B6C9"; MINT="#DDF5E3"; DMINT="#BFE8CB"
def star(x,y,s,c,o=1): return f'<svg style="position:absolute;left:{x}px;top:{y}px;opacity:{o}" width="{s}" height="{s}" viewBox="0 0 20 20"><path d="M10 0l2.6 7.4L20 10l-7.4 2.6L10 20l-2.6-7.4L0 10l7.4-2.6z" fill="{c}"/></svg>'
CSS=f"""*{{margin:0;padding:0;box-sizing:border-box}} body{{width:1080px;height:1350px;background:{MINT};font-family:Inter;color:{NAVY};position:relative;overflow:hidden}}
.h{{font-weight:800;letter-spacing:-0.035em;line-height:1.04}}
.tags{{display:flex;gap:14px}} .tag{{font-weight:700;font-size:28px;padding:9px 22px;border-radius:30px}}
.t1{{background:{NAVY};color:#fff}} .t2{{background:#fff;box-shadow:inset 0 0 0 3px {NAVY}}}
.card{{position:absolute;left:70px;right:70px;top:90px;bottom:150px;background:#fff;border-radius:44px}}
.foot{{position:absolute;left:90px;right:90px;bottom:58px;display:flex;justify-content:space-between;align-items:center}}
.brand{{font-weight:800;font-size:38px;letter-spacing:-0.03em}}"""
deco=star(40,30,36,"#fff")+star(1000,40,28,NAVY,.25)+star(1010,1190,34,"#fff")+star(30,1230,22,NAVY,.25)
def foot(i,n):
    d="".join(f'<div style="width:{40 if j==i else 14}px;height:14px;border-radius:7px;background:{NAVY};opacity:{1 if j==i else .25}"></div>' for j in range(n))
    return f'<div class="foot"><div class="brand">BabySorted</div><div style="display:flex;gap:12px">{d}</div></div>'
TYPES=[("Manual","Now and then",1,1,PINK),("Single electric","About once a day",2,2,"#F3F4F6"),("Double electric","Often, or back at work",3,3,ROSE),("Wearable","On the move",2,3,DMINT)]
def scale(n,total=3,size=26):
    return "".join(f'<span style="display:inline-block;width:{size}px;height:{size}px;border-radius:50%;margin-right:8px;background:{NAVY if k<n else "transparent"};box-shadow:inset 0 0 0 3px {NAVY};opacity:{1 if k<n else .35}"></span>' for k in range(total))
def pounds(n): return f'<span style="font-weight:800">{"£"*n}</span><span style="font-weight:800;opacity:.2">{"£"*(3-n)}</span>'
def cover():
    opts="".join(f'''<div style="display:flex;align-items:center;gap:24px;background:{c};border-radius:28px;padding:22px 30px;margin-top:16px">
<div style="flex:none;width:56px;height:56px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:28px">{"ABCD"[i]}</div>
<div class="h" style="font-size:44px">{n}</div></div>''' for i,(n,f,_,_,c) in enumerate(TYPES))
    return f"""{deco}<div class="card"></div>
<div style="position:absolute;left:680px;top:150px;width:280px;height:340px;border-radius:36px;background:{PINK}"></div>
<img src="data:image/png;base64,{PUMP}" style="position:absolute;left:690px;top:170px;height:290px;{SH}">
<div style="position:absolute;left:130px;right:130px;top:160px">
<div class="tags"><span class="tag t1">Buying guide</span><span class="tag t2">Nursing &amp; Feeding</span></div>
<div class="h" style="font-size:72px;margin-top:30px;width:500px">Which breast pump is right for you?</div>
<div style="margin-top:56px">{opts}</div>
<div style="margin-top:34px;font-weight:700;font-size:34px;opacity:.7">Swipe to find your match</div></div>"""
def question():
    rows="".join(f'''<div style="display:flex;justify-content:space-between;align-items:center;padding:30px 0;border-top:{"0" if i==0 else "3px solid #EEF2F0"}">
<div style="font-size:42px;font-weight:600">{f}</div><div style="font-weight:800;font-size:34px;background:{c};padding:12px 24px;border-radius:24px">{n}</div></div>''' for i,(n,f,_,_,c) in enumerate(TYPES))
    return f"""{deco}<div class="card"></div><div style="position:absolute;left:130px;right:130px;top:170px">
<div style="font-weight:800;font-size:30px;letter-spacing:.06em;opacity:.5">START WITH ONE QUESTION</div>
<div class="h" style="font-size:100px;margin-top:18px">How often will you pump?</div>
<div style="margin-top:50px">{rows}</div></div>"""
def ptype(idx,best,good,watch,img=""):
    n,f,freq,price,c=TYPES[idx]
    row=lambda lab,txt,col: f'<div style="display:flex;gap:24px;padding:28px 0;border-top:3px solid #EEF2F0"><div style="flex:none;width:200px;font-weight:800;font-size:30px;color:{col};padding-top:6px">{lab}</div><div style="font-size:40px;font-weight:500;line-height:1.35">{txt}</div></div>'
    return f"""{deco}<div class="card" style="overflow:hidden"><div style="height:430px;background:{c}"></div></div>
<div style="position:absolute;left:130px;right:130px;top:160px">
<div style="font-weight:700;font-size:30px;opacity:.6">Type {idx+1} of 4</div>
<div class="h" style="font-size:{(110 if len(n)<10 else 88) if img else (110 if len(n)<10 else 96)}px;margin-top:12px;{"width:470px" if img else ""}">{n}</div>
<div style="display:flex;gap:60px;margin-top:34px">
<div><div style="font-weight:800;font-size:24px;letter-spacing:.06em;opacity:.55">HOW OFTEN</div><div style="margin-top:12px">{scale(freq)}</div></div>
<div><div style="font-weight:800;font-size:24px;letter-spacing:.06em;opacity:.55">PRICE</div><div style="margin-top:4px;font-size:40px">{pounds(price)}</div></div></div></div>
{img}<div style="position:absolute;left:130px;right:130px;top:560px">{row("Best if",best,NAVY)}{row("Good",good,"#2E7D5B")}{row("Watch out",watch,"#B5476E")}</div>"""
def checks():
    items=[("Flange size","The wrong size can hurt and lower your milk flow. Pick a pump that offers more sizes."),
           ("Noise","A quiet pump matters for night feeds and the office."),
           ("Spare parts","Check that shops sell valves and tubes, and what they cost.")]
    rows="".join(f'''<div style="display:flex;gap:26px;padding:28px 0;border-top:{"0" if i==0 else "3px solid #EEF2F0"}">
<div style="flex:none;width:64px;height:64px;border-radius:50%;background:{MINT};display:flex;align-items:center;justify-content:center;font-weight:800;font-size:32px">{i+1}</div>
<div><div class="h" style="font-size:46px">{t}</div><div style="font-size:36px;font-weight:500;line-height:1.35;margin-top:8px">{b}</div></div></div>''' for i,(t,b) in enumerate(items))
    return f"""{deco}<div class="card"></div><div style="position:absolute;left:130px;right:130px;top:170px">
<div style="font-weight:800;font-size:30px;letter-spacing:.06em;opacity:.5">BEFORE YOU BUY</div>
<div class="h" style="font-size:90px;margin-top:18px">3 things to check on any pump</div>
<div style="margin-top:36px">{rows}</div>
<div style="margin-top:20px;font-size:30px;font-weight:600;opacity:.6">Not sure? Ask your midwife or health visitor.</div></div>"""
def cta():
    chips="".join(f'<span style="font-weight:800;font-size:28px;background:{c};padding:10px 20px;border-radius:22px">{n}</span>' for n,f,_,_,c in TYPES)
    return f"""{deco}<div class="card"></div><div style="position:absolute;left:130px;right:130px;top:0;bottom:150px;display:flex;flex-direction:column;justify-content:center">
<div style="align-self:flex-start;background:{PINK};border-radius:36px;padding:20px 40px;margin-bottom:36px"><img src="data:image/png;base64,{PUMP}" style="height:230px;display:block;{SH}"></div>
<div style="display:flex;gap:12px;flex-wrap:wrap">{chips}</div>
<div class="h" style="font-size:80px;margin-top:36px">Know your type? Check the price first</div>
<div style="font-size:40px;font-weight:500;margin-top:26px">Compare breast pump prices from UK shops in one place.</div>
<div style="margin-top:44px;display:flex;align-items:center;gap:16px;align-self:flex-start"><div class="h" style="font-size:46px;background:{MINT};padding:22px 32px;border-radius:24px">babysorted.com/links</div>
<div style="background:{NAVY};color:#fff;font-weight:800;font-size:32px;padding:22px 26px;border-radius:24px;white-space:nowrap">Link in bio ↑</div></div>
<div style="margin-top:26px;font-size:32px;font-weight:700;opacity:.55">Save this post for later</div></div>"""
bodies=[cover(),question(),
 ptype(0,"You pump now and then, for a bottle or two.","Small, quiet and cheap. No battery needed.","Slow, and your hand gets tired.",f'<img src="data:image/png;base64,{PUMP}" style="position:absolute;right:120px;top:130px;height:350px;{SH}">'),
 ptype(1,"You pump about once a day.","Less effort than manual. Easy to carry.","One side at a time takes longer.",f'<img src="data:image/png;base64,{IMG["single"]}" style="position:absolute;right:110px;top:120px;height:370px;max-width:400px;object-fit:contain;{SH}">'),
 ptype(2,"You pump often or go back to work.","Both sides at once, so it saves time.","Bigger and louder. Costs more.",f'<img src="data:image/png;base64,{IMG["double"]}" style="position:absolute;right:110px;top:140px;height:330px;max-width:400px;object-fit:contain;{SH}">'),
 ptype(3,"You want to pump on the move.","Fits in your bra. No tubes, hands free.","Often the priciest. Some mums collect less milk.",f'<img src="data:image/png;base64,{IMG["wear"]}" style="position:absolute;right:110px;top:130px;height:340px;max-width:400px;object-fit:contain;{SH}">'),
 checks(),cta()]
n=len(bodies)
# Pinterest
prow="".join(f'''<div style="display:flex;align-items:center;gap:22px;background:{c};border-radius:26px;padding:18px 28px 18px 18px;margin-top:16px">
<div style="flex:none;width:120px;height:120px;background:#fff;border-radius:22px;display:flex;align-items:center;justify-content:center"><img src="data:image/png;base64,{IMG[im]}" style="max-width:104px;max-height:104px"></div>
<div style="flex:1"><div class="h" style="font-size:40px">{nm}</div><div style="font-size:28px;font-weight:600;margin-top:8px;opacity:.8">{bi}</div></div>
<div style="flex:none;text-align:right"><div style="font-size:20px;font-weight:800;letter-spacing:.06em;opacity:.55">HOW OFTEN</div><div style="margin-top:8px">{scale(fq,3,20)}</div>
<div style="font-size:30px;margin-top:6px">{pounds(pr)}</div></div></div>'''
  for (nm,f,fq,pr,c),bi,im in zip(TYPES,["Now and then. Small and cheap.","About once a day.","Often, or back at work.","On the move. Fits in your bra."],["manual","single","double","wear"]))
pin=f"""{star(40,30,34,"#fff")}{star(930,40,26,NAVY,.25)}
<div style="position:absolute;left:50px;right:50px;top:70px;bottom:140px;background:#fff;border-radius:44px"></div>

<div style="position:absolute;left:100px;right:100px;top:120px">
<div class="tags"><span class="tag t1" style="font-size:24px">Buying guide</span><span class="tag t2" style="font-size:24px">Nursing &amp; Feeding</span></div>
<div class="h" style="font-size:78px;margin-top:24px">Which breast pump is right for you?</div>
<div style="font-size:30px;font-weight:600;opacity:.7;margin-top:14px">Start with one question: how often will you pump?</div>
<div style="margin-top:26px">{prow}</div>
<div style="margin-top:30px;background:{NAVY};color:#fff;border-radius:26px;padding:28px 30px"><div style="font-weight:800;font-size:22px;opacity:.6;letter-spacing:.06em">TOP TIP</div>
<div style="font-size:28px;font-weight:600;margin-top:6px;line-height:1.35">Check the flange size. The wrong size can hurt and lower your milk flow.</div></div></div>
<div style="position:absolute;left:60px;right:60px;bottom:48px;display:flex;justify-content:space-between;align-items:center">
<div style="font-weight:700;font-size:27px">Compare breast pump prices from UK shops</div><div class="h" style="font-size:34px">babysorted.com</div></div>"""
with sync_playwright() as p:
    br=p.chromium.launch(); pg=br.new_page(viewport=dict(width=1080,height=1350))
    for i,b in enumerate(bodies):
        pg.set_content(f"<html><head><style>{CSS}</style></head><body>{b}{foot(i,n)}</body></html>"); pg.wait_for_timeout(200)
        pg.screenshot(path=f"/mnt/user-data/outputs/pump/slide_{i+1}.png")
    pg2=br.new_page(viewport=dict(width=1000,height=1500),device_scale_factor=2)
    pg2.set_content(f"<html><head><style>{CSS.replace('width:1080px;height:1350px','width:1000px;height:1500px')}</style></head><body>{pin}</body></html>"); pg2.wait_for_timeout(200)
    pg2.screenshot(path="/mnt/user-data/outputs/pump/pinterest_breast_pump_guide.png"); br.close()
from PIL import Image
W=Image.new('RGB',(1440,900),'white')
for k in range(8): W.paste(Image.open(f'/mnt/user-data/outputs/pump/slide_{k+1}.png').resize((288,360)),((k%5)*288,(k//5)*450))
W.paste(Image.open('/mnt/user-data/outputs/pump/pinterest_breast_pump_guide.png').resize((300,450)),(1140,450))
W.save('/home/claude/preview.png')
