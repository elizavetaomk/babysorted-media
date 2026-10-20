from playwright.sync_api import sync_playwright
import base64
PINK="#F1D3DF"; NAVY="#051F45"; ROSE="#E6B6C9"; MINT="#DDF5E3"; GREY="#EEF0F3"
b=lambda f: base64.b64encode(open(f,"rb").read()).decode()
PRAM=b("carrycot_2x.png"); PUSH=b("aer_2x.png"); SEATF=b("seatframe_2x.png"); CAR=b("carseat_2x.png")
def star(x,y,s,c,o=1): return f'<svg style="position:absolute;left:{x}px;top:{y}px;opacity:{o}" width="{s}" height="{s}" viewBox="0 0 20 20"><path d="M10 0l2.6 7.4L20 10l-7.4 2.6L10 20l-2.6-7.4L0 10l7.4-2.6z" fill="{c}"/></svg>'
CSS=f"""*{{margin:0;padding:0;box-sizing:border-box}} body{{width:1080px;height:1350px;background:#fff;font-family:Inter;color:{NAVY};position:relative;overflow:hidden}}
.h{{font-weight:800;letter-spacing:-0.035em;line-height:1.04}}
.tags{{display:flex;gap:14px}} .tag{{font-weight:700;font-size:28px;padding:9px 22px;border-radius:30px}}
.t1{{background:{MINT}}} .t2{{background:#fff;box-shadow:inset 0 0 0 3px {NAVY}}}
.panel{{position:absolute;left:70px;right:70px;top:70px;height:560px;border-radius:44px;display:flex;align-items:center;justify-content:center;gap:30px}}
.panel img{{max-height:470px;filter:drop-shadow(0 20px 20px rgba(5,31,69,.16))}}
.kick{{font-weight:800;font-size:28px;letter-spacing:.06em;opacity:.5}}
.foot{{position:absolute;left:80px;right:80px;bottom:56px;display:flex;justify-content:space-between;align-items:center}}
.brand{{font-weight:800;font-size:36px;letter-spacing:-0.03em}}"""
def foot(i,n):
    d="".join(f'<div style="width:{40 if j==i else 14}px;height:14px;border-radius:7px;background:{NAVY};opacity:{1 if j==i else .2}"></div>' for j in range(n))
    return f'<div class="foot"><div class="brand">BabySorted</div><div style="display:flex;gap:12px">{d}</div></div>'
def ts(h,cw=0.47):
    return f'<div style="position:relative;height:{h}px;display:inline-block"><img src="data:image/png;base64,{SEATF}" style="height:{h}px;filter:drop-shadow(0 14px 14px rgba(5,31,69,.15))"><img src="data:image/png;base64,{CAR}" style="position:absolute;right:-{int(h*0.32)}px;bottom:0;height:{int(h*cw)}px;filter:drop-shadow(0 10px 10px rgba(5,31,69,.18))"></div>'
