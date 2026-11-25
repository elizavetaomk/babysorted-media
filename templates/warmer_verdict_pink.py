# Pink "verdict stamp" layout (25 Nov 2026): pink bg, white panel on top with a tilted navy stamp (NOT NEEDED / HANDY / SKIP IT ...)
# and a product, navy text below. Used for: #54 Bottle warmers: do you need one?
# Facts: NHS Best Start in Life "How to make up a bottle feed" (70C water, cool under tap, wrist test, throw away leftovers),
# NHS "Expressing and storing breast milk" (cold from fridge is fine, warm in jug of warm water, no microwave, use within 1 hour).
# Prices from the BabySorted catalog, last updated 22 Nov 2026.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css(PINK,NAVY,NAVY,"#fff")+".t2{background:#fff;box-shadow:none}"
DATE="22 Nov 2026"; NHS="Source: NHS"
BZ=b("brezza.png",700); TT=b("ttwarm.png",700); MV=b("moov.png",700)
deco=star(46,40,24,"#fff")+star(1000,60,30,"#fff",.9)
def stamp(word,rot=-8,fs=78):
    return f'<div style="transform:rotate({rot}deg);border:8px solid {NAVY};color:{NAVY};border-radius:26px;padding:10px 30px;font-weight:900;font-size:{fs}px;letter-spacing:.02em;white-space:nowrap">{word}</div>'
def disc(big,small,fs=96):
    return f'<div style="width:300px;height:300px;border-radius:50%;background:{NAVY};color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center"><div class="h" style="font-size:{fs}px">{big}</div><div style="font-weight:700;font-size:26px;margin-top:6px;opacity:.85">{small}</div></div>'
def slide(kick,q,word,title,body,img=None,h=330,src=NHS,ifs=78,dsc=None):
    pic=f'<img src="{img}" style="max-height:{h}px;max-width:330px;object-fit:contain;{SH}">' if img else (disc(*dsc) if dsc else "")
    s=f'<div style="position:absolute;left:70px;right:70px;top:1185px;font-size:23px;font-weight:700;opacity:.75">{src}</div>' if src else ""
    return deco+f'''<div style="position:absolute;left:50px;right:50px;top:90px;height:560px;background:#fff;border-radius:40px">
<div style="position:absolute;left:44px;top:40px;font-weight:800;font-size:26px;letter-spacing:.05em;opacity:.6">{kick}</div>
<div class="h" style="position:absolute;left:44px;top:84px;width:{560 if (img or dsc) else 880}px;font-size:46px">{q}</div>
<div style="position:absolute;left:44px;bottom:60px">{stamp(word,fs=ifs)}</div>
<div style="position:absolute;right:40px;top:60px;bottom:40px;width:360px;display:flex;align-items:center;justify-content:center">{pic}</div></div>
<div style="position:absolute;left:70px;right:70px;top:700px"><div class="h" style="font-size:60px">{title}</div><div class="b" style="margin-top:16px;font-size:35px">{body}</div></div>{s}'''
cover=hero_cover(baby(18,1080,800,.5,.45,1.0),'<div class="tags"><span class="tag t1">Buying guide</span><span class="tag t2" style="box-shadow:inset 0 0 0 3px #051F45">Nursing &amp; Feeding</span></div>',"Bottle warmers: do you need one?","Handy at 3am. But not for everyone.",f'<img src="{BZ}" style="height:330px;{SH}">',1,card=PINK,fg=NAVY,title_fs=74)
s2=slide("1 · POWDERED FORMULA","You make up powdered formula","NOT NEEDED","Formula needs cooling, not warming","Make it with water at 70C or hotter to kill germs, then cool the bottle under a cold tap. A warmer can’t do that step for you.",None,dsc=("70C+","water to make it"))
s3=slide("2 · EXPRESSED BREAST MILK","You give expressed milk from the fridge","HANDY","A warmer saves you a few minutes","You can warm milk to body temperature in a jug of warm water. A warmer does the same job, hands free. Never use a microwave: hot spots can burn.",TT,h=300)
s4=slide("3 · TRY IT FIRST","Your baby drinks milk cold","SKIP IT","Cold milk is fine if your baby is happy","Expressed milk can go straight from the fridge if your baby drinks it cold. Try a cold bottle before you buy anything.",None,dsc=("Cold","is OK too",92))
s5=slide("4 · EVERY BOTTLE","Warmer, jug or tap: check before you feed","WRIST TEST","Test a few drops on your wrist","It should feel warm or cool, but not hot. Check every bottle, however you warmed it.",None,src=NHS,dsc=("Warm","not hot",92))
s6=slide("5 · AFTER THE FEED","Can you keep it warm for later?","1 HOUR","Don’t keep milk warm for the next feed","Once your baby has drunk from a bottle of breast milk, use it within 1 hour, then throw the rest away. Throw away leftover formula after a feed too.",None,dsc=("1h","then throw away",110))
def pc(img,h,p,n): return f'<div style="flex:1;background:#fff;border-radius:34px;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;padding:26px 16px 22px"><img src="{img}" style="max-height:{h}px;max-width:90%;object-fit:contain;{SH}"><div class="h" style="font-size:44px;margin-top:14px">{p}</div><div style="font-size:20px;font-weight:600;opacity:.7;text-align:center;line-height:1.25;margin-top:4px">{n}</div></div>'
s7=deco+f'''<div style="position:absolute;left:50px;right:50px;top:90px;height:520px;display:flex;gap:20px">
{pc(TT,250,"£24.95","Tommee Tippee Electric<br>Bottle Warmer, White")}{pc(MV,280,"£67.99","babymoov Moov &amp; Feed<br>Bottle Warmer")}{pc(BZ,300,"£110.46","Baby Brezza Superfast<br>Portable Bottle Warmer, Black")}</div>
<div style="position:absolute;left:70px;right:70px;top:650px"><div class="kick">6 · BEFORE YOU BUY</div><div class="h" style="font-size:58px;margin-top:6px">From £24.95 to £110.46</div>
<div class="b" style="margin-top:14px;font-size:33px;line-height:1.4">✓ Fits your bottles, wide neck too<br>✓ Switches itself off when done<br>✓ Warms food pouches if weaning is close<br>✓ Battery models: only if you’re out a lot</div></div>
<div style="position:absolute;left:70px;right:70px;top:1185px;font-size:22px;font-weight:700;opacity:.75">Prices on BabySorted, {DATE}. Bottle warmers in our catalog.</div>'''
s8=hero_last(baby(7,1080,760,.5,.5),"Need one? Compare prices first","Compare bottle warmer prices from UK shops in one place.","#fff",fg=NAVY)
pin=pin_hero(baby(50,1000,660,.55,.45,1.1),pin_tags("Buying guide","Nursing &amp; Feeding"),"Bottle warmer: do you need one?",
 ["Formula: cool it, don’t warm it","Breast milk: a warm water jug works","Cold milk is fine if baby is happy","Never microwave breast milk","Wrist test: warm, not hot","Use within 1 hour of a feed"],
 BZ,240,PINK,NAVY,NAVY,"#fff","Source: NHS.","Compare bottle warmer prices at babysorted.com",line="#fff",photo_h=660,title_fs=56)
render(ROOT+"/out/a",[cover,s2,s3,s4,s5,s6,s7,s8],pin,CSS,NAVY)
