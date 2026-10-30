# Pink "close-up cover + mistake cards" layout: pink bg, cover = product close-up bleeding off the top with white card;
# inner = whole product centred above a white card with "MISTAKE n OF 7" and a navy/mint fact pill.
# Used for: 7 nursery mistakes to avoid (30 Oct 2026). Run from folder with cut/cot.png, cut/dresser.png; writes ./out_nursery
from playwright.sync_api import sync_playwright
import base64, os
PINK="#F1D3DF"; NAVY="#051F45"; ROSE="#E6B6C9"; MINT="#DDF5E3"
b=lambda f: base64.b64encode(open(f,"rb").read()).decode()
COT=b("cut/cot.png"); DR=b("cut/dresser.png")
OUT="out_nursery"; os.makedirs(OUT,exist_ok=True)
SH="filter:drop-shadow(0 24px 24px rgba(5,31,69,.18))"
def star(x,y,s,c,o=1): return f'<svg style="position:absolute;left:{x}px;top:{y}px;opacity:{o}" width="{s}" height="{s}" viewBox="0 0 20 20"><path d="M10 0l2.6 7.4L20 10l-7.4 2.6L10 20l-2.6-7.4L0 10l7.4-2.6z" fill="{c}"/></svg>'
CSS=f"""*{{margin:0;padding:0;box-sizing:border-box}} body{{width:1080px;height:1350px;background:{PINK};font-family:Inter;color:{NAVY};position:relative;overflow:hidden}}
.h{{font-weight:800;letter-spacing:-0.035em;line-height:1.04}}
.tags{{display:flex;gap:14px}} .tag{{font-weight:700;font-size:28px;padding:9px 22px;border-radius:30px}}
.t1{{background:{MINT}}} .t2{{background:#fff;box-shadow:inset 0 0 0 3px {NAVY}}}
.card{{position:absolute;left:50px;right:50px;bottom:130px;background:#fff;border-radius:44px;padding:46px 54px;box-shadow:0 20px 40px rgba(5,31,69,.12)}}
.kick{{font-weight:800;font-size:28px;letter-spacing:.06em;color:#B5476E}}
.body{{font-size:37px;font-weight:500;line-height:1.4;margin-top:18px}}
.stage{{position:absolute;left:0;right:0;top:0;height:600px;padding:80px 70px 40px;display:flex;align-items:center;justify-content:center;gap:44px}}
.stage img{{max-height:100%;max-width:60%;object-fit:contain;{SH}}}
.pill{{display:inline-block;font-weight:800;font-size:34px;padding:16px 28px;border-radius:30px;white-space:nowrap}}
.foot{{position:absolute;left:70px;right:70px;bottom:52px;display:flex;justify-content:space-between;align-items:center}}
.brand{{font-weight:800;font-size:36px;letter-spacing:-0.03em}}"""
def foot(i,n):
    d="".join(f'<div style="width:{40 if j==i else 14}px;height:14px;border-radius:7px;background:{NAVY};opacity:{1 if j==i else .25}"></div>' for j in range(n))
    return f'<div class="foot"><div class="brand">BabySorted</div><div style="display:flex;gap:12px">{d}</div></div>'
im=lambda s,h: f'<img src="data:image/png;base64,{s}" style="height:{h}px">'
deco=star(70,70,40,"#fff")+star(960,120,30,"#fff")+star(120,520,22,NAVY,.2)
def pills(*ps): return '<div style="display:flex;flex-direction:column;align-items:flex-start;gap:18px">'+"".join(ps)+'</div>'
P=lambda t,bg=NAVY,c="#fff",fs=34: f'<span class="pill" style="background:{bg};color:{c};font-size:{fs}px">{t}</span>'
def mis(k,title,body,vis):
    return deco+f'<div class="stage">{vis}</div><div class="card"><div class="kick">MISTAKE {k} OF 7</div><div class="h" style="font-size:66px;margin-top:12px">{title}</div><div class="body">{body}</div></div>'
