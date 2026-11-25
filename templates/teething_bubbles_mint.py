# Mint "big bubble" layout for Parenting Tips (25 Nov 2026): mint bg, one large white circle on the top half holding
# a short keyword or a teether, a navy number badge on the circle, navy text below.
# Used for: Parenting Tips #75 Teething: what helps. No prices (not a buying post).
# Facts: NHS "Tips for helping your teething baby" (fridge not freezer, never tie a ring round the neck, 6 months+ raw fruit and veg,
# watch for choking, rusks contain sugar, gels only from pharmacies and little evidence, homeopathic not recommended, brush from
# first tooth with fluoride toothpaste, register with a dentist); NHS 111 Wales "Teething" (timing and order of teeth, tiny smear
# under 3, no evidence teething causes fever or diarrhoea, ask GP or 111 if worried).
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css(MINT,NAVY,NAVY,"#fff")+".t2{background:#fff;box-shadow:none}"
NHS="Source: NHS"
CH=b("chomp.png",900); ML=b("mlion.png",700); TX=b("trixie.png",700)
def bubble(inner,n):
    return f'''<div style="position:absolute;left:290px;top:70px;width:500px;height:500px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center;text-align:center">{inner}</div>
<div class="h" style="position:absolute;left:250px;top:90px;width:110px;height:110px;border-radius:50%;background:{NAVY};color:#fff;font-size:56px;display:flex;align-items:center;justify-content:center">{n}</div>'''
def slide(n,inner,title,body,src=NHS):
    s=f'<div style="position:absolute;left:70px;right:70px;top:1185px;font-size:23px;font-weight:700;opacity:.75">{src}</div>' if src else ""
    return bubble(inner,n)+f'''<div style="position:absolute;left:70px;right:70px;top:630px"><div class="h" style="font-size:62px">{title}</div><div class="b" style="margin-top:16px;font-size:35px">{body}</div></div>{s}'''
word=lambda a,c,fs=110: f'<div><div class="h" style="font-size:{fs}px;line-height:.95">{a}</div><div style="font-weight:700;font-size:30px;margin-top:12px;opacity:.7">{c}</div></div>'
img=lambda s,h: f'<img src="{s}" style="max-height:{h}px;max-width:330px;object-fit:contain;{SH}">'
cover=hero_cover(baby(5,1080,800,.42,.5,1.15),'<div class="tags"><span class="tag t1">Parenting Tips</span><span class="tag t2">Nursing &amp; Feeding</span></div>',"Teething: what really helps","Sore gums, grumpy days. Small things that help.",f'<img src="{CH}" style="width:270px;{SH}">',1,card=MINT,fg=NAVY,title_fs=74,pill="Swipe for 7 tips")
s2=slide(1,word("5–7","months: usually the<br>first tooth, bottom front",120),"The first tooth can come any time in year one","Some babies start before 4 months, some after 12. Most have all their milk teeth by about two and a half.")
s3=slide(2,img(TX,300),"Chill in the fridge, never the freezer","Some teething rings can be cooled in the fridge first. A frozen ring can hurt your baby’s gums. The ring’s instructions say how long to chill it.")
s4=slide(3,img(ML,330),"Never tie a teether round the neck","A teething ring tied around your baby’s neck can be a choking hazard. Keep it in their hands instead.")
s5=slide(4,word("6m+","something real to chew",120),"From 6 months: let them chew","Raw fruit or veg, like a piece of apple or carrot, can help. Always stay close in case they choke, and skip rusks: nearly all contain sugar.")
s6=slide(5,word("Ask","a pharmacist first",130),"Gels and medicines: ask before you buy","Teething gels are only sold in pharmacies and there’s little proof they work. Speak to a pharmacist or GP before giving any gel or medicine.")
s7=slide(6,word("1st","tooth = first brush",130),"Start brushing from the first tooth","Use a baby toothbrush with a tiny smear of fluoride toothpaste, and register your baby with a dentist once teeth come through.")
s8=slide(7,word("Not<br>teething?","fever or upset tummy",86),"Fever or diarrhoea isn’t ‘just teeth’","There’s no evidence teething causes them. If you’re worried, call your GP or NHS 111 (free from landlines and mobiles in England, Scotland and Wales).")
s9=hero_last(baby(37,1080,760,.5,.45),"Gentle help for sore gums","Compare teether prices from UK shops in one place.","#fff",fg=NAVY)
pin=pin_hero(baby(1,1000,660,.45,.4,1.0),pin_tags("Parenting Tips","Nursing &amp; Feeding"),"Teething: 6 things that help",
 ["Chill rings in the fridge, not freezer","Never tie a ring round the neck","6m+: apple or carrot, stay close","Skip rusks: most contain sugar","Gel or medicine? Ask a pharmacist","First tooth: start brushing"],
 TX,220,MINT,NAVY,NAVY,"#fff","Source: NHS.","Compare teether prices at babysorted.com",line="#fff",photo_h=660,title_fs=56)
render(ROOT+"/out/c",[cover,s2,s3,s4,s5,s6,s7,s8,s9],pin,CSS,NAVY)
