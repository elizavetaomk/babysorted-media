# Deeper-pink "cup card" layout (27 Nov 2026): deeper pink bg, a big white rounded card on the top half holding the product
# or one short keyword, a navy pill on the card edge, navy text below. Used for: #59 First cups. No prices.
# Facts: NHS "Drinks and cups for babies and young children" (cup from around 6 months, sips of water with meals; open or
# free-flow cup without a valve helps learn to sip and is better for teeth; water over 6 months needn't be boiled; cows' milk
# in cooking from 6 months, not a main drink until 12 months; under 12 months don't need juice or smoothies; squash can cause
# tooth decay even diluted; from 1 year bottles should be discouraged; only breast milk, formula or water in a bottle or trainer cup).
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css(ROSE,NAVY,NAVY,"#fff")+".t2{background:#fff;box-shadow:none}"
NHS="Source: NHS"
MC=b("mcups.png",800); MS=b("mstraw.png",700)
def card(inner,pill):
    return f'''<div style="position:absolute;left:70px;right:70px;top:70px;height:520px;background:#fff;border-radius:48px;display:flex;align-items:center;justify-content:center;text-align:center">{inner}</div>
<div class="h" style="position:absolute;left:110px;top:560px;background:{NAVY};color:#fff;font-size:32px;padding:16px 30px;border-radius:40px">{pill}</div>'''
def slide(inner,pill,title,body,src=NHS):
    s=f'<div style="position:absolute;left:70px;right:70px;top:1190px;font-size:24px;font-weight:700;opacity:.8">{src}</div>' if src else ""
    return card(inner,pill)+f'''<div style="position:absolute;left:70px;right:70px;top:680px"><div class="h" style="font-size:68px">{title}</div>
<div class="b" style="margin-top:18px;font-size:38px">{body}</div></div>{s}'''
pimg=lambda s,h: f'<img src="{s}" style="height:{h}px;max-width:820px;object-fit:contain;{SH}">'
word=lambda a,c,fs=150: f'<div><div class="h" style="font-size:{fs}px">{a}</div><div style="font-weight:700;font-size:34px;opacity:.7;margin-top:10px">{c}</div></div>'
cover=hero_cover(baby(39,1080,800,.5,.42,1.15),'<div class="tags"><span class="tag t1">Tips</span><span class="tag t2">Nursing &amp; Feeding</span></div>',
 "First cups: what to start with","From 6 months, sips beat sucks.",f'<img src="{MS}" style="width:250px;{SH}">',1,card=ROSE,title_fs=74,pill="Swipe for 7 tips")
s2=slide(word("6m+","around 6 months, with meals",170),"FROM ~6 MONTHS","Start with sips at mealtimes","Offer sips of water from a cup with meals from around 6 months. Spills are part of learning.")
s3=slide(pimg(MC,330),"NO VALVE","Open or free-flow cup","An open cup, or a free-flow cup without a valve, helps your baby learn to sip rather than suck. It’s better for their teeth too.")
s4=slide(word("Valve?","check the lid before you buy"),"SHOPPING TIP","‘Non-spill’ can mean a valve","Leak-proof lids often work with a valve. Read the listing or check the lid in the shop, and pick a free-flow lid to start.",src="")
s5=slide(pimg(MS,400),"WATER","Tap water, no boiling needed","Drinking water for babies over 6 months doesn’t need to be boiled first. Keep offering it with meals.")
s6=slide(word("12m","cows’ milk as a main drink",170),"COWS’ MILK","In food first, as a drink later","Cows’ milk can go in cooking from around 6 months, but not as a main drink until 12 months.")
s7=slide(word("No juice","needed in year one",130),"SKIP","Juice and squash can wait","Babies under 12 months don’t need fruit juice or smoothies. Squash can cause tooth decay, even when diluted.")
s8=slide(word("Age 1","time to move off the bottle",170),"FIRST BIRTHDAY","From 1, cup instead of bottle","Once your baby is 1, the NHS says bottle feeding should be discouraged. In a bottle or trainer cup: only milk or water.")
s9=hero_last(baby(30,1080,760,.6,.4,1.1),"Sip, spill, repeat","Compare baby cup prices from UK shops in one place.","#fff")
pin=pin_hero(baby(38,1000,660,.5,.45,1.15),pin_tags("Tips","Nursing &amp; Feeding"),"First cups: 6 simple rules",
 ["Start sips at around 6 months","Open or free-flow, no valve","Tap water: no boiling from 6m","Cows’ milk as a drink from 12m","No juice needed in year one","From age 1, move off the bottle"],
 MC,200,ROSE,NAVY,NAVY,"#fff","Source: NHS.","Compare baby cup prices at babysorted.com",line="#fff",photo_h=660,title_fs=58)
render(ROOT+"/out/b",[cover,s2,s3,s4,s5,s6,s7,s8,s9],pin,CSS,NAVY)
