# Lunchtime Pinterest extras for 17-18 Nov 2026 (reuse published topics; photo-led pins, no IG, no Stories).
# L1 sterilising bottles (NHS), L2 winter walks without overheating (The Lullaby Trust).
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
def shot(out,CSS,body):
    os.makedirs(out,exist_ok=True)
    with sync_playwright() as p:
        br=p.chromium.launch(); pg=br.new_page(viewport=dict(width=1000,height=1500),device_scale_factor=2)
        pg.set_content(f"<html><head><style>{CSS.replace('width:1080px;height:1350px','width:1000px;height:1500px')}</style></head><body>{body}</body></html>"); pg.wait_for_timeout(350)
        pg.screenshot(path=f"{out}/pin.png"); br.close()
    Image.open(f"{out}/pin.png").resize((667,1000)).save(f"{out}/pinp.png")
MA=b("mam.png",900); MU=b("muff.png",700)
l1=pin_hero(baby(50,1000,660,.5,.45),pin_tags("Tips","Nursing &amp; Feeding"),"Sterilising bottles: 6 NHS rules",
  ["Sterilise until at least 12 months","Wash in hot soapy water first","Cold-water solution: 30 min, fresh daily","Boiling: at least 10 minutes","A dishwasher cleans, it doesn't sterilise","Out of the steriliser? Teats on straight away"],
  MA,230,PINK,NAVY,NAVY,"#fff","Source: NHS.","Compare steriliser prices at babysorted.com",line="#fff",photo_h=660,title_fs=56)
shot(ROOT+"/out/l1",css(PINK,NAVY,NAVY,"#fff"),l1)
l2=pin_hero(baby(6,1000,660,.5,.4),pin_tags("Tips","Pushchairs"),"Winter walks: warm, not too warm",
  ["Never cover the pram with a blanket","Hats off indoors and in the car","Feel the chest or back of the neck","Sweaty or clammy? Take a layer off","Napping indoors? Outdoor clothes off","No hot water bottles in the pram"],
  MU,330,"#fff",NAVY,NAVY,"#fff","Source: The Lullaby Trust, the UK safer baby sleep charity.","Compare footmuff prices at babysorted.com",line=PINK,photo_h=660,title_fs=56)
shot(ROOT+"/out/l2",css("#fff",NAVY,NAVY,"#fff"),l2)
