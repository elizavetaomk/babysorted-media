# Lunchtime Pinterest extras for 10-11 Nov 2026: mint "high chair habits" (NHS, RoSPA) and white "falls rules" (RoSPA).
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
def shot(out,CSS,body):
    os.makedirs(out,exist_ok=True)
    with sync_playwright() as p:
        br=p.chromium.launch(); pg=br.new_page(viewport=dict(width=1000,height=1500),device_scale_factor=2)
        pg.set_content(f"<html><head><style>{CSS.replace('width:1080px;height:1350px','width:1000px;height:1500px')}</style></head><body>{body}</body></html>"); pg.wait_for_timeout(350)
        pg.screenshot(path=f"{out}/pin.png"); br.close()
    Image.open(f"{out}/pin.png").resize((667,1000)).save(f"{out}/pinp.png")
foot_=lambda t,c=NAVY:f'<div style="position:absolute;left:60px;right:60px;bottom:40px;display:flex;justify-content:space-between;align-items:center;color:{c}"><div class="brand" style="font-size:34px">BabySorted</div><div style="font-weight:700;font-size:25px">{t}</div></div>'
MU=b("multiply.png",900); ME=b("mateuc.png",900)
H=[("Harness on, every time","A securely fitted five-point harness.","RoSPA"),("Sit them upright","So they can swallow properly.","NHS"),("Stay right there","Always stay with them while they eat.","NHS"),("Quarter round foods","Grapes and cherry tomatoes in 4 pieces.","NHS"),("Know the gag","Watery eyes and tongue pushing out are gagging, not choking.","NHS")]
hc="".join(f'<div style="display:flex;gap:22px;align-items:center;padding:20px 0;border-top:{"0" if i==0 else f"3px solid {MINT}"}"><div class="h" style="flex:none;width:66px;height:66px;border-radius:50%;background:{NAVY};color:#fff;font-size:34px;display:flex;align-items:center;justify-content:center">{i+1}</div><div><div class="h" style="font-size:40px">{a}</div><div style="font-size:28px;font-weight:500;margin-top:3px">{c}</div></div></div>' for i,(a,c,s) in enumerate(H))
l1=f'''{star(920,44,30,"#fff")}<div style="position:absolute;left:60px;top:56px;width:560px"><div class="tags"><span class="tag t1" style="font-size:24px">Tips</span><span class="tag t2" style="font-size:24px">Kids Furniture</span></div>
<div class="h" style="font-size:80px;margin-top:20px">5 high chair habits that matter most</div><div style="font-size:32px;font-weight:700;margin-top:14px">More than which chair you buy.</div></div>
<div style="position:absolute;right:60px;top:110px;width:330px;height:440px;background:#fff;border-radius:165px 165px 34px 34px;display:flex;align-items:flex-end;justify-content:center;padding-bottom:20px"><img src="{MU}" style="height:390px;{SH}"></div>
<div style="position:absolute;left:60px;right:60px;top:580px;background:#fff;border-radius:40px;padding:18px 38px">{hc}</div>
<div style="position:absolute;left:60px;right:60px;top:1330px;font-size:25px;font-weight:600;opacity:.75;line-height:1.3">Source: NHS and RoSPA, the UK accident prevention charity.</div>
{foot_("Compare high chair prices at babysorted.com")}'''
shot(ROOT+"/out/l1",css(MINT,NAVY,NAVY,"#fff")+".t2{background:#fff;box-shadow:none}",l1)
F=[("Change nappies on the floor","Not on a high table top or the sofa."),("Never leave them up high alone","A bed, sofa or changing unit counts."),("Bouncers go on the floor","Never on a table or worktop. They can move off."),("Gates at the top AND bottom","Wall-mounted stair gates for under 2s.")]
fc="".join(f'<div style="background:{PINK};border-radius:28px;padding:30px 30px;margin-top:{0 if i==0 else 22}px;display:flex;gap:22px;align-items:center"><div class="h" style="flex:none;width:64px;height:64px;border-radius:18px;background:{NAVY};color:#fff;font-size:34px;display:flex;align-items:center;justify-content:center">{i+1}</div><div><div class="h" style="font-size:40px">{a}</div><div style="font-size:28px;font-weight:500;margin-top:3px">{c}</div></div></div>' for i,(a,c) in enumerate(F))
l2=f'''{star(920,44,30,PINK)}<div style="position:absolute;left:60px;right:60px;top:56px"><div class="tags"><span class="tag t1" style="font-size:24px">Tips</span><span class="tag t2" style="font-size:24px">Kids Furniture</span></div>
<div class="h" style="font-size:84px;margin-top:20px;width:620px">Falls are the most common home accident</div><div style="font-size:33px;font-weight:700;margin-top:14px;width:600px">4 rules for the first two years</div></div>
<img src="{ME}" style="position:absolute;right:50px;top:150px;height:400px;transform:rotate(-8deg);{SH}">
<div style="position:absolute;left:60px;right:60px;top:600px">{fc}</div>
<div style="position:absolute;left:60px;right:60px;top:1310px;font-size:25px;font-weight:600;opacity:.75;line-height:1.3">Source: RoSPA, the UK accident prevention charity.</div>
{foot_("Compare changing mat prices at babysorted.com")}'''
shot(ROOT+"/out/l2",css("#fff",NAVY,NAVY,"#fff"),l2)
