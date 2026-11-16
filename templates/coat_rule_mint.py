# Mint "rule cards" checklist (17 Nov 2026): mint bg, navy side tab with the rule number, white card with a simple
# illustration or product, tick row. Photo-led cover and last slide.
# Used for: #47 Winter car seat safety: the puffy coat rule. Facts: RoSPA (childcarseats.org.uk), NHS (MKUH car seat leaflet), The Lullaby Trust.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css(MINT,NAVY,NAVY,"#fff")+".t2{background:#fff;box-shadow:none}"
CT=b("cloudt.png",1000)
deco=star(36,30,26,"#fff")+star(1004,40,30,"#fff")
RS="Source: RoSPA, the UK accident prevention charity"; LT="Source: The Lullaby Trust, the UK safer baby sleep charity"
def ico(word,sub,bg=PINK): return f'<div style="text-align:center"><div class="h" style="font-size:118px;background:{bg};padding:10px 44px;border-radius:40px;display:inline-block">{word}</div><div style="font-weight:700;font-size:32px;margin-top:20px">{sub}</div></div>'
def rule(k,title,body,src,inner):
    dots="".join(f'<div style="width:22px;height:22px;border-radius:50%;background:{NAVY if j<=k else "#fff"}"></div>' for j in range(7))
    return deco+f'''<div style="position:absolute;left:60px;right:60px;top:60px;height:560px;background:#fff;border-radius:44px;overflow:hidden">
<div style="position:absolute;left:0;top:0;bottom:0;width:150px;background:{NAVY};color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center"><div style="font-weight:700;font-size:24px;letter-spacing:.08em;opacity:.7">RULE</div><div class="h" style="font-size:110px">{k+1}</div></div>
<div style="position:absolute;left:150px;right:0;top:0;bottom:0;display:flex;align-items:center;justify-content:center;padding:30px">{inner}</div></div>
<div style="position:absolute;left:70px;right:70px;top:665px"><div style="display:flex;gap:10px">{dots}</div><div class="h" style="font-size:64px;margin-top:22px">{title}</div><div class="b" style="margin-top:14px;font-size:37px">{body}</div>
<div style="font-size:25px;font-weight:700;opacity:.6;margin-top:14px">{src}</div></div>'''
seat=lambda h: f'<img src="{CT}" style="height:{h}px;{SH}">'
cover=hero_cover(baby(21,1080,800,.5,.45),'<div class="tags"><span class="tag t1">Checklist</span><span class="tag t2">Car Seats</span></div>',"Winter car seats: the puffy coat rule","7 checks before every cold drive.",seat(250),1,card=MINT,fg=NAVY,pill_bg=NAVY,pill_fg="#fff",title_fs=64)
vs=lambda t,c,bg: f'<div style="flex:1;background:{bg};border-radius:34px;padding:36px 30px"><div class="h" style="font-size:48px">{t}</div><div style="font-size:31px;font-weight:500;line-height:1.35;margin-top:12px">{c}</div></div>'
s2=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="kick">WHY IT MATTERS</div><div class="h" style="font-size:80px;margin-top:8px">It feels tight. It isn't.</div></div>
<div style="position:absolute;left:60px;right:60px;top:330px;display:flex;gap:20px">{vs("Over a puffy coat","The harness presses on padding, not on your child. It feels snug, but the slack is hidden.","#fff")}{vs("Coat off","The harness sits close to your child's body, the way the seat is designed to work.",PINK)}</div>
<div class="b" style="position:absolute;left:70px;right:70px;top:800px;font-size:39px">NHS car seat advice is clear: no thick clothing or coats under a harness. Here's how to keep them safe and warm.</div>
<div style="position:absolute;left:70px;top:1180px;font-size:25px;font-weight:700;opacity:.6">Source: NHS</div>'''
R=[("Coat off, then strap in","Take off snowsuits and thick coats before the harness goes on. Do it in the car, with the heating on, so it's quick.","Source: NHS",ico("Coat off","before the straps go on")),
("The two-finger check","Only one or two fingers should fit between your child's chest and the harness. Clothes change the fit, so check every journey.",RS,ico("1–2","fingers, no more",MINT)),
("The pinch test","Try to pinch the harness strap at your child's shoulder. If you can pinch a fold of it, it's too loose. Tighten it.","Source: NHS",ico("No fold","= tight enough")),
("Warmth goes on top","Once they're strapped in, lay a blanket over the top of the harness. Never put blankets or towels under your baby.","Source: NHS",seat(400)),
("Hats and hoods off","Once your baby is in a warm car, take off hats and hoods so they don't get too hot.",LT,ico("Hat off","in a warm car",MINT)),
("Check the chest or neck","Check the chest or the back of the neck. Sweaty or clammy? They are too hot, so take a layer off.",LT,ico("Chest","or back of the neck")),
("Only liners made for your seat","Footmuffs and liners that go behind your baby change how the harness fits. Car seat makers say use only ones made for your seat.","",ico("Made for","your seat only",MINT))]
rules=[rule(k,*r) for k,r in enumerate(R)]
s10=hero_last(baby(27,1080,760,.5,.45),"Need a new seat for winter? Compare prices first","Compare car seat prices from UK shops in one place.",NAVY,fg=NAVY)
s10=s10.replace(f'background:{NAVY};color:{NAVY};padding:22px 30px',f'background:#fff;color:{NAVY};padding:22px 30px')
pin=pin_hero(baby(13,1000,680,.5,.4),pin_tags("Checklist","Car Seats"),"The puffy coat rule",["Coat off, then strap in","1–2 fingers under the harness","Pinch test at the shoulder","Blanket over the top, not under","Hats off in a warm car","Check the chest or neck"],CT,280,MINT,NAVY,NAVY,"#fff","Sources: RoSPA, the UK accident prevention charity, NHS and The Lullaby Trust, the UK safer baby sleep charity.","Compare car seat prices at babysorted.com",line="#fff",photo_h=680,title_fs=60)
render(ROOT+"/out/c",[cover,s2]+rules+[s10],pin,CSS,NAVY)
