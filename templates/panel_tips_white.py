# White "panel tips" layout: white bg, coloured rounded panel with product on top (pink/grey/mint rotate),
# "n of 7" badge, big headline + body + verdict pill below. Cover = title on top, 3 products in coloured cards.
# Used for: How to choose baby bottles (31 Oct 2026). Run from folder with cut/*.png; writes ./out_bottles
from playwright.sync_api import sync_playwright
import base64, os
PINK="#F1D3DF"; NAVY="#051F45"; ROSE="#E6B6C9"; MINT="#DDF5E3"; GREY="#EEF0F3"
b=lambda f: base64.b64encode(open(f,"rb").read()).decode()
BI=b("cut/bibs1.png"); TT=b("cut/tt.png"); LO=b("cut/lola.png"); TE=b("cut/teat.png")
OUT="out_bottles"; os.makedirs(OUT,exist_ok=True)
SH="filter:drop-shadow(0 18px 18px rgba(5,31,69,.16))"
def star(x,y,s,c,o=1): return f'<svg style="position:absolute;left:{x}px;top:{y}px;opacity:{o}" width="{s}" height="{s}" viewBox="0 0 20 20"><path d="M10 0l2.6 7.4L20 10l-7.4 2.6L10 20l-2.6-7.4L0 10l7.4-2.6z" fill="{c}"/></svg>'
CSS=f"""*{{margin:0;padding:0;box-sizing:border-box}} body{{width:1080px;height:1350px;background:#fff;font-family:Inter;color:{NAVY};position:relative;overflow:hidden}}
.h{{font-weight:800;letter-spacing:-0.035em;line-height:1.04}}
.tags{{display:flex;gap:14px}} .tag{{font-weight:700;font-size:28px;padding:9px 22px;border-radius:30px}}
.t1{{background:{MINT}}} .t2{{background:#fff;box-shadow:inset 0 0 0 3px {NAVY}}}
.panel{{position:absolute;left:70px;right:70px;top:70px;height:540px;border-radius:44px;display:flex;align-items:center;justify-content:center;gap:40px}}
.kick{{font-weight:800;font-size:28px;letter-spacing:.06em;opacity:.5}}
.pill{{display:inline-block;font-weight:800;font-size:32px;padding:14px 26px;border-radius:26px;white-space:nowrap}}
.foot{{position:absolute;left:80px;right:80px;bottom:56px;display:flex;justify-content:space-between;align-items:center}}
.brand{{font-weight:800;font-size:36px;letter-spacing:-0.03em}}"""
def foot(i,n):
    d="".join(f'<div style="width:{40 if j==i else 14}px;height:14px;border-radius:7px;background:{NAVY};opacity:{1 if j==i else .2}"></div>' for j in range(n))
    return f'<div class="foot"><div class="brand">BabySorted</div><div style="display:flex;gap:12px">{d}</div></div>'
