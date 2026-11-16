# Navy "buy now / can wait" checklist (17 Nov 2026): navy bg, white paper card, big mint tick, "2 of 6" counter,
# product on a pink panel inside the card, progress boxes. Photo-led cover and last slide.
# Used for: #46 Big baby gear checklist: what to buy before birth. Facts: GOV.UK, The Lullaby Trust, NHS.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css(NAVY,"#fff",MINT,NAVY)+f".t2{{background:{PINK};color:{NAVY};box-shadow:none}}"
IS=b("isnug.png",1000); CR=b("crib.png",1000); SB=b("sbag.png",800)
TICK='<svg viewBox="0 0 24 24" width="{s}" height="{s}"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="#051F45" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def box(s,on,r=None):
    r=r or s*.28
    return f'<div style="flex:none;width:{s}px;height:{s}px;border-radius:{r}px;background:{MINT if on else "#fff"};box-shadow:inset 0 0 0 {max(3,s//16)}px {NAVY};display:flex;align-items:center;justify-content:center">{TICK.format(s=int(s*.8)) if on else ""}</div>'
deco=star(40,26,30,PINK)+star(1000,30,26,"#fff",.6)
ITEMS=[("Infant car seat","Rear-facing, and fitted before your due date so you're not learning in the hospital car park. By law, children use a car seat until 12 years old or 135cm tall.","Source: GOV.UK",IS,330),
("A safe sleep space in your room","For the first 6 months, your baby sleeps in a crib, cot or Moses basket in your room. Firm, flat, waterproof mattress that fits with no gaps.","Source: The Lullaby Trust, the UK safer baby sleep charity",CR,320),
("A pram that works from birth","A carrycot or a seat that lies flat. Before you buy, measure your boot and your front door.","",None,0),
("Baby sleeping bags","The right size, so your baby can't slip down inside, and the right tog for the room. Aim for a room of 16 to 20°C.","Source: The Lullaby Trust, the UK safer baby sleep charity",SB,330),
("Feeding basics","Bottle feeding? Bottles, formula and a way to sterilise: the NHS says sterilise feeding kit until at least 12 months. Breastfeeding? You may need very little at first.","Source: NHS",None,0),
("A changing mat for the floor","Change nappies on a mat on the floor, so your baby can't roll off. A changing table is a nice extra, not a must.","Source: NHS",None,0)]
N=len(ITEMS)
def big(txt,sub): return f'<div style="text-align:center"><div class="h" style="font-size:120px;color:{NAVY}">{txt}</div><div style="font-weight:700;font-size:34px;color:{NAVY};margin-top:6px">{sub}</div></div>'
EXTRA={2:big("Flat","carrycot or lie-flat seat"),4:big("12","months of sterilising"),5:big("Floor","the safest place to change")}
def item(k):
    t,body,src,pic,h=ITEMS[k]
    prog="".join(box(44,j<=k,12) for j in range(N))
    panel=f'<img src="{pic}" style="height:{h+50}px;max-width:100%;object-fit:contain;{SH}">' if pic else EXTRA[k]
    return deco+f'''<div style="position:absolute;left:60px;right:60px;top:60px;bottom:140px;background:#fff;border-radius:44px"></div>
<div style="position:absolute;left:100px;right:100px;top:100px;height:470px;background:{PINK if k%2==0 else MINT};border-radius:34px;display:flex;align-items:center;justify-content:center">{panel}</div>
<div style="position:absolute;left:124px;top:124px">{box(84,True,22)}</div>
<div style="position:absolute;right:124px;top:128px;font-weight:800;font-size:30px;background:{NAVY};color:#fff;padding:10px 22px;border-radius:24px">{k+1} of {N}</div>
<div style="position:absolute;left:110px;right:110px;top:605px;color:{NAVY}"><div class="kick">BUY BEFORE BIRTH</div><div class="h" style="font-size:{68 if len(t)<24 else 60}px;margin-top:8px">{t}</div>
<div class="b" style="font-size:35px;margin-top:14px">{body}</div><div style="font-size:24px;font-weight:700;opacity:.6;margin-top:12px">{src}</div></div>
<div style="position:absolute;left:110px;right:110px;bottom:170px;display:flex;gap:14px">{prog}</div>'''
cover=hero_cover(baby(34,1080,800,.5,.45),'<div class="tags"><span class="tag t1">Checklist</span><span class="tag t2">All categories</span></div>',"Big baby gear checklist: what to buy before birth","Six things first. The rest can wait.",f'<img src="{CR}" style="height:230px;{SH}">',1,card=NAVY,fg="#fff",pill_bg=PINK,pill_fg=NAVY,title_fs=58)
s2=deco+f'''<div style="position:absolute;left:70px;right:70px;top:90px"><div class="kick">THE ORDER MATTERS</div><div class="h" style="font-size:82px;margin-top:8px">You need less than the shop says</div></div>
<div style="position:absolute;left:60px;right:60px;top:400px;display:flex;gap:20px">
<div style="flex:1;background:#fff;color:{NAVY};border-radius:36px;padding:40px 34px"><div class="h" style="font-size:96px">6</div><div class="h" style="font-size:40px;margin-top:6px">things before birth</div><div style="font-size:30px;font-weight:500;margin-top:12px;line-height:1.35">Getting home, sleeping, feeding, changing.</div></div>
<div style="flex:1;background:{PINK};color:{NAVY};border-radius:36px;padding:40px 34px"><div class="h" style="font-size:96px">6+</div><div class="h" style="font-size:40px;margin-top:6px">months for the rest</div><div style="font-size:30px;font-weight:500;margin-top:12px;line-height:1.35">Buy later, when you know what your baby needs.</div></div></div>
<div class="b" style="position:absolute;left:70px;right:70px;top:880px;font-size:38px">Spreading it out also means more time to compare prices on the big buys.</div>'''
W=[("High chair","Solid food starts at around 6 months."),("Next-stage car seat","Only once your baby outgrows the first one."),("Big cot or cot bed","Can wait if your baby starts in a crib or Moses basket."),("Baby monitor","Your baby sleeps in your room for 6 months."),("Breast pump","Only if and when you need one.")]
wr="".join(f'<div style="display:flex;align-items:center;gap:22px;padding:20px 0;border-top:{"0" if i==0 else f"3px solid {PINK}"}">{box(54,False,14)}<div><div class="h" style="font-size:40px">{a}</div><div style="font-size:29px;font-weight:500;margin-top:4px">{c}</div></div></div>' for i,(a,c) in enumerate(W))
s9=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="kick">CAN WAIT</div><div class="h" style="font-size:80px;margin-top:8px">5 things to buy later</div></div>
<div style="position:absolute;left:60px;right:60px;top:300px;background:#fff;color:{NAVY};border-radius:40px;padding:16px 44px 20px">{wr}</div>
<div style="position:absolute;left:70px;right:70px;top:1150px;font-size:24px;font-weight:700;opacity:.7">Source: NHS and The Lullaby Trust, the UK safer baby sleep charity</div>'''
s10=hero_last(baby(16,1080,760,.5,.5),"Ready to tick them off? Compare prices first","Compare car seat, crib and pram prices from UK shops in one place.",PINK,fg="#fff")
pin=pin_hero(baby(24,1000,660,.5,.5),pin_tags("Checklist","All categories"),"What to buy before birth",["Infant car seat, fitted early","A safe sleep space in your room","A pram that works from birth","Baby sleeping bags","Feeding basics","A changing mat for the floor"],CR,230,NAVY,"#fff",MINT,NAVY,"Sources: GOV.UK, NHS and The Lullaby Trust, the UK safer baby sleep charity. High chair, monitor and next car seat can wait.","Compare baby gear prices at babysorted.com",line="#25406a",photo_h=660,title_fs=58)
render(ROOT+"/out/b",[cover,s2]+[item(k) for k in range(N)]+[s9,s10],pin,CSS,"#fff")
