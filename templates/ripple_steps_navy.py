# Navy "ripple steps" layout for Parenting Tips: navy bg, white stage card with pink water ripples behind the product, step number pill, white text.
# Used for: Bath time safety in the first year (11 Nov 2026). Facts: NHS, Best Start in Life (NHS), RoSPA.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css(NAVY,"#fff",PINK,NAVY)
deco=star(36,30,26,PINK)+star(1000,40,30,"#fff",.6)
BW=b("bathw.png",1000); BG=b("bathg.png",1000)
DATE="9 Nov 2026"
def ripple(cx,cy): return "".join(f'<div style="position:absolute;left:{cx-r}px;top:{cy-r*0.42}px;width:{2*r}px;height:{r*0.84}px;border-radius:50%;border:5px solid {PINK};opacity:{o}"></div>' for r,o in ((360,.35),(270,.6),(180,1)))
def step(k,title,body,vis,src,price=""):
    pr=f'<div style="position:absolute;right:30px;top:26px;text-align:right;color:{NAVY}"><div class="h" style="font-size:44px">{price[0]}</div><div style="font-size:21px;font-weight:600;opacity:.7">{price[1]}<br>Price on BabySorted, {DATE}</div></div>' if price else ""
    lab=f'<span style="background:{PINK};color:{NAVY};font-weight:800;font-size:28px;padding:10px 22px;border-radius:20px;letter-spacing:.05em">{k}</span>'
    return deco+f'''<div style="position:absolute;left:60px;right:60px;top:60px;height:600px;background:#fff;border-radius:44px;overflow:hidden">{ripple(480,470)}<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">{vis}</div>{pr}</div>
<div style="position:absolute;left:70px;right:70px;top:705px">{lab}<div class="h" style="font-size:70px;margin-top:22px">{title}</div><div class="b" style="margin-top:16px;font-size:40px">{body}</div></div>
<div style="position:absolute;left:70px;right:70px;top:1195px;font-size:26px;font-weight:700;color:{PINK}">{src}</div>'''
img=lambda s,h,x="": f'<img src="{s}" style="height:{h}px;object-fit:contain;{SH};{x}">'
big=lambda a,c: f'<div style="text-align:center;color:{NAVY}"><div class="h" style="font-size:190px;line-height:1">{a}</div><div class="h" style="font-size:52px;margin-top:6px">{c}</div></div>'
cover=star(980,60,36,PINK)+star(60,1010,24,"#fff",.6)+f'''<div style="position:absolute;left:70px;right:70px;top:70px"><div class="tags"><span class="tag t1">Parenting Tips</span><span class="tag t2">Bathtime &amp; Changing</span></div>
<div class="h" style="font-size:100px;margin-top:28px">Bath time safety in the first year</div>
<div style="font-size:44px;font-weight:700;margin-top:16px;color:{PINK}">Calm, warm and always within reach.</div></div>
{round_pic(baby(4,440,600,.5,.55,1.05),60,610,440,600,44)}
<div style="position:absolute;left:520px;right:60px;top:610px;height:600px;background:#fff;border-radius:44px;overflow:hidden">{ripple(250,420)}<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">{img(BW,400)}</div></div>
<div style="position:absolute;left:84px;top:1125px;background:{PINK};color:{NAVY};font-weight:700;font-size:30px;padding:14px 26px;border-radius:40px">Swipe for the steps</div>'''
s2=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="kick">GOOD NEWS FIRST</div><div class="h" style="font-size:84px;margin-top:8px">You don't need a daily bath</div></div>
<div style="position:absolute;left:60px;right:60px;top:340px;height:430px;background:#fff;color:{NAVY};border-radius:44px;display:flex;flex-direction:column;align-items:center;justify-content:center"><div class="h" style="font-size:200px;line-height:1">2–3</div><div class="h" style="font-size:58px">times a week is fine</div></div>
<div class="b" style="position:absolute;left:70px;right:70px;top:820px;font-size:41px">That's for a newborn. You can top and tail in between. And in the first month, plain water is best for your baby's skin. No bubbles or lotions needed.</div>
<div style="position:absolute;left:70px;right:70px;top:1150px;font-size:27px;font-weight:700;color:{PINK}">Source: NHS</div>'''
s3=step("STEP 1","Get it all ready first","Two towels, a clean nappy and clothes, all in reach before the water goes in. Pick a time when your baby is awake and content: not straight after a feed, or when hungry or tired.",img(BG,420),"Source: NHS",("£18.29","Shnuggle baby bath, pebble grey"))
s4=step("STEP 2","Cold in first, then hot","Run the cold tap first, then add hot. Mix it well so there are no hot patches. About 8 to 10cm of water is enough.",big("8–10cm","of water"),"Source: NHS")
s5=step("STEP 3","Do the elbow test","Dip your elbow or wrist in. The water should feel the same as your body: warm, not hot. Test it every time, even when the tap feels fine.",img(BW,420),"Source: NHS",("£17.28","Shnuggle newborn baby bath, white"))
s6=step("STEP 4","Never leave, not for a second","Babies can drown quickly and silently in very shallow water. They don't splash or cry. Need to leave? Take your baby with you. The phone and the door can wait. Don't leave older children in charge.",big("0","seconds alone"),"Source: RoSPA, the UK accident prevention charity")
s7=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="kick">WORTH KNOWING</div><div class="h" style="font-size:80px;margin-top:8px">A bath seat is not a safety device</div></div>
<div style="position:absolute;left:60px;right:60px;top:340px;background:#fff;color:{NAVY};border-radius:44px;padding:40px 46px;display:flex;gap:30px;align-items:center"><div class="h" style="font-size:190px;line-height:1">9+</div><div class="h" style="font-size:44px;line-height:1.2">of the 14 babies under 1 who drowned in the bath in England, 2019 to 2025, were in a bath seat</div></div>
<div class="b" style="position:absolute;left:70px;right:70px;top:680px;font-size:41px">Seats can come away from the bath, and they don't stop drowning. RoSPA recommends not using them. The safe set-up is a little water and your hands on your baby.</div>
<div style="position:absolute;left:70px;right:70px;top:1150px;font-size:27px;font-weight:700;color:{PINK}">Source: RoSPA, the UK accident prevention charity</div>'''
s8=step("STEP 5","Empty it straight away","Drain the bath as soon as you've finished. Then pat your baby dry and cover them up, so they stay warm.",img(BG,420),"Source: NHS")
s9=star(36,30,26,PINK)+f'''{round_pic(baby(4,960,520,.5,.5),60,60,960,520,44)}
<div style="position:absolute;left:70px;right:70px;top:610px"><div style="display:inline-block;background:#fff;color:{NAVY};border-radius:24px;padding:16px 22px;font-size:30px;font-weight:700">Worried about your baby's skin or cord? Ask your midwife or health visitor.</div>
<div class="h" style="font-size:72px;margin-top:26px">Need a baby bath? Compare prices first</div>
<div style="margin-top:28px">{link_row(PINK)}</div>
<div style="margin-top:20px;font-size:32px;font-weight:700;opacity:.7">Save this post for later</div></div>'''
L=[("Get it all ready first","Towels, nappy, clothes in reach."),("Cold in first, then hot","Mix well. About 8–10cm of water."),("Do the elbow test","Warm, not hot. Like your body."),("Never leave, not for a second","Take your baby with you."),("Skip the bath seat","It's not a safety device."),("Empty it straight away","Pat dry, keep warm.")]
ls="".join(f'<div style="display:flex;align-items:center;gap:20px;padding:14px 0;border-top:{"0" if i==0 else f"3px solid {PINK}"}"><div class="h" style="flex:none;width:56px;height:56px;border-radius:50%;background:{NAVY};color:#fff;font-size:29px;display:flex;align-items:center;justify-content:center">{i+1}</div><div><div class="h" style="font-size:34px">{a}</div><div style="font-size:25px;font-weight:500;opacity:.85;margin-top:2px">{c}</div></div></div>' for i,(a,c) in enumerate(L))
pin=f'''{star(920,44,30,PINK)}<div style="position:absolute;left:60px;right:60px;top:56px"><div class="tags"><span class="tag t1" style="font-size:24px">Parenting Tips</span><span class="tag t2" style="font-size:24px">Bathtime &amp; Changing</span></div>
<div class="h" style="font-size:74px;margin-top:20px">Bath time safety in the first year</div></div>
<div style="position:absolute;left:60px;right:60px;top:345px;height:270px;display:flex;gap:18px"><img src="{baby(4,330,270,.5,.55)}" style="width:330px;height:270px;border-radius:30px;object-fit:cover"><div style="flex:1;background:#fff;border-radius:30px;display:flex;align-items:center;justify-content:center">{img(BW,250)}</div></div>
<div style="position:absolute;left:60px;right:60px;top:640px;background:#fff;color:{NAVY};border-radius:34px;padding:10px 34px 12px">{ls}</div>
<div style="position:absolute;left:60px;right:60px;top:1300px;font-size:24px;font-weight:600;color:{PINK};line-height:1.3">Source: NHS and RoSPA, the UK accident prevention charity.</div>
<div style="position:absolute;left:60px;right:60px;bottom:30px;display:flex;justify-content:space-between;align-items:center"><div class="brand" style="font-size:34px">BabySorted</div><div style="font-weight:700;font-size:25px">Compare baby bath prices at babysorted.com</div></div>'''
render(ROOT+"/out/d",[cover,s2,s3,s4,s5,s6,s7,s8,s9],pin,CSS,"#fff")
