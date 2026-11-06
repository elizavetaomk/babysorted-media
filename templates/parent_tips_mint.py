# Mint "parent tips" layout for Parenting Tips posts: mint bg, big numbered white circle, white product stage, tip below; closing health note.
# Used for: Baby hates tummy time? (Nov 2026). Facts: NHS, Best Start in Life, NHS Devon. No medical advice; worries go to the health visitor.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css(MINT,NAVY,NAVY,"#fff")+".t2{background:#fff;box-shadow:none}"
deco=star(36,30,26,"#fff")+star(1000,36,30,"#fff")
MI=b("mirror.png",1000); CR=b("croco.png",900); CM=b("cammat.png",900); TM=b("tinymat.png",900); GY=b("gym.png",900); GI=b("gymini.png",900)
def tip(k,title,body,pic,h,src):
    return deco+f'''<div style="position:absolute;left:60px;top:60px;right:60px;height:640px;background:#fff;border-radius:300px 44px 44px 44px;display:flex;align-items:center;justify-content:center;overflow:hidden"><img src="{pic}" style="height:{h}px;max-width:860px;object-fit:contain;margin-left:120px;{SH}"></div>
<div class="h" style="position:absolute;left:50px;top:50px;width:210px;height:210px;border-radius:50%;background:{NAVY};color:#fff;display:flex;align-items:center;justify-content:center;font-size:120px">{k}</div>
<div style="position:absolute;left:70px;right:70px;top:735px"><div class="h" style="font-size:76px">{title}</div><div class="b" style="margin-top:16px;font-size:40px">{body}</div>
<div style="font-size:28px;font-weight:700;opacity:.55;margin-top:14px">{src}</div></div>'''
cover=star(980,60,36,"#fff")+star(50,650,24,"#fff")+f'''<div style="position:absolute;left:70px;right:70px;top:70px"><div class="tags"><span class="tag t1">Parenting Tips</span><span class="tag t2">Play &amp; Development</span></div>
<div class="h" style="font-size:104px;margin-top:28px">Baby hates tummy time?</div>
<div style="font-size:46px;font-weight:700;margin-top:16px">Try these 6 small changes</div></div>
{round_pic(baby(2,560,670,.62,.62,1.45),60,540,560,670,44)}
<div style="position:absolute;left:640px;right:60px;top:540px;height:670px;background:#fff;border-radius:44px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:40px;padding:20px"><img src="{MI}" style="width:300px;{SH}"><img src="{CR}" style="width:300px;{SH}"></div>
<div style="position:absolute;left:92px;top:1130px;background:{NAVY};color:#fff;font-weight:700;font-size:30px;padding:14px 26px;border-radius:40px">Swipe for the ideas</div>'''
s2=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="kick">THE GOAL</div><div class="h" style="font-size:84px;margin-top:8px">It sounds like a lot. It isn't.</div></div>
<div style="position:absolute;left:60px;right:60px;top:345px;height:480px;background:#fff;border-radius:44px;display:flex;flex-direction:column;align-items:center;justify-content:center"><div class="h" style="font-size:230px">30</div><div class="h" style="font-size:58px;margin-top:-4px">minutes a day</div><div style="margin-top:20px"><span class="pill" style="background:{MINT}">spread out, when awake</span></div></div>
<div class="b" style="position:absolute;left:70px;right:70px;top:860px;font-size:40px">That's the NHS goal for babies who can't move around yet. Think lots of tiny bits, not one long session. It builds the back, neck and shoulders for sitting and crawling.</div><div style="position:absolute;left:70px;right:70px;top:1135px;font-size:27px;font-weight:600;opacity:.7;">Source: NHS</div>'''
s3=tip(1,"Start on your chest","You can begin from birth. Lie back and rest your baby on you, tummy down. Only do this when you're wide awake.",CM,470,"Source: NHS")
s4=tip(2,"Keep it really short","Start with a few minutes, twice a day, then build up. If your baby cries, stop and try later.",TM,470,"Source: NHS Devon")
s5=tip(3,"Roll up a towel","If lifting their head is hard, put a small rolled towel under their arms. It gives a little lift.",CR,300,"Source: NHS")
s6=tip(4,"Try your lap","Lay your baby across your knees or lap, tummy down. Same muscles, but it feels close and cosy.",GY,430,"Source: NHS Devon")
s7=tip(5,"Get down there too","Lie on the floor, face to face. Your face is the best toy. From about 3 months, add toys in reach.",MI,440,"Source: NHS Devon")
s8=tip(6,"Swap some seat time","Bouncers and baby walkers are best for no more than 20 minutes at a time, says the NHS. Floor time can fill the gap.",GI,450,"Source: NHS")
NT=[("Always stay with them","Your baby should only be on their tummy when awake and watched."),("Back to sleep","Always lay your baby down to sleep on their back."),("Worried about anything?","Talk to your health visitor or GP. That includes if your baby shows no signs of moving by 12 months.")]
nt="".join(f'''<div style="padding:34px 0;border-top:{"0" if i==0 else f"3px solid {MINT}"}"><div class="h" style="font-size:52px">{a}</div><div style="font-size:38px;font-weight:500;line-height:1.32;margin-top:10px">{c}</div></div>''' for i,(a,c) in enumerate(NT))
s9=deco+f'''<div style="position:absolute;left:70px;right:70px;top:70px"><div class="kick">KEEP IN MIND</div><div class="h" style="font-size:80px;margin-top:8px">3 things that never change</div></div>
<div style="position:absolute;left:60px;right:60px;top:320px;background:#fff;border-radius:40px;padding:14px 44px 22px">{nt}</div><div style="position:absolute;left:70px;right:70px;top:1140px;font-size:27px;font-weight:600;opacity:.7;">Source: NHS and NHS Devon</div>'''
s10=star(36,30,26,"#fff")+f'''{round_pic(baby(11,960,560,.5,.36),60,60,960,560,44)}
<div style="position:absolute;left:70px;right:70px;top:650px"><div class="h" style="font-size:78px">Want a softer floor? Compare prices first</div>
<div class="b" style="margin-top:18px;font-size:38px">Compare play mat prices from UK shops in one place.</div>
<div style="margin-top:30px">{link_row("#fff")}</div>
<div style="margin-top:20px;font-size:32px;font-weight:700;opacity:.6">Save this post for later</div></div>'''
L=[("Start on your chest","From birth, only when you're wide awake."),("Keep it short","A few minutes, twice a day. Then build up."),("Roll up a towel","Small roll under the arms for a lift."),("Try your lap","Tummy down across your knees."),("Get down there too","Your face is the best toy."),("Swap some seat time","Bouncers: 20 minutes at a time at most.")]
ls="".join(f'<div style="display:flex;align-items:center;gap:20px;padding:15px 0;border-top:{"0" if i==0 else f"3px solid {MINT}"}"><div class="h" style="flex:none;width:58px;height:58px;border-radius:50%;background:{NAVY};color:#fff;font-size:30px;display:flex;align-items:center;justify-content:center">{i+1}</div><div><div class="h" style="font-size:35px">{a}</div><div style="font-size:25px;font-weight:500;opacity:.85;margin-top:2px">{c}</div></div></div>' for i,(a,c) in enumerate(L))
pin=f'''{star(920,44,30,"#fff")}<div style="position:absolute;left:60px;right:60px;top:56px"><div class="tags"><span class="tag t1" style="font-size:24px">Parenting Tips</span><span class="tag t2" style="font-size:24px">Play &amp; Development</span></div>
<div class="h" style="font-size:75px;margin-top:20px;white-space:nowrap">Baby hates tummy time?</div><div style="font-size:34px;font-weight:700;margin-top:10px">6 small changes that help</div></div>
<div style="position:absolute;left:60px;right:60px;top:270px;height:330px;display:flex;gap:18px"><img src="{baby(2,350,330,.62,.62,1.5)}" style="width:350px;height:330px;border-radius:34px;object-fit:cover"><div style="flex:1;background:#fff;border-radius:34px;display:flex;align-items:center;justify-content:center"><img src="{MI}" style="width:420px;{SH}"></div></div>
<div style="position:absolute;left:60px;right:60px;top:620px;background:#fff;border-radius:34px;padding:14px 34px 16px">{ls}</div>
<div style="position:absolute;left:60px;right:60px;top:1302px;background:{NAVY};color:#fff;border-radius:24px;padding:16px 26px;font-size:26px;font-weight:600;line-height:1.3">NHS goal: 30 minutes a day, spread out. Always watch your baby. Back to sleep, tummy to play. Source: NHS.</div>
<div style="position:absolute;left:60px;right:60px;bottom:30px;display:flex;justify-content:space-between;align-items:center"><div class="brand" style="font-size:34px">BabySorted</div><div style="font-weight:700;font-size:25px">Compare play mat prices at babysorted.com</div></div>'''
render(ROOT+"/out/p4",[cover,s2,s3,s4,s5,s6,s7,s8,s9,s10],pin,CSS,NAVY)