cover=star(60,60,44,"#fff")+star(980,90,30,"#fff")+f'''<img src="data:image/png;base64,{COT}" style="position:absolute;left:-110px;top:-230px;width:1300px;{SH}">
<div class="card" style="bottom:130px"><div class="tags"><span class="tag t1">Tips</span><span class="tag t2">Kids Furniture</span></div>
<div class="h" style="font-size:84px;margin-top:24px">7 nursery mistakes to avoid</div>
<div style="font-size:38px;font-weight:600;opacity:.75;margin-top:16px">Pretty is nice. Practical is better at 3am.</div>
<div style="margin-top:26px;display:inline-block;background:{NAVY};color:#fff;font-weight:700;font-size:30px;padding:14px 28px;border-radius:40px">Swipe before you buy</div></div>'''
s2=deco+f'''<div class="stage"><div style="text-align:center"><div class="h" style="font-size:210px">6</div><div class="h" style="font-size:64px;margin-top:-6px">months</div>
<div class="pill" style="background:#fff;margin-top:22px">in your room, day and night</div></div></div>
<div class="card"><div class="kick" style="color:{NAVY};opacity:.5">BEFORE YOU START</div><div class="h" style="font-size:64px;margin-top:12px">No rush to finish the nursery</div>
<div class="body">The Lullaby Trust advises your baby sleeps in the same room as you for at least the first 6 months, for every sleep. Spend on the things you'll use from day one. The rest can wait.</div></div>'''
s3=mis(1,"The cot under the window",
 "Looped blind cords can strangle. Most of these deaths happen in bedrooms, at around 2 years old, not in the newborn months. Keep the cot away from the window. Choose cordless blinds or fit a cleat at least 1.5 m high.",
 im(COT,480)+pills(P("Cot away from cords"),P("Cleat 1.5 m+ high",MINT,NAVY)))
s4=mis(2,"The cot next to the radiator",
 "Babies can't cool down well. The ideal room is 16–20°C. Keep the cot away from radiators and direct sun. Put a room thermometer near the cot, not in a sunny spot.",
 im(COT,480)+f'<div style="text-align:center"><div class="h" style="font-size:104px;white-space:nowrap">16–20°C</div><div class="pill" style="background:{NAVY};color:#fff;margin-top:14px">the ideal room</div></div>')
s5=mis(3,"A shelf or frame above the cot",
 "Which? advises against a cot under shelves, frames or mirrors. They can fall. RoSPA adds: nothing that dangles in or near the cot. Keep cables out of reach too.",
 im(COT,480)+pills(P("Clear wall above"),P("No dangling cords",MINT,NAVY)))
s6=mis(4,"Drawers not fixed to the wall",
 "Toddlers climb open drawers like stairs. RoSPA says secure drawers, bookshelves and wardrobes to the wall. And keep furniture away from windows, so it can't become a step up.",
 im(DR,500)+pills(P("Anchor it"),P("Not under a window",MINT,NAVY)))
s7=mis(5,"Nappy sacks on the changing unit",
 "RoSPA links at least 17 baby deaths to nappy sacks. Babies grab things and put them to their mouths. Never leave them in or near the cot, pram or changing area. Store them high, out of reach.",
 im(DR,500)+f'<div style="text-align:center"><div class="h" style="font-size:150px">17</div><div class="pill" style="background:{NAVY};color:#fff;margin-top:10px">baby deaths linked</div></div>')
s8=mis(6,"Only changing on a high table",
 "The NHS says change nappies on a mat on the floor. If you use a changing unit, stay with your baby every second. Have nappies, wipes and clothes in reach before you start.",
 im(DR,500)+pills(P("Floor mat = safest"),P("Never step away",MINT,NAVY)))
s9=mis(7,"Sanding old furniture while pregnant",
 "Lead paint was common before the 1970s. Sanding it makes dust that is harmful. UKHSA advises pregnant women to avoid this kind of work, and children should stay away until all the dust is gone.",
 im(COT,470)+pills(P("Old paint?"),P("Don't sand it yourself",MINT,NAVY)))
