# White "timeline signs" layout: white bg, a mint/pink age track across the top of each sign slide with a moving marker, photo panel, text below.
# Used for: When to switch from carrycot to seat unit (Nov 2026). Facts: RoSPA, Lullaby Trust, pushchair makers. Green product on white/pink.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css("#fff",NAVY,MINT,NAVY)+".t2{background:#fff}"
deco=star(36,30,26,ROSE)+star(1000,36,30,ROSE)
CU=b("cubset.png",1000); FE=b("fern.png",900); MU=b("muff.png",800); CA=b("carry.png",1000)
def track(k):
    st=[("0","Lying flat"),("6 mths","Signs start"),("9 mths","Most have moved")]
    seg=f'<div style="display:flex;height:22px;border-radius:11px;overflow:hidden"><div style="flex:6;background:{MINT}"></div><div style="flex:3;background:{ROSE}"></div><div style="flex:3;background:{PINK}"></div></div>'
    lab=f'<div style="position:relative;height:40px;font-weight:800;font-size:25px;margin-top:10px;opacity:.65"><span style="position:absolute;left:0">Birth</span><span style="position:absolute;left:50%;transform:translateX(-50%)">6 months</span><span style="position:absolute;right:0">Later</span></div>'
    x={1:0.52,2:0.62,3:0.72}[k]
    return f'<div style="position:absolute;left:70px;right:70px;top:66px"><div style="position:relative">{seg}<div style="position:absolute;left:calc({x*100}% - 25px);top:-14px;width:50px;height:50px;border-radius:50%;background:{NAVY};box-shadow:0 0 0 6px #fff"></div></div>{lab}</div>'
