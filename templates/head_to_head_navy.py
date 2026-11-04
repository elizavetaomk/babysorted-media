# Navy "head to head" layout: navy bg, deep-pink arches holding white products; compare table; pick slides with stat strip; white text cards.
# Used for: Best bottle sterilisers: steam vs UV (Nov 2026). White products sit on navy or deeper pink.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from slide_lib import *
MI=b("ttmicro.png"); EL=b("ttelec.png"); BR=b("brezza.png"); UV=b("ttuv.png")
CSS=css(NAVY,"#fff",ROSE,NAVY)
deco=star(40,40,26,"#ffffff",.45)+star(990,60,32,ROSE)
SH="filter:drop-shadow(0 18px 18px rgba(5,31,69,.28))"
im=lambda s,h,x="": f'<img src="{s}" style="height:{h}px;max-width:100%;object-fit:contain;{SH};{x}">'
def arch(s,h,lab):
    return f'<div style="flex:1;background:{ROSE};border-radius:300px 300px 40px 40px;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;padding:30px 24px 26px">{im(s,h)}<div class="h c" style="font-size:52px;margin-top:22px">{lab}</div></div>'
cover=deco+f'''<div style="position:absolute;left:80px;right:80px;top:90px"><div class="tags"><span class="tag t1">Buying guide</span><span class="tag t2">Nursing &amp; Feeding</span></div>
<div class="h" style="font-size:84px;margin-top:24px;white-space:nowrap">Best bottle sterilisers:<br>steam vs UV</div>
<div style="font-size:40px;font-weight:600;opacity:.75;margin-top:18px">Fast, simple, safe. Which type suits you?</div></div>
<div style="position:absolute;left:60px;right:60px;top:530px;height:630px;display:flex;gap:24px">{arch(EL,330,"Steam")}{arch(UV,330,"UV")}</div>
<div style="position:absolute;left:50%;top:760px;transform:translateX(-50%);width:130px;height:130px;border-radius:50%;background:{NAVY};box-shadow:0 0 0 10px {ROSE};display:flex;align-items:center;justify-content:center"><div class="h" style="font-size:54px">VS</div></div>
<div style="position:absolute;left:80px;top:1182px;font-weight:700;font-size:30px;opacity:.7">Swipe before you buy</div>'''
def wrow(a,c): return f'<div style="padding:42px 0;border-top:3px solid {PINK}"><div class="h c" style="font-size:47px">{a}</div><div class="b c" style="font-size:38px;margin-top:10px">{c}</div></div>'
s2=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="kick" style="color:{ROSE};opacity:1">FIRST, THE BASICS</div><div class="h" style="font-size:88px;margin-top:8px">No steriliser replaces the wash</div></div>
<div style="position:absolute;left:60px;right:60px;top:340px;background:#fff;border-radius:40px;padding:6px 44px 22px"><div style="border-top:0;margin-top:-3px">{wrow("Wash, then rinse, then sterilise","Hot soapy water and a bottle brush soon after a feed. Rinse in cold running water.")}{wrow("A dishwasher only cleans","The NHS says it won't sterilise your bottles.")}{wrow("Keep going to 12 months","The NHS says sterilise until at least 12 months, to help protect against sickness and diarrhoea.")}</div></div>'''
T=[("HOW IT WORKS","Hot steam","UV light"),("SPEED","About 4 to 10 mins","35 mins"),("DRYING","Usually none. Some models add it","Built in"),("POWER","Microwave or mains","Mains"),("NHS PAGE","Listed","Not mentioned")]
tt="".join(f'''<div style="display:flex;align-items:center;padding:30px 0;border-top:{"0" if i==0 else f"3px solid {PINK}"}"><div style="flex:none;width:250px;font-weight:800;font-size:25px;letter-spacing:.05em;opacity:.6">{a}</div><div class="h" style="flex:1;font-size:38px">{c}</div><div class="h" style="flex:none;width:250px;font-size:38px">{d}</div></div>''' for i,(a,c,d) in enumerate(T))
s3=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="kick" style="color:{ROSE};opacity:1">HEAD TO HEAD</div><div class="h" style="font-size:80px;margin-top:8px;white-space:nowrap">Steam is quick. UV is dry.</div></div>
<div class="c" style="position:absolute;left:60px;right:60px;top:230px;background:#fff;border-radius:40px;padding:22px 44px 24px"><div style="display:flex;font-weight:800;font-size:30px;padding:6px 0 12px"><div style="flex:none;width:250px"></div><div style="flex:1">Steam</div><div style="flex:none;width:250px">UV</div></div>{tt}</div>
<div style="position:absolute;left:70px;right:70px;top:1010px;font-size:28px;font-weight:600;opacity:.75;line-height:1.35">Times are makers' figures for the models in this post. The NHS lists steam, cold water and boiling. It doesn't cover UV, so go by the maker's guide or ask your health visitor.</div>'''
def pick(k,name,best,pic,h,stats,good,watch,ph=560):
    st="".join(f'<div style="flex:1;background:{PINK};border-radius:24px;padding:16px 18px"><div style="font-weight:800;font-size:20px;letter-spacing:.05em;opacity:.65">{a}</div><div class="h" style="font-size:36px;margin-top:6px;white-space:nowrap">{c}</div></div>' for a,c in stats)
    return deco+f'''<div style="position:absolute;left:60px;right:60px;top:60px;height:{ph}px;padding-bottom:30px;background:{ROSE};border-radius:44px;display:flex;align-items:center;justify-content:center">{im(pic,h)}</div>
<div class="c" style="position:absolute;left:92px;top:88px;font-weight:800;font-size:26px;background:#fff;padding:7px 16px;border-radius:18px">{k} of 4</div>
<div class="c" style="position:absolute;left:60px;right:60px;top:{ph+20}px;bottom:126px;background:#fff;border-radius:40px;padding:34px 40px"><div class="h" style="font-size:58px">{name}</div>
<div style="margin-top:12px"><span class="pill" style="background:{NAVY};color:#fff;font-size:28px">{best}</span></div>
<div style="display:flex;gap:14px;margin-top:20px">{st}</div>
<div class="b" style="font-size:36px;margin-top:20px">{good}</div><div class="b" style="font-size:36px;margin-top:10px"><b style="font-weight:800">Watch out:</b> {watch}</div></div>'''
s4=pick(1,"Tommee Tippee 2-in-1 Microwave","Best for a tiny budget",MI,370,[("PRICE","From £24.95"),("HOLDS","4 bottles"),("TIME","4 mins*")],"Also works as a cold-water unit, and it's light to pack.","24 cm wide, so measure your microwave. *Based on 1100W, plus cool-down.")
s5=pick(2,"Tommee Tippee Electric","Best everyday steam",EL,480,[("PRICE","£54.95"),("HOLDS","6 bottles"),("TIME","Under 8 mins")],"Simple, one button, and no microwave needed.","no drying cycle listed, so expect damp bottles.",ph=650)
s6=pick(3,"Baby Brezza Steriliser Dryer","Best for pump parts",BR,450,[("PRICE","£129.99"),("HOLDS","8 bottles"),("TIME","About 10 mins")],"Steam, then dry, in one go. Also holds two full pump part sets.","drying adds about 30 minutes, and it's tall. Measure under your cupboards.")
s7=pick(4,"Tommee Tippee Ultra UV","Best for dry and ready",UV,470,[("PRICE","£111.84"),("HOLDS","6 bottles"),("TIME","35 mins*")],"No water or steam. Dries, and stores bottles inside.","*for 6 clear bottles. Separate every part so light reaches each surface.",ph=620)
ST=[("Tommee Tippee Microwave","24 hours","Lid kept closed"),("Baby Brezza","24 hours","Left unopened"),("Tommee Tippee Ultra UV","Until turned off","In storage mode")]
st="".join(f'''<div style="display:flex;align-items:center;padding:30px 0;border-top:{"0" if i==0 else f"3px solid {PINK}"}"><div style="flex:1"><div class="h" style="font-size:40px">{a}</div><div style="font-size:30px;font-weight:600;opacity:.65;margin-top:4px">{d}</div></div><div class="h" style="font-size:42px;text-align:right">{c}</div></div>''' for i,(a,c,d) in enumerate(ST))
s8=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="kick" style="color:{ROSE};opacity:1">THE SMALL PRINT</div><div class="h" style="font-size:80px;margin-top:8px">How long does sterile last?</div>
<div class="b" style="margin-top:16px">It depends on your model. The NHS doesn't give a number, so check the manual.</div></div>
<div class="c" style="position:absolute;left:60px;right:60px;top:480px;background:#fff;border-radius:40px;padding:14px 44px 18px">{st}</div>
<div style="position:absolute;left:70px;right:70px;top:960px"><div class="b" style="font-size:36px">Open the lid? Wash and dry your hands, put teats and lids on bottles straight away, and use a clean surface.</div>
<div style="font-size:27px;font-weight:600;opacity:.7;margin-top:14px">Makers' figures. Clean equipment only.</div></div>'''
BK=[("Cold water","At least 30 minutes, says the NHS, even if a pack says less. Change the solution every 24 hours. Keep everything under the water with no air bubbles."),("Boiling","At least 10 minutes, all under the water. Check items are safe to boil. Teats wear out faster, so check them often."),("Mini UV pods","Made for soothers, teats and small items. Not a full bottle set.")]
bk="".join(f'''<div style="padding:28px 0;border-top:{"0" if i==0 else f"3px solid {PINK}"}"><div class="h c" style="font-size:47px">{a}</div><div class="b c" style="font-size:35px;margin-top:8px">{c}</div></div>''' for i,(a,c) in enumerate(BK))
s9=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="kick" style="color:{ROSE};opacity:1">POWER CUT OR HOLIDAY</div><div class="h" style="font-size:84px;margin-top:8px">Know your backup</div></div>
<div style="position:absolute;left:60px;right:60px;top:250px;background:#fff;border-radius:40px;padding:12px 44px 22px">{bk}</div>'''
s10=deco+f'''<div style="position:absolute;left:60px;right:60px;top:60px;height:540px;background:{ROSE};border-radius:44px;display:flex;align-items:flex-end;justify-content:center;gap:22px;padding:44px">{im(MI,210,"flex:none")}{im(BR,420,"flex:none")}{im(UV,280,"flex:none")}</div>
<div style="position:absolute;left:70px;right:70px;top:640px"><div class="h" style="font-size:80px">Picked your type? Compare prices first</div>
<div class="b" style="margin-top:18px;font-size:38px">Compare steriliser prices from UK shops in one place.</div>
<div style="margin-top:30px;display:flex;align-items:center;gap:16px"><div class="h c" style="font-size:46px;background:#fff;padding:22px 32px;border-radius:24px">babysorted.com/links</div>
<div style="background:{MINT};color:{NAVY};font-weight:800;font-size:32px;padding:22px 26px;border-radius:24px;white-space:nowrap">Link in bio ↑</div></div>
<div style="margin-top:22px;font-size:32px;font-weight:700;opacity:.6">Save this post for later</div></div>'''
s10=s10.replace(f"background:{MINT};color:{NAVY}",f"background:{ROSE};color:{NAVY}")
PN=[(MI,"Microwave steam","Tommee Tippee 2-in-1. 4 bottles in 4 mins.*","From £24.95"),(EL,"Electric steam","Tommee Tippee Electric. 6 bottles, under 8 mins.","£54.95"),(BR,"Steam and dry","Baby Brezza. 8 bottles plus pump parts.","£129.99"),(UV,"UV and dry","Tommee Tippee Ultra UV. 6 clear bottles, 35 mins.","£111.84")]
pn="".join(f'''<div class="c" style="display:flex;align-items:center;gap:20px;background:#fff;border-radius:28px;padding:12px 26px 12px 16px;margin-top:14px"><div style="flex:none;width:150px;height:150px;display:flex;align-items:center;justify-content:center;background:{ROSE};border-radius:20px"><img src="{s}" style="max-width:124px;max-height:126px"></div><div style="flex:1"><div class="h" style="font-size:38px">{a}</div><div style="font-size:26px;font-weight:600;opacity:.75;margin-top:6px;line-height:1.25">{c}</div></div><div class="h" style="font-size:33px;text-align:right;white-space:nowrap">{e}</div></div>''' for s,a,c,e in PN)
pin=f'''{star(910,50,32,ROSE)}<div style="position:absolute;left:60px;right:60px;top:60px"><div class="tags"><span class="tag t1" style="font-size:24px">Buying guide</span><span class="tag t2" style="font-size:24px">Nursing &amp; Feeding</span></div>
<div class="h" style="font-size:80px;margin-top:20px">Best bottle sterilisers: steam vs UV</div>
<div style="font-size:31px;font-weight:600;opacity:.8;margin-top:12px">Steam is quick. UV is dry. Wash first with both.</div></div>
<div style="position:absolute;left:60px;right:60px;top:368px">{pn}</div>
<div style="position:absolute;left:60px;right:60px;top:1136px;background:{ROSE};color:{NAVY};border-radius:26px;padding:22px 28px"><div style="font-weight:800;font-size:22px;opacity:.7;letter-spacing:.06em">GOOD TO KNOW</div><div style="font-size:28px;font-weight:600;margin-top:4px;line-height:1.3">A dishwasher cleans but doesn't sterilise. The NHS says sterilise until at least 12 months. It lists steam, cold water and boiling, but doesn't cover UV.</div></div>
<div style="position:absolute;left:60px;right:60px;top:1352px;font-size:23px;font-weight:600;opacity:.7">*Based on 1100W, plus cool-down. Times are makers' figures.</div>
<div style="position:absolute;left:60px;right:60px;bottom:40px;display:flex;justify-content:space-between;align-items:center"><div class="brand" style="font-size:34px">BabySorted</div><div style="font-weight:700;font-size:25px">Compare steriliser prices at babysorted.com</div></div>'''
render(ROOT+"/out/p2",[cover,s2,s3,s4,s5,s6,s7,s8,s9,s10],pin,CSS,"#fff")