s10=deco+f'''<div class="stage">{im(COT,360)}{im(DR,330)}</div><div class="card"><div class="h" style="font-size:70px">Planning the nursery? Compare prices first</div>
<div class="body">Compare cots, cot beds and dressers from UK shops in one place.</div>
<div style="margin-top:30px;display:flex;align-items:center;gap:16px"><div class="h" style="font-size:44px;background:{PINK};padding:20px 30px;border-radius:24px">babysorted.com/links</div>
<div style="background:{NAVY};color:#fff;font-weight:800;font-size:30px;padding:20px 24px;border-radius:24px;white-space:nowrap">Link in bio ↑</div></div>
<div style="margin-top:20px;font-size:30px;font-weight:700;opacity:.55">Save this post for later</div></div>'''
bodies=[cover,s2,s3,s4,s5,s6,s7,s8,s9,s10]; n=len(bodies)
rows=[("Cot under the window","Blind cords. Cordless blinds or a cleat 1.5 m+ high."),("Cot by the radiator","Aim for 16–20°C. Use a room thermometer."),
      ("Shelf or frame above the cot","Clear wall. Nothing dangling."),("Drawers not fixed to the wall","Anchor them. Keep them away from windows."),
      ("Nappy sacks in reach","Never near the cot, pram or changing area."),("Only a high changing table","A mat on the floor is safest."),("Sanding old paint when pregnant","Pre-1970s paint can contain lead.")]
rr="".join(f'''<div style="display:flex;gap:20px;align-items:center;padding:11px 0;border-top:{"0" if i==0 else "2px solid #F3E4EA"}"><div style="flex:none;width:52px;height:52px;border-radius:50%;background:{PINK};display:flex;align-items:center;justify-content:center;font-weight:800;font-size:27px">{i+1}</div>
<div><div class="h" style="font-size:31px">{t}</div><div style="font-size:23px;font-weight:500;opacity:.85;margin-top:3px">{d}</div></div></div>''' for i,(t,d) in enumerate(rows))
pin=f'''{star(60,50,36,"#fff")}{star(900,90,28,"#fff")}<img src="data:image/png;base64,{COT}" style="position:absolute;left:150px;top:40px;width:700px;{SH}">
<div style="position:absolute;left:44px;right:44px;bottom:44px;background:#fff;border-radius:44px;padding:40px 46px;box-shadow:0 20px 40px rgba(5,31,69,.12)">
<div class="tags"><span class="tag t1" style="font-size:22px">Tips</span><span class="tag t2" style="font-size:22px">Kids Furniture</span></div>
<div class="h" style="font-size:62px;margin-top:16px">7 nursery mistakes to avoid</div>
<div style="margin-top:10px">{rr}</div>
<div style="margin-top:14px;background:{NAVY};color:#fff;border-radius:22px;padding:18px 24px;font-size:24px;font-weight:600;line-height:1.35"><b>No rush:</b> for the first 6 months your baby sleeps in your room, day and night.</div>
<div style="margin-top:16px;display:flex;justify-content:space-between;align-items:center"><div class="brand" style="font-size:30px">BabySorted</div><div style="font-weight:700;font-size:24px">Compare nursery prices at babysorted.com</div></div></div>'''
with sync_playwright() as p:
    br=p.chromium.launch(); pg=br.new_page(viewport=dict(width=1080,height=1350))
    for i,bd in enumerate(bodies):
        pg.set_content(f"<html><head><style>{CSS}</style></head><body>{bd}{foot(i,n)}</body></html>"); pg.wait_for_timeout(250)
        pg.evaluate("""()=>{const c=document.querySelector('.card');document.querySelectorAll('.stage').forEach(s=>{s.style.height=c.getBoundingClientRect().top+'px'})}""")
        pg.screenshot(path=f"{OUT}/slide_{i+1}.png")
    pg2=br.new_page(viewport=dict(width=1000,height=1500),device_scale_factor=2)
    pg2.set_content(f"<html><head><style>{CSS.replace('width:1080px;height:1350px','width:1000px;height:1500px')}</style></head><body>{pin}</body></html>"); pg2.wait_for_timeout(250)
    pg2.screenshot(path=f"{OUT}/pin.png"); br.close()
from PIL import Image
W=Image.new('RGB',(1500,1250),'white')
for k in range(n): W.paste(Image.open(f'{OUT}/slide_{k+1}.png').resize((288,360)),((k%5)*300,(k//5)*380))
W.paste(Image.open(f'{OUT}/pin.png').resize((300,450)),(1200,780)); W.save(f'{OUT}/preview.png')
