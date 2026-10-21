# Versus layout: navy background, two products on pink/white halves with mint "VS" circle.
# Used for: Infant carrier vs extended rear-facing seat (22 Oct 2026).
# Run from a folder that holds carrier_cut.png and erf_cut.png; writes to ./out
from playwright.sync_api import sync_playwright
import base64, os
PINK="#F1D3DF"; NAVY="#051F45"; ROSE="#E6B6C9"; MINT="#DDF5E3"
b=lambda f: base64.b64encode(open(f,"rb").read()).decode()
A=b("carrier_cut.png"); B=b("erf_cut.png")
os.makedirs("out",exist_ok=True)
def star(x,y,s,c,o=1): return f'<svg style="position:absolute;left:{x}px;top:{y}px;opacity:{o}" width="{s}" height="{s}" viewBox="0 0 20 20"><path d="M10 0l2.6 7.4L20 10l-7.4 2.6L10 20l-2.6-7.4L0 10l7.4-2.6z" fill="{c}"/></svg>'
CSS=f"""*{{margin:0;padding:0;box-sizing:border-box}} body{{width:1080px;height:1350px;background:{NAVY};font-family:Inter;color:{NAVY};position:relative;overflow:hidden}}
.h{{font-weight:800;letter-spacing:-0.035em;line-height:1.04}}
.tags{{display:flex;gap:14px}} .tag{{font-weight:700;font-size:28px;padding:9px 22px;border-radius:30px}}
.t1{{background:{MINT};color:{NAVY}}} .t2{{color:#fff;box-shadow:inset 0 0 0 3px #fff}}
.card{{position:absolute;left:60px;right:60px;bottom:140px;background:#fff;border-radius:44px;padding:44px 52px}}
.kick{{font-weight:800;font-size:28px;letter-spacing:.06em;opacity:.5}}
.body{{font-size:37px;font-weight:500;line-height:1.4;margin-top:18px}}
.stage{{position:absolute;left:60px;right:60px;top:70px;display:flex;align-items:center;justify-content:center}}
.panel{{border-radius:44px;width:100%;height:100%;display:flex;align-items:center;justify-content:center;gap:40px;padding:36px}}
.panel img{{max-height:100%;max-width:100%;object-fit:contain;filter:drop-shadow(0 20px 20px rgba(5,31,69,.18))}}
.foot{{position:absolute;left:80px;right:80px;bottom:56px;display:flex;justify-content:space-between;align-items:center;color:#fff}}
.brand{{font-weight:800;font-size:36px;letter-spacing:-0.03em}}
.pill{{display:inline-block;font-weight:800;font-size:28px;padding:10px 20px;border-radius:22px}}"""
def foot(i,n):
    d="".join(f'<div style="width:{40 if j==i else 14}px;height:14px;border-radius:7px;background:#fff;opacity:{1 if j==i else .3}"></div>' for j in range(n))
    return f'<div class="foot"><div class="brand">BabySorted</div><div style="display:flex;gap:12px">{d}</div></div>'
im=lambda s,h=None: f'<img src="data:image/png;base64,{s}" style="{f"height:{h}px" if h else ""}">'
deco=star(970,70,34,PINK)+star(40,40,26,"#fff",.5)
def stage(inner,bg): return f'<div class="stage" id="st"><div class="panel" style="background:{bg}">{inner}</div></div>'
def row(lab,txt,col): return f'<div style="display:flex;gap:22px;padding:16px 0;border-top:3px solid #F1F2F5"><div style="flex:none;width:180px;font-weight:800;font-size:27px;color:{col};padding-top:6px">{lab}</div><div style="font-size:34px;font-weight:500;line-height:1.35">{txt}</div></div>'
def seat(n,name,pill,good,watch,pic,bg):
    return deco+stage(im(pic),bg)+f'''<div style="position:absolute;left:90px;top:95px;font-weight:800;font-size:27px;background:{NAVY};color:#fff;padding:8px 18px;border-radius:20px">Seat {n} of 2</div>
<div class="card"><div class="h" style="font-size:72px">{name}</div><div class="pill" style="background:{MINT};margin-top:16px">{pill}</div>
<div style="margin-top:22px">{row("Good",good,"#2E7D5B")}{row("Watch out",watch,"#B5476E")}</div></div>'''
def tip(k,title,body,pic,bg):
    return deco+stage(pic,bg)+f'<div class="card"><div class="kick">{k}</div><div class="h" style="font-size:64px;margin-top:12px">{title}</div><div class="body">{body}</div></div>'
