from playwright.sync_api import sync_playwright
import base64, os
PINK="#F1D3DF"; NAVY="#051F45"; ROSE="#E6B6C9"; MINT="#DDF5E3"; RED="#D9485F"
b=lambda f: base64.b64encode(open(f,"rb").read()).decode()
CRIB=b("crib_cut.png"); COT=b("cot_cut.png"); MAT=b("mat_cut.png")
TICK='<svg viewBox="0 0 24 24" width="{s}" height="{s}"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="{c}" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def box(size,checked,rad=None):
    rad=rad or size*0.28
    inner=TICK.format(s=int(size*.8),c=NAVY) if checked else ""
    return f'<div style="flex:none;width:{size}px;height:{size}px;border-radius:{rad}px;background:{MINT if checked else "#fff"};box-shadow:inset 0 0 0 {max(3,size//16)}px {NAVY};display:flex;align-items:center;justify-content:center">{inner}</div>'
def star(x,y,s,c,o=1): return f'<svg style="position:absolute;left:{x}px;top:{y}px;opacity:{o}" width="{s}" height="{s}" viewBox="0 0 20 20"><path d="M10 0l2.6 7.4L20 10l-7.4 2.6L10 20l-2.6-7.4L0 10l7.4-2.6z" fill="{c}"/></svg>'
CSS=f"""*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:{NAVY};font-family:Inter;color:{NAVY};position:relative;overflow:hidden}}
.h{{font-weight:800;letter-spacing:-0.035em;line-height:1.04}}
.paper{{position:absolute;left:80px;right:80px;top:80px;bottom:150px;background:#fff;border-radius:40px}}
.tags{{display:flex;gap:14px}} .tag{{font-weight:700;font-size:28px;padding:9px 22px;border-radius:30px}}
.t1{{background:{MINT}}} .t2{{background:#fff;box-shadow:inset 0 0 0 3px {NAVY}}}
.foot{{position:absolute;left:90px;right:90px;bottom:58px;display:flex;justify-content:space-between;align-items:center;color:#fff}}
.brand{{font-weight:800;font-size:38px;letter-spacing:-0.03em}}
.stage{{position:absolute;left:80px;right:80px;display:flex;align-items:center;justify-content:center}}
.stage img{{max-height:100%;max-width:100%;object-fit:contain;filter:drop-shadow(0 18px 18px rgba(5,31,69,.16))}}"""
deco=star(60,30,40,PINK)+star(980,40,30,"#fff",.6)+star(990,1190,36,PINK)+star(30,1220,24,"#fff",.5)
ITEMS=[("New baby, new mattress","Buy new for each baby. A used one from another home is linked to a higher risk of SIDS."),
("The press test","Press the mattress with your hand. A baby's head should not sink in by more than a few millimetres."),
("Check the safety label","Cots: BS EN 716. Bedside cribs: BS EN 1130. Never fix a normal cot to your bed yourself."),
("Skip pods and nests","They are sold as cosy beds, but there is no safety standard for them as a place to sleep."),
("No sleep in bouncers","Bouncers, swings and hammocks keep babies sitting up. Move your baby to a flat cot to sleep."),
("No weighted sleep bags","Not advised under one year. They can cause overheating and cover your baby's head."),
("Two 1 TOG ≠ one 2 TOG","Two thin sleep bags together are warmer than one thick one. Use the maker's TOG guide for your room."),
("Avoid drop-side cots","Old cots with a side that fully drops down don't meet today's safety standard. Watch for them when buying second-hand.")]
N=len(ITEMS)
def foot(i,n):
    d="".join(f'<div style="width:{40 if j==i else 14}px;height:14px;border-radius:7px;background:#fff;opacity:{1 if j==i else .3}"></div>' for j in range(n))
    return f'<div class="foot"><div class="brand">BabySorted</div><div style="display:flex;gap:12px">{d}</div></div>'
