# Pink "weight ruler" layout (27 Nov 2026): pink bg, product in the free space at the top, a white 0-36 kg ruler with the
# group's range in navy, navy text below. Used for: #62 Group 0+, 1, 2, 3: the old names explained. No prices.
# Facts: GOV.UK "Child car seats: the law" (weight-based seats carry an 'ECE R44' label; group table 0: 0-10 kg, 0+: 0-13 kg
# rear-facing, 1: 9-18 kg rear- or forward-facing with harness or shield, 2: 15-25 kg and 3: 22-36 kg high-backed booster or
# booster cushion; height-based seats carry 'R129' and must be rear facing until over 15 months; only group 3 booster
# cushions can now be made; car seat until 12 years or 135 cm). RoSPA childcarseats.org.uk (new booster cushion models not for
# children under 125 cm or 22 kg; seats approved for weight, not age).
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css(PINK,NAVY,NAVY,"#fff")+".t2{background:#fff;box-shadow:none}"
GOV="Source: GOV.UK"; ROS="Source: RoSPA, the UK accident prevention charity"
PI=b("pipa.png",800); SP=b("spin.png",700); EL=b("elevate.png",700); TG=b("travelgo.png",800)
def ruler(segs):
    bars="".join(f'<div style="position:absolute;left:{a/36*100}%;width:{(z-a)/36*100}%;top:{8+k*0}px;height:44px;background:{NAVY};opacity:{1 if k==0 else .45};border-radius:22px"></div>' for k,(a,z) in enumerate(segs))
    ticks="".join(f'<div style="position:absolute;left:{v/36*100}%;top:58px;transform:translateX(-50%);font-weight:800;font-size:24px">{v}</div>' for v in (0,9,13,18,25,36))
    return f'''<div style="background:#fff;border-radius:30px;padding:22px 34px 18px"><div style="display:flex;justify-content:space-between;font-weight:800;font-size:22px;letter-spacing:.06em;opacity:.6"><span>CHILD’S WEIGHT</span><span>KG</span></div>
<div style="position:relative;height:96px;margin-top:10px"><div style="position:absolute;left:0;right:0;top:20px;height:20px;background:{PINK};border-radius:10px"></div>{bars}{ticks}</div></div>'''
def slide(inner,ruler_html,title,body,src=GOV):
    s=f'<div style="position:absolute;left:70px;right:70px;top:1190px;font-size:23px;font-weight:700;opacity:.75">{src}</div>' if src else ""
    r=f'<div style="position:absolute;left:60px;right:60px;top:520px">{ruler_html}</div>' if ruler_html else ""
    return f'<div style="position:absolute;left:0;right:0;top:40px;height:470px;display:flex;align-items:center;justify-content:center;gap:40px">{inner}</div>'+r+f'''
<div style="position:absolute;left:70px;right:70px;top:{720 if ruler_html else 600}px"><div class="h" style="font-size:64px">{title}</div>
<div class="b" style="margin-top:14px;font-size:37px">{body}</div></div>{s}'''
pimg=lambda s,h: f'<img src="{s}" style="height:{h}px;object-fit:contain;{SH}">'
word=lambda a,c,fs=150: f'<div style="text-align:center"><div class="h" style="font-size:{fs}px">{a}</div><div style="font-weight:700;font-size:34px;opacity:.7;margin-top:6px">{c}</div></div>'
cover=hero_cover(baby(14,1080,800,.62,.4,1.25),'<div class="tags"><span class="tag t1">Tips</span><span class="tag t2">Car Seats</span></div>',
 "Group 0+, 1, 2, 3: what they mean","Still on the box. Here’s how to read it.",f'<img src="{EL}" style="height:400px;{SH}">',1,card=PINK,title_fs=70,pill="Swipe for the decoder")
s2=slide(word("R44","= weight groups",170),None,"Group numbers mean weight","They come from weight-based seats with an ‘ECE R44’ label. Newer height-based seats carry an ‘R129’ label and use cm instead. Both are approved in the UK.")
s3=slide(pimg(PI,440),ruler([(0,13)]),"Group 0+: 0–13 kg","A rear-facing baby carrier or baby seat with a harness. (Plain Group 0 stops at 10 kg.)")
s4=slide(pimg(SP,460),ruler([(9,18)]),"Group 1: 9–18 kg","A harnessed seat, rear- or forward-facing. The ranges overlap, so a 10 kg baby can fit both groups: check each seat’s own limits.")
s5=slide(pimg(TG,330),ruler([(15,25),(22,36)]),"Group 2: 15–25 kg · Group 3: 22–36 kg","High-back boosters or booster cushions, usually with the adult seat belt.")
s6=slide(pimg(EL,450),ruler([(9,36)]),"‘Group 1/2/3’ = one seat, stages","Combined seats change as your child grows, often a harness first, then the adult belt. The manual says when to switch.",src="")
s7=slide(word("125 cm","and 22 kg+ for new booster cushions",140),None,"Booster cushions have moved up","New booster cushion models aren’t approved for children under 125 cm or 22 kg. Seats are approved for weight, not age.",ROS)
s8=slide(word("cm","on R129 seats",200),None,"R129 seats: read the cm","Height-based seats list a height range. They must stay rear-facing until your child is over 15 months old.")
s9=slide(word("12 or<br>135 cm","whichever comes first",130),None,"How long the law needs a seat","Children must normally use a child car seat until they’re 12 years old or 135 cm tall, whichever comes first.")
s10=hero_last(baby(51,1080,760,.45,.4,1.0),"Know your group, then compare","Compare car seat prices from UK shops in one place.","#fff")
pin=pin_hero(baby(11,1000,660,.5,.3,1.0),pin_tags("Tips","Car Seats"),"Car seat groups decoded",
 ["Group 0+: 0–13 kg, rear-facing","Group 1: 9–18 kg, harness","Group 2: 15–25 kg, booster","Group 3: 22–36 kg, booster","New cushions: 125 cm & 22 kg+","R129 seats use cm, not kg"],
 SP,330,PINK,NAVY,NAVY,"#fff","Sources: GOV.UK; RoSPA, the UK accident prevention charity.","Compare car seat prices at babysorted.com",line="#fff",photo_h=660,title_fs=58)
render(ROOT+"/out/e",[cover,s2,s3,s4,s5,s6,s7,s8,s9,s10],pin,CSS,NAVY)
