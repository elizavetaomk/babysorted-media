# Navy "coupon" style for ALL Deals posts (owner's request, 11 Nov 2026: deals must look different from normal posts).
# Navy background, white tear-off coupons with side notches and a dashed tear line, deeper-pink starburst SAVE badges,
# a tilted deeper-pink event ribbon, and the dearer shop's price struck through. Only navy + deeper pink + white.
# Used for: #20 Black Friday pram deals (25 Nov 2026) and #21 Black Friday car seat deals (27 Nov 2026, this file).
# Prices from the BabySorted catalog, last updated 22 Nov 2026. Same product and colour compared across shops.
# Facts: GOV.UK child car seats (label with capital E in a circle and R129 or ECE R44), GOV.UK consumer rights (14 days to cancel online orders).
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
EVENT="BLACK FRIDAY"; DATE="22 Nov 2026"
CSS=css(NAVY,"#fff",ROSE,NAVY)+".t2{box-shadow:inset 0 0 0 3px #fff}"
D=[("doona","Car seat &amp; stroller","Doona X Car Seat &amp; Stroller, Dusty Sage",428.00,"Mamas &amp; Papas",549.00,"CuddleCo",470),
   ("axkid","Extended rear-facing","Axkid Movekid Car Seat, Tar",265.00,"Natural Baby Shower",355.50,"Winstanleys Pramworld",520),
   ("sirona","Rotating","Cybex Sirona Gi i-Size Car Seat, Magic Black",185.00,"Natural Baby Shower",249.95,"Cybex UK",500),
   ("cloudt","Infant carrier","Cybex Cloud T i-Size Plus Car Seat, Sage Green",175.00,"Natural Baby Shower",219.95,"Winstanleys Pramworld",500),
   ("maple","Infant carrier","Thule Maple Infant Car Seat, Faded Khaki",211.65,"Natural Baby Shower",249.00,"Winstanleys Pramworld",500),
   ("todl","Toddler","Nuna TODL Next Car Seat, Caviar",297.00,"Natural Baby Shower",330.00,"Mamas &amp; Papas",500)]
IM={k:b(k+".png",900) for k,*_ in D}
TOTAL=sum(d[5]-d[3] for d in D)
gbp=lambda v: f"£{v:,.2f}"
def burst(x,y,s,top,big,fs=48,rot=-10):
    pts=[]
    import math
    for i in range(32):
        r=50 if i%2==0 else 42; a=math.pi*2*i/32
        pts.append(f"{50+r*math.cos(a):.1f},{50+r*math.sin(a):.1f}")
    return f'''<div style="position:absolute;left:{x}px;top:{y}px;width:{s}px;height:{s}px;transform:rotate({rot}deg);z-index:3"><svg width="{s}" height="{s}" viewBox="0 0 100 100" style="position:absolute;inset:0;filter:drop-shadow(0 10px 14px rgba(0,0,0,.25))"><polygon points="{' '.join(pts)}" fill="{ROSE}"/></svg>
<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;color:{NAVY}"><div style="font-weight:800;font-size:{int(fs*.5)}px;letter-spacing:.08em">{top}</div><div class="h" style="font-size:{fs}px">{big}</div></div></div>'''
def ribbon(text=EVENT,x=-60,y=58,w=420):
    return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;background:{ROSE};color:{NAVY};text-align:center;font-weight:900;font-size:30px;letter-spacing:.12em;padding:12px 0;transform:rotate(-8deg);z-index:4;box-shadow:0 8px 14px rgba(0,0,0,.25)">{text}</div>'
