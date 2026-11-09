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
l1=pin_hero(baby(11,1000,700,.5,.36),pin_tags("Tips","Kids Furniture"),"5 high chair habits that matter most",["Harness on, every time","Sit them upright","Stay right there","Quarter grapes and tomatoes","Know gagging from choking"],MU,330,MINT,NAVY,NAVY,"#fff","Source: NHS and RoSPA, the UK accident prevention charity.","Compare high chair prices at babysorted.com",line="#fff")
shot(ROOT+"/out/l1",css(MINT,NAVY,NAVY,"#fff")+".t2{background:#fff;box-shadow:none}",l1)
F=[("Change nappies on the floor","Not on a high table top or the sofa."),("Never leave them up high alone","A bed, sofa or changing unit counts."),("Bouncers go on the floor","Never on a table or worktop. They can move off."),("Gates at the top AND bottom","Wall-mounted stair gates for under 2s.")]
fc="".join(f'<div style="background:{PINK};border-radius:28px;padding:30px 30px;margin-top:{0 if i==0 else 22}px;display:flex;gap:22px;align-items:center"><div class="h" style="flex:none;width:64px;height:64px;border-radius:18px;background:{NAVY};color:#fff;font-size:34px;display:flex;align-items:center;justify-content:center">{i+1}</div><div><div class="h" style="font-size:40px">{a}</div><div style="font-size:28px;font-weight:500;margin-top:3px">{c}</div></div></div>' for i,(a,c) in enumerate(F))
l2=pin_hero(baby(1,1000,700,.45,.45,1.05),pin_tags("Tips","Kids Furniture"),"Baby falls at home: 4 rules for the first 2 years",["Change nappies on the floor","Never leave them up high alone","Bouncers on the floor only","Gates at the top AND bottom of stairs"],ME,300,"#fff",NAVY,PINK,NAVY,"Source: RoSPA, the UK accident prevention charity.","Compare changing mat prices at babysorted.com")
shot(ROOT+"/out/l2",css("#fff",NAVY,NAVY,"#fff"),l2)