BIG=lambda big,small,c=NAVY: f'<div style="text-align:center"><div class="h" style="font-size:170px;color:{c};white-space:nowrap">{big}</div><div class="pill" style="background:{NAVY};color:#fff;font-size:40px;margin-top:18px;padding:14px 30px;border-radius:40px">{small}</div></div>'
VS=f'<div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:150px;height:150px;border-radius:50%;background:{MINT};box-shadow:0 0 0 12px {NAVY};display:flex;align-items:center;justify-content:center"><div class="h" style="font-size:58px">VS</div></div>'
def halves(top,h,lab=True,ih=380):
    L=f'<div style="flex:1;background:{PINK};display:flex;flex-direction:column;align-items:center;justify-content:center;padding:30px 30px 34px">{im(A,ih)}{"<div class=h style=font-size:36px;margin-top:22px;text-align:center>Infant carrier</div>" if lab else ""}</div>'
    R=f'<div style="flex:1;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:30px 30px 34px">{im(B,ih)}{"<div class=h style=font-size:36px;margin-top:22px;text-align:center>Extended rear-facing</div>" if lab else ""}</div>'
    return f'<div style="position:absolute;left:60px;right:60px;top:{top}px;height:{h}px;border-radius:44px;overflow:hidden;display:flex">{L}{R}</div><div style="position:absolute;left:60px;right:60px;top:{top}px;height:{h}px">{VS}</div>'
cover=deco+f'''<div style="position:absolute;left:90px;right:90px;top:100px;color:#fff"><div class="tags"><span class="tag t1">Comparison</span><span class="tag t2">Car Seats</span></div>
<div class="h" style="font-size:84px;margin-top:28px">Infant carrier or extended rear-facing seat?</div>
<div style="font-size:38px;font-weight:600;opacity:.75;margin-top:18px">Which one first? It depends on your car and your plans.</div></div>
{halves(630,530)}<div style="position:absolute;left:90px;top:1185px;font-weight:700;font-size:30px;color:#fff;opacity:.6">Swipe to compare</div>'''
s2=seat(1,"Infant carrier","Birth to about 12–15 months",
 "Lift it out with the handle. Many click onto a pram frame, so a sleeping baby can stay asleep.",
 "Outgrown at around 12–15 months, so you will need a second seat.",A,PINK)
s3=seat(2,"Extended rear-facing","Rear-facing to 18 kg, some to 25 kg",
 "One seat for years. Your child faces backwards for longer.",
 "Big and heavy. It stays in the car and can take leg room from the front seat.",B,"#fff")
s4=tip("WHEN TO MOVE ON","Watch the head, not the birthday",
 "The carrier is outgrown when the top of your baby's head is above the top of the seat, or they pass its weight or height limit.",
 f'<div style="display:flex;align-items:center;gap:50px;height:100%">{im(A,440)}<div style="display:flex;flex-direction:column;align-items:flex-start;gap:18px"><span class="pill" style="background:{MINT}">Head above the shell?</span><span class="pill" style="background:{NAVY};color:#fff">Time for the next seat</span></div></div>',PINK)
s5=tip("TURNING FORWARD","15 months is the minimum, not the goal",
 "i-Size seats must stay rear-facing until at least 15 months. UK safety experts suggest an extended rear-facing seat to keep going for longer.",
 BIG("15 months","the earliest, not the target"),MINT)
s6=tip("NEWBORNS","Under 4 weeks? Keep car trips to 30 minutes",
 "RoSPA warns young babies can have breathing problems sitting curled up in a car seat. On long trips, stop often and take your baby out.",
 BIG("30 min","max for babies under 4 weeks"),"#fff")
s7=tip("CARRIER TRAP","A car seat is not a bed",
 "Arrived? Lift your baby out, even if they are asleep. No naps or feeds in the seat at home. If your baby slumps forward, stop and take them out.",
 f'<div style="display:flex;align-items:center;gap:50px;height:100%">{im(A,440)}<div style="display:flex;flex-direction:column;align-items:flex-start;gap:18px"><span class="pill" style="background:{NAVY};color:#fff">For the car only</span><span class="pill" style="background:{PINK}">Not for sleep at home</span></div></div>',MINT)
s8=tip("FRONT SEAT","Rear-facing in the front? Airbag off",
 "UK rules: switch off the front airbag before you fit any rear-facing seat in the front. This goes for both seat types.",
 f'<div style="display:flex;align-items:center;gap:50px;height:100%">{im(B,440)}<span class="pill" style="background:{NAVY};color:#fff;font-size:40px;padding:16px 28px">Airbag OFF</span></div>',PINK)
