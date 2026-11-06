# Lunchtime Pinterest extras (13:00): three 2:3 list pins on published topics. Mint "route", navy "night card", pink "tap check". Facts: Lullaby Trust, RoSPA.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
PB=b("pebble.png",900); DR=b("dream.png",800); EG=b("egg.png",700); BZ=b("beezy.png",800)
def shot(out,CSS,body):
    os.makedirs(out,exist_ok=True)
    with sync_playwright() as p:
        br=p.chromium.launch(); pg=br.new_page(viewport=dict(width=1000,height=1500),device_scale_factor=2)
        pg.set_content(f"<html><head><style>{CSS.replace('width:1080px;height:1350px','width:1000px;height:1500px')}</style></head><body>{body}</body></html>"); pg.wait_for_timeout(350)
        pg.screenshot(path=f"{out}/pin.png"); br.close()
    Image.open(f"{out}/pin.png").resize((667,1000)).save(f"{out}/pinp.png")
foot_=lambda t,c=NAVY:f'<div style="position:absolute;left:60px;right:60px;bottom:40px;display:flex;justify-content:space-between;align-items:center;color:{c}"><div class="brand" style="font-size:34px">BabySorted</div><div style="font-weight:700;font-size:25px">{t}</div></div>'
# L1 mint: long drive
S=[("Hats and hoods off","They can overheat in the car."),("Plan regular breaks","Take your baby out to stretch and move."),("Slumped forward? Stop","Stop straight away. Lift out, sit upright."),("Out on arrival","Even if asleep. Move to a firm, flat surface."),("Young baby? Go shorter","Avoid long drives with very young babies.")]
st="".join(f'<div style="display:flex;gap:26px;position:relative;padding-bottom:{0 if i==4 else 44}px">{"" if i==4 else f"""<div style="position:absolute;left:37px;top:60px;bottom:-4px;width:6px;background:{NAVY}"></div>"""}<div class="h" style="flex:none;width:80px;height:80px;border-radius:50%;background:{NAVY};color:#fff;font-size:42px;display:flex;align-items:center;justify-content:center;position:relative">{i+1}</div><div><div class="h" style="font-size:44px">{a}</div><div style="font-size:31px;font-weight:500;margin-top:4px">{c}</div></div></div>' for i,(a,c) in enumerate(S))
l1=f'''{star(920,44,30,"#fff")}<div style="position:absolute;left:60px;right:60px;top:56px"><div class="tags"><span class="tag t1" style="font-size:24px">Tips</span><span class="tag t2" style="font-size:24px">Car Seats</span></div>
<div class="h" style="font-size:86px;margin-top:20px;width:560px">Long drive with a baby?</div></div>
<img src="{PB}" style="position:absolute;right:50px;top:70px;height:330px;{SH}">
<div style="position:absolute;left:60px;right:60px;top:430px;background:#fff;border-radius:40px;padding:44px 38px">{st}</div>
<div style="position:absolute;left:60px;right:60px;top:1290px;font-size:28px;font-weight:600;opacity:.7;line-height:1.3">Car seats are for travel, not a main place to sleep. Source: The Lullaby Trust, the UK safer baby sleep charity.</div>
{foot_("Compare car seat prices at babysorted.com")}'''
shot(ROOT+"/out/l1",css(MINT,NAVY,NAVY,"#fff")+".t2{background:#fff;box-shadow:none}",l1)
# L2 navy: winter nights
W=[("Feel the chest or neck","Cold hands and feet are normal."),("Hot or clammy? One layer off","Sweaty means too hot."),("No hats indoors","Hats and hoods off when you get in."),("A doubled blanket counts as two","Add a thin layer, not a heavy one."),("Keep the cot off the radiator","Point any heater away from your baby."),("Cold room? Layer or higher tog","Follow the sleep bag maker's guide.")]
wc="".join(f'<div style="padding:24px 0;border-top:{"0" if i==0 else f"3px solid {PINK}"}"><div class="h" style="font-size:37px">{a}</div><div style="font-size:28px;font-weight:500;margin-top:3px">{c}</div></div>' for i,(a,c) in enumerate(W))
l2=f'''{star(930,44,30,PINK)}{star(40,330,22,"#fff",.5)}<div style="position:absolute;left:60px;right:60px;top:56px"><div class="tags"><span class="tag t1" style="font-size:24px">Tips</span><span class="tag t2" style="font-size:24px">Kids Furniture</span></div>
<div class="h" style="font-size:84px;margin-top:20px;width:600px">Cold night? 6 safe sleep checks</div></div>
<div style="position:absolute;right:60px;top:150px;width:210px;height:210px;background:{MINT};border-radius:50%;color:{NAVY};display:flex;flex-direction:column;align-items:center;justify-content:center"><div class="h" style="font-size:42px;white-space:nowrap">16–20°C</div><div style="font-weight:700;font-size:23px;margin-top:4px">baby's room</div></div>
<div style="position:absolute;left:60px;right:60px;top:440px;height:860px;background:#fff;color:{NAVY};border-radius:40px;padding:12px 34px"><div style="width:600px">{wc}</div>
<img src="{DR}" style="position:absolute;right:16px;top:90px;height:360px;{SH}"><img src="{EG}" style="position:absolute;right:34px;bottom:50px;height:230px;{SH}"></div>
<div style="position:absolute;left:60px;right:60px;top:1320px;font-size:26px;font-weight:600;color:{PINK}">Source: The Lullaby Trust, the UK safer baby sleep charity.</div>
{foot_("Compare sleep bag prices at babysorted.com","#fff")}'''
shot(ROOT+"/out/l2",css(NAVY,"#fff",MINT,NAVY),l2)
# L3 pink: 5 checks
C=[("Five straps","Check the harness has all five."),("Lock, unlock, push","Test the brakes before you set off."),("Nothing on the handles","Shopping bags can tip it over."),("Nothing on top","Coats and bags can tip it too."),("A safety standard","Look for BS EN 1888-1 or BS 7409.")]
cc="".join(f'<div style="background:#fff;border-radius:26px;padding:14px 24px;margin-top:14px;display:flex;gap:22px;align-items:center;width:600px"><div style="flex:none;width:58px;height:58px;border-radius:18px;background:{NAVY};color:#fff;font-weight:800;font-size:32px;display:flex;align-items:center;justify-content:center">✓</div><div><div class="h" style="font-size:37px">{a}</div><div style="font-size:26px;font-weight:500;margin-top:2px">{c}</div></div></div>' for a,c in C)
l3=f'''{star(920,44,30,"#fff")}{star(50,1300,22,"#fff")}<div style="position:absolute;left:60px;right:60px;top:56px"><div class="tags"><span class="tag t1" style="font-size:24px">Tips</span><span class="tag t2" style="font-size:24px">Pushchairs</span></div>
<div class="h" style="font-size:96px;margin-top:20px">5 quick pushchair checks</div></div>
<div style="position:absolute;right:40px;top:410px;width:380px;height:900px;background:{ROSE};border-radius:190px 190px 40px 40px"></div>
<img src="{BZ}" style="position:absolute;right:30px;top:640px;height:640px;{SH}">
<div style="position:absolute;left:60px;top:400px">{cc}</div>
<div style="position:absolute;left:60px;top:1190px;width:520px;font-size:28px;font-weight:600;opacity:.75;line-height:1.3">Source: RoSPA, the UK accident prevention charity.</div>
{foot_("Compare pushchair prices at babysorted.com")}'''
shot(ROOT+"/out/l3",css(PINK,NAVY,NAVY,"#fff")+".t2{background:#fff;box-shadow:none}",l3)
