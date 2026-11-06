# Navy "short list" layout: white paper on navy with tick boxes, counter and progress boxes, plus can-wait / never-buy lists and a running bill.
# Used for: Nursery furniture you really need (Nov 2026). Facts: Lullaby Trust, NHS. Prices: BabySorted catalog.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
RED="#D9485F"
CSS=css(NAVY,"#fff",MINT,NAVY)+f""".paper{{position:absolute;left:60px;right:60px;top:60px;bottom:130px;background:#fff;border-radius:40px;color:{NAVY}}} .t2{{background:#fff;color:{NAVY};box-shadow:inset 0 0 0 3px {NAVY}}}"""
deco=star(24,24,26,PINK)+star(1020,28,24,"#fff",.6)
MO=b("moses.png",900); MA=b("bedmat.png",900); DR=b("dream.png",800); EG=b("egg.png",700); CH=b("chgmat.png",900); MI=b("misha.png",1000)
TICK='<svg viewBox="0 0 24 24" width="{s}" height="{s}"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="{c}" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def box(size,checked):
    inner=TICK.format(s=int(size*.8),c=NAVY) if checked else ""
    return f'<div style="flex:none;width:{size}px;height:{size}px;border-radius:{int(size*.28)}px;background:{MINT if checked else "#fff"};box-shadow:inset 0 0 0 {max(3,size//16)}px {NAVY};display:flex;align-items:center;justify-content:center">{inner}</div>'
N=5
SRCS=["The Lullaby Trust, the UK safer baby sleep charity"]*4+["NHS"]
ITEMS=[("A small bed for your room","The Lullaby Trust says your baby sleeps in your room, day and night, for at least 6 months. So the first bed isn't in the nursery at all.",MO,"£99.99","Shnuggle Dreami, mattress included",380),
("A good new mattress","Firm, flat and waterproof, and new for each baby. It should fit with no gaps. Most Moses baskets come with one, so check first.",MA,"£55","Tutti Bambini fibre, cot bed size",300),
("A sleep bag or sheets","Sleep bags stop bedding covering your baby's head. Look for BS EN 16781 and choose by your baby's weight.",DR,"£25","Dreampod 2.5 tog",380),
("A room thermometer","Keep the room at 16 to 20°C. This one small thing tells you when to change the layers.",EG,"£19.98","Tommee Tippee Gro Egg 2",340),
("A mat for changing","The NHS says change on a mat on the floor. So a dresser is a nice extra, not a need.",CH,"£15","Mama Shack mat",300)]
def item(k):
    t,bd,pic,pr,nm,h=ITEMS[k]
    prog="".join(box(58,j<=k) for j in range(N))
    return deco+f'''<div class="paper"></div><div style="position:absolute;left:110px;right:110px;top:100px;display:flex;justify-content:space-between;align-items:center;color:{NAVY}"><span style="font-weight:700;font-size:30px;opacity:.6">The short list</span><span style="font-weight:800;font-size:32px;background:{PINK};padding:9px 22px;border-radius:26px">{k+1} of {N}</span></div>
<div style="position:absolute;left:110px;right:110px;top:180px;height:400px;display:flex;align-items:center;justify-content:space-between;gap:30px"><img src="{pic}" style="height:{h}px;max-width:520px;object-fit:contain;{SH}"><div style="text-align:right;color:{NAVY}"><div class="h" style="font-size:84px">{pr}</div><div style="font-size:27px;font-weight:600;opacity:.65;margin-top:8px;width:290px;line-height:1.25;margin-left:auto">{nm}</div><div style="font-size:24px;font-weight:600;opacity:.6;margin-top:8px;width:290px;line-height:1.25;margin-left:auto">Price on BabySorted,<br>6 Nov 2026</div></div></div>
<div style="position:absolute;left:110px;right:110px;top:600px;color:{NAVY}">{box(90,True)}<div class="h" style="font-size:66px;margin-top:20px">{t}</div><div style="font-size:38px;line-height:1.36;font-weight:500;margin-top:14px">{bd}</div></div>
<div style="position:absolute;left:110px;top:1115px;display:flex;gap:18px">{prog}</div><div style="position:absolute;left:510px;right:110px;top:1116px;height:58px;display:flex;align-items:center;justify-content:flex-end;text-align:right;font-size:24px;line-height:1.2;font-weight:600;opacity:.6;color:{NAVY}">Source: {SRCS[k]}</div>'''
crow="".join(f'<div style="display:flex;align-items:center;gap:20px;padding:11px 0">{box(46,i<2)}<div style="font-weight:700;font-size:33px;{"opacity:.45;text-decoration:line-through" if i<2 else ""}">{t}</div></div>' for i,t in enumerate(["Matching 4-piece set","Big wardrobe","A small bed for your room","A mattress that fits"]))
cover=deco+f'''<div class="paper"></div>
<div style="position:absolute;left:110px;right:110px;top:110px;color:{NAVY}"><div class="tags"><span class="tag t1">Checklist</span><span class="tag t2">Kids Furniture</span></div>
<div class="h" style="font-size:92px;margin-top:26px">Nursery furniture you really need</div>
<div style="font-size:37px;font-weight:600;opacity:.7;margin-top:14px">The short list. Everything else can wait.</div>
<div style="margin-top:24px;width:530px">{crow}</div></div>
<img src="{MO}" style="position:absolute;right:90px;bottom:160px;height:400px;{SH}">
{round_pic(baby(1,300,300,.46,.3,1.5),110,860,300,300,150,PINK)}'''
def lst(k,t,li,bg,src):
    r="".join(f'<div style="display:flex;gap:20px;align-items:flex-start;padding:32px 0;border-top:{"0" if i==0 else f"3px solid {PINK}"}"><div style="flex:none;width:52px;height:52px;border-radius:50%;background:{bg};color:{"#fff" if bg==RED else NAVY};font-weight:800;font-size:32px;display:flex;align-items:center;justify-content:center">{"✕" if bg==RED else "…"}</div><div><div class="h" style="font-size:47px">{a}</div><div style="font-size:36px;font-weight:500;line-height:1.28;margin-top:6px">{c}</div></div></div>' for i,(a,c) in enumerate(li))
    return deco+f'''<div class="paper"></div><div style="position:absolute;left:110px;right:110px;top:100px;color:{NAVY}"><div class="kick" style="opacity:.55">{k}</div><div class="h" style="font-size:76px;margin-top:8px">{t}</div><div style="margin-top:18px">{r}</div></div><div style="position:absolute;left:110px;top:1135px;font-size:26px;font-weight:600;opacity:.6;color:{NAVY}">{"Source: "+src if src else ""}</div>'''