img=lambda s,h,extra="": f'<img src="data:image/png;base64,{s}" style="height:{h}px;{extra}">'
def row(lab,txt,col): return f'<div style="display:flex;gap:24px;padding:20px 0;border-top:3px solid #F1F2F5"><div style="flex:none;width:190px;font-weight:800;font-size:28px;color:{col};padding-top:5px">{lab}</div><div style="font-size:36px;font-weight:500;line-height:1.35">{txt}</div></div>'
def typ(n,name,tagline,bg,pics,frm,good,watch):
    return f"""<div class="panel" style="background:{bg}">{pics}</div>
<div style="position:absolute;left:70px;top:90px;font-weight:800;font-size:28px;background:#fff;padding:8px 18px;border-radius:20px">{n} of 3</div>
<div style="position:absolute;left:90px;right:90px;top:665px"><div style="display:flex;align-items:baseline;gap:20px"><div class="h" style="font-size:88px">{name}</div>
<div style="font-weight:800;font-size:28px;background:{NAVY};color:#fff;padding:8px 18px;border-radius:20px;white-space:nowrap">{frm}</div></div>
<div style="font-size:38px;font-weight:600;opacity:.75;margin-top:10px">{tagline}</div>
<div style="margin-top:22px">{row("Good",good,"#2E7D5B")}{row("Watch out",watch,"#B5476E")}</div></div>"""
cover=f"""{star(950,80,40,ROSE)}{star(80,600,26,ROSE)}
<div style="position:absolute;left:90px;right:90px;top:100px"><div class="tags"><span class="tag t1">Comparison</span><span class="tag t2">Pushchairs</span></div>
<div class="h" style="font-size:96px;margin-top:30px">Pram, pushchair or travel system?</div>
<div style="font-size:38px;font-weight:600;opacity:.7;margin-top:18px">What's the difference, and which one do you need?</div></div>
<div style="position:absolute;left:70px;right:70px;top:640px;height:500px;display:flex;gap:20px">
{''.join(f'<div style="flex:1;background:{bg};border-radius:36px;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;padding:20px 10px 26px"><div style="flex:1;display:flex;align-items:center">{img(s,h,"max-width:280px;object-fit:contain;filter:drop-shadow(0 14px 14px rgba(5,31,69,.15))") if s else '<div style="margin-left:-77px">'+ts(240)+'</div>'}</div><div class="h" style="font-size:34px;margin-top:10px;text-align:center">{t}</div></div>' for t,s,h,bg in [("Pram",PRAM,330,PINK),("Pushchair",PUSH,340,GREY),("Travel system",None,0,MINT)])}</div>
<div style="position:absolute;left:90px;top:1170px;font-weight:700;font-size:30px;opacity:.6">Swipe to compare</div>"""
s2=typ(1,"Pram","Baby lies flat in a carrycot, facing you.",PINK,img(PRAM,470),"From birth","Lying flat, which newborns need. You can see your baby.","Big and heavy. Babies outgrow the carrycot in months.")
s3=typ(2,"Pushchair","A seat for babies who can sit up.",GREY,img(PUSH,470),"Usually 6 months+","Lighter, folds small and is easy on buses.","For a newborn, the seat must lie fully flat. Check this.")
s4=typ(3,"Travel system","A pushchair plus a car seat that clicks onto the frame.",MINT,img(SEATF,430)+'<div class="h" style="font-size:80px">+</div>'+img(CAR,250),"From birth","Move a sleeping baby from car to frame without waking them.","Car seats are for travel, not long naps. Take your baby out when you arrive.")
def boxrow(t,d,bg): return f'<div style="display:flex;gap:26px;align-items:center;background:{bg};border-radius:30px;padding:34px 36px;margin-top:20px"><div class="h" style="flex:none;width:220px;font-size:60px">{t}</div><div style="font-size:36px;font-weight:600;line-height:1.35">{d}</div></div>'
s5=f"""{star(950,90,36,ROSE)}<div style="position:absolute;left:90px;right:90px;top:0;bottom:130px;display:flex;flex-direction:column;justify-content:center"><div class="kick">BUYING A BUNDLE?</div>
<div class="h" style="font-size:84px;margin-top:16px">2-in-1, 3-in-1, 4-in-1: what's in the box</div>
<div style="margin-top:36px">{boxrow("2-in-1","Frame, seat and carrycot",PINK)}{boxrow("3-in-1","The same, plus a baby car seat",GREY)}{boxrow("4-in-1","The same, plus an ISOFIX base for the car",MINT)}</div>
<div style="margin-top:34px;font-size:36px;font-weight:600;line-height:1.4">Brands use these names differently. Always count the pieces, not the number in the name.</div></div>"""
def ans(q,a,bg): return f'<div style="background:{bg};border-radius:30px;padding:36px 38px;margin-top:22px"><div style="font-size:34px;font-weight:700;opacity:.7">{q}</div><div class="h" style="font-size:56px;margin-top:8px">{a}</div></div>'
s6=f"""{star(950,90,36,ROSE)}<div style="position:absolute;left:90px;right:90px;top:0;bottom:130px;display:flex;flex-direction:column;justify-content:center"><div class="kick">QUICK ANSWER</div>
<div class="h" style="font-size:88px;margin-top:16px">Which one is right for you?</div>
<div style="margin-top:30px">{ans("You drive most days","A travel system",MINT)}{ans("No car, lots of buses and stairs","A pram that converts to a seat",PINK)}{ans("Small budget, one buy","A pushchair that lies flat from birth",GREY)}</div></div>"""
s7=f"""{star(950,90,40,ROSE)}{star(80,520,26,ROSE)}
<div style="position:absolute;left:70px;right:70px;top:70px;height:460px;border-radius:44px;background:{PINK};display:flex;align-items:center;justify-content:center;gap:24px">{img(PRAM,330)}{img(PUSH,340)}<div style="margin-right:90px">{ts(320)}</div></div>
<div style="position:absolute;left:90px;right:90px;top:590px"><div class="h" style="font-size:84px">Know what you need? Compare prices first</div>
<div style="font-size:38px;font-weight:500;margin-top:20px">We track over 4,000 pushchair listings from UK shops, updated every night.</div>
<div style="margin-top:34px;display:flex;align-items:center;gap:16px"><div class="h" style="font-size:46px;background:{PINK};padding:22px 32px;border-radius:24px">babysorted.com/links</div>
<div style="background:{NAVY};color:#fff;font-weight:800;font-size:32px;padding:22px 26px;border-radius:24px;white-space:nowrap">Link in bio ↑</div></div>
<div style="margin-top:22px;font-size:32px;font-weight:700;opacity:.55">Save this post for later</div></div>"""
bodies=[cover,s2,s3,s4,s5,s6,s7]; n=len(bodies)
col=lambda t,s,h,bg,frm,g,w: f'''<div style="flex:1;background:{bg};border-radius:28px;padding:24px 20px 34px"><div style="height:300px;display:flex;align-items:center;justify-content:center">{img(s,h,"max-width:100%;object-fit:contain") if s else '<div style="margin-left:-90px">'+ts(240)+'</div>'}</div>
<div class="h" style="font-size:38px;margin-top:10px">{t}</div><div style="margin-top:8px;display:inline-block;font-weight:800;font-size:21px;background:{NAVY};color:#fff;padding:6px 12px;border-radius:14px">{frm}</div>
<div style="font-size:20px;font-weight:800;opacity:.55;margin-top:20px">GOOD</div><div style="font-size:27px;font-weight:600;line-height:1.3;margin-top:4px">{g}</div>
<div style="font-size:20px;font-weight:800;opacity:.55;margin-top:16px">WATCH OUT</div><div style="font-size:27px;font-weight:600;line-height:1.3;margin-top:4px">{w}</div></div>'''
pin=f"""{star(900,60,34,ROSE)}
<div style="position:absolute;left:60px;right:60px;top:80px"><div class="tags"><span class="tag t1" style="font-size:24px">Comparison</span><span class="tag t2" style="font-size:24px">Pushchairs</span></div>
<div class="h" style="font-size:80px;margin-top:22px">Pram, pushchair or travel system?</div>
<div style="font-size:32px;font-weight:600;opacity:.7;margin-top:12px">What's the difference, and which one you need</div>
<div style="display:flex;gap:16px;margin-top:40px">{col("Pram",PRAM,290,PINK,"From birth","Baby lies flat, facing you.","Outgrown in months.")}{col("Pushchair",PUSH,295,GREY,"Usually 6m+","Light, folds small.","Newborns need a fully flat seat.")}{col("Travel system",None,0,MINT,"From birth","Car seat clicks onto the frame.","Car seats are for travel, not naps.")}</div>
<div style="margin-top:26px;background:{NAVY};color:#fff;border-radius:24px;padding:24px 28px"><div style="font-weight:800;font-size:21px;opacity:.6;letter-spacing:.06em">BUYING A BUNDLE?</div>
<div style="font-size:28px;font-weight:600;margin-top:6px;line-height:1.35">2-in-1, 3-in-1 and 4-in-1 mean different things at different brands. Count the pieces in the box.</div></div></div>
<div style="position:absolute;left:60px;right:60px;bottom:50px;display:flex;justify-content:space-between;align-items:center"><div class="brand" style="font-size:34px">BabySorted</div><div style="font-weight:700;font-size:28px">Compare prices at babysorted.com</div></div>"""
with sync_playwright() as p:
    br=p.chromium.launch(); pg=br.new_page(viewport=dict(width=1080,height=1350))
    for i,bd in enumerate(bodies):
        pg.set_content(f"<html><head><style>{CSS}</style></head><body>{bd}{foot(i,n)}</body></html>"); pg.wait_for_timeout(200)
        pg.screenshot(path=f"/mnt/user-data/outputs/prams/slide_{i+1}.png")
    pg2=br.new_page(viewport=dict(width=1000,height=1500),device_scale_factor=2)
    pg2.set_content(f"<html><head><style>{CSS.replace('width:1080px;height:1350px','width:1000px;height:1500px')}</style></head><body>{pin}</body></html>"); pg2.wait_for_timeout(200)
    pg2.screenshot(path="/mnt/user-data/outputs/prams/pinterest_pram_pushchair_travel_system.png"); br.close()
from PIL import Image
W=Image.new('RGB',(1440,900),'white')
for k in range(7): W.paste(Image.open(f'/mnt/user-data/outputs/prams/slide_{k+1}.png').resize((288,360)),((k%4)*360,(k//4)*450))
W.paste(Image.open('/mnt/user-data/outputs/prams/pinterest_pram_pushchair_travel_system.png').resize((300,450)),(1110,450))
W.save('/home/claude/preview.png')
