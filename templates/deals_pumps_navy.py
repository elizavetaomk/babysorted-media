# Navy "coupon" Deals style (per CLAUDE.md) for the breast pump deals post (15 Nov 2026).
# Same product and colour compared across BabySorted shops; the dearer shop's price struck through.
# Prices read from the BabySorted catalog on 13 Nov 2026.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
EVENT="PUMP DEALS"; DATE="13 Nov 2026"
CSS=css(NAVY,"#fff",ROSE,NAVY)+".t2{box-shadow:inset 0 0 0 3px #fff}"
# (key, label, name, lowPrice, lowShop, highPrice, highShop, productHeight)
D=[("m9d","Wearable double","Momcozy M9 Double, pink",215.99,"JoyBuy UK",269.99,"Natural Baby Shower",470),
   ("fmini","Wearable double","Medela Freestyle Mini Hands-Free Double",126.99,"Medela UK",159.00,"JoyBuy UK",430),
   ("elvied","Wearable double","Elvie Double",369.00,"Natural Baby Shower",399.20,"Samuel Johnston",470),
   ("m5d","Wearable double","Momcozy M5 Double, grey",132.00,"Mamas & Papas",154.99,"Samuel Johnston",460),
   ("m9s","Wearable single","Momcozy M9 Single, pink and white",111.99,"Mamas & Papas",134.99,"Samuel Johnston",470),
   ("elvies","Wearable single","Elvie Single",199.00,"Mamas & Papas",218.99,"Samuel Johnston",470)]
IM={k:b(k+".png",900) for k,*_ in D}
gbp=lambda v:f"£{v:,.2f}"
import math
def burst(x,y,s,top,big,fs=48,rot=-10):
    pts=[]
    for i in range(32):
        r=50 if i%2==0 else 42;a=math.pi*2*i/32;pts.append(f"{50+r*math.cos(a):.1f},{50+r*math.sin(a):.1f}")
    return f'''<div style="position:absolute;left:{x}px;top:{y}px;width:{s}px;height:{s}px;transform:rotate({rot}deg);z-index:3"><svg width="{s}" height="{s}" viewBox="0 0 100 100" style="position:absolute;inset:0;filter:drop-shadow(0 10px 14px rgba(0,0,0,.25))"><polygon points="{' '.join(pts)}" fill="{ROSE}"/></svg>
<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;color:{NAVY}"><div style="font-weight:800;font-size:{int(fs*.5)}px;letter-spacing:.08em">{top}</div><div class="h" style="font-size:{fs}px">{big}</div></div></div>'''
def ribbon(text=EVENT,x=-60,y=58,w=420):
    return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;background:{ROSE};color:{NAVY};text-align:center;font-weight:900;font-size:30px;letter-spacing:.12em;padding:12px 0;transform:rotate(-8deg);z-index:4;box-shadow:0 8px 14px rgba(0,0,0,.25)">{text}</div>'
def coupon(x,y,w,h,split,top,bot,nb=NAVY):
    return f'''<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:#fff;border-radius:34px;color:{NAVY};overflow:hidden">
<div style="position:absolute;left:0;right:0;top:0;height:{split}px">{top}</div>
<div style="position:absolute;left:44px;right:44px;top:{split}px;border-top:5px dashed {NAVY};opacity:.25"></div>
<div style="position:absolute;left:0;right:0;top:{split}px;bottom:0">{bot}</div>
<div style="position:absolute;left:-30px;top:{split-30}px;width:60px;height:60px;border-radius:50%;background:{nb}"></div>
<div style="position:absolute;right:-30px;top:{split-30}px;width:60px;height:60px;border-radius:50%;background:{nb}"></div></div>'''
fn=lambda t:f'<div style="position:absolute;left:70px;right:70px;top:1200px;font-size:23px;font-weight:600;color:{ROSE}">{t}</div>'
def deal(i,k,cat,name,lo,ls,hi,hs,h):
    top=f'''<div style="position:absolute;left:40px;top:34px;font-weight:800;font-size:24px;letter-spacing:.06em;opacity:.6">DEAL {i} OF 6 · {cat.upper()}</div>
<div style="position:absolute;inset:60px 0 20px;display:flex;align-items:center;justify-content:center"><img src="{IM[k]}" style="height:{h}px;max-width:70%;object-fit:contain;{SH}"></div>'''
    bot=f'''<div style="position:absolute;left:44px;right:44px;top:34px"><div class="h" style="font-size:44px">{name}</div>
<div style="display:flex;align-items:flex-end;gap:28px;margin-top:20px"><div><div style="font-weight:800;font-size:21px;letter-spacing:.06em;opacity:.6">LOWEST TODAY</div><div class="h" style="font-size:82px;line-height:1">{gbp(lo)}</div><div style="font-size:24px;font-weight:700;margin-top:4px">at {ls}</div></div>
<div style="padding-bottom:4px"><div style="font-weight:800;font-size:21px;letter-spacing:.06em;opacity:.5">ANOTHER SHOP</div><div class="h" style="font-size:44px;opacity:.5;text-decoration:line-through;text-decoration-thickness:4px">{gbp(hi)}</div><div style="font-size:22px;font-weight:600;opacity:.6">at {hs}</div></div></div></div>'''
    return coupon(50,70,980,1110,660,top,bot)+burst(770,10,270,"SAVE",gbp(hi-lo),44)+fn(f"Same pump and colour, two shops. Prices on BabySorted, {DATE}. Prices can change.")
