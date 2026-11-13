# White "temperature gauge" layout: white bg, navy stage panels holding white/cream products, a pink thermometer
# with a 70°C mark on the side of each machine slide. Used for: Best bottle prep machines (14 Nov 2026).
# Facts: NHS (making up formula, prep machines). Maker-only care tips are labelled "makers say", no brand.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css("#fff",NAVY,NAVY,"#fff")
DATE="13 Nov 2026"
deco=star(36,30,26,PINK)+star(1000,36,30,PINK)
PP=b("perfect.png",1000); BZ=b("brezza.png",1000); GP=b("goprep.png",1000)
def thermo(h=470,mark=.62):
    return f'''<div style="position:relative;width:70px;height:{h}px"><div style="position:absolute;left:20px;top:0;width:30px;height:{h-50}px;background:#fff;border-radius:15px"></div>
<div style="position:absolute;left:26px;top:{int((h-50)*(1-mark))}px;width:18px;height:{int((h-50)*mark)}px;background:{ROSE};border-radius:9px"></div>
<div style="position:absolute;left:5px;bottom:0;width:60px;height:60px;border-radius:50%;background:{ROSE};box-shadow:0 0 0 6px #fff"></div>
<div style="position:absolute;left:58px;top:{int((h-50)*(1-mark))-18}px;background:#fff;color:{NAVY};font-weight:800;font-size:26px;padding:4px 12px;border-radius:12px;white-space:nowrap">70°C</div></div>'''
def panel(inner,price=None,th=True):
    pr=f'<div style="position:absolute;right:34px;top:30px;text-align:right;color:#fff"><div class="h" style="font-size:46px">{price[0]}</div><div style="font-size:21px;font-weight:600;opacity:.8;line-height:1.3">{price[1]}<br>Price on BabySorted, {DATE}</div></div>' if price else ""
    t=f'<div style="position:absolute;left:44px;top:70px">{thermo()}</div>' if th else ""
    return f'<div style="position:absolute;left:60px;right:60px;top:60px;height:620px;background:{NAVY};border-radius:44px;overflow:hidden">{t}<div style="position:absolute;inset:40px 40px 30px 160px;display:flex;align-items:center;justify-content:center">{inner}</div>{pr}</div>'
def slide(kick,title,body,inner,src="",price=None,th=True):
    s=f'<div style="font-size:26px;font-weight:700;opacity:.6;margin-top:14px">{src}</div>' if src else ""
    return deco+panel(inner,price,th)+f'''<div style="position:absolute;left:70px;right:70px;top:725px"><div class="kick">{kick}</div><div class="h" style="font-size:70px;margin-top:8px">{title}</div><div class="b" style="margin-top:14px;font-size:38px">{body}</div>{s}</div>'''
