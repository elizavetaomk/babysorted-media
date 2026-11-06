# Deeper-pink "basket ticket" layout: rose bg, white till-receipt card with a dashed tear line, item count and a running basket; printable pin.
# Used for: Bottle feeding starter kit (Nov 2026). Facts: NHS Best Start in Life. Prices: BabySorted catalog. No formula products shown.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css(ROSE,NAVY,NAVY,"#fff")+".t2{background:#fff;box-shadow:none}"
deco=star(36,30,26,"#fff")+star(1000,40,30,"#fff")
MA=b("mam.png",1000); TT=b("ttset.png",1000); ST=b("steril.png",1000); BR=b("brush.png",800)
N=6
def tear(y): return f'<div style="position:absolute;left:0;right:0;top:{y}px;border-top:5px dashed {ROSE}"></div>'
def nub(y): return f'<div style="position:absolute;left:-26px;top:{y-24}px;width:52px;height:52px;border-radius:50%;background:{ROSE}"></div><div style="position:absolute;right:-26px;top:{y-24}px;width:52px;height:52px;border-radius:50%;background:{ROSE}"></div>'
def ticket(k,title,body,vis,price="",sub="",src="Source: NHS"):
    chk=f'<div style="flex:none;width:76px;height:76px;border-radius:22px;background:{MINT};box-shadow:inset 0 0 0 5px {NAVY};display:flex;align-items:center;justify-content:center"><svg viewBox="0 0 24 24" width="58" height="58"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="{NAVY}" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
    pr=f'<div style="text-align:right"><div class="h" style="font-size:52px">{price}</div><div style="font-size:24px;font-weight:600;opacity:.6;white-space:nowrap">{sub}</div></div>' if price else ""
    return deco+f'''<div style="position:absolute;left:70px;right:70px;top:60px;height:1180px;background:#fff;border-radius:36px;overflow:hidden">
<div style="position:absolute;left:44px;right:44px;top:34px;display:flex;justify-content:space-between;align-items:center"><span class="kick" style="opacity:.55">YOUR DAY-ONE BASKET</span><span style="font-weight:800;font-size:30px;background:{ROSE};padding:8px 20px;border-radius:24px">{k} of {N}</span></div>
<div style="position:absolute;left:0;right:0;top:110px;height:520px;display:flex;align-items:center;justify-content:center;padding:10px 60px">{vis}</div>
{tear(650)}{nub(652)}
<div style="position:absolute;left:44px;right:44px;top:690px;display:flex;gap:24px;align-items:flex-start">{chk}<div class="h" style="font-size:62px;flex:1">{title}</div>{pr}</div>
<div class="b" style="position:absolute;left:44px;right:44px;top:{860 if len(title)>18 else 790}px;font-size:41px">{body}</div><div style="position:absolute;left:44px;right:44px;bottom:24px;font-size:26px;font-weight:600;opacity:.6">{src}</div></div>'''
I=lambda s,h,x="": f'<img src="{s}" style="height:{h}px;max-width:100%;object-fit:contain;{SH};{x}">'
big=lambda t,s: f'<div style="width:100%;height:100%;background:{MINT};border-radius:36px;display:flex;align-items:center;justify-content:center;margin-top:10px"><div class="h" style="font-size:{s}px">{t}</div></div>'
cover=star(50,40,34,"#fff")+star(1000,700,30,"#fff")+f'''<div style="position:absolute;left:70px;right:70px;top:70px"><div class="tags"><span class="tag t1">Checklist</span><span class="tag t2">Nursing &amp; Feeding</span></div>
<div class="h" style="font-size:100px;margin-top:28px">Bottle feeding starter kit</div>
<div style="font-size:38px;font-weight:600;opacity:.8;margin-top:18px;width:510px;line-height:1.25">Everything you need before day one. And what you can skip.</div></div>
{round_pic(baby(7,400,430,.42,.5),610,290,400,430,44)}
<div style="position:absolute;left:60px;right:60px;top:760px;height:450px;background:#fff;border-radius:44px;display:flex;align-items:center;justify-content:center;gap:50px;padding:24px 50px">{I(MA,330)}{I(ST,300)}</div>
<div style="position:absolute;left:70px;top:640px;background:{NAVY};color:#fff;font-weight:700;font-size:30px;padding:14px 28px;border-radius:40px">Swipe before you buy</div>'''
s2=ticket(1,"Small bottles first","Newborns feed little and often, so many parents start small and size up. A pack of 4 is plenty until you know what your baby likes.",I(MA,470),"£32","MAM 160 ml × 4","Price on BabySorted, 6 Nov 2026.")
s3=ticket(2,"Slow-flow teats","A slower flow is generally advised for newborns, so milk doesn't come too fast. Teats also come in round and natural shapes. Try both and follow your baby's lead.",I(TT,500),"£32.98","Tommee Tippee set","Price on BabySorted, 6 Nov 2026.")
s4=ticket(3,"A bottle and teat brush","Bottles need a wash in hot, soapy water before they go in the steriliser. Check teats for damage as you go. Then rinse in cold running water.",I(BR,490),"£2.49","Jane dual brush","Price on BabySorted, 6 Nov 2026.")
s5=ticket(4,"A steriliser","Steam, microwave or cold water all work. A dishwasher cleans bottles but does not sterilise them. Face openings down, and change cold-water solution every 24 hours.",I(ST,470),"£24.95","Tommee Tippee 2-in-1","Source: NHS. Price on BabySorted, 6 Nov 2026.")
s6=ticket(5,"First infant formula","By UK law all infant formula must meet the same standards. So there's no need to pay extra for a name. The NHS says follow-on formula isn't needed either.",big("Any brand",130)+"")
s7=ticket(6,"Ready-to-feed backup","Handy for a hard night. Once open, keep it at the back of the top fridge shelf for up to 24 hours. Bottles still need sterilising.",big("Plan B",150))
PR=[("Fresh water, every time","Boil at least 1 litre of cold tap water. Not bottled, and not boiled twice."),("Wait no more than 30 minutes","Then it's still 70°C or above, which is what the NHS asks for."),("One feed at a time","Throw away what's left after a feed. Bin any left out over 2 hours."),("Prep machine? Test it","The water must reach 70°C. Check with a digital food thermometer.")]
pr="".join(f'''<div style="display:flex;gap:24px;padding:34px 0;border-top:{"0" if i==0 else f"4px dashed {ROSE}"}"><div class="h" style="flex:none;width:64px;height:64px;border-radius:50%;background:{NAVY};color:#fff;font-size:34px;display:flex;align-items:center;justify-content:center">{i+1}</div><div><div class="h" style="font-size:45px">{a}</div><div style="font-size:36px;font-weight:500;line-height:1.3;margin-top:8px">{c}</div></div></div>''' for i,(a,c) in enumerate(PR))
s8=deco+f'''<div style="position:absolute;left:70px;right:70px;top:70px"><div class="kick">NOT IN THE BOX</div><div class="h" style="font-size:80px;margin-top:8px">4 habits that matter more</div></div>
<div style="position:absolute;left:60px;right:60px;top:230px;background:#fff;border-radius:40px;padding:14px 44px 16px">{pr}</div><div style="position:absolute;left:70px;right:70px;top:1165px;font-size:27px;font-weight:600;opacity:.7;">Source: NHS</div>'''
s9=f'''{star(36,30,26,"#fff")}{round_pic(baby(1,960,560,.45,.32),60,60,960,560,44)}
<div style="position:absolute;left:70px;right:70px;top:650px"><div class="h" style="font-size:78px">Ready to fill the basket? Compare prices first</div>
<div class="b" style="margin-top:18px;font-size:38px">Compare bottle and steriliser prices from UK shops in one place.</div>
<div style="margin-top:30px">{link_row("#fff")}</div>
<div style="margin-top:20px;font-size:32px;font-weight:700;opacity:.6">Save this post for later</div></div>'''
L=[("Small bottles","Start small, size up as your baby grows."),("Slow-flow teats","Try round and natural shapes."),("Bottle and teat brush","Hot soapy water, then rinse."),("A steriliser","Steam, microwave or cold water."),("First infant formula","Any brand. Follow-on isn't needed."),("Ready-to-feed backup","24 hours in the fridge once open.")]
def bx(): return f'<div style="flex:none;width:44px;height:44px;border-radius:12px;background:#fff;box-shadow:inset 0 0 0 4px {NAVY}"></div>'
ls="".join(f'<div style="display:flex;align-items:center;gap:20px;padding:17px 0;border-top:{"0" if i==0 else f"3px dashed {ROSE}"}">{bx()}<div><div class="h" style="font-size:33px">{a}</div><div style="font-size:24px;font-weight:500;opacity:.8;margin-top:2px">{c}</div></div></div>' for i,(a,c) in enumerate(L))
pin=f'''{star(920,44,32,"#fff")}<div style="position:absolute;left:60px;right:60px;top:56px"><div class="tags"><span class="tag t1" style="font-size:24px">Checklist</span><span class="tag t2" style="font-size:24px">Nursing &amp; Feeding</span></div>
<div class="h" style="font-size:88px;margin-top:20px">Bottle feeding starter kit</div></div>
<div style="position:absolute;left:60px;right:60px;top:370px;background:#fff;border-radius:34px;padding:22px 34px 18px;height:760px"><div style="position:absolute;right:26px;top:30px;width:240px;display:flex;flex-direction:column;align-items:center;gap:40px">{I(MA,220)}{I(ST,200)}</div><div style="width:560px">{ls}</div>
<div style="position:absolute;left:34px;right:34px;bottom:22px;font-size:24px;font-weight:600;opacity:.6">Source: NHS Best Start in Life</div></div>
<div style="position:absolute;left:60px;right:60px;top:1150px;background:{NAVY};color:#fff;border-radius:28px;padding:22px 30px"><div style="font-weight:800;font-size:22px;opacity:.7;letter-spacing:.06em">EVERY FEED</div><div style="font-size:29px;font-weight:600;margin-top:4px;line-height:1.3">Fresh cold tap water, boiled. Cool no more than 30 minutes, so it's 70°C or above. Make one feed at a time. Throw away leftovers.</div></div>
<div style="position:absolute;left:60px;right:60px;bottom:38px;display:flex;justify-content:space-between;align-items:center"><div class="brand" style="font-size:34px">BabySorted</div><div style="font-weight:700;font-size:25px">Compare bottle prices at babysorted.com</div></div>'''
render(ROOT+"/out/p2",[cover,s2,s3,s4,s5,s6,s7,s8,s9],pin,CSS,NAVY)