cover=hero_cover(baby(23,1080,800,.5,.34,1.0),'<div class="tags"><span class="tag t1">Deals</span><span class="tag t2">Nursing &amp; Feeding</span></div>',"Breast pump deals this month","The same pump, cheaper at another UK shop.",None,0,card=NAVY,fg="#fff",pill_bg=ROSE,pill_fg=NAVY,pill="Swipe for the deals",title_fs=76)+ribbon(x=-70,y=60,w=470)+burst(740,640,300,"SAVE UP TO",gbp(max(d[5]-d[3] for d in D)),46,-8)
s2=f'''<div style="position:absolute;left:70px;right:70px;top:150px"><div class="kick" style="color:{ROSE};opacity:1">HOW WE PICK A DEAL</div><div class="h" style="font-size:62px;margin-top:8px">Same pump. Same colour. Best price.</div></div>
<div style="position:absolute;left:60px;right:60px;top:360px;background:#fff;color:{NAVY};border-radius:34px;padding:44px 48px">
<div class="b" style="font-size:40px">We don't trust a shop's own "was" price. We line up the <b>exact same pump</b>, in the <b>same colour</b>, across every UK shop we track, and show the lowest price today next to the dearest.</div>
<div style="margin-top:30px;display:flex;align-items:center;gap:24px"><div style="background:{ROSE};border-radius:22px;padding:14px 24px" class="h"><span style="font-size:50px">{gbp(sum(d[5]-d[3] for d in D))}</span></div><div style="font-size:30px;font-weight:700;line-height:1.25">saved across these 6 by<br>buying from the cheaper shop</div></div></div>'''+ribbon()+fn(f"Prices read from the BabySorted aggregator, {DATE}.")
T=[("Need hands-free?","If not, a standard electric pump usually costs less than a wearable."),("Count the extras","Check flange sizes and spare parts are included, not sold on top."),("Single vs double","A double pump saves time if you pump every day; a single suits once a day."),("Check again before you pay","Pump prices move. Compare on the day you buy.")]
tt="".join(f'''<div style="display:flex;gap:22px;padding:22px 0;border-top:{"0" if i==0 else f"4px dashed {ROSE}"}"><div class="h" style="flex:none;width:58px;height:58px;border-radius:50%;background:{ROSE};color:{NAVY};font-size:30px;display:flex;align-items:center;justify-content:center">{i+1}</div><div><div class="h" style="font-size:40px">{a}</div><div style="font-size:29px;font-weight:500;line-height:1.3;margin-top:6px">{c}</div></div></div>''' for i,(a,c) in enumerate(T))
s9=f'''<div style="position:absolute;left:70px;right:70px;top:170px"><div class="kick" style="color:{ROSE};opacity:1">BEFORE YOU BUY</div><div class="h" style="font-size:76px;margin-top:8px">4 checks so a deal stays a deal</div></div>
<div style="position:absolute;left:50px;right:50px;top:430px;background:#fff;color:{NAVY};border-radius:34px;padding:14px 44px 18px">{tt}</div>'''+ribbon()
s10=hero_last(baby(50,1080,760,.5,.45,1.0),"Compare pump prices before you buy","See every UK shop's price for the same pump in one place.",ROSE,fg="#fff")+ribbon(x=-70,y=60,w=470)
SN=["Momcozy M9 Double","Medela Freestyle Mini Double","Elvie Double","Momcozy M5 Double","Momcozy M9 Single","Elvie Single"]
rows="".join(f'<div style="display:flex;align-items:center;justify-content:space-between;padding:15px 0;border-top:{"0" if i==0 else f"4px dashed {ROSE}"}"><div class="h" style="font-size:33px">{n}</div><div style="background:{ROSE};border-radius:16px;padding:6px 14px;font-weight:800;font-size:28px;white-space:nowrap">save {gbp(d[5]-d[3])}</div></div>' for i,(n,d) in enumerate(zip(SN,D)))
pin=f'''<img src="{baby(45,1000,600,.5,.38,1.0)}" style="position:absolute;left:0;top:0;width:1000px;height:600px;object-fit:cover">
{ribbon(x=-60,y=50,w=450)}{burst(700,430,270,"SAVE UP TO",gbp(max(d[5]-d[3] for d in D)),42,-8)}
<div style="position:absolute;left:0;right:0;top:570px;bottom:0;background:{NAVY};border-radius:40px 40px 0 0"></div>
<div style="position:absolute;left:56px;top:600px;width:660px" class="h"><span style="font-size:56px">Breast pump deals this month</span></div>
<div style="position:absolute;left:50px;right:50px;top:770px;background:#fff;color:{NAVY};border-radius:30px;padding:8px 34px">{rows}</div>
<div style="position:absolute;left:56px;right:56px;bottom:96px;font-size:22px;font-weight:600;color:{ROSE};line-height:1.3">Lowest vs highest price for the same pump and colour at UK shops. Prices on BabySorted, {DATE}. Prices can change.</div>
<div style="position:absolute;left:56px;right:56px;bottom:34px;display:flex;justify-content:space-between;align-items:center"><div class="brand" style="font-size:34px">BabySorted</div><div style="font-weight:700;font-size:25px">Compare breast pump prices at babysorted.com</div></div>'''
render(ROOT+"/out/deals2",[cover,s2]+[deal(i+1,*d) for i,d in enumerate(D)]+[s9,s10],pin,CSS,"#fff")
