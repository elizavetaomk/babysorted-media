# Lunchtime Pinterest extras for 28-30 Nov 2026 (reuse published topics; photo-led pins, no IG, no Stories).
# L1 Sat 28 Nov: baby-safe Christmas (topic of #60 Baby-proofing). Facts: RoSPA Christmas safety and Christmas novelties pages
#    (decorations are not toys, place high up; under-36-month choking risk), RoSPA toy safety (under-3 labels, CE/UKCA marks),
#    GOV.UK fire safety at Christmas (lights with British safety mark, switch off and unplug at bedtime, candles out of reach and
#    away from the tree), RoSPA (trailing cables), OPSS leaflet (store spare button batteries securely).
# L2 Sun 29 Nov: baby seat in the front (topics #14 / #24). Facts: GOV.UK child car seats law (deactivate front airbags before a
#    rear-facing seat in front; not in side-facing seats; diagonal strap unless lap-belt design or ISOFIX); RoSPA childcarseats.org.uk
#    (illegal with an active airbag; safer in the rear; forward-facing in front: car seat as far back as possible; follow car maker).
# L3 Mon 30 Nov: stop furniture tipping (topics #19 / #60). Facts: RoSPA accidents to children, flat-screen TVs and falls pages.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
def shot(out,CSS,body):
    os.makedirs(out,exist_ok=True)
    with sync_playwright() as p:
        br=p.chromium.launch(); pg=br.new_page(viewport=dict(width=1000,height=1500),device_scale_factor=2)
        pg.set_content(f"<html><head><style>{CSS.replace('width:1080px;height:1350px','width:1000px;height:1500px')}</style></head><body>{body}</body></html>"); pg.wait_for_timeout(350)
        pg.screenshot(path=f"{out}/pin.png"); br.close()
    Image.open(f"{out}/pin.png").resize((667,1000)).save(f"{out}/pinp.png")
ROS="RoSPA, the UK accident prevention charity"
l1=pin_hero(baby(26,1000,680,.42,.45,1.0),pin_tags("Parenting Tips","Play &amp; Development"),"A baby-safe Christmas: 6 checks",
  ["Decorations up high: they’re not toys","Under 3? Check the toy’s age label","Lights: UK safety mark, off at bedtime","Candles out of reach, away from the tree","Tidy trailing cables from new gadgets","Lock spare button batteries away"],
  None,0,"#fff",NAVY,PINK,NAVY,f"Sources: {ROS}; GOV.UK.","Compare baby gift prices at babysorted.com",line=PINK,photo_h=660,title_fs=56)
shot(ROOT+"/out/l1",css("#fff",NAVY,NAVY,"#fff"),l1)
CG=b("cloudg3.png",800)
l2=pin_hero(baby(33,1000,640,.5,.4,1.0),pin_tags("Tips","Car Seats"),"Baby seat in the front? 5 rules",
  ["The back seat is safer","Rear-facing: airbag must be off","Check the car handbook first","Forward-facing: seat right back","Never in a side-facing seat"],
  CG,200,MINT,NAVY,NAVY,"#fff",f"Sources: GOV.UK; {ROS}. A rear-facing seat in front of an active airbag is illegal.","Compare car seat prices at babysorted.com",line="#fff",photo_h=640,title_fs=58)
shot(ROOT+"/out/l2",css(MINT,NAVY,NAVY,"#fff"),l2)
SL=b("sleigh.png",700)
l3=pin_hero(baby(7,1000,660,.5,.45,1.0),pin_tags("Tips","Kids Furniture"),"Stop furniture tipping: 6 checks",
  ["Fix tall furniture to the wall","Strap the TV with anti-tip straps","Plasterboard? Fix into the studs","Keep furniture away from windows","Window restrictors upstairs","No climbing on drawers or TV units"],
  SL,280,ROSE,NAVY,NAVY,"#fff",f"Source: {ROS}.","Compare nursery furniture prices at babysorted.com",line="#fff",photo_h=660,title_fs=56)
shot(ROOT+"/out/l3",css(ROSE,NAVY,NAVY,"#fff"),l3)