img=lambda s,h,x="": f'<img src="data:image/png;base64,{s}" style="height:{h}px;max-width:100%;object-fit:contain;{SH};{x}">'
deco=star(960,40,30,ROSE)
def tip(k,title,body,bg,vis,pill):
    return deco+f'''<div class="panel" style="background:{bg}">{vis}</div>
<div style="position:absolute;left:100px;top:100px;font-weight:800;font-size:28px;background:#fff;padding:8px 18px;border-radius:20px">{k} of 7</div>
<div style="position:absolute;left:90px;right:90px;top:660px"><div class="h" style="font-size:72px">{title}</div>
<div style="font-size:37px;font-weight:500;line-height:1.4;margin-top:20px">{body}</div><div style="margin-top:28px">{pill}</div></div>'''
NP=lambda t: f'<span class="pill" style="background:{NAVY};color:#fff">{t}</span>'
MP=lambda t: f'<span class="pill" style="background:{MINT}">{t}</span>'
PP=lambda t: f'<span class="pill" style="background:{PINK}">{t}</span>'
BIG=lambda big,small,fs=150: f'<div style="text-align:center"><div class="h" style="font-size:{fs}px;white-space:nowrap">{big}</div><div class="pill" style="background:{NAVY};color:#fff;margin-top:14px">{small}</div></div>'
cover=f"""{star(950,80,40,ROSE)}{star(70,620,26,ROSE)}
<div style="position:absolute;left:90px;right:90px;top:100px"><div class="tags"><span class="tag t1">Tips</span><span class="tag t2">Nursing &amp; Feeding</span></div>
<div class="h" style="font-size:104px;margin-top:30px">How to choose baby bottles</div>
<div style="font-size:40px;font-weight:600;opacity:.7;margin-top:20px">Anti-colic, teat flow, size. Made simple.</div>
<div style="margin-top:28px;display:inline-block;background:{NAVY};color:#fff;font-weight:700;font-size:30px;padding:14px 28px;border-radius:40px">Swipe before you buy</div></div>
<div style="position:absolute;left:70px;right:70px;top:650px;height:510px;display:flex;gap:20px">
{''.join(f'<div style="flex:1;background:{bg};border-radius:36px;display:flex;align-items:center;justify-content:center;padding:30px 16px">{img(s,h)}</div>' for s,h,bg in [(BI,400,PINK),(TT,290,GREY),(LO,400,MINT)])}</div>"""
s2=tip(1,"Simple beats clever",
 "UNICEF UK: there's no evidence one teat is better than another. A simple bottle that's easy to clean is probably best. Ridges and fancy shapes can be hard to get clean.",
 PINK,img(LO,440),NP("Easy to clean > clever shape"))
s3=tip(2,"“Anti-colic” is a maybe",
 "The NHS says you could try an anti-colic bottle to see if it helps. It's not a promise. Holding your baby upright while feeding also helps them swallow less air.",
 GREY,img(TT,400),MP("Try one before you buy six"))
s4=tip(3,"Start with the slowest teat",
 "The NHS suggests slower flow teats for newborns, so milk doesn't come too fast. Move up only if your baby seems to struggle. Let your baby lead, not the age on the box.",
 MINT,img(TE,330)+BIG("Slow","flow first",130),PP("Led by your baby"))
s5=tip(4,"How you hold it matters more",
 "Hold your baby fairly upright. Keep the bottle almost flat. Touch the teat to their top lip and let them draw it in. Pause often, and never push them to finish.",
 PINK,img(BI,440),NP("Never prop the bottle"))
s6=tip(5,"“BPA-free” is the law, not a bonus",
 "BPA has been banned in baby bottles since 2011, and the ban is part of UK law. Every bottle sold here should be BPA-free. Don't pay extra for the label.",
 GREY,BIG("BPA-free","required since 2011",140),MP("Compare on what really differs"))
s7=tip(6,"Buy two, not a full set",
 "The NHS suggests trying both rounded and natural-shaped teats. You'll sterilise bottles until at least 12 months, so check they fit your steriliser and breast pump too.",
 MINT,img(BI,400)+img(LO,380),PP("Test first, then stock up"))
s8=tip(7,"Plan the exit at 6 months",
 "The NHS suggests a cup from around 6 months. An open or free-flow cup (no valve) helps babies learn to sip. From 1 year, bottles should be phased out. Skip big “toddler” bottle sets.",
 PINK,BIG("6 m","cup time",170),NP("Bottles out after 1 year"))
