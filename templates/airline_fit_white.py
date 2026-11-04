# White "airline fit" layout: white bg, pink rounded panels, folded-size gauge bars against airline limits, tick matrix.
# Used for: Best compact strollers for travel and flights (Nov 2026).
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from slide_lib import *
LI=b("libelle.png"); AE=b("aer2.png"); NI=b("nia.png")
CSS=css("#fff",NAVY,PINK,NAVY)
deco=star(990,50,34,ROSE)+star(36,36,22,ROSE)
SH="filter:drop-shadow(0 18px 18px rgba(5,31,69,.18))"
im=lambda s,h,x="": f'<img src="{s}" style="height:{h}px;max-width:100%;object-fit:contain;{SH};{x}">'
cover=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="tags"><span class="tag t1">Buying guide</span><span class="tag t2">Pushchairs</span></div>
<div class="h" style="font-size:100px;margin-top:28px">Best compact strollers for travel and flights</div>
<div style="font-size:39px;font-weight:600;opacity:.7;margin-top:18px">“Cabin approved” isn't the whole story.</div></div>
<div style="position:absolute;left:60px;right:60px;top:600px;height:620px;background:{PINK};border-radius:44px;overflow:hidden">
<img src="{LI}" style="position:absolute;right:30px;top:30px;height:560px;{SH}"></div>
<div style="position:absolute;left:100px;top:660px;width:310px"><div class="h" style="font-size:54px">Will it fit your airline?</div><div style="font-size:32px;font-weight:600;margin-top:14px;line-height:1.3">3 strollers, 4 airlines, the real numbers.</div>
<div style="margin-top:26px;display:inline-block;background:{NAVY};color:#fff;font-weight:700;font-size:28px;padding:13px 24px;border-radius:40px;white-space:nowrap">Swipe before you buy</div></div>'''
PTS=[("It's not one rule","Each airline sets its own size, weight and fee. There's no single pass."),("Space can run out","Which? says cabin storage can depend on the room on the day."),("Numbers can be off","Which? found makers' sizes don't always match its lab measurements.")]
pts="".join(f'''<div style="background:{PINK};border-radius:32px;padding:34px 38px;margin-top:20px"><div class="h" style="font-size:50px">{a}</div><div class="b" style="margin-top:10px">{c}</div></div>''' for a,c in PTS)
s2=deco+f'''<div style="position:absolute;left:70px;right:70px;top:70px"><div class="kick">FIRST, THE CATCH</div><div class="h" style="font-size:86px;margin-top:8px">“Cabin approved” isn't a promise</div></div>
<div style="position:absolute;left:60px;right:60px;top:320px">{pts}</div>'''
AL=[("easyJet","56 × 45 × 25 cm","Book it as a large cabin bag. Overhead locker only."),("Ryanair","55 × 40 × 20 cm","10 kg max. It replaces the cabin bag you paid for."),("Jet2","Hand luggage size","Counts as your hand luggage. Space permitting."),("British Airways","Hand luggage size","In the hold, folds up to 117 × 38 × 38 cm can come back to the aircraft door.")]
al="".join(f'''<div style="padding:26px 0;border-top:{"0" if i==0 else "3px solid #fff"}"><div style="display:flex;justify-content:space-between;align-items:baseline;gap:20px"><div class="h" style="font-size:46px">{a}</div><div class="h" style="font-size:38px;white-space:nowrap">{c}</div></div><div style="font-size:33px;font-weight:500;line-height:1.3;margin-top:8px">{d}</div></div>''' for i,(a,c,d) in enumerate(AL))
s3=deco+f'''<div style="position:absolute;left:70px;right:70px;top:70px"><div class="kick">THE REAL LIMITS</div><div class="h" style="font-size:80px;margin-top:8px;white-space:nowrap">4 airlines, 4 rulebooks</div></div>
<div style="position:absolute;left:60px;right:60px;top:240px;background:{PINK};border-radius:40px;padding:14px 44px 18px">{al}</div>
<div style="position:absolute;left:70px;right:70px;top:1064px;font-size:28px;font-weight:600;opacity:.65;line-height:1.35">Rules checked 4 Nov 2026 (Ryanair from Which?, 25 Mar 2026). They change, so check yours before you fly.</div>'''

