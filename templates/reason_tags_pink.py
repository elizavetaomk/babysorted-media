# Pink "reason tags" layout: pink bg, close-up cover with white card, inner slides show a whole product with a navy luggage tag ("Crash history: unknown").
# Used for: Why you should never buy a used car seat (Nov 2026). Facts: RoSPA childcarseats.org.uk, Lullaby Trust.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css(PINK,NAVY,NAVY,"#fff")+".t2{background:#fff;box-shadow:none}"
deco=star(36,30,26,"#fff")+star(1000,36,30,"#fff")
CL=b("cloud.png",1000); PB=b("pebble.png",1000)
def luggage(a,c,x="right:60px;top:230px"):
    return f'''<div style="position:absolute;{x};width:420px;background:{NAVY};color:#fff;border-radius:30px 30px 30px 30px;padding:30px 34px;transform:rotate(-3deg);box-shadow:0 14px 24px rgba(5,31,69,.22)"><div style="position:absolute;left:30px;top:24px;width:26px;height:26px;border-radius:50%;background:{PINK}"></div><div style="font-weight:800;font-size:26px;letter-spacing:.05em;opacity:.7;margin-left:42px">{a}</div><div class="h" style="font-size:58px;margin-top:16px">{c}</div></div>'''
def reason(k,tagA,tagC,title,body,src,pic=CL,h=520):
    return deco+f'''<img src="{pic}" style="position:absolute;left:70px;top:60px;height:{h}px;{SH}">{luggage(tagA,tagC)}
<div style="position:absolute;left:60px;right:60px;top:640px;height:590px;background:#fff;border-radius:44px;padding:40px 44px"><div class="kick">REASON {k} OF 4</div><div class="h" style="font-size:68px;margin-top:10px">{title}</div><div class="b" style="margin-top:18px;font-size:43px;line-height:1.34">{body}</div><div style="position:absolute;left:44px;bottom:30px;font-size:27px;font-weight:700;opacity:.55">{src}</div></div>'''
cover=star(60,60,44,"#fff")+star(980,90,30,"#fff")+f'''<img src="{CL}" style="position:absolute;left:300px;top:-30px;width:800px;{SH}">
{round_pic(baby(15,270,270,.5,.36,3.0),30,170,270,270,135,"#fff")}
<div style="position:absolute;left:60px;right:60px;top:810px;height:400px;background:#fff;border-radius:44px;padding:34px 44px"><div class="tags"><span class="tag t1">Tips</span><span class="tag t2" style="box-shadow:inset 0 0 0 3px {NAVY}">Car Seats</span></div>
<div class="h" style="font-size:80px;margin-top:20px">Why you should never buy a used car seat</div>
<div style="font-size:35px;font-weight:600;opacity:.75;margin-top:14px">You can't see crash damage.</div></div>'''
s2=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="kick">THE SHORT VERSION</div></div>
<div style="position:absolute;left:60px;right:60px;top:140px;background:#fff;border-radius:44px;padding:44px 50px"><div class="h" style="font-size:150px;line-height:.7;color:{ROSE}">“</div><div class="h" style="font-size:78px;margin-top:-6px">The best advice is do not buy a second-hand child seat.</div><div style="font-size:32px;font-weight:700;opacity:.6;margin-top:22px">Source: RoSPA, the UK accident prevention charity</div></div>
<div style="position:absolute;left:60px;right:60px;top:790px;background:{NAVY};color:#fff;border-radius:34px;padding:44px 50px"><div class="h" style="font-size:72px">The Lullaby Trust says the same.</div><div class="b" style="font-size:40px;margin-top:16px">It's the UK safer baby sleep charity. Here are the 4 reasons why.</div></div>'''
s3=reason(1,"CRASH HISTORY","Unknown","Damage can hide","A seat that has been in a crash should be replaced, even with no visible damage. Not all damage shows to the naked eye.","Source: RoSPA, the UK accident prevention charity")
s4=reason(2,"MADE IN","Which year?","Seats have a use-by","Some makers set a limit of 5 to 12 years. Older seats have also had more wear and tear. Check the manual.","Source: RoSPA, the UK accident prevention charity",PB)
s5=reason(3,"INSTRUCTIONS","Missing","Often no manual","Second-hand seats often come without one. Then it's easy to fit or use the seat the wrong way, and you may not know.","Source: RoSPA, the UK accident prevention charity")
s6=reason(4,"SAFETY LABEL","Too old?","Rules move on","Look for the E mark and R129 (i-Size) or R44.04 on the label. Older seats may not have them.","Source: RoSPA, the UK accident prevention charity",PB)
CK=[("You know its full history","Family or a close friend only. Never a stranger, a shop or online."),("It has the original instructions","Check the maker's age limit too."),("It suits your child","Right height and weight today."),("It fits every car you'll use","Try it in grandparents' cars too.")]
ck="".join(f'''<div style="display:flex;gap:24px;padding:26px 0;border-top:{"0" if i==0 else f"3px solid {PINK}"}"><div style="flex:none;width:60px;height:60px;border-radius:18px;background:{NAVY};color:#fff;font-weight:800;font-size:32px;display:flex;align-items:center;justify-content:center">✓</div><div><div class="h" style="font-size:45px">{a}</div><div style="font-size:35px;font-weight:500;line-height:1.3;margin-top:6px">{c}</div></div></div>''' for i,(a,c) in enumerate(CK))
s7=deco+f'''<div style="position:absolute;left:70px;right:70px;top:70px"><div class="kick">THE ONE EXCEPTION</div><div class="h" style="font-size:80px;margin-top:8px">A hand-me-down, if all 4 are true</div></div>
<div style="position:absolute;left:60px;right:60px;top:320px;background:#fff;border-radius:40px;padding:14px 44px 18px">{ck}</div><div style="position:absolute;left:70px;right:70px;top:1060px;font-size:27px;font-weight:600;opacity:.7;">Source: RoSPA, the UK accident prevention charity</div>'''
SV=[("Ask your council","Road safety teams may know of child seat discount schemes."),("Compare new seat prices","New i-Size infant seats start from about £65 in our catalog."),("Had a crash?","Add a new seat to your insurance claim. RoSPA has a letter that can help.")]
sv="".join(f'''<div style="padding:34px 0;border-top:{"0" if i==0 else f"3px solid {PINK}"}"><div class="h" style="font-size:52px">{a}</div><div style="font-size:38px;font-weight:500;line-height:1.32;margin-top:10px">{c}</div></div>''' for i,(a,c) in enumerate(SV))
s8=deco+f'''<div style="position:absolute;left:70px;right:70px;top:70px"><div class="kick">IF MONEY IS TIGHT</div><div class="h" style="font-size:80px;margin-top:8px">Safer ways to save</div></div>
<div style="position:absolute;left:60px;right:60px;top:240px;background:#fff;border-radius:40px;padding:14px 44px 18px">{sv}</div>
<div style="position:absolute;left:74px;right:70px;top:1145px;font-size:27px;font-weight:600;opacity:.65">Source: RoSPA, the UK accident prevention charity. Price on BabySorted, 6 Nov 2026.</div>'''
s9=star(36,30,26,"#fff")+f'''{round_pic(baby(7,960,560,.42,.5),60,60,960,560,44)}
<div style="position:absolute;left:70px;right:70px;top:650px"><div class="h" style="font-size:78px">Buying new? Compare prices first</div>
<div class="b" style="margin-top:18px;font-size:38px">Compare car seat prices from UK shops in one place.</div>
<div style="margin-top:30px">{link_row("#fff")}</div>
<div style="margin-top:20px;font-size:32px;font-weight:700;opacity:.6">Save this post for later</div></div>'''
R=[("Hidden crash damage","Replace after a crash, even with no visible damage."),("Too old","Makers set limits of 5 to 12 years."),("No manual","Easy to fit it the wrong way."),("Old labels","Look for R129 (i-Size) or R44.04.")]
r="".join(f'<div style="display:flex;gap:20px;align-items:center;padding:17px 0;border-top:{"0" if i==0 else f"3px solid {PINK}"}"><div class="h" style="flex:none;width:60px;height:60px;border-radius:50%;background:{NAVY};color:#fff;font-size:32px;display:flex;align-items:center;justify-content:center">{i+1}</div><div><div class="h" style="font-size:37px">{a}</div><div style="font-size:27px;font-weight:500;opacity:.85;margin-top:3px">{c}</div></div></div>' for i,(a,c) in enumerate(R))
pin=f'''{star(920,44,32,"#fff")}<div style="position:absolute;left:60px;right:60px;top:56px"><div class="tags"><span class="tag t1" style="font-size:24px">Tips</span><span class="tag t2" style="font-size:24px">Car Seats</span></div>
<div class="h" style="font-size:80px;margin-top:20px">Why you should never buy a used car seat</div></div>
<img src="{CL}" style="position:absolute;left:60px;top:345px;height:440px;{SH}">{luggage("CRASH HISTORY","Unknown","right:60px;top:470px")}
<div style="position:absolute;left:60px;right:60px;top:795px;background:#fff;border-radius:34px;padding:10px 34px 12px">{r}</div>
<div style="position:absolute;left:60px;right:60px;top:1280px;background:{NAVY};color:#fff;border-radius:24px;padding:14px 26px;font-size:25px;font-weight:600;line-height:1.28">Only exception: family or a close friend, full history, original manual, not too old. Source: RoSPA, the UK accident prevention charity</div>
<div style="position:absolute;left:60px;right:60px;bottom:32px;display:flex;justify-content:space-between;align-items:center"><div class="brand" style="font-size:34px">BabySorted</div><div style="font-weight:700;font-size:25px">Compare car seat prices at babysorted.com</div></div>'''
render(ROOT+"/out/p5",[cover,s2,s3,s4,s5,s6,s7,s8,s9],pin,CSS,NAVY)
