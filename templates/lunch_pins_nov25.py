# Lunchtime Pinterest extra for 25 Nov 2026 (reuses published topics #19 / #39 nursery set-up; photo-led pin, no IG, no Stories).
# L1 blind cords in the nursery (RoSPA, GOV.UK OPSS guidance).
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
def shot(out,CSS,body):
    os.makedirs(out,exist_ok=True)
    with sync_playwright() as p:
        br=p.chromium.launch(); pg=br.new_page(viewport=dict(width=1000,height=1500),device_scale_factor=2)
        pg.set_content(f"<html><head><style>{CSS.replace('width:1080px;height:1350px','width:1000px;height:1500px')}</style></head><body>{body}</body></html>"); pg.wait_for_timeout(350)
        pg.screenshot(path=f"{out}/pin.png"); br.close()
    Image.open(f"{out}/pin.png").resize((667,1000)).save(f"{out}/pinp.png")
NK=b("nika.png",700)
l1=pin_hero(baby(30,1000,660,.5,.35,1.05),pin_tags("Tips","Kids Furniture"),"Blind cords: 6 nursery checks",
  ["Cot away from the window","No looped cords in their room","Cleats at least 1.5m off the floor","Wind cords in a figure of eight","Cutting cords won't make it safe","New blind? Choose cordless"],
  NK,190,MINT,NAVY,NAVY,"#fff","Sources: RoSPA, the UK accident prevention charity; GOV.UK. Also keep beds, high chairs and play pens away from blinds.","Compare cot prices at babysorted.com",line="#fff",photo_h=660,title_fs=56)
shot(ROOT+"/out/l1",css(MINT,NAVY,NAVY,"#fff"),l1)
