# Mint "price gap" layout for Deals posts: the same product at two UK shops on BabySorted, cheapest vs dearest, with the gap as a navy badge.
# Used for: 11.11 deals (11 Nov 2026). All prices read from the BabySorted catalog on the morning of 11 Nov 2026.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css(MINT,NAVY,NAVY,"#fff")+".t2{background:#fff;box-shadow:none}"
deco=star(36,30,26,"#fff")+star(1000,40,30,"#fff")
DATE="11 Nov 2026"
D=[("egg3","Pushchairs","egg 3 Stroller, Carbonite",703.20,"Winstanleys Pramworld",879.00,"Samuel Johnston",520),
   ("metro3","Pushchairs","Ergobaby Metro 3 Compact Stroller, Natural Beige",219.90,"Winstanleys Pramworld",369.90,"Natural Baby Shower",500),
   ("snoozi","Kids Furniture","Stokke Snoozi Bassinet, Graphite Grey",144.95,"Winstanleys Pramworld",290.00,"Natural Baby Shower",380),
   ("michair","High Chairs","iCandy MiChair, White",169.00,"Winstanleys Pramworld",260.00,"iCandy World",500),
   ("oneair","Baby Carriers","BabyBjorn One Air Carrier, Anthracite",109.95,"Winstanleys Pramworld (with a free bib)",151.12,"Natural Baby Shower",460),
   ("pebble2","Car Seats","Maxi-Cosi Pebble 360 Pro 2, Twillic Black",179.00,"Natural Baby Shower",219.95,"Winstanleys Pramworld",420)]
IM={k:b(k+".png",900) for k,*_ in D}
TOTAL=sum(hi-lo for _,_,_,lo,_,hi,_,_ in D)
gbp=lambda v: f"£{v:,.2f}"
def deal(i,k,cat,name,lo,ls,hi,hs,h):
    gap=hi-lo
    return deco+f'''<div style="position:absolute;left:60px;right:60px;top:60px;height:560px;background:#fff;border-radius:44px;display:flex;align-items:center;justify-content:center;overflow:hidden"><img src="{IM[k]}" style="height:{h}px;max-width:80%;object-fit:contain;{SH}"></div>
<div style="position:absolute;left:90px;top:90px"><span class="pill" style="background:{MINT};font-size:26px">Deal {i} of 6 · {cat}</span></div>
<div style="position:absolute;right:80px;top:84px;width:230px;height:230px;border-radius:50%;background:{NAVY};color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-6deg)"><div style="font-weight:800;font-size:26px;letter-spacing:.06em">SAVE</div><div class="h" style="font-size:44px">{gbp(gap)}</div></div>
<div style="position:absolute;left:70px;right:70px;top:650px"><div class="h" style="font-size:54px">{name}</div>
<div style="margin-top:22px;background:#fff;border-radius:28px;padding:20px 26px;display:flex;align-items:center;gap:20px"><div style="flex:none;width:52px;height:52px;border-radius:16px;background:{NAVY};color:#fff;font-weight:800;font-size:30px;display:flex;align-items:center;justify-content:center">✓</div><div><div style="font-weight:800;font-size:22px;letter-spacing:.05em;opacity:.6">LOWEST WE FOUND TODAY</div><div class="h" style="font-size:44px;margin-top:2px">{gbp(lo)} <span style="font-size:28px;font-weight:600">at {ls}</span></div></div></div>
<div style="margin-top:14px;border:3px solid #fff;border-radius:28px;padding:16px 26px 16px 98px"><div style="font-weight:800;font-size:22px;letter-spacing:.05em;opacity:.6">SAME ITEM, ANOTHER SHOP</div><div class="h" style="font-size:38px;margin-top:2px;opacity:.75">{gbp(hi)} <span style="font-size:27px;font-weight:600">at {hs}</span></div></div></div>
<div style="position:absolute;left:70px;right:70px;top:1215px;font-size:24px;font-weight:700;opacity:.6">Prices on BabySorted, {DATE}. Prices can change during the day.</div>'''
cover=hero_cover(baby(11,1080,800,.5,.36),'<div class="tags"><span class="tag t1">Deals</span><span class="tag t2" style="box-shadow:inset 0 0 0 3px #051F45">All categories</span></div>',"11.11 deals: same product, less money","6 price gaps between UK shops we found today.",f'<img src="{IM["egg3"]}" style="height:330px;{SH}">',1,card=MINT,title_fs=70)+star(1000,40,30,"#fff")
s2=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="kick">WHY COMPARE</div><div class="h" style="font-size:80px;margin-top:8px">Same item. Same colour. Different price.</div></div>
<div style="position:absolute;left:60px;right:60px;top:420px;height:420px;background:#fff;border-radius:44px;display:flex;flex-direction:column;align-items:center;justify-content:center"><div style="font-weight:800;font-size:32px;opacity:.6">you'd save on these 6</div><div class="h" style="font-size:170px;line-height:1.05">{gbp(TOTAL)}</div><div style="font-weight:700;font-size:30px;opacity:.7">by picking the cheaper shop</div></div>
<div class="b" style="position:absolute;left:70px;right:70px;top:880px;font-size:40px">We checked prices across UK shops on BabySorted this morning. These are the biggest gaps on the same product, in the same colour.</div>
<div style="position:absolute;left:70px;right:70px;top:1180px;font-size:24px;font-weight:700;opacity:.6">Prices on BabySorted, {DATE}.</div>'''
deals=[deal(i+1,*d) for i,d in enumerate(D)]
T=[("Check the exact version","“Plus”, “Pro” or “2” in a name can be a different product."),("Check what's in the box","A carrycot, base or rain cover can be extra."),("Check delivery and returns","A cheaper price can cost more to send back."),("Check again before you pay","Prices on baby gear can change from day to day.")]
tt="".join(f'''<div style="padding:26px 0;border-top:{"0" if i==0 else f"3px solid {MINT}"}"><div class="h" style="font-size:46px">{a}</div><div style="font-size:33px;font-weight:500;line-height:1.3;margin-top:8px">{c}</div></div>''' for i,(a,c) in enumerate(T))
s9=deco+f'''<div style="position:absolute;left:70px;right:70px;top:70px"><div class="kick">BEFORE YOU BUY</div><div class="h" style="font-size:80px;margin-top:8px">4 checks so a deal stays a deal</div></div>
<div style="position:absolute;left:60px;right:60px;top:330px;background:#fff;border-radius:40px;padding:14px 44px 18px">{tt}</div>'''
s10=hero_last(baby(13,1080,760,.5,.42),"Compare prices before you buy","See every UK shop's price for the same product in one place.","#fff")
SN=["egg 3 Stroller","Ergobaby Metro 3","Stokke Snoozi Bassinet","iCandy MiChair","BabyBjorn One Air","Maxi-Cosi Pebble 360 Pro 2"]
items=[f'{n}<span style="float:right;font-size:32px">save {gbp(d[5]-d[3])}</span>' for n,d in zip(SN,D)]
pin=pin_hero(baby(7,1000,700,.36,.5),pin_tags("Deals","All categories"),"11.11 baby gear deals: same product, less money",items,None,0,MINT,NAVY,NAVY,"#fff",f"Lowest vs highest price for the same item at UK shops. Prices on BabySorted, {DATE}. Prices can change.","Compare baby gear prices at babysorted.com",line="#fff",title_fs=56,photo_h=640)
print("TOTAL",TOTAL)
render(ROOT+"/out/deals",[cover,s2]+deals+[s9,s10],pin,CSS,NAVY)
