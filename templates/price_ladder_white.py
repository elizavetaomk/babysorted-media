# White "price ladder" layout for budget posts (16 Nov 2026): white bg, navy text, pink tier cards with a step badge,
# mint price chips. Used for: #45 How much should you really spend on a pram? Prices from our aggregator only.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css("#fff",NAVY,NAVY,"#fff")+f".t2{{background:{PINK};box-shadow:none}}"
DATE="16 Nov 2026"
deco=star(36,30,26,PINK)+star(1004,40,30,ROSE)
VT=b("versatrax.png",900); EG=b("egg3.png",1000); PE=b("peach.png",1000)
def plabel(n=1): return f"Price{'s' if n>1 else ''} on BabySorted, {DATE}"
def tier(step,band,title,body,pic,h,price,name):
    steps="".join(f'<div style="width:46px;height:{40+i*34}px;border-radius:12px;background:{NAVY if i<=step else ROSE}"></div>' for i in range(3))
    return deco+f'''<div style="position:absolute;left:60px;right:60px;top:60px;height:600px;background:{PINK};border-radius:44px;overflow:hidden">
<div style="position:absolute;left:40px;top:36px;display:flex;align-items:flex-end;gap:10px">{steps}</div>
<div style="position:absolute;left:40px;top:160px;font-weight:800;font-size:34px">{band}</div>
<div style="position:absolute;right:40px;top:30px;bottom:110px;left:330px;display:flex;align-items:center;justify-content:center"><img src="{pic}" style="height:{h}px;max-width:100%;object-fit:contain;{SH}"></div>
<div style="position:absolute;left:40px;right:40px;bottom:26px;display:flex;justify-content:space-between;align-items:flex-end"><div style="font-size:23px;font-weight:600;line-height:1.3;max-width:560px">{name}<br><span style="opacity:.7">{plabel()}</span></div><div class="h" style="font-size:58px;background:#fff;padding:8px 22px;border-radius:20px">{price}</div></div></div>
<div style="position:absolute;left:70px;right:70px;top:705px"><div class="h" style="font-size:64px">{title}</div><div class="b" style="margin-top:16px;font-size:37px">{body}</div></div>'''
cover=hero_cover(baby(51,1080,800,.5,.42),'<div class="tags"><span class="tag t1">Tips</span><span class="tag t2">Pushchairs</span></div>',"How much should you really spend on a pram?","Price is not the same as quality.",f'<img src="{EG}" style="height:280px;{SH}">',1,card="#fff",fg=NAVY,pill_bg=NAVY,pill_fg="#fff",title_fs=62)
row=lambda a,c,bg: f'<div style="display:flex;align-items:center;gap:26px;background:{bg};border-radius:30px;padding:26px 34px"><div class="h" style="font-size:54px;width:330px;flex:none">{a}</div><div style="font-size:33px;font-weight:600;line-height:1.3">{c}</div></div>'
s2=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="kick">THE REAL RANGE</div><div class="h" style="font-size:80px;margin-top:8px">Prams and travel systems we track today</div></div>
<div style="position:absolute;left:60px;right:60px;top:380px;display:flex;flex-direction:column;gap:20px">
{row("£169.95","the cheapest travel system",MINT)}{row("£799–£1,275","what the middle half of prams cost",PINK)}{row("£3,715","the dearest travel system",ROSE)}</div>
<div class="b" style="position:absolute;left:70px;right:70px;top:860px;font-size:42px">So there's no single "right" price. What changes is what you get for it. Here's what each step buys.</div>
<div style="position:absolute;left:70px;top:1185px;font-size:24px;font-weight:600;opacity:.6">{plabel(2)}</div>'''
s3=tier(0,"UNDER £400","A full travel system is possible","Pushchair, carrycot and infant car seat in one box. You usually give up some lightness, a smoother ride and a compact fold. Fine if you mostly drive.",VT,440,"£339.95","Joie Versatrax Travel System, Moonlight<br>(with carrycot and i-Snug car seat)")
s4=tier(1,"£400 TO £1,000","Better ride, but read the box","Mid-range prams often ride and fold better. But many prices here are for the pushchair only: the carrycot and car seat cost extra.",EG,470,"£703.20","egg 3 Stroller, Panther<br>(pushchair only, no carrycot)")
s5=tier(2,"OVER £1,000","You pay for years, not just looks","Premium bundles add nicer fabrics and parts that grow with your family. This one turns from single to double later, so a second baby doesn't mean a second pram.",PE,480,"£1,099","iCandy Peach 8 Complete Pushchair Bundle, Grey")
cmp=lambda a,c,bg: f'<div style="flex:1;background:{bg};border-radius:34px;padding:34px 30px;text-align:center"><div style="font-size:30px;font-weight:700">{c}</div><div class="h" style="font-size:76px;margin-top:10px">{a}</div></div>'
s6=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="kick">SAME PRAM, TWO PRICES</div><div class="h" style="font-size:80px;margin-top:8px">The shop matters as much as the model</div></div>
<div style="position:absolute;left:60px;right:60px;top:370px;height:330px;display:flex;align-items:center;justify-content:center"><img src="{EG}" style="height:320px;{SH}"></div>
<div style="position:absolute;left:60px;right:60px;top:720px;display:flex;gap:20px">{cmp("£703.20","One UK shop",MINT)}{cmp("£879.00","Another UK shop",PINK)}</div>
<div class="b" style="position:absolute;left:70px;right:70px;top:965px;font-size:37px">The exact same egg 3 Stroller in Panther. That's £175.80 for nothing but the checkout page.</div>
<div style="position:absolute;left:70px;top:1185px;font-size:24px;font-weight:600;opacity:.6">{plabel(2)}</div>'''
s7=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="kick">COLOUR COSTS MONEY</div><div class="h" style="font-size:80px;margin-top:8px">Not fussed about colour? Save £100</div></div>
<div style="position:absolute;left:60px;right:60px;top:370px;height:330px;display:flex;align-items:center;justify-content:center"><img src="{PE}" style="height:320px;{SH}"></div>
<div style="position:absolute;left:60px;right:60px;top:720px;display:flex;gap:20px">{cmp("£1,099","Grey",MINT)}{cmp("£1,199","Coco",PINK)}</div>
<div class="b" style="position:absolute;left:70px;right:70px;top:965px;font-size:37px">Same iCandy Peach 8 Complete Bundle, same shop, same day. Only the fabric colour is different. Always check every colour.</div>
<div style="position:absolute;left:70px;top:1185px;font-size:24px;font-weight:600;opacity:.6">{plabel(2)}</div>'''
q=lambda n,t,c: f'<div style="display:flex;gap:26px;padding:28px 0;border-top:{"0" if n==1 else f"3px solid {PINK}"}"><div class="h" style="flex:none;width:76px;height:76px;border-radius:50%;background:{NAVY};color:#fff;font-size:40px;display:flex;align-items:center;justify-content:center">{n}</div><div><div class="h" style="font-size:46px">{t}</div><div style="font-size:33px;font-weight:500;line-height:1.35;margin-top:8px">{c}</div></div></div>'
s8=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="kick">SET YOUR BUDGET</div><div class="h" style="font-size:80px;margin-top:8px">3 questions before you look at prices</div></div>
<div style="position:absolute;left:70px;right:70px;top:360px">{q(1,"Car, bus or on foot?","Lots of walking is where a smoother ride is worth paying for. Mostly driving? Check the fold and your boot.")}{q(2,"Another baby soon?","A pram that converts to a double can save buying twice.")}{q(3,"What's not in the box?","Add the carrycot, car seat, adapters, footmuff and rain cover before you compare.")}</div>'''
s9=hero_last(baby(47,1080,760,.5,.5),"Found your budget? Compare pram prices first","See the same pram across UK shops and every colour in one place.",PINK,fg=NAVY)
pin=pin_hero(baby(44,1000,680,.5,.42),pin_tags("Tips","Pushchairs"),"How much to spend on a pram",["Under £400: full travel systems","£400–£1,000: check what's included","Over £1,000: grows with your family","Same pram, other shop: £175.80 less","Other colour, same pram: £100 less"],EG,290,"#fff",NAVY,NAVY,"#fff",f"{plabel(2)}.","Compare pram prices at babysorted.com",line=PINK,photo_h=680,title_fs=58)
render(ROOT+"/out/a",[cover,s2,s3,s4,s5,s6,s7,s8,s9],pin,CSS,NAVY)