def coupon(x,y,w,h,split,inner_top,inner_bottom,notch_bg=NAVY):
    """White coupon with side notches at `split` px from its top and a dashed tear line."""
    return f'''<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:#fff;border-radius:34px;color:{NAVY};overflow:hidden">
<div style="position:absolute;left:0;right:0;top:0;height:{split}px">{inner_top}</div>
<div style="position:absolute;left:44px;right:44px;top:{split}px;border-top:5px dashed {NAVY};opacity:.25"></div>
<div style="position:absolute;left:0;right:0;top:{split}px;bottom:0">{inner_bottom}</div>
<div style="position:absolute;left:-30px;top:{split-30}px;width:60px;height:60px;border-radius:50%;background:{notch_bg}"></div>
<div style="position:absolute;right:-30px;top:{split-30}px;width:60px;height:60px;border-radius:50%;background:{notch_bg}"></div></div>'''
foot_note=lambda t: f'<div style="position:absolute;left:70px;right:70px;top:1200px;font-size:23px;font-weight:600;color:{ROSE}">{t}</div>'
def deal(i,k,cat,name,lo,ls,hi,hs,h):
    top=f'''<div style="position:absolute;left:40px;top:34px;font-weight:800;font-size:24px;letter-spacing:.06em;opacity:.6">DEAL {i} OF 6 · {cat.upper()}</div>
<div style="position:absolute;inset:60px 0 20px;display:flex;align-items:center;justify-content:center"><img src="{IM[k]}" style="height:{h}px;max-width:76%;object-fit:contain;{SH}"></div>'''
    bot=f'''<div style="position:absolute;left:44px;right:44px;top:34px"><div class="h" style="font-size:46px">{name}</div>
<div style="display:flex;align-items:flex-end;gap:28px;margin-top:20px"><div><div style="font-weight:800;font-size:21px;letter-spacing:.06em;opacity:.6">LOWEST TODAY</div><div class="h" style="font-size:82px;line-height:1">{gbp(lo)}</div><div style="font-size:24px;font-weight:700;margin-top:4px">at {ls}</div></div>
<div style="padding-bottom:4px"><div style="font-weight:800;font-size:21px;letter-spacing:.06em;opacity:.5">ANOTHER SHOP</div><div class="h" style="font-size:44px;opacity:.5;text-decoration:line-through;text-decoration-thickness:4px">{gbp(hi)}</div><div style="font-size:22px;font-weight:600;opacity:.6">at {hs}</div></div></div></div>'''
    return coupon(50,70,980,1110,660,top,bot)+burst(770,10,270,"SAVE",gbp(hi-lo),44)+foot_note(f"Prices on BabySorted, {DATE}. Prices can change.")
