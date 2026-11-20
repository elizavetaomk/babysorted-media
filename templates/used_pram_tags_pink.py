# Pink "inspection tag" layout (21 Nov 2026): pink bg, tall white tag card with a punched hole and string,
# mint CHECK stamp, title + body inside the tag, deeper-pink "why" strip. Photo-led cover and last slide.
# Used for: #49 New or second-hand pram. Facts: The Lullaby Trust, RoSPA, GOV.UK recalls.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css(PINK,NAVY,NAVY,"#fff")+".t2{background:#fff;box-shadow:none}"
EGG=b("egg.png",900); DATE="20 Nov 2026"
LT="Source: The Lullaby Trust, the UK safer baby sleep charity"; RO="Source: RoSPA, the UK accident prevention charity"
deco=star(46,40,26,"#fff")+star(1000,60,32,"#fff")+star(980,1150,22,"#fff")
def bigv(a,c): return f'<div style="margin-top:70px;text-align:center"><div class="h" style="font-size:118px;line-height:1">{a}</div><div class="h" style="font-size:36px;margin-top:12px;opacity:.6">{c}</div></div>'
def tag(stamp,title,body,why,src=None,visual=""):
    s=f'<div style="font-size:23px;font-weight:700;opacity:.65;margin-top:18px">{src}</div>' if src else ""
    return deco+f'''<svg style="position:absolute;left:520px;top:0" width="40" height="120"><path d="M20 0 C 5 40, 35 70, 20 118" stroke="{NAVY}" stroke-width="4" fill="none"/></svg>
<div style="position:absolute;left:90px;right:90px;top:110px;bottom:150px;background:#fff;border-radius:40px 40px 40px 40px;padding:110px 60px 50px">
<div style="position:absolute;left:50%;top:34px;width:46px;height:46px;margin-left:-23px;border-radius:50%;background:{PINK};box-shadow:inset 0 0 0 6px {ROSE}"></div>
<div style="display:inline-block;background:{MINT};font-weight:800;font-size:30px;padding:10px 24px;border-radius:14px;transform:rotate(-3deg);letter-spacing:.04em">{stamp}</div>
<div class="h" style="font-size:66px;margin-top:22px">{title}</div><div class="b" style="margin-top:16px;font-size:36px">{body}</div>{visual}
<div style="position:absolute;left:40px;right:40px;bottom:40px"><div style="background:{ROSE};border-radius:24px;padding:20px 28px;font-weight:800;font-size:30px;line-height:1.25">{why}</div>{s}</div></div>'''
cover=hero_cover(baby(41,1080,800,.45,.45,1.05),'<div class="tags"><span class="tag t1">Comparison</span><span class="tag t2">Pushchairs</span></div>',"New or second-hand pram?","Second-hand can be smart. Check these first.",f'<img src="{EGG}" style="height:300px;{SH}">',1,card=PINK,fg=NAVY,pill_bg=NAVY,pill_fg="#fff",title_fs=72)
s2=tag("THE SHORT ANSWER","A used frame can be fine. The mattress should be new.","The Lullaby Trust advises a new mattress for each baby. If your baby will nap in the carrycot, use the same rule for its mattress.","Ask what's included before you agree a price.",LT+".",visual=bigv("New","mattress for each baby"))
S=[tag("CHECK 1","Get the model name and the instructions","Most makers put manuals online. Look for the safety standard on the label: BS EN 1888 for pushchairs and prams.","No model name? Walk away.",LT+".",visual=bigv("BS EN 1888","on the label")),
tag("CHECK 2","Search GOV.UK for recalls","Type the brand and model into the GOV.UK product safety alerts, reports and recalls list. Prams and carrycots do get recalled.","Takes 2 minutes. Do it before you travel to collect.","Source: GOV.UK.",visual=bigv("2 min","brand + model search")),
tag("CHECK 3","Brakes: lock, then push","Put the brake on and push the pram hard. It shouldn't roll. Then unlock it and check the wheels turn freely.","A brake that slips is a deal-breaker.",RO+".",visual=bigv("Lock + push","it shouldn't roll")),
tag("CHECK 4","All five harness straps","Two shoulder straps, two waist straps and one between the legs. Check every buckle clicks and the straps aren't frayed.","Missing a strap? Don't buy it.",RO+".",visual=bigv("5 straps","shoulders, waist, legs")),
tag("CHECK 5","Unfold it and look for the lock","Open the pram yourself. It should lock firmly into place with no wobble at the joints. Look for broken or missing parts too.","Fold and unfold it 3 times before you pay.","Sources: RoSPA, the UK accident prevention charity; The Lullaby Trust.",visual=bigv("Click","no wobble")),
tag("BEFORE YOU PAY","Test it in person","A private seller may not take it back. Push it over a kerb, check the hood clips and ask for the rain cover and adaptors.","Missing parts add up fast.",visual=bigv("Kerb test","before you pay"))]
egg=f'''<div style="display:flex;align-items:center;gap:30px;margin-top:22px"><img src="{EGG}" style="height:330px;{SH}"><div><div class="h" style="font-size:58px">£879.00</div><div style="font-size:22px;font-weight:600;opacity:.7;line-height:1.3;margin-top:6px">Egg 3 Stroller, Celestial<br>Price on BabySorted, {DATE}</div></div></div>'''
s9=tag("BUYING NEW?","Compare before you pay","New comes with the maker's warranty and a fresh mattress. The same pram can cost different amounts in different shops.",'Compare pram prices at babysorted.com',visual=egg)
s10=hero_last(baby(13,1080,700,.5,.35),"New or used, compare prices first","Compare pram and pushchair prices from UK shops in one place.",MINT,fg=NAVY,photo_h=700)
pin=pin_hero(baby(51,1000,680,.5,.4),pin_tags("Comparison","Pushchairs"),"Buying a second-hand pram?",
 ["A new mattress for each baby","Get the model name and manual","Search GOV.UK for recalls","Brakes: lock, then push hard","All 5 harness straps","It locks open with no wobble"],
 EGG,240,PINK,NAVY,NAVY,"#fff","Sources: The Lullaby Trust, the UK safer baby sleep charity; RoSPA, the UK accident prevention charity; GOV.UK.","Compare pram prices at babysorted.com",line="#fff",photo_h=680,title_fs=56)
render(ROOT+"/out/b",[cover,s2]+S+[s9,s10],pin,CSS,NAVY)
