# Lunchtime Pinterest extras for 15-17 Nov 2026 (reuse published topics; photo-led pins, no IG, no Stories).
# L1 breast milk storage (NHS), L2 car seat belt fitting (RoSPA), L3 second-hand cot mattress (Lullaby Trust).
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
def shot(out,CSS,body):
    os.makedirs(out,exist_ok=True)
    with sync_playwright() as p:
        br=p.chromium.launch(); pg=br.new_page(viewport=dict(width=1000,height=1500),device_scale_factor=2)
        pg.set_content(f"<html><head><style>{CSS.replace('width:1080px;height:1350px','width:1000px;height:1500px')}</style></head><body>{body}</body></html>"); pg.wait_for_timeout(350)
        pg.screenshot(path=f"{out}/pin.png"); br.close()
    Image.open(f"{out}/pin.png").resize((667,1000)).save(f"{out}/pinp.png")
BG=b("bags.png",900); BE=b("beyond.png",900); TU=b("tutti.png",900)
# L1 — breast milk storage, mint
l1=pin_hero(baby(34,1000,680,.5,.4),pin_tags("Tips","Nursing &amp; Feeding"),"How long does expressed breast milk keep?",
  ["Back of the fridge, 4°C: up to 8 days","Ice compartment: 2 weeks","Freezer at -18°C: up to 6 months","Cool bag with ice packs: 24 hours","Fed from it? Use within 1 hour"],
  BG,300,MINT,NAVY,NAVY,"#fff","Source: NHS. Defrost in the fridge, never the microwave.","Compare milk storage bag prices at babysorted.com",line="#fff",photo_h=680,title_fs=52)
shot(ROOT+"/out/l1",css(MINT,NAVY,NAVY,"#fff"),l1)
# L2 — car seat belt fitting, white
l2=pin_hero(baby(6,1000,680,.45,.45,1.1),pin_tags("Tips","Car Seats"),"Fitting a car seat with the seat belt",
  ["Thread the belt through every guide","No buckle crunch on the seat frame","Pull out all the slack","Blue guide = rear, red = forward"],
  BE,300,"#fff",NAVY,NAVY,"#fff","Source: RoSPA, the UK accident prevention charity.","Compare car seat prices at babysorted.com",line=PINK,photo_h=680,title_fs=56)
shot(ROOT+"/out/l2",css("#fff",NAVY,NAVY,"#fff"),l2)
# L3 — second-hand cot mattress, pink
l3=pin_hero(baby(29,1000,680,.5,.45),pin_tags("Tips","Kids Furniture"),"Is a second-hand cot mattress safe?",
  ["New is safest for each baby","Firm and flat, with no sagging","Fully waterproof, no rips or tears","Fits the cot with no gaps","Stored clean, dry and smoke-free"],
  TU,330,PINK,NAVY,NAVY,"#fff","Source: The Lullaby Trust, the UK safer baby sleep charity.","Compare cot mattress prices at babysorted.com",line="#fff",photo_h=680,title_fs=54)
shot(ROOT+"/out/l3",css(PINK,NAVY,NAVY,"#fff"),l3)