def pick(k,name,best,pic,h,folded,kg,start,price,good,watch):
    T=[("FOLDED",folded),("WEIGHT",kg),("FROM",start),("PRICE",price)]
    t="".join(f'<div style="background:#fff;border-radius:22px;padding:13px 20px"><div style="font-weight:800;font-size:20px;letter-spacing:.06em;opacity:.6">{a}</div><div class="h" style="font-size:35px;margin-top:4px;white-space:nowrap">{c}</div></div>' for a,c in T)
    return deco+f'''<div style="position:absolute;left:60px;right:60px;top:60px;height:640px;background:{PINK};border-radius:44px;display:flex;align-items:center;padding:30px 30px;gap:20px">
<div style="flex:1;display:flex;justify-content:center;align-items:center;height:100%">{im(pic,h)}</div><div style="flex:none;width:340px;display:flex;flex-direction:column;gap:12px">{t}</div></div>
<div style="position:absolute;left:90px;top:86px;font-weight:800;font-size:26px;background:{NAVY};color:#fff;padding:7px 16px;border-radius:18px">{k} of 3</div>
<div style="position:absolute;left:70px;right:70px;top:726px"><div class="h" style="font-size:74px">{name}</div>
<div style="margin-top:14px"><span class="pill" style="background:{NAVY};color:#fff">{best}</span></div>
<div class="b" style="margin-top:22px">{good}</div><div class="b" style="margin-top:12px"><b style="font-weight:800">Watch out:</b> {watch}</div></div>'''
s4=pick(1,"Cybex Libelle","Best for budget airlines",LI,560,"48 × 32 × 20 cm","About 6 kg","6 months","£219","The smallest fold here, and the only one of the three within Ryanair's 20 cm depth.","it's not for newborns. Its depth is right on Ryanair's limit, with no room to spare.")
s5=pick(2,"Joolz Aer2","Best for one-hand parents",AE,540,"53 × 44 × 23.5 cm","6.5 kg","Birth","£439","Fold, steer and recline it with one hand. It has a shoulder strap and a lie-flat seat.","44 cm wide and 23.5 cm deep, so over Ryanair's limit.")
s6=pick(3,"Silver Cross Nia","Best from birth",NI,540,"54 × 45 × 23 cm","7.3 kg","Birth","£395","Lie-flat seat, one-hand fold and an 8 kg basket. Adaptors for the Glide Plus 360 car seat are included.","45 cm wide sits right on easyJet's limit, so check before you book.")
Y='<div style="width:62px;height:62px;border-radius:50%;background:'+NAVY+';color:#fff;font-weight:800;font-size:34px;display:flex;align-items:center;justify-content:center;margin:0 auto">✓</div>'
N=f'<div style="width:62px;height:62px;border-radius:50%;background:#fff;box-shadow:inset 0 0 0 3px {ROSE};color:{NAVY};font-weight:800;font-size:32px;display:flex;align-items:center;justify-content:center;margin:0 auto">×</div>'
MX=[("Cybex Libelle","48 × 32 × 20",Y,Y),("Joolz Aer2","53 × 44 × 23.5",Y,N),("Silver Cross Nia","54 × 45 × 23",Y,N)]
mx="".join(f'''<div style="display:flex;align-items:center;padding:30px 0;border-top:3px solid #fff"><div style="flex:1"><div class="h" style="font-size:44px">{a}</div><div style="font-size:30px;font-weight:600;opacity:.65;margin-top:4px">{c} cm</div></div><div style="width:170px">{d}</div><div style="width:170px">{e}</div></div>''' for a,c,d,e in MX)
s7=deco+f'''<div style="position:absolute;left:70px;right:70px;top:70px"><div class="kick">THE QUICK CHECK</div><div class="h" style="font-size:84px;margin-top:8px">Which one fits which limit?</div></div>
<div style="position:absolute;left:60px;right:60px;top:340px;background:{PINK};border-radius:40px;padding:22px 44px 18px"><div style="display:flex;padding-bottom:18px"><div style="flex:1"></div><div class="h" style="width:170px;text-align:center;font-size:33px">easyJet<div style="font-size:23px;font-weight:600;opacity:.65;margin-top:4px;letter-spacing:0">56×45×25</div></div><div class="h" style="width:170px;text-align:center;font-size:33px">Ryanair<div style="font-size:23px;font-weight:600;opacity:.65;margin-top:4px;letter-spacing:0">55×40×20</div></div></div>{mx}</div>
<div style="position:absolute;left:70px;right:70px;top:960px"><div class="b">Most airlines take a stroller in the hold for free, so a “no” here isn't a problem unless you want it on board.</div><div style="font-size:27px;font-weight:600;opacity:.65;margin-top:14px;line-height:1.35">Based on published folded sizes, not airline approval. Staff have the final say.</div></div>'''
TP=[("Bag drop or gate?","You can usually leave it at bag drop, or keep it to the gate if it's tagged at check-in."),("Plan for the carousel","Ask where you'll get it back. It may be baggage reclaim, not the aircraft door."),("Lift baby out for security","easyJet says your child must come out of the pushchair to go through security."),("Count your free items","easyJet, Jet2 and BA allow two free baby items per child. Check yours.")]
tp="".join(f'''<div style="padding:26px 0;border-top:{"0" if i==0 else f"3px solid #fff"}"><div class="h" style="font-size:45px">{a}</div><div style="font-size:35px;font-weight:500;line-height:1.3;margin-top:8px">{c}</div></div>''' for i,(a,c) in enumerate(TP))
s8=deco+f'''<div style="position:absolute;left:70px;right:70px;top:70px"><div class="kick">ON THE DAY</div><div class="h" style="font-size:84px;margin-top:8px">At the airport</div></div>
<div style="position:absolute;left:60px;right:60px;top:240px;background:{PINK};border-radius:40px;padding:14px 44px 22px">{tp}</div>'''
s9=deco+f'''<div style="position:absolute;left:60px;right:60px;top:60px;height:560px;background:{PINK};border-radius:44px;display:flex;align-items:center;justify-content:center;gap:0;padding:30px">{im(LI,400,"flex:none")}{im(AE,400,"flex:none;margin-left:-6px")}{im(NI,380,"flex:none;margin-left:-14px")}</div>
<div style="position:absolute;left:70px;right:70px;top:660px"><div class="h" style="font-size:80px">Ready to book? Compare prices first</div>
<div class="b" style="margin-top:18px;font-size:38px">Compare stroller prices from UK shops in one place.</div>
<div style="margin-top:30px;display:flex;align-items:center;gap:16px"><div class="h" style="font-size:46px;background:{PINK};padding:22px 32px;border-radius:24px">babysorted.com/links</div>
<div style="background:{NAVY};color:#fff;font-weight:800;font-size:32px;padding:22px 26px;border-radius:24px;white-space:nowrap">Link in bio ↑</div></div>
<div style="margin-top:22px;font-size:32px;font-weight:700;opacity:.55">Save this post for later</div></div>'''
PN=[(LI,"Cybex Libelle","Best for budget airlines","48 × 32 × 20 cm","£219"),(AE,"Joolz Aer2","Best for one-hand parents","53 × 44 × 23.5 cm","£439"),(NI,"Silver Cross Nia","Best from birth","54 × 45 × 23 cm","£395")]
pn="".join(f'''<div style="display:flex;align-items:center;gap:20px;background:{PINK};border-radius:28px;padding:14px 28px 14px 18px;margin-top:14px"><div style="flex:none;width:150px;height:170px;background:#fff;border-radius:20px;display:flex;align-items:center;justify-content:center"><img src="{s}" style="max-width:130px;max-height:150px"></div><div style="flex:1"><div class="h" style="font-size:42px">{a}</div><div style="font-size:27px;font-weight:600;opacity:.75;margin-top:4px">{c}</div><div style="font-size:27px;font-weight:600;opacity:.75;margin-top:2px">Folded {d}</div></div><div class="h" style="font-size:42px">{e}</div></div>''' for s,a,c,d,e in PN)
pin=f'''{star(910,50,32,ROSE)}<div style="position:absolute;left:60px;right:60px;top:60px"><div class="tags"><span class="tag t1" style="font-size:24px">Buying guide</span><span class="tag t2" style="font-size:24px">Pushchairs</span></div>
<div class="h" style="font-size:78px;margin-top:20px">Best compact strollers for travel and flights</div>
<div style="font-size:31px;font-weight:600;opacity:.75;margin-top:12px">“Cabin approved” isn't a promise. Check these limits.</div></div>
<div style="position:absolute;left:60px;right:60px;top:372px">{pn}</div>
<div style="position:absolute;left:60px;right:60px;top:1046px;background:{NAVY};color:#fff;border-radius:26px;padding:24px 30px"><div style="font-weight:800;font-size:22px;opacity:.7;letter-spacing:.06em">CABIN LIMITS</div><div style="font-size:30px;font-weight:600;margin-top:8px;line-height:1.36">easyJet: 56 × 45 × 25 cm, book as a large cabin bag.<br>Ryanair: 55 × 40 × 20 cm, 10 kg, swaps your cabin bag.<br>Jet2: hand luggage size, space permitting.<br>Check your airline before you fly.</div></div>
<div style="position:absolute;left:60px;right:60px;bottom:40px;display:flex;justify-content:space-between;align-items:center"><div class="brand" style="font-size:34px">BabySorted</div><div style="font-weight:700;font-size:25px">Compare stroller prices at babysorted.com</div></div>'''
render(ROOT+"/out/p3",[cover,s2,s3,s4,s5,s6,s7,s8,s9],pin,CSS,NAVY)