img=lambda s,h: f'<img src="{s}" style="height:{h}px;max-width:760px;object-fit:contain;filter:drop-shadow(0 18px 24px rgba(0,0,0,.35))">'
bigw=lambda a,c: f'<div style="text-align:center;color:#fff"><div class="h" style="font-size:200px;line-height:1">{a}</div><div class="h" style="font-size:50px;margin-top:8px">{c}</div></div>'
circle=f'<div style="width:270px;height:270px;border-radius:50%;background:{NAVY};display:flex;align-items:center;justify-content:center"><img src="{PP}" style="height:220px;filter:drop-shadow(0 12px 16px rgba(0,0,0,.35))"></div>'
cover=hero_cover(baby(30,1080,800,.45,.4,1.0),'<div class="tags"><span class="tag t1">Buying guide</span><span class="tag t2">Nursing &amp; Feeding</span></div>',"Bottle prep machines: are they worth it?","Check one number before you buy: 70°C.",circle,1,card="#fff",fg=NAVY,pill_bg=PINK,pill_fg=NAVY,pill="Swipe before you buy",title_fs=70)+star(1000,40,30,"#fff")
s2=slide("THE RULE BEHIND EVERY FEED","Formula needs water at 70°C or more","Powdered formula isn't sterile, even in a sealed tin. Water at 70°C or more kills harmful bacteria. A kettle does it if you use the water within 30 minutes of boiling.",bigw("70°C","or hotter, mixed with the powder"),"Source: NHS")
s3=slide("CHECK THIS FIRST","Test the water your machine pours","The NHS says the water from a prep machine should be at least 70°C when it's mixed with the powder. Check with a digital food thermometer. Too cool? Stop using it and make feeds by hand.",bigw("Test","with a food thermometer"),"Source: NHS")
s4=slide("TYPE 1: HOT SHOT, THEN COOL","Countertop machines","A small hot shot mixes with the powder, then cooler water tops it up. Fast at night. Test the first shot's temperature, then follow the maker's steps exactly.",img(PP,470),"",("£109.99","Tommee Tippee Perfect Prep, chalk"))
s5=slide("TYPE 2: POWDER DISPENSERS","Machines that add the powder","You fill a powder hopper and the machine measures it. Makers say to set it for your exact formula. Check the water temperature the NHS way too.",img(BZ,480),"",("£199.99","Baby Brezza Formula Pro mini, white"))
s6=slide("TYPE 3: PORTABLE","Flasks for days out","Handy away from home. Check how the water gets to 70°C, and follow the maker's steps for mixing and cooling.",img(GP,470),"",("£28.99","Tommee Tippee GoPrep feed maker"))
R=[("Change the filter","when the maker says"),("Descale","on the maker's schedule"),("Clean the funnel","after every use")]
rr="".join(f'<div style="display:flex;gap:22px;align-items:center;padding:26px 0;border-top:{"0" if i==0 else f"3px solid {PINK}"}"><div class="h" style="flex:none;width:64px;height:64px;border-radius:50%;background:{PINK};color:{NAVY};font-size:34px;display:flex;align-items:center;justify-content:center">{i+1}</div><div><div class="h" style="font-size:46px">{a}</div><div style="font-size:32px;font-weight:500;margin-top:4px">{c}</div></div></div>' for i,(a,c) in enumerate(R))
s7=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="kick">THE HIDDEN JOBS</div><div class="h" style="font-size:80px;margin-top:8px">What machine makers say you'll need to do</div></div>
<div style="position:absolute;left:60px;right:60px;top:430px;background:{NAVY};color:#fff;border-radius:44px;padding:16px 46px 20px">{rr.replace(f"border-top:3px solid {PINK}","border-top:3px solid #ffffff33")}</div>
<div class="b" style="position:absolute;left:70px;right:70px;top:960px;font-size:38px">Filters and descaler cost extra. Add them to the price when you compare.</div>'''
K=[("One feed at a time","Make each bottle when your baby needs it."),("Leftovers go","Throw away formula left after a feed."),("Body temperature","Warm or cool, never hot, before it goes in.")]
kk="".join(f'<div style="padding:28px 0;border-top:{"0" if i==0 else f"3px solid {PINK}"}"><div class="h" style="font-size:48px">{a}</div><div style="font-size:34px;font-weight:500;margin-top:6px">{c}</div></div>' for i,(a,c) in enumerate(K))
s8=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="kick">MACHINE OR KETTLE</div><div class="h" style="font-size:80px;margin-top:8px">These rules never change</div></div>
<div style="position:absolute;left:60px;right:60px;top:345px;background:{PINK};border-radius:44px;padding:14px 46px 20px">{kk.replace(f"border-top:3px solid {PINK}","border-top:3px solid #fff")}</div>
<div style="position:absolute;left:70px;right:70px;top:1000px;font-size:26px;font-weight:700;opacity:.6">Source: NHS</div>
<div class="b" style="position:absolute;left:70px;right:70px;top:1050px;font-size:34px">Prep machines on BabySorted today: £28.99 to £249.99. Prices on BabySorted, {DATE}.</div>'''
s9=hero_last(baby(39,1080,760,.5,.45,1.0),"Night feeds coming? Compare prep machine prices first","See prep machine prices from UK shops in one place.",PINK,fg=NAVY)
pin=pin_hero(baby(38,1000,660,.5,.4),pin_tags("Buying guide","Nursing &amp; Feeding"),"Bottle prep machines: check this first",["Formula needs water at 70°C+","Test your machine with a food thermometer","Too cool? Make feeds by hand","Filters and descaler cost extra","One feed at a time, no leftovers"],PP,300,"#fff",NAVY,NAVY,"#fff","Source: NHS. Care tips: machine makers.","Compare prep machine prices at babysorted.com",line=PINK,photo_h=660,title_fs=58)
render(ROOT+"/out/p2",[cover,s2,s3,s4,s5,s6,s7,s8,s9],pin,CSS,NAVY)