SN=["Doona X","Axkid Movekid","Cybex Sirona Gi i-Size","Cybex Cloud T i-Size Plus","Thule Maple","Nuna TODL Next"]
# Cover: photo-led, navy coupon world with ribbon + starburst
cover=hero_cover(baby(9,1080,800,.5,.42,1.05),'<div class="tags"><span class="tag t1">Deals</span><span class="tag t2">Car Seats</span></div>',"Black Friday car seat deals","Same seat, same colour, a lower price in another UK shop.",None,0,card=NAVY,fg="#fff",pill_bg=ROSE,pill_fg=NAVY,pill="Swipe for the deals",title_fs=72)+ribbon(x=-70,y=60,w=460)+burst(760,620,290,"SAVE UP TO",gbp(max(d[5]-d[3] for d in D)),46,-8)+foot_note(f"Prices on BabySorted, {DATE}. Prices can change.")
T=[("Same model, same colour","“Plus”, “Gi” or “Next” in a name can mean a different seat."),("Check it fits your car","Seat makers publish car fit lists. Check yours first."),("Look for the label","A capital E in a circle and R129 (or ECE R44)."),("Check delivery and returns","Bought online? You usually get 14 days to cancel.")]
tt="".join(f'''<div style="display:flex;gap:22px;padding:22px 0;border-top:{"0" if i==0 else f"4px dashed {ROSE}"}"><div class="h" style="flex:none;width:58px;height:58px;border-radius:50%;background:{ROSE};color:{NAVY};font-size:30px;display:flex;align-items:center;justify-content:center">{i+1}</div><div><div class="h" style="font-size:42px">{a}</div><div style="font-size:31px;font-weight:500;line-height:1.3;margin-top:6px">{c}</div></div></div>''' for i,(a,c) in enumerate(T))
s2=f'''<div style="position:absolute;left:70px;right:70px;top:190px"><div class="kick" style="color:{ROSE};opacity:1">BEFORE YOU BUY</div><div class="h" style="font-size:74px;margin-top:8px">4 checks before you buy a car seat</div></div>
<div style="position:absolute;left:50px;right:50px;top:440px;background:#fff;color:{NAVY};border-radius:34px;padding:12px 44px 16px">{tt}</div>'''+ribbon()+foot_note("Source: GOV.UK (car seat labels, cancelling online orders).")
s9=f'''<div style="position:absolute;left:70px;right:70px;top:200px"><div class="kick" style="color:{ROSE};opacity:1">ON BABYSORTED TODAY</div><div class="h" style="font-size:76px;margin-top:8px">{gbp(TOTAL)}</div><div class="h" style="font-size:46px;margin-top:10px">saved on these 6 car seats by picking the cheaper UK shop</div></div>
<div style="position:absolute;left:50px;right:50px;top:500px;background:#fff;color:{NAVY};border-radius:34px;padding:10px 40px">{"".join(f'<div style="display:flex;justify-content:space-between;align-items:center;padding:16px 0;border-top:{"0" if i==0 else f"4px dashed {ROSE}"}"><div class="h" style="font-size:34px">{n}</div><div style="background:{ROSE};border-radius:16px;padding:6px 14px;font-weight:800;font-size:28px;white-space:nowrap">save {gbp(d[5]-d[3])}</div></div>' for i,(n,d) in enumerate(zip(SN,D)))}</div>'''+ribbon()+foot_note(f"Prices on BabySorted, {DATE}. Prices can change.")
s10=hero_last(baby(31,1080,760,.5,.38,1.05),"Compare car seat prices before you buy","See every UK shop’s price for the same car seat in one place.",ROSE,fg="#fff")+ribbon(x=-70,y=60,w=460)
# Pin: photo-led, navy coupon list
rows="".join(f'<div style="display:flex;align-items:center;justify-content:space-between;padding:15px 0;border-top:{"0" if i==0 else f"4px dashed {ROSE}"}"><div class="h" style="font-size:34px">{n}</div><div style="background:{ROSE};border-radius:16px;padding:6px 14px;font-weight:800;font-size:28px;white-space:nowrap">save {gbp(d[5]-d[3])}</div></div>' for i,(n,d) in enumerate(zip(SN,D)))
pin=f'''<img src="{baby(23,1000,600,.5,.35,1.0)}" style="position:absolute;left:0;top:0;width:1000px;height:600px;object-fit:cover">
{ribbon(x=-60,y=50,w=440)}{burst(700,430,270,"SAVE UP TO",gbp(max(d[5]-d[3] for d in D)),42,-8)}
<div style="position:absolute;left:0;right:0;top:570px;bottom:0;background:{NAVY};border-radius:40px 40px 0 0"></div>
<div style="position:absolute;left:56px;top:600px;width:640px" class="h"><span style="font-size:54px">Black Friday car seat deals</span></div>
<div style="position:absolute;left:50px;right:50px;top:760px;background:#fff;color:{NAVY};border-radius:30px;padding:8px 34px">{rows}</div>
<div style="position:absolute;left:56px;right:56px;bottom:96px;font-size:22px;font-weight:600;color:{ROSE};line-height:1.3">Lowest vs highest price for the same car seat and colour at UK shops. Prices on BabySorted, {DATE}. Prices can change.</div>
<div style="position:absolute;left:56px;right:56px;bottom:34px;display:flex;justify-content:space-between;align-items:center"><div class="brand" style="font-size:34px">BabySorted</div><div style="font-weight:700;font-size:25px">Compare car seat prices at babysorted.com</div></div>'''
render(ROOT+"/out/d",[cover,s2]+[deal(i+1,*d) for i,d in enumerate(D)]+[s9,s10],pin,CSS,"#fff")