s9=f"""{deco}
<div style="position:absolute;left:70px;right:70px;top:70px;height:480px;border-radius:44px;background:{MINT};display:flex;align-items:center;justify-content:center;gap:40px">{img(BI,330)}{img(TT,240)}{img(LO,330)}</div>
<div style="position:absolute;left:90px;right:90px;top:610px"><div class="h" style="font-size:84px">Found your bottle? Compare prices first</div>
<div style="font-size:38px;font-weight:500;margin-top:20px">Compare baby bottles and feeding gear from UK shops in one place.</div>
<div style="margin-top:34px;display:flex;align-items:center;gap:16px"><div class="h" style="font-size:46px;background:{PINK};padding:22px 32px;border-radius:24px">babysorted.com/links</div>
<div style="background:{NAVY};color:#fff;font-weight:800;font-size:32px;padding:22px 26px;border-radius:24px;white-space:nowrap">Link in bio ↑</div></div>
<div style="margin-top:22px;font-size:32px;font-weight:700;opacity:.55">Save this post for later</div></div>"""
bodies=[cover,s2,s3,s4,s5,s6,s7,s8,s9]; n=len(bodies)
rows=[("Simple beats clever","Easy to clean matters more than shape.",PINK),("“Anti-colic” is a maybe","Worth a try, not a promise.",GREY),("Start with the slowest teat","Move up only if baby struggles.",MINT),
      ("How you hold it matters","Upright baby, bottle almost flat, pauses.",PINK),("BPA-free is the law","Banned in baby bottles since 2011.",GREY),("Buy two, not a full set","Check they fit your steriliser and pump.",MINT),("Cup from around 6 months","Phase out bottles after 1 year.",PINK)]
rr="".join(f'''<div style="display:flex;gap:20px;align-items:center;padding:12px 0;border-top:{"0" if i==0 else "2px solid #F1F2F5"}"><div style="flex:none;width:54px;height:54px;border-radius:50%;background:{c};display:flex;align-items:center;justify-content:center;font-weight:800;font-size:28px">{i+1}</div>
<div><div class="h" style="font-size:33px">{t}</div><div style="font-size:25px;font-weight:500;opacity:.8;margin-top:3px">{d}</div></div></div>''' for i,(t,d,c) in enumerate(rows))
pin=f"""{star(900,60,34,ROSE)}
<div style="position:absolute;left:60px;right:60px;top:70px"><div class="tags"><span class="tag t1" style="font-size:24px">Tips</span><span class="tag t2" style="font-size:24px">Nursing &amp; Feeding</span></div>
<div class="h" style="font-size:76px;margin-top:20px">How to choose baby bottles</div></div>
<div style="position:absolute;left:60px;right:60px;top:330px;height:330px;display:flex;gap:16px">
{''.join(f'<div style="flex:1;background:{bg};border-radius:30px;display:flex;align-items:center;justify-content:center;padding:20px 10px">{img(s,h)}</div>' for s,h,bg in [(BI,270,PINK),(TT,200,GREY),(LO,270,MINT)])}</div>
<div style="position:absolute;left:60px;right:60px;top:690px">{rr}</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:110px;background:{NAVY};color:#fff;display:flex;justify-content:space-between;align-items:center;padding:0 60px"><div class="brand" style="font-size:34px">BabySorted</div><div style="font-weight:700;font-size:26px">Compare bottle prices at babysorted.com</div></div>"""
with sync_playwright() as p:
    br=p.chromium.launch(); pg=br.new_page(viewport=dict(width=1080,height=1350))
    for i,bd in enumerate(bodies):
        pg.set_content(f"<html><head><style>{CSS}</style></head><body>{bd}{foot(i,n)}</body></html>"); pg.wait_for_timeout(250)
        pg.screenshot(path=f"{OUT}/slide_{i+1}.png")
    pg2=br.new_page(viewport=dict(width=1000,height=1500),device_scale_factor=2)
    pg2.set_content(f"<html><head><style>{CSS.replace('width:1080px;height:1350px','width:1000px;height:1500px')}</style></head><body>{pin}</body></html>"); pg2.wait_for_timeout(250)
    pg2.screenshot(path=f"{OUT}/pin.png"); br.close()
from PIL import Image
W=Image.new('RGB',(1500,1250),'#ddd')
for k in range(n): W.paste(Image.open(f'{OUT}/slide_{k+1}.png').resize((288,360)),((k%5)*300,(k//5)*380))
W.paste(Image.open(f'{OUT}/pin.png').resize((300,450)),(1200,780)); W.save(f'{OUT}/preview.png')