def cover():
    rows="".join(f'<div style="display:flex;align-items:center;gap:22px;padding:13px 0">{box(48,i<3)}<div style="font-weight:700;font-size:34px;{"opacity:.45;text-decoration:line-through" if i<3 else ""}">{t}</div></div>' for i,(t,_) in enumerate(ITEMS[:4]))
    return f"""{deco}<div class="paper"></div>
<div style="position:absolute;left:150px;right:150px;top:160px"><div class="tags"><span class="tag t1">Checklist</span><span class="tag t2">Kids Furniture</span></div>
<div style="font-size:34px;font-weight:700;margin-top:28px;opacity:.6">Before you buy</div>
<div class="h" style="font-size:84px;margin-top:8px">8 safe sleep checks most parents miss</div>
<div style="margin-top:30px">{rows}</div>
<div style="font-weight:700;font-size:30px;opacity:.5;margin-top:6px">+ 4 more inside</div></div>
<img src="data:image/png;base64,{CRIB}" style="position:absolute;right:110px;bottom:175px;height:400px;filter:drop-shadow(0 18px 20px rgba(5,31,69,.18))">"""
def item(k):
    t,bd=ITEMS[k]
    prog="".join(box(60,j<=k,15) for j in range(N))
    pics={0:f'<div style="background:{PINK};border-radius:36px;padding:24px 50px;height:100%;display:flex;align-items:center;justify-content:center"><img src="data:image/png;base64,{MAT}" style="height:100%;max-width:640px;object-fit:contain"></div>',
 1:f'''<svg style="height:100%;max-width:100%" viewBox="0 0 640 300"><rect x="20" y="110" width="600" height="120" rx="30" fill="#fff" stroke="{NAVY}" stroke-width="7"/>
<path d="M240 110 Q320 140 400 110" fill="{PINK}" stroke="{NAVY}" stroke-width="7"/>
<path d="M320 14 V88" stroke="{NAVY}" stroke-width="9" stroke-linecap="round"/><path d="M296 66 L320 92 L344 66" fill="none" stroke="{NAVY}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>
<text x="320" y="285" text-anchor="middle" font-family="Inter" font-weight="800" font-size="40" fill="{RED}">sinks a few mm at most</text></svg>''',
 2:f'<div style="display:flex;align-items:center;gap:30px;height:100%"><img src="data:image/png;base64,{CRIB}" style="height:340px"><div style="display:flex;flex-direction:column;gap:14px"><span style="font-weight:800;font-size:30px;background:{MINT};padding:10px 18px;border-radius:18px">BS EN 716</span><span style="font-weight:800;font-size:30px;background:{PINK};padding:10px 18px;border-radius:18px">BS EN 1130</span></div></div>'}
    pic=f'<div class="stage" id="st">{pics[k]}</div>' if k in pics else ""
    return f"""{deco}<div class="paper"></div>
<div style="position:absolute;left:150px;right:150px;top:150px" id="top">
<div style="display:flex;justify-content:space-between;align-items:center"><span style="font-weight:700;font-size:30px;opacity:.6">Safe sleep checks</span>
<span style="font-weight:800;font-size:34px;background:{PINK};padding:10px 22px;border-radius:26px">{k+1} of {N}</span></div>
<div style="margin-top:50px">{box(120,True,32)}</div>
<div class="h" style="font-size:{88 if len(t)<20 else 76}px;margin-top:36px">{t}</div>
<div style="font-size:40px;line-height:1.45;font-weight:500;margin-top:22px">{bd}</div></div>
{pic}<div id="prog" style="position:absolute;left:150px;right:150px;bottom:210px;display:flex;justify-content:space-between">{prog}</div>"""
def spot():
    mark=lambda n,x,y: f'<div style="position:absolute;left:{x}px;top:{y}px;width:72px;height:72px;border-radius:50%;background:{RED};color:#fff;font-weight:800;font-size:38px;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 8px rgba(217,72,95,.25)">{n}</div>'
    row=lambda n,t,d: f'<div style="display:flex;gap:22px;align-items:flex-start;padding:16px 0"><div style="flex:none;width:52px;height:52px;border-radius:50%;background:{RED};color:#fff;font-weight:800;font-size:28px;display:flex;align-items:center;justify-content:center">{n}</div><div><div class="h" style="font-size:42px">{t}</div><div style="font-size:32px;font-weight:500;margin-top:6px;line-height:1.35">{d}</div></div></div>'
    return f"""{deco}<div class="paper"></div>
<div style="position:absolute;left:150px;right:150px;top:140px">
<div style="font-weight:800;font-size:30px;letter-spacing:.06em;opacity:.5">SPOT THE MISTAKES</div>
<div class="h" style="font-size:72px;margin-top:14px">This cot looks cosy. But it breaks 2 rules.</div></div>
<div style="position:absolute;left:160px;top:430px;width:760px;height:531px"><img src="data:image/png;base64,{COT}" style="width:760px">{mark(1,140,120)}{mark(2,470,270)}</div>
<div style="position:absolute;left:150px;right:150px;top:930px">{row(1,"Loose blanket","It can fall in and cover your baby's face.")}{row(2,"Cot bumper","Not safe for sleep. Keep the cot sides clear.")}</div>"""
def cta():
    prog="".join(box(50,True,13) for _ in range(N))
    return f"""{deco}<div class="paper"></div>
<div class="stage" id="st" style="top:110px;height:420px"><img src="data:image/png;base64,{CRIB}" style="height:380px"></div>
<div style="position:absolute;left:150px;right:150px;top:560px">
<div style="display:flex;gap:12px">{prog}</div>
<div class="h" style="font-size:78px;margin-top:34px">All checked? Now compare prices</div>
<div style="font-size:38px;font-weight:500;margin-top:18px">Compare cot, crib and mattress prices from UK shops in one place.</div>
<div style="margin-top:30px;display:flex;align-items:center;gap:16px"><div class="h" style="font-size:44px;background:{PINK};padding:20px 30px;border-radius:24px">babysorted.com/links</div>
<div style="background:{NAVY};color:#fff;font-weight:800;font-size:32px;padding:20px 26px;border-radius:24px;white-space:nowrap">Link in bio ↑</div></div></div>"""
bodies=[cover()]+[item(k) for k in range(N)]+[spot(),cta()]
n=len(bodies)
# pin
rows="".join(f'<div style="display:flex;align-items:center;gap:22px;padding:9px 0;border-top:{"0" if i==0 else "2px solid #F3E4EA"}">{box(42,False,11)}<div><div class="h" style="font-size:30px">{t}</div><div style="font-size:21px;font-weight:500;opacity:.8;margin-top:3px">{d}</div></div></div>' for i,(t,d) in enumerate(ITEMS))
pin=f"""{star(50,30,34,PINK)}{star(930,40,26,"#fff",.6)}
<div style="position:absolute;left:60px;right:60px;top:70px;bottom:130px;background:#fff;border-radius:40px"></div>
<img src="data:image/png;base64,{CRIB}" style="position:absolute;right:95px;top:120px;height:290px;filter:drop-shadow(0 14px 14px rgba(5,31,69,.16))">
<div style="position:absolute;left:120px;right:120px;top:140px">
<div class="tags"><span class="tag t1" style="font-size:24px">Checklist</span><span class="tag t2" style="font-size:24px">Kids Furniture</span></div>
<div style="font-size:28px;font-weight:700;opacity:.6;margin-top:22px">Before you buy</div><div class="h" style="font-size:62px;margin-top:6px;width:470px">8 safe sleep checks most parents miss</div>
<div style="margin-top:28px">{rows}</div>
<div style="margin-top:14px;font-size:22px;font-weight:600;opacity:.55">Based on The Lullaby Trust safer sleep advice.</div></div>
<div style="position:absolute;left:60px;right:60px;bottom:44px;display:flex;justify-content:space-between;align-items:center;color:#fff">
<div style="font-weight:700;font-size:27px">Compare cot prices from UK shops</div><div class="h" style="font-size:34px">babysorted.com</div></div>"""
out="/mnt/user-data/outputs/sleep"
JS="""()=>{const st=document.getElementById('st'),t=document.getElementById('top'),p=document.getElementById('prog');
if(st&&t&&p){const a=t.getBoundingClientRect().bottom+20,b=p.getBoundingClientRect().top-20;st.style.top=a+'px';st.style.height=(b-a)+'px';}}"""
with sync_playwright() as pw:
    br=pw.chromium.launch(); pg=br.new_page(viewport=dict(width=1080,height=1350))
    for i,bd in enumerate(bodies):
        pg.set_content(f"<html><head><style>{CSS}</style></head><body>{bd}{foot(i,n)}</body></html>"); pg.wait_for_timeout(200)
        pg.evaluate(JS); pg.screenshot(path=f"{out}/slide_{i+1}.png")
    pg2=br.new_page(viewport=dict(width=1000,height=1500),device_scale_factor=2)
    pg2.set_content(f"<html><head><style>{CSS.replace('width:1080px;height:1350px','width:1000px;height:1500px')}</style></head><body>{pin}</body></html>"); pg2.wait_for_timeout(200)
    pg2.screenshot(path=f"{out}/pinterest_safe_sleep_checks.png"); br.close()
from PIL import Image
W=Image.new('RGB',(1440,900),'white')
for k in range(11): W.paste(Image.open(f'{out}/slide_{k+1}.png').resize((240,300)),((k%6)*240,(k//6)*450))
W.paste(Image.open(f'{out}/pinterest_safe_sleep_checks.png').resize((300,450)),(1140,450))
W.save('/home/claude/preview.png')
