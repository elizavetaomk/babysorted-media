# Pink "price tags" layout: pink bg, white photo panel with a navy price tag (now / was / saving), notes below; true-cost table; checks list.
# Used for: Nursery furniture deals before Christmas (Nov 2026). Prices from the BabySorted catalog.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from slide_lib import *
KU=b("kuba.png"); MO=b("modena.png"); KUW=b("kuba_w.jpg"); MOW=b("modena_w.jpg"); LU=b("luna_w2.jpg"); WA=b("walton_w2.jpg")
CSS=css(PINK,NAVY,NAVY,"#fff")+".t2{background:#fff}"
deco=star(36,30,26,"#fff")+star(1000,36,30,"#fff")
SH="filter:drop-shadow(0 18px 18px rgba(5,31,69,.20))"
def tag(now,was,save,x=""):
    return f'''<div style="position:absolute;{x};background:{NAVY};color:#fff;border-radius:30px;padding:20px 32px;text-align:left;transform:rotate(-3deg);box-shadow:0 14px 24px rgba(5,31,69,.22)">
<div class="h" style="font-size:74px">{now}</div><div style="font-size:29px;font-weight:600;margin-top:6px;white-space:nowrap"><s style="opacity:.75">was {was}</s> &nbsp;<b style="color:{PINK};font-weight:800">{save}</b></div></div>'''
def deal(k,name,best,pic,h,now,was,save,get,watch):
    return deco+f'''<div style="position:absolute;left:60px;right:60px;top:60px;height:610px;background:#fff;border-radius:44px;overflow:hidden;display:flex;align-items:center;justify-content:center"><img src="{pic}" style="height:{h}px;max-width:880px;object-fit:contain;margin-top:34px"></div>
<div style="position:absolute;left:92px;top:90px;font-weight:800;font-size:26px;background:{PINK};padding:7px 16px;border-radius:18px">Deal {k} of 4</div>
{tag(now,was,save,"right:40px;top:520px")}
<div style="position:absolute;left:70px;right:70px;top:700px"><div class="h" style="font-size:66px;width:600px">{name}</div>
<div style="margin-top:16px"><span class="pill" style="background:#fff">{best}</span></div>
<div class="b" style="margin-top:20px">{get}</div><div class="b" style="margin-top:12px"><b style="font-weight:800">Watch out:</b> {watch}</div></div>'''
cover=star(980,60,40,"#fff")+star(50,640,24,"#fff")+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="tags"><span class="tag t1">Deals</span><span class="tag t2">Kids Furniture</span></div>
<div class="h" style="font-size:98px;margin-top:26px">Nursery furniture deals before Christmas</div>
<div style="font-size:38px;font-weight:600;opacity:.75;margin-top:16px;white-space:nowrap">Set up for less. Check the sums first.</div></div>
<img src="{KU}" style="position:absolute;left:-90px;bottom:120px;width:960px;{SH}">
{tag("£179","£399","Save £220","right:40px;top:690px")}
<div style="position:absolute;left:70px;bottom:124px"></div>
<div style="position:absolute;right:60px;bottom:136px;background:{NAVY};color:#fff;font-weight:700;font-size:30px;padding:14px 28px;border-radius:40px">Swipe before you buy</div>'''
def stat(n,t): return f'<div style="background:#fff;border-radius:34px;padding:30px 36px;margin-top:20px;display:flex;align-items:center;gap:30px"><div class="h" style="flex:none;width:250px;font-size:92px">{n}</div><div class="b" style="font-size:36px">{t}</div></div>'
s2=deco+f'''<div style="position:absolute;left:70px;right:70px;top:70px"><div class="kick">BEFORE ANY DEAL</div><div class="h" style="font-size:84px;margin-top:8px">A big “was” price proves nothing</div></div>
<div style="position:absolute;left:60px;right:60px;top:350px">{stat("83%","of products Which? tracked were the same price or cheaper outside the Black Friday sales period.")}{stat("0","of those deals were at their lowest price of the year on Black Friday itself.")}</div>
<div style="position:absolute;left:70px;right:70px;top:840px"><div class="b">So you don't have to wait for one big day. Compare today's price across shops, then decide.</div>
<div style="font-size:27px;font-weight:600;opacity:.65;margin-top:22px;line-height:1.35">Which?, Nov 2025: 175 home, tech and health products from eight retailers. It did not test nursery furniture, but the habit is the same.</div></div>'''
s3=deal(1,"Tutti Bambini Kuba","Best under £200",KUW,510,"£179","£399","Save £220","Golden oak finish with a sage weave. Comes with a matching bed guard and teething rails.","it's a cot bed only, so add a mattress.")
s4=deal(2,"Tutti Bambini Modena","Best for the long run",MOW,510,"£239","£459","Save £220","Cot, toddler bed, then a small sofa, up to about age 6. Three mattress heights.","the sofa stage needs floor space. Measure first.")
s5=deal(3,"CuddleCo Luna","Best first set",LU,440,"£449","£798","Save £349","Cot bed and dresser changer in white and oak. Three drawers and a removable top.","compare the set price across shops, not just the saving.")
s6=deal(4,"Mamas &amp; Papas Walton","Best full room",WA,530,"£599","£1,000","Save £401","Cot bed, dresser changer and wardrobe. The bed converts to a toddler bed.","tall pieces should be fixed to the wall. See slide 9.")
RW=[("Kuba","£179","£55","£234"),("Modena","£239","£55","£294"),("Luna set","£449","£55","£504"),("Walton set","£599","£55","£654")]
rw="".join(f'''<div style="display:flex;align-items:center;padding:24px 0;border-top:{"0" if i==0 else f"3px solid {PINK}"}"><div class="h" style="flex:1;font-size:44px">{a}</div><div style="width:150px;text-align:right;font-size:38px;font-weight:600;opacity:.65">{c}</div><div style="width:150px;text-align:right;font-size:38px;font-weight:600;opacity:.65">{d}</div><div class="h" style="width:190px;text-align:right;font-size:50px">{e}</div></div>''' for i,(a,c,d,e) in enumerate(RW))
s7=deco+f'''<div style="position:absolute;left:70px;right:70px;top:70px"><div class="kick">THE CATCH</div><div class="h" style="font-size:84px;margin-top:8px">The deal price isn't the bedtime price</div>
<div class="b" style="margin-top:16px">Most cot beds take a 140 × 70 cm mattress. It must fit snugly, so buy new and check your cot's size.</div></div>
<div style="position:absolute;left:60px;right:60px;top:510px;background:#fff;border-radius:40px;padding:24px 44px 26px"><div style="display:flex;font-weight:800;font-size:24px;letter-spacing:.05em;opacity:.55;padding:10px 0"><div style="flex:1"></div><div style="width:150px;text-align:right">DEAL</div><div style="width:150px;text-align:right">MATTRESS</div><div style="width:190px;text-align:right">REAL COST</div></div>{rw}</div>
<div style="position:absolute;left:74px;right:70px;top:1050px;font-size:27px;font-weight:600;opacity:.65;line-height:1.35">Prices from the BabySorted catalog on 4 Nov. Mattress from £55, a basic fibre cot bed mattress. Prices can change.</div>'''
CK=[("A safety standard on the label","BS EN 716 for cots, BS 8509 for cot beds."),("Bars 2.5 to 6.5 cm apart","Which? says this stops a head getting trapped."),("No mattress gap over 3 cm","Measure all round once it's in the cot."),("At least 50 cm of side height","From the top of the mattress to the top of the side.")]
ck="".join(f'''<div style="display:flex;gap:24px;padding:38px 0;border-top:{"0" if i==0 else f"3px solid {PINK}"}"><div style="flex:none;width:60px;height:60px;border-radius:18px;background:{NAVY};color:#fff;font-weight:800;font-size:32px;display:flex;align-items:center;justify-content:center">✓</div><div><div class="h" style="font-size:47px">{a}</div><div style="font-size:37px;font-weight:500;line-height:1.32;margin-top:10px">{c}</div></div></div>''' for i,(a,c) in enumerate(CK))
s8=deco+f'''<div style="position:absolute;left:70px;right:70px;top:70px"><div class="kick">A LOW PRICE CHANGES NOTHING</div><div class="h" style="font-size:80px;margin-top:8px">4 checks on any cot</div></div>
<div style="position:absolute;left:60px;right:60px;top:240px;background:#fff;border-radius:40px;padding:18px 44px 22px">{ck}</div>'''
US=[("Fix tall pieces to the wall","RoSPA says furniture at risk of being pulled over should be secured. To a child, drawers look like a climbing frame."),("Know your 14 days","Online orders usually have a 14-day cooling-off period from delivery. Custom-made items don't. Check who pays for returns."),("Measure the route in","Measure doors, stairs and turns before you order. Then ask about delivery dates for your area.")]
us="".join(f'''<div style="padding:36px 0;border-top:{"0" if i==0 else f"3px solid {PINK}"}"><div class="h" style="font-size:50px">{a}</div><div style="font-size:37px;font-weight:500;line-height:1.34;margin-top:10px">{c}</div></div>''' for i,(a,c) in enumerate(US))
s9=deco+f'''<div style="position:absolute;left:70px;right:70px;top:70px"><div class="kick">BEFORE YOU ORDER</div><div class="h" style="font-size:80px;margin-top:8px">The bits nobody adds up</div></div>
<div style="position:absolute;left:60px;right:60px;top:240px;background:#fff;border-radius:40px;padding:18px 44px 26px">{us}</div>'''
s10=deco+f'''<div style="position:absolute;left:60px;right:60px;top:60px;height:540px;background:#fff;border-radius:44px;display:flex;align-items:center;justify-content:center;padding:30px"><img src="{MOW}" style="height:470px;object-fit:contain"></div>
<div style="position:absolute;left:70px;right:70px;top:640px"><div class="h" style="font-size:80px">Found one you like? Compare prices first</div>
<div class="b" style="margin-top:18px;font-size:38px">Compare nursery furniture prices from UK shops in one place.</div>
<div style="margin-top:30px;display:flex;align-items:center;gap:16px"><div class="h" style="font-size:46px;background:#fff;padding:22px 32px;border-radius:24px">babysorted.com/links</div>
<div style="background:{NAVY};color:#fff;font-weight:800;font-size:32px;padding:22px 26px;border-radius:24px;white-space:nowrap">Link in bio ↑</div></div>
<div style="margin-top:22px;font-size:32px;font-weight:700;opacity:.55">Save this post for later</div></div>'''
PN=[(KUW,"Tutti Bambini Kuba","Cot bed under £200","£179","was £399"),(MOW,"Tutti Bambini Modena","Cot, toddler bed, sofa","£239","was £459"),(LU,"CuddleCo Luna","Cot bed + dresser","£449","was £798"),(WA,"Mamas &amp; Papas Walton","Cot bed, dresser, wardrobe","£599","was £1,000")]
pn="".join(f'''<div style="display:flex;align-items:center;gap:20px;background:#fff;border-radius:28px;padding:12px 26px 12px 16px;margin-top:14px"><div style="flex:none;width:170px;height:150px;display:flex;align-items:center;justify-content:center"><img src="{s}" style="max-width:166px;max-height:146px"></div><div style="flex:1"><div class="h" style="font-size:37px">{a}</div><div style="font-size:26px;font-weight:600;opacity:.75;margin-top:6px">{c}</div></div><div style="text-align:right"><div class="h" style="font-size:44px">{e}</div><div style="font-size:23px;font-weight:600;opacity:.6;margin-top:4px;white-space:nowrap">{f}</div></div></div>''' for s,a,c,e,f in PN)
pin=f'''{star(910,50,32,"#fff")}<div style="position:absolute;left:60px;right:60px;top:60px"><div class="tags"><span class="tag t1" style="font-size:24px">Deals</span><span class="tag t2" style="font-size:24px">Kids Furniture</span></div>
<div class="h" style="font-size:80px;margin-top:20px">Nursery furniture deals before Christmas</div>
<div style="font-size:31px;font-weight:600;opacity:.75;margin-top:12px">Add a mattress from £55 before you compare.</div></div>
<div style="position:absolute;left:60px;right:60px;top:368px">{pn}</div>
<div style="position:absolute;left:60px;right:60px;top:1132px;background:{NAVY};color:#fff;border-radius:26px;padding:22px 28px"><div style="font-weight:800;font-size:22px;opacity:.7;letter-spacing:.06em">4 CHECKS ON ANY COT</div><div style="font-size:28px;font-weight:600;margin-top:4px;line-height:1.3">BS EN 716 or BS 8509 on the label. Bars 2.5 to 6.5 cm apart. No mattress gap over 3 cm. 50 cm of side above the mattress.</div></div>
<div style="position:absolute;left:60px;right:60px;top:1332px;font-size:23px;font-weight:600;opacity:.65">Prices from the BabySorted catalog on 4 Nov. Prices can change.</div>
<div style="position:absolute;left:60px;right:60px;bottom:40px;display:flex;justify-content:space-between;align-items:center"><div class="brand" style="font-size:34px">BabySorted</div><div style="font-weight:700;font-size:25px">Compare nursery prices at babysorted.com</div></div>'''
render(ROOT+"/out/p1",[cover,s2,s3,s4,s5,s6,s7,s8,s9,s10],pin,CSS,NAVY)
