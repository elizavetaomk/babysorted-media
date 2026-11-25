# Lunchtime Pinterest extras for 26-27 Nov 2026 (reuse published topics; photo-led pins, no IG, no Stories).
# L1 Thu 26 Nov: button batteries before Christmas (topic of #60 Baby-proofing). Facts: GOV.UK (OPSS button battery campaign),
#    RoSPA button batteries page. L2 Fri 27 Nov: calm, responsive bottle feeds (topics #22 / #31). Facts: NHS Best Start in Life
#    "Bottle feeding your baby".
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
def shot(out,CSS,body):
    os.makedirs(out,exist_ok=True)
    with sync_playwright() as p:
        br=p.chromium.launch(); pg=br.new_page(viewport=dict(width=1000,height=1500),device_scale_factor=2)
        pg.set_content(f"<html><head><style>{CSS.replace('width:1080px;height:1350px','width:1000px;height:1500px')}</style></head><body>{body}</body></html>"); pg.wait_for_timeout(350)
        pg.screenshot(path=f"{out}/pin.png"); br.close()
    Image.open(f"{out}/pin.png").resize((667,1000)).save(f"{out}/pinp.png")
l1=pin_hero(baby(32,1000,680,.5,.18,1.0),pin_tags("Parenting Tips","Play &amp; Development"),"Button batteries: 6 checks before Christmas",
  ["Check remotes, car keys, musical cards","No screw on the battery lid? Out of reach","Lock spares away, not in a drawer","‘Dead’ batteries can still burn: recycle","Swallowed one? A&amp;E now or call 999","No food, drink or making them sick"],
  None,0,PINK,NAVY,NAVY,"#fff","Sources: GOV.UK; RoSPA, the UK accident prevention charity. 999 is the free UK emergency number. Act fast even if there are no symptoms.","Compare baby gear prices at babysorted.com",line="#fff",photo_h=640,title_fs=54)
shot(ROOT+"/out/l1",css(PINK,NAVY,NAVY,"#fff"),l1)
GL=b("glass.png",600)
l2=pin_hero(baby(34,1000,660,.5,.35,1.0),pin_tags("Tips","Nursing &amp; Feeding"),"6 calm bottle-feeding habits",
  ["Hold baby close and semi-upright","Feed on early cues, before crying","Rub the teat on their top lip first","Keep the bottle almost flat","Pause when they turn away","Never force a finish or prop it"],
  GL,260,"#fff",NAVY,MINT,NAVY,"Source: NHS Best Start in Life.","Compare baby bottle prices at babysorted.com",line=MINT,photo_h=660,title_fs=56)
shot(ROOT+"/out/l2",css("#fff",NAVY,NAVY,"#fff"),l2)