s7=lst("IT CAN WAIT","These can wait",[("A cot or cot bed","You'll need one at about 6 months. Compare prices in your own time."),("A dresser changer","Handy, but a floor mat does the job."),("A wardrobe","Baby clothes are tiny. Drawers you own may do."),("A nursing chair","Try your sofa or bed first.")],MINT,"")
s8=lst("NEVER BUY","Not safe for sleep",[("Pods and nests","Soft sides don't belong in a sleep space."),("Cot bumpers","Keep the cot clear."),("Pillows and duvets","Not for a baby's cot."),("Hammocks and positioners","No wedges or straps that hold a set position.")],RED,"The Lullaby Trust, the UK safer baby sleep charity")
BL=[("Moses basket and stand","£99.99"),("Sleep bag","£25.00"),("Room thermometer","£19.98"),("Changing mat","£15.00")]
BL2=[("Cot bed","£189.00"),("Cot bed mattress","£55.00")]
rows=lambda L:"".join(f'<div style="display:flex;justify-content:space-between;font-size:37px;font-weight:600;padding:9px 0"><span>{a}</span><span>{c}</span></div>' for a,c in L)
s9=deco+f'''<div class="paper"></div><div style="position:absolute;left:110px;right:110px;top:100px;color:{NAVY}"><div class="kick" style="opacity:.55">ADD IT UP</div><div class="h" style="font-size:76px;margin-top:8px">Day one: about £160</div>
<div style="margin-top:26px;font-weight:800;font-size:30px;opacity:.55">DAY ONE</div>{rows(BL)}<div style="display:flex;justify-content:space-between;border-top:4px solid {NAVY};margin-top:10px;padding-top:14px"><span class="h" style="font-size:48px">Total</span><span class="h" style="font-size:48px">£159.97</span></div>
<div style="margin-top:32px;font-weight:800;font-size:30px;opacity:.55">AT ABOUT 6 MONTHS</div>{rows(BL2)}<div style="display:flex;justify-content:space-between;border-top:4px solid {NAVY};margin-top:10px;padding-top:14px"><span class="h" style="font-size:48px">Total</span><span class="h" style="font-size:48px">£244.00</span></div></div>
<div style="position:absolute;left:110px;right:110px;top:1095px;font-size:26px;font-weight:600;opacity:.6;color:{NAVY}">Prices on BabySorted, 6 Nov 2026.</div>'''
s10=deco+f'''<div class="paper"></div>{round_pic(baby(13,880,500,.42,.43),100,100,880,500,34)}
<div style="position:absolute;left:110px;right:110px;top:630px;color:{NAVY}"><div style="display:flex;gap:14px">{"".join(box(50,True) for _ in range(N))}</div>
<div class="h" style="font-size:72px;margin-top:24px">All ticked? Now compare prices</div>
<div style="font-size:36px;font-weight:500;margin-top:14px">Compare nursery prices from UK shops in one place.</div>
<div style="margin-top:24px;display:flex;align-items:center;gap:14px"><div class="h" style="font-size:42px;background:{PINK};padding:20px 28px;border-radius:24px;white-space:nowrap">babysorted.com/links</div><div style="background:{NAVY};color:#fff;font-weight:800;font-size:30px;padding:20px 24px;border-radius:24px;white-space:nowrap">Link in bio ↑</div></div></div>'''
PL=[("A small bed for your room","Moses basket, crib or cot. Your room for 6 months."),("A good new mattress","Firm, flat, waterproof. No gaps."),("A sleep bag or sheets","Sleep bags can't cover the head."),("A room thermometer","Keep it at 16 to 20°C."),("A mat for changing","On the floor, says the NHS.")]
pl="".join(f'<div style="display:flex;align-items:center;gap:20px;padding:19px 0;border-top:{"0" if i==0 else f"2px solid {PINK}"}">{box(46,False)}<div><div class="h" style="font-size:34px">{a}</div><div style="font-size:25px;font-weight:500;opacity:.8;margin-top:2px">{c}</div></div></div>' for i,(a,c) in enumerate(PL))
pin=f'''{star(30,26,28,PINK)}{star(950,30,24,"#fff",.6)}
<div style="position:absolute;left:50px;right:50px;top:60px;height:1240px;background:#fff;border-radius:40px"></div>
<div style="position:absolute;left:100px;right:100px;top:100px;color:{NAVY}"><div class="tags"><span class="tag t1" style="font-size:24px">Checklist</span><span class="tag t2" style="font-size:24px">Kids Furniture</span></div>
<div class="h" style="font-size:74px;margin-top:22px;width:520px">Nursery furniture you really need</div>
<div style="width:800px;margin-top:24px">{pl}</div>
<div style="margin-top:20px;background:{MINT};border-radius:24px;padding:18px 24px"><div style="font-weight:800;font-size:22px;opacity:.6;letter-spacing:.05em">CAN WAIT</div><div style="font-size:27px;font-weight:600;margin-top:2px;line-height:1.3">Cot bed (at about 6 months), dresser, wardrobe, nursing chair.</div></div>
<div style="margin-top:12px;background:{PINK};border-radius:24px;padding:18px 24px"><div style="font-weight:800;font-size:22px;opacity:.6;letter-spacing:.05em">NEVER FOR SLEEP</div><div style="font-size:27px;font-weight:600;margin-top:2px;line-height:1.3">Pods, nests, bumpers, pillows, duvets, hammocks.</div></div>
<div style="margin-top:14px;font-size:24px;font-weight:600;opacity:.6">Source: The Lullaby Trust, the UK safer baby sleep charity, and NHS</div></div>
<img src="{MO}" style="position:absolute;right:85px;top:110px;height:280px;{SH}">
<div style="position:absolute;left:60px;right:60px;bottom:50px;display:flex;justify-content:space-between;align-items:center;color:#fff"><div class="brand" style="font-size:34px">BabySorted</div><div style="font-weight:700;font-size:25px">Compare nursery prices at babysorted.com</div></div>'''
render(ROOT+"/out/p6",[cover]+[item(k) for k in range(N)]+[s7,s8,s9,s10],pin,CSS,"#fff")
