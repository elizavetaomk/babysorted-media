# White "split column" layout (23 Nov 2026): white bg, two columns (footmuff on mint, blanket on pink) at the top;
# the side a slide is about stays bright, the other fades. Title + body below. Photo-led cover and last slide.
# Used for: #51 Footmuff vs pram blanket. Facts: NHS (Best Start in Life), The Lullaby Trust.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css("#fff",NAVY,NAVY,"#fff")+f".t2{{background:{MINT};box-shadow:none}}"
MU=b("muff.png",700); BL=b("blanket.png",800); DATE="20 Nov 2026"
NHS="Source: NHS"; LT="Source: The Lullaby Trust, the UK safer baby sleep charity"
def split(focus,lt="",rt=""):
    ol=1 if focus in ("L","B") else .35; orr=1 if focus in ("R","B") else .35
    return f'''<div style="position:absolute;left:60px;right:60px;top:70px;height:500px;display:flex;gap:20px">
<div style="flex:1;background:{MINT};border-radius:40px;opacity:{ol};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px"><img src="{MU}" style="height:330px;{SH}"><div class="h" style="font-size:38px">Footmuff</div><div style="font-weight:700;font-size:26px">{lt}</div></div>
<div style="flex:1;background:{PINK};border-radius:40px;opacity:{orr};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px"><img src="{BL}" style="height:300px;{SH}"><div class="h" style="font-size:38px">Blanket</div><div style="font-weight:700;font-size:26px">{rt}</div></div></div>'''
def sl(kick,title,body,top,src=None):
    s=f'<div style="position:absolute;left:70px;right:70px;top:1110px;font-size:23px;font-weight:700;opacity:.65">{src}</div>' if src else ""
    return top+f'''<div style="position:absolute;left:70px;right:70px;top:610px"><div class="kick">{kick}</div><div class="h" style="font-size:64px;margin-top:6px">{title}</div><div class="b" style="margin-top:14px;font-size:36px">{body}</div></div>{s}'''
def banner(a,c,bg=ROSE): return f'<div style="position:absolute;left:60px;right:60px;top:70px;height:500px;background:{bg};border-radius:40px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center"><div class="h" style="font-size:130px;line-height:1">{a}</div><div class="h" style="font-size:40px;margin-top:16px">{c}</div></div>'
cover=hero_cover(baby(40,1080,800,.5,.35,1.0),'<div class="tags"><span class="tag t1">Comparison</span><span class="tag t2">Pushchairs</span></div>',"Footmuff or pram blanket?","One stays put. One slips off. Here's when each wins.",f'<div style="display:flex;align-items:flex-end;gap:6px"><img src="{MU}" style="height:270px;{SH}"><img src="{BL}" style="height:190px;{SH}"></div>',1,card="#fff",fg=NAVY,pill_bg=NAVY,pill_fg="#fff",title_fs=72)
s2=sl("THE SHORT ANSWER","Both work. They do different jobs","A footmuff zips around your baby and stays put on long walks. A cellular blanket is cheap, light and easy to add or take off as the day changes.",split("B","stays put","easy to adjust"))
s3=sl("RULE 1","Never cover the pram","Don't drape a blanket or muslin over the pram, even to keep the cold out. Your baby can overheat under it.",banner("Never","a blanket over the pram"),NHS+".")
s4=sl("BLANKETS","Cellular, tucked, shoulder height","Pick lightweight cellular blankets, not thick fleecy or padded ones. Tuck them in firmly and no higher than your baby's shoulders.",split("R","","cellular, tucked in"),"Sources: NHS; The Lullaby Trust, the UK safer baby sleep charity.")
s5=sl("FOOTMUFFS","Harness through, not over","Footmuff makers say: thread the harness through the footmuff's slots, so the straps sit snug on your baby, not on top of the padding.",split("L","harness through the slots",""))
s6=sl("CHECK","Feel the chest, not the hands","Cold hands and feet are normal. Check the chest or the back of the neck. Sweaty or clammy means too hot: take a layer off.",banner("Chest","or back of the neck",MINT),"Sources: The Lullaby Trust, the UK safer baby sleep charity; NHS.")
s7=sl("INDOORS","Hats and layers off inside","Take hats and extra layers off as soon as you're indoors or in a warm car. In the café, unzip the footmuff or fold it back.",banner("Off","as soon as you're inside"),NHS+".")
s8=sl("VERDICT","Which one for you?","Daily winter walks or a baby who kicks blankets off: a footmuff. Newborn in the carrycot, or mild days: a cellular blanket. You can also use both.",split("B","winter walks","mild days, layers"))
pp=f'''<div style="position:absolute;left:60px;right:60px;top:70px;height:500px;display:flex;gap:20px">
<div style="flex:1;background:{MINT};border-radius:40px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center"><img src="{MU}" style="height:300px;{SH}"><div class="h" style="font-size:52px;margin-top:10px">£59.95</div><div style="font-size:21px;font-weight:600;opacity:.75">Mamas &amp; Papas Flip XT<br>Footmuff, Juniper</div></div>
<div style="flex:1;background:{PINK};border-radius:40px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center"><img src="{BL}" style="height:280px;{SH}"><div class="h" style="font-size:52px;margin-top:10px">£11.25</div><div style="font-size:21px;font-weight:600;opacity:.75">Mamas &amp; Papas Cellular<br>Blanket, Sage</div></div></div>'''
s9=sl("PRICES","What they cost today","A blanket is the cheap start. A footmuff costs more but stays put on every walk. Check it fits your seat before you buy.",pp,f"Prices on BabySorted, {DATE}.")
s10=hero_last(baby(39,1080,700,.5,.4,1.05),"Winter walks? Compare prices first","Compare footmuff and blanket prices from UK shops in one place.",MINT,fg=NAVY,photo_h=700)
pin=pin_hero(baby(37,1000,680,.5,.4),pin_tags("Comparison","Pushchairs"),"Footmuff or pram blanket?",
 ["Never cover the pram","Cellular blankets, not fleecy","Tuck in, no higher than shoulders","Harness through the footmuff","Feel the chest, not the hands","Layers off indoors"],
 MU,330,"#fff",NAVY,NAVY,"#fff","Sources: NHS; The Lullaby Trust, the UK safer baby sleep charity.","Compare footmuff prices at babysorted.com",line=MINT,photo_h=680,title_fs=56)
render(ROOT+"/out/f",[cover,s2,s3,s4,s5,s6,s7,s8,s9,s10],pin,CSS,NAVY)
