# Lunchtime Pinterest extras for 21-23 Nov 2026 (reuse published topics; photo-led pins, no IG, no Stories).
# L1 Black Friday: spotting a real deal (GOV.UK, legislation.gov.uk), L2 making up a formula feed (NHS),
# L3 long car journeys with a baby (The Lullaby Trust, RoSPA).
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
def shot(out,CSS,body):
    os.makedirs(out,exist_ok=True)
    with sync_playwright() as p:
        br=p.chromium.launch(); pg=br.new_page(viewport=dict(width=1000,height=1500),device_scale_factor=2)
        pg.set_content(f"<html><head><style>{CSS.replace('width:1080px;height:1350px','width:1000px;height:1500px')}</style></head><body>{body}</body></html>"); pg.wait_for_timeout(350)
        pg.screenshot(path=f"{out}/pin.png"); br.close()
    Image.open(f"{out}/pin.png").resize((667,1000)).save(f"{out}/pinp.png")
DATE="20 Nov 2026"
TR=b("triv.png",700); BO=b("bottle.png",500); MI=b("mirror.png",600)
gap=f'''<div style="text-align:center;font-weight:800"><img src="{TR}" style="height:230px;{SH}"><div style="font-size:24px;margin-top:6px">Same pushchair today</div><div class="h" style="font-size:44px">£449 <span style="font-size:28px;opacity:.55;text-decoration:line-through">£600</span></div><div style="font-size:17px;font-weight:600;opacity:.75;line-height:1.25">Nuna Triv Next, Chateau<br>Prices on BabySorted, {DATE}</div></div>'''
l1=pin_hero(baby(5,1000,640,.5,.45),pin_tags("Deals","All categories"),"Black Friday: is it a real deal?",
  ["Compare the same model and colour","Don't trust bundle \"was\" prices","A \"was\" price must be genuine","Fake countdowns are banned","Online? 14 days to change your mind","Check GOV.UK for recalls"],
  "",0,MINT,NAVY,NAVY,"#fff","Source: GOV.UK. Cancelling online orders: Consumer Contracts Regulations 2013, some exceptions.","Compare baby gear prices at babysorted.com",line="#fff",photo_h=640,title_fs=54)
l1=l1.replace('<div style="display:flex;gap:16px;margin-top:14px"><div style="flex:1">','<div style="display:flex;gap:16px;margin-top:14px"><div style="flex:1">',1)
# add the price-gap card beside the list
l1=l1.replace("</div></div></div>\n<div style=\"position:absolute;left:56px;right:56px;bottom:96px",f'</div><div style="flex:none;width:250px;display:flex;align-items:center">{gap}</div></div></div>\n<div style="position:absolute;left:56px;right:56px;bottom:96px',1)
shot(ROOT+"/out/l1",css(MINT,NAVY,NAVY,"#fff"),l1)
l2=pin_hero(baby(34,1000,660,.5,.35),pin_tags("Tips","Nursing &amp; Feeding"),"Making up a formula feed: NHS steps",
  ["Fresh tap water, boiled once","Cool no more than 30 min (70C+)","Water in first, then the powder","Never add extra powder","Cool under the cold tap, test on wrist","Leftovers after a feed: throw away"],
  BO,330,ROSE,NAVY,NAVY,"#fff","Source: NHS. Never warm formula in a microwave.","Compare baby bottle prices at babysorted.com",line="#fff",photo_h=660,title_fs=52)
shot(ROOT+"/out/l2",css(ROSE,NAVY,NAVY,"#fff"),l2)
l3=pin_hero(baby(31,1000,660,.5,.3),pin_tags("Tips","Car Seats"),"Long car journeys with a baby",
  ["A car seat is for travel, not sleep","Take them out when you arrive","Regular breaks out of the seat","First months: ideally 30 min or less","A second adult in the back, or a mirror","Head slumps forward? Stop straight away"],
  MI,200,NAVY,"#fff",MINT,NAVY,"Sources: The Lullaby Trust, the UK safer baby sleep charity; RoSPA, the UK accident prevention charity.","Compare car seat prices at babysorted.com",line="rgba(255,255,255,.25)",photo_h=660,title_fs=54)
shot(ROOT+"/out/l3",css(NAVY,"#fff",MINT,NAVY),l3)
