# Navy "plate" layout (22 Nov 2026): navy bg, a big white plate (circle) with a pink rim at the top holding the key fact
# or the kit products, white text below, mint step pill. Photo-led cover and last slide.
# Used for: Parenting Tips #65 First foods: what you need for weaning. Facts: NHS (incl. Best Start in Life weaning pages).
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css(NAVY,"#fff",MINT,NAVY)+".t2{background:#fff;color:#051F45;box-shadow:none}"
BOWL=b("bowl.png",700); SPOON=b("spoon.png",700); BIB=b("bibs.png",700); DATE="20 Nov 2026"
NHS="Source: NHS"
deco=star(50,50,26,ROSE)+star(1000,70,30,PINK,.8)+star(960,600,20,MINT,.8)
def plate(inner,w=500):
    return f'<div style="position:absolute;left:{540-w//2}px;top:60px;width:{w}px;height:{w}px;border-radius:50%;background:#fff;box-shadow:0 0 0 22px {ROSE},0 0 0 26px {PINK};display:flex;align-items:center;justify-content:center;color:{NAVY};text-align:center">{inner}</div>'
def sl(step,title,body,inner,src=NHS):
    return deco+plate(inner)+f'''<div style="position:absolute;left:70px;right:70px;top:640px"><span style="background:{MINT};color:{NAVY};font-weight:800;font-size:27px;padding:9px 22px;border-radius:30px;letter-spacing:.04em">{step}</span>
<div class="h" style="font-size:64px;margin-top:22px">{title}</div><div class="b" style="margin-top:14px;font-size:36px">{body}</div></div>
<div style="position:absolute;left:70px;right:70px;top:1110px;font-size:23px;font-weight:700;opacity:.7">{src}.</div>'''
def big(a,c,fs=110): return f'<div style="padding:30px"><div class="h" style="font-size:{fs}px;line-height:1">{a}</div><div class="h" style="font-size:34px;margin-top:12px">{c}</div></div>'
def prodp(src,h,price,name): return f'<div><img src="{src}" style="height:{h}px;{SH}"><div class="h" style="font-size:38px;margin-top:6px">{price}</div><div style="font-size:19px;font-weight:600;opacity:.75;line-height:1.2">{name}</div></div>'
cover=hero_cover(baby(27,1080,800,.5,.32,1.1),'<div class="tags"><span class="tag t1">Parenting Tips</span><span class="tag t2">Nursing &amp; Feeding</span></div>',"First foods: what you really need","A short list for a messy, happy start.",f'<div style="position:relative;width:280px;height:280px"><img src="{BOWL}" style="position:absolute;left:0;top:70px;width:190px;{SH}"><img src="{SPOON}" style="position:absolute;right:0;top:20px;width:130px;{SH}"></div>',1,card=NAVY,fg="#fff",pill_bg=MINT,pill_fg=NAVY,title_fs=70)
s2=sl("WHEN","Around 6 months, 3 signs together","They can stay sitting and hold their head steady, coordinate eyes, hands and mouth, and swallow food rather than push it back out.",big("6","months, give or take",150))
s3=sl("NOT A SIGN","Easy to mistake for ready","Chewing fists, wanting extra milk feeds and waking in the night more than usual are normal baby behaviour. They don't mean your baby needs food yet.",big("Fists","chewing isn't a sign",96))
s4=sl("KIT 1","A seat with straps","Your baby needs to sit upright and strapped in, so they can swallow properly. Check the high chair's straps before you buy.",big("Upright","and strapped in",92))
s5=sl("KIT 2","Soft spoons, a suction bowl","Soft weaning spoons are kinder on gums. A bowl with a suction base stays on the tray. That's it: no gadgets needed.",f'<div style="display:flex;gap:22px;align-items:flex-end">{prodp(BOWL,175,"£14.02","Mushie bowl")}{prodp(SPOON,215,"£7.96","Bibado spoon")}</div>',f"Source: NHS. Prices on BabySorted, {DATE}")
s6=sl("KIT 3","An open cup and a bib","Offer sips of water with meals from around 6 months, in an open or free-flow cup without a valve. Plastic or pelican bibs are easiest to clean.",f'<div style="display:flex;align-items:center;gap:10px">{prodp(BIB,220,"£9.56","Lassig silicone bib")}</div>',f"Source: NHS. Price on BabySorted, {DATE}")
s7=sl("FOOD","Lumps and finger food early","Move from purées to mashed and finger foods as soon as you can. Finger food should be big enough to hold in a fist with a bit sticking out.",big("Fist","+ a bit sticking out",110))
s8=sl("SAFETY","Gagging is loud. Choking is quiet.","Gagging, with watery eyes and retching, is a normal part of learning. Choking is quiet. Always stay with your baby while they eat.",big("Stay","with them at every meal",110))
s9=sl("AVOID","Small changes, big difference","Cut grapes and cherry tomatoes into quarters. No honey before 1 year. No whole nuts before 5. No added salt or sugar.",big("¼","grapes in quarters",150))
s10=hero_last(baby(30,1080,700,.5,.4),"Setting up for weaning? Compare prices first","Compare high chair and feeding prices from UK shops in one place.",PINK,fg="#fff",photo_h=700,note="Worried about feeding? Talk to your health visitor or GP.")
pin=pin_hero(baby(38,1000,680,.45,.45,1.15),pin_tags("Parenting Tips","Nursing &amp; Feeding"),"First foods: what you really need",
 ["Start at around 6 months","Sitting up, strapped in","Soft spoons, suction bowl","Open cup for sips of water","Quarter grapes, no honey before 1","Always stay while they eat"],
 BOWL,170,NAVY,"#fff",MINT,NAVY,"Source: NHS.","Compare weaning kit prices at babysorted.com",line="rgba(255,255,255,.25)",photo_h=680,title_fs=54)
render(ROOT+"/out/d",[cover,s2,s3,s4,s5,s6,s7,s8,s9,s10],pin,CSS,"#fff")