def ans(q,a,bg): return f'<div style="background:{bg};border-radius:30px;padding:30px 36px;margin-top:20px"><div style="font-size:32px;font-weight:700;opacity:.7">{q}</div><div class="h" style="font-size:50px;margin-top:8px">{a}</div></div>'
s9=deco+f'''<div style="position:absolute;left:60px;right:60px;top:70px;bottom:140px;background:#fff;border-radius:44px;padding:56px 52px;display:flex;flex-direction:column;justify-content:center">
<div class="kick">QUICK ANSWER</div><div class="h" style="font-size:80px;margin-top:14px">Which one first?</div>
{ans("You will take the seat out of the car a lot","A carrier first, then an ERF seat",PINK)}
{ans("The seat will mostly stay in the car","An ERF seat that fits from 40 cm",MINT)}
{ans("Small car or tall driver","Test the seat in your car first","#EEF0F3")}</div>'''
s10=deco+halves(70,470,False,330)+f'''<div class="card" style="top:590px;bottom:140px"><div class="h" style="font-size:72px">Know which seat you need? Compare prices first</div>
<div class="body">Compare car seat prices from UK shops in one place.</div>
<div style="margin-top:30px;display:flex;align-items:center;gap:16px"><div class="h" style="font-size:44px;background:{PINK};padding:20px 30px;border-radius:24px">babysorted.com/links</div>
<div style="background:{NAVY};color:#fff;font-weight:800;font-size:30px;padding:20px 24px;border-radius:24px;white-space:nowrap">Link in bio ↑</div></div>
<div style="margin-top:20px;font-size:30px;font-weight:700;opacity:.55">Save this post for later</div></div>'''
bodies=[cover,s2,s3,s4,s5,s6,s7,s8,s9,s10]; n=len(bodies)
# Pinterest pin
def col(t,pic,bg,pill,g,w): return f'''<div style="flex:1;background:{bg};border-radius:28px;padding:22px 24px 28px"><div style="height:220px;display:flex;align-items:center;justify-content:center">{im(pic,210)}</div>
<div class="h" style="font-size:36px;margin-top:10px">{t}</div><div class="pill" style="background:{NAVY};color:#fff;font-size:20px;padding:6px 12px;border-radius:14px;margin-top:8px">{pill}</div>
<div style="font-size:19px;font-weight:800;opacity:.55;margin-top:16px">GOOD</div><div style="font-size:25px;font-weight:600;line-height:1.3;margin-top:4px">{g}</div>
<div style="font-size:19px;font-weight:800;opacity:.55;margin-top:14px">WATCH OUT</div><div style="font-size:25px;font-weight:600;line-height:1.3;margin-top:4px">{w}</div></div>'''
rules=[("Move on by head, not age","Outgrown when the head is above the top of the shell."),("15 months is the minimum","i-Size: rear-facing until at least 15 months."),("Newborns: 30 minutes","Under 4 weeks, keep car trips short."),("Not a bed","Take your baby out when you arrive."),("Airbag off","Before fitting a rear-facing seat in the front.")]
rr="".join(f'<div style="display:flex;gap:18px;align-items:center;padding:9px 0;border-top:{"0" if i==0 else "2px solid #EEF0F3"}"><div style="flex:none;width:46px;height:46px;border-radius:50%;background:{MINT};display:flex;align-items:center;justify-content:center;font-weight:800;font-size:24px">{i+1}</div><div><span class="h" style="font-size:28px">{t}.</span> <span style="font-size:24px;font-weight:500">{d}</span></div></div>' for i,(t,d) in enumerate(rules))
pin=f'''{star(900,50,32,PINK)}<div style="position:absolute;left:50px;right:50px;top:56px;bottom:110px;display:flex;flex-direction:column;justify-content:space-between">
<div style="color:#fff"><div class="tags"><span class="tag t1" style="font-size:22px">Comparison</span><span class="tag t2" style="font-size:22px">Car Seats</span></div>
<div class="h" style="font-size:64px;margin-top:18px">Infant carrier or extended rear-facing seat?</div></div>
<div style="display:flex;gap:16px">{col("Infant carrier",A,PINK,"Birth to ~12–15 months","Carry it out, clicks onto many prams.","Outgrown at around 12–15 months.")}{col("Extended rear-facing",B,"#fff","Rear-facing to 18–25 kg","One seat for years, rear-facing longer.","Big, heavy, stays in the car.")}</div>
<div style="background:#fff;border-radius:28px;padding:20px 28px"><div class="kick" style="font-size:20px">5 RULES FOR BOTH</div>{rr}</div></div>'''
pinfoot=f'<div style="position:absolute;left:50px;right:50px;bottom:34px;display:flex;justify-content:space-between;align-items:center;color:#fff"><div class="brand" style="font-size:30px">BabySorted</div><div style="font-weight:700;font-size:24px">Compare car seat prices from UK shops at babysorted.com</div></div>'
with sync_playwright() as p:
    br=p.chromium.launch(); pg=br.new_page(viewport=dict(width=1080,height=1350))
    for i,bd in enumerate(bodies):
        pg.set_content(f"<html><head><style>{CSS}</style></head><body>{bd}{foot(i,n)}</body></html>"); pg.wait_for_timeout(250)
        pg.evaluate("""()=>{const c=document.querySelector('.card');const s=document.getElementById('st');if(c&&s){s.style.height=(c.getBoundingClientRect().top-40-70)+'px'}}""")
        pg.screenshot(path=f"out/slide_{i+1}.png")
    pg2=br.new_page(viewport=dict(width=1000,height=1500),device_scale_factor=2)
    pg2.set_content(f"<html><head><style>{CSS.replace('width:1080px;height:1350px','width:1000px;height:1500px')}</style></head><body>{pin}{pinfoot}</body></html>"); pg2.wait_for_timeout(250)
    pg2.screenshot(path="out/pin.png"); br.close()
from PIL import Image
W=Image.new('RGB',(1500,1300),'white')
for k in range(n): W.paste(Image.open(f'out/slide_{k+1}.png').resize((288,360)),((k%5)*300,(k//5)*380))
W.paste(Image.open('out/pin.png').resize((300,450)),(0,780)); W.save('out/preview.png')