def sign(k,title,body,pic,h,note):
    return deco+track(k)+f'''<div style="position:absolute;left:60px;right:60px;top:190px;height:560px;background:{PINK};border-radius:44px;display:flex;align-items:center;justify-content:center"><img src="{pic}" style="height:{h}px;max-width:880px;object-fit:contain;{SH}"></div>
<div style="position:absolute;left:92px;top:216px"><span class="pill" style="background:{NAVY};color:#fff;font-size:27px">Sign {k} of 3</span></div>
<div style="position:absolute;left:70px;right:70px;top:785px"><div class="h" style="font-size:72px">{title}</div><div class="b" style="margin-top:16px;font-size:39px">{body}</div>
<div style="font-size:29px;font-weight:600;opacity:.6;margin-top:16px;line-height:1.3">{note}</div></div>'''
cover=star(60,1010,28,ROSE)+f'''<div style="position:absolute;left:70px;top:70px;width:580px"><div class="tags"><span class="tag t1">Tips</span><span class="tag t2">Pushchairs</span></div>
<div class="h" style="font-size:92px;margin-top:26px">When to switch from carrycot to seat unit</div></div>
{round_pic(baby(13,330,520,.42,.45),690,60,330,520,44)}
<div style="position:absolute;left:60px;right:60px;top:610px;height:600px;background:{PINK};border-radius:44px;display:flex;align-items:center;justify-content:center"><img src="{CU}" style="height:530px;margin-left:150px;{SH}"></div>
<div style="position:absolute;left:92px;top:636px;background:{NAVY};color:#fff;font-weight:700;font-size:30px;padding:14px 26px;border-radius:40px">Swipe before you switch</div>'''
def st(n,t,src): return f'<div style="background:{PINK};border-radius:34px;padding:28px 34px;margin-top:20px;display:flex;align-items:center;gap:28px"><div class="h" style="flex:none;width:330px;font-size:70px;white-space:nowrap">{n}</div><div><div class="b" style="font-size:36px;line-height:1.28">{t}</div><div style="font-size:26px;font-weight:700;opacity:.55;margin-top:6px">{src}</div></div></div>'
s2=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="kick">FORGET THE BIRTHDAY</div><div class="h" style="font-size:84px;margin-top:8px">The age on the box is only a guide</div></div>
<div style="position:absolute;left:60px;right:60px;top:345px">{st("6 months","the time a carrycot usually lasts","")}{st("Under 6","too young for a seat that doesn't recline","Source: RoSPA, the UK accident prevention charity")}{st("150°","the least a from-birth seat should recline","")}</div>
<div class="b" style="position:absolute;left:70px;right:70px;top:990px;font-size:42px">Every baby is different. So watch your baby, not the calendar. Here are the 3 signs.</div>'''
s3=sign(1,"Sits with no support","Pushchair makers say to wait until your baby can sit up unaided. Steady head control comes first.",CU,450,"Not sure? Ask your health visitor.")
s4=sign(2,"Close to the weight limit","Every carrycot has one, and it's easy to miss. Look in your manual, because the limit changes from brand to brand.",CA,470,"Past the limit? Time to move.")
s5=sign(3,"Rolling and looking out","A cramped baby who rolls or strains to see out may be ready to move. Check the other signs too.",FE,470,"")
RO=[("Does your seat go flat enough?","Newborns can't hold their own weight, so a from-birth seat must lie almost flat."),("Is the carrycot OK overnight?","Only if the maker says so. The Lullaby Trust says check before you use one for night sleep."),("Does the seat face you?","Some seats only face forward. Check before you buy if you want to see your baby.")]
ro="".join(f'''<div style="padding:40px 0;border-top:{"0" if i==0 else f"3px solid {PINK}"}"><div class="h" style="font-size:52px">{a}</div><div style="font-size:37px;font-weight:500;line-height:1.32;margin-top:10px">{c}</div></div>''' for i,(a,c) in enumerate(RO))
s6=deco+f'''<div style="position:absolute;left:70px;right:70px;top:70px"><div class="kick">BEFORE YOU DECIDE</div><div class="h" style="font-size:80px;margin-top:8px">3 questions to ask</div></div>
<div style="position:absolute;left:60px;right:60px;top:240px;background:{MINT};border-radius:40px;padding:20px 44px 34px">{ro}</div><div style="position:absolute;left:70px;right:70px;top:1045px;font-size:27px;font-weight:600;opacity:.7;">Source: The Lullaby Trust, the UK safer baby sleep charity</div>'''
s7=deco+f'''<div style="position:absolute;left:70px;right:70px;top:70px"><div class="kick">SWITCH DAY</div><div class="h" style="font-size:80px;margin-top:8px">A seat is more open than a carrycot</div></div>
<div style="position:absolute;left:60px;right:60px;top:320px;height:430px;background:{PINK};border-radius:44px;display:flex;align-items:center;justify-content:center"><img src="{MU}" style="height:380px;{SH}"></div>
<div style="position:absolute;left:70px;right:70px;top:780px"><div class="b" style="font-size:37px"><b style="font-weight:800">Five straps, every trip.</b> RoSPA says keep your child harnessed at all times.</div>
<div class="b" style="font-size:37px;margin-top:14px"><b style="font-weight:800">Nothing on the handles.</b> Bags and coats can tip a buggy over.</div>
<div class="b" style="font-size:37px;margin-top:14px"><b style="font-weight:800">Cold day?</b> A footmuff helps. Take hats and extra layers off indoors.</div></div><div style="position:absolute;left:70px;right:70px;top:1140px;font-size:27px;font-weight:600;opacity:.7;">Source: RoSPA (UK accident prevention charity) and The Lullaby Trust (UK safer baby sleep charity)</div>'''
s8=star(36,30,26,ROSE)+f'''{round_pic(baby(4,960,560,.72,.45),60,60,960,560,44)}
<div style="position:absolute;left:70px;right:70px;top:650px"><div class="h" style="font-size:78px">Need a seat that lasts? Compare prices first</div>
<div class="b" style="margin-top:18px;font-size:38px">Compare pushchair prices from UK shops in one place.</div>
<div style="margin-top:30px">{link_row(MINT)}</div>
<div style="margin-top:20px;font-size:32px;font-weight:700;opacity:.6">Save this post for later</div></div>'''
SG=[("Sits with no support","Head control comes first."),("Close to the weight limit","It's in your manual. Brands differ."),("Rolling or straining to see out","A cramped baby is telling you something.")]
sg="".join(f'<div style="display:flex;gap:22px;align-items:center;padding:22px 0;border-top:{"0" if i==0 else f"3px solid {PINK}"}"><div class="h" style="flex:none;width:68px;height:68px;border-radius:50%;background:{NAVY};color:#fff;font-size:36px;display:flex;align-items:center;justify-content:center">{i+1}</div><div><div class="h" style="font-size:42px">{a}</div><div style="font-size:29px;font-weight:500;opacity:.85;margin-top:4px">{c}</div></div></div>' for i,(a,c) in enumerate(SG))
pin=f'''{star(920,44,30,ROSE)}<div style="position:absolute;left:60px;right:60px;top:56px"><div class="tags"><span class="tag t1" style="font-size:24px">Tips</span><span class="tag t2" style="font-size:24px">Pushchairs</span></div>
<div class="h" style="font-size:80px;margin-top:20px">When to switch from carrycot to seat unit</div></div>
<div style="position:absolute;left:60px;right:60px;top:340px;height:490px;background:{PINK};border-radius:40px;display:flex;align-items:center;justify-content:center"><img src="{CU}" style="height:440px;{SH}"></div>
<div style="position:absolute;left:60px;right:60px;top:850px;background:{MINT};border-radius:34px;padding:6px 34px 10px">{sg}</div>
<div style="position:absolute;left:60px;right:60px;top:1255px;font-size:28px;font-weight:600;opacity:.7;line-height:1.3">Carrycots usually last about 6 months. Seats that don't recline aren't suitable under 6 months. Source: RoSPA, the UK accident prevention charity.</div>
<div style="position:absolute;left:60px;right:60px;bottom:38px;display:flex;justify-content:space-between;align-items:center"><div class="brand" style="font-size:34px">BabySorted</div><div style="font-weight:700;font-size:25px">Compare pushchair prices at babysorted.com</div></div>'''
render(ROOT+"/out/p3",[cover,s2,s3,s4,s5,s6,s7,s8],pin,CSS,NAVY)
