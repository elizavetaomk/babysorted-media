# Pink "trail tiles" layout (22 Nov 2026): pink bg, a dotted trail line with a navy marker across the top,
# two side-by-side spec tiles (white + deeper pink), title + body below. Photo-led cover and last slide.
# Used for: #50 Best all-terrain prams for parks and countryside. Buying advice; safety points from RoSPA.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css(PINK,NAVY,NAVY,"#fff")+".t2{background:#fff;box-shadow:none}"
UJ=b("uj.png",800); NI=b("nipper.png",900); CUB=b("cub.png",900); DATE="20 Nov 2026"
RO="Source: RoSPA, the UK accident prevention charity"
def trail(k,n=8):
    k0=k; k=k-1
    x=90+k*(900/(n-1))
    return f'''<svg style="position:absolute;left:0;top:40px" width="1080" height="80"><path d="M60 50 C 250 10, 400 80, 560 40 S 900 20, 1020 50" stroke="#fff" stroke-width="8" stroke-dasharray="2 20" stroke-linecap="round" fill="none"/></svg>
<div class="h" style="position:absolute;left:{x-32}px;top:52px;width:64px;height:64px;border-radius:50%;background:{NAVY};color:#fff;font-size:32px;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 8px {PINK}">{k0}</div>'''
def tile(bg,a,c,fs=86): return f'<div style="flex:1;background:{bg};border-radius:36px;padding:34px 30px;display:flex;flex-direction:column;justify-content:center"><div class="h" style="font-size:{fs}px">{a}</div><div class="b" style="font-size:34px;margin-top:14px;line-height:1.3;font-weight:600">{c}</div></div>'
def sl(k,kick,title,body,tiles,src=None):
    s=f'<div style="position:absolute;left:70px;right:70px;top:1110px;font-size:23px;font-weight:700;opacity:.7">{src}</div>' if src else ""
    return trail(k)+f'''<div style="position:absolute;left:60px;right:60px;top:150px;height:380px;display:flex;gap:22px">{tiles}</div>
<div style="position:absolute;left:70px;right:70px;top:580px"><div class="kick">{kick}</div><div class="h" style="font-size:66px;margin-top:6px">{title}</div><div class="b" style="margin-top:14px;font-size:36px">{body}</div></div>{s}'''
cover=hero_cover(baby(46,1080,800,.5,.42,1.05),'<div class="tags"><span class="tag t1">Buying guide</span><span class="tag t2">Pushchairs</span></div>',"All-terrain prams: what really matters","Parks, fields and muddy paths, sorted.",f'<img src="{NI}" style="height:290px;{SH}">',1,card=PINK,fg=NAVY,pill_bg=NAVY,pill_fg="#fff",title_fs=68)
s2=sl(1,"THE BIG THREE","What makes it all-terrain","Big wheels, real suspension and a frame that feels solid when you push it over bumps. Fancy fabrics don't help on a muddy path.",tile("#fff","Wheels","Bigger rolls over roots and gravel")+tile(ROSE,"Suspension","Smooths the ride for a sleeping baby"))
s3=sl(2,"TYRES","Air or puncture-proof?","Air-filled tyres give the most grip and the softest ride, but they can puncture and need pumping. Foam-filled ones never go flat but feel a bit firmer.",tile("#fff","Air","Softest ride. Keep a pump.")+tile(ROSE,"Foam","No flats. A bit firmer."))
s4=sl(3,"FRONT WHEEL","Lock it off-road","A swivel front wheel turns easily in town. On grass, gravel and slopes, lock it straight so the pram doesn't pull to one side.",tile("#fff","Swivel","shops and pavements")+tile(ROSE,"Locked","fields and slopes"))
s5=sl(4,"FIT","Handle and suspension","Test the handlebar at your height: a short push on a long walk soon hurts. Adjustable suspension lets you go softer on rough paths.",tile("#fff","Handle","test it at your height")+tile(ROSE,"Adjust","softer for rough paths"))
s6=sl(5,"SAFETY","Brakes on, bags off the handle","Check the brake: lock it, then push. Keep shopping bags off the handle, as they can tip the pram. Use the basket for the picnic.",tile("#fff","Lock + push","before every slope")+tile(ROSE,"Basket","not the handle"),RO+".")
s7=sl(6,"THE BOOT","Big wheels, big fold","Chunky wheels often mean a chunky fold. Measure your boot and check the folded size before you buy. Quick-release wheels can save space.",tile("#fff","Measure","boot length and height")+tile(ROSE,"Folded","size in the spec"))
s8=sl(7,"RUNNING?","Jogging needs a jogging pram","Pushchair makers say: only run with a pushchair made for jogging. An all-terrain pram is built for walks, not for running.",tile("#fff","Walk","all-terrain")+tile(ROSE,"Run","jogging-rated only"))
def pk(src,h,price,name): return f'<div style="flex:1;background:#fff;border-radius:36px;padding:24px 14px;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;text-align:center"><img src="{src}" style="height:{h}px;max-width:100%;object-fit:contain;{SH}"><div class="h" style="font-size:40px;margin-top:10px">{price}</div><div style="font-size:19px;font-weight:600;opacity:.75;line-height:1.25">{name}</div></div>'
s9=trail(8)+f'''<div style="position:absolute;left:60px;right:60px;top:150px;height:440px;display:flex;gap:18px">{pk(UJ,250,"£466.65","Mountain Buggy Urban Jungle V4")}{pk(NI,250,"£525.00","Out 'n' About Nipper V6")}{pk(CUB,240,"£636.65","Bugaboo Cub All Terrain")}</div>
<div style="position:absolute;left:70px;right:70px;top:640px"><div class="kick">3 TO COMPARE</div><div class="h" style="font-size:66px;margin-top:6px">Three to start with</div><div class="b" style="margin-top:14px;font-size:36px">All three are in our catalog today. Check the tyres, fold and handle against your walks and your boot.</div></div>
<div style="position:absolute;left:70px;right:70px;top:1110px;font-size:23px;font-weight:700;opacity:.7">Prices on BabySorted, {DATE}.</div>'''
s10=hero_last(baby(47,1080,700,.5,.5),"Muddy walks ahead? Compare prices first","Compare all-terrain pram prices from UK shops in one place.",MINT,fg=NAVY,photo_h=700)
pin=pin_hero(baby(45,1000,680,.5,.42),pin_tags("Buying guide","Pushchairs"),"All-terrain prams: what matters",
 ["Big wheels, real suspension","Air tyres: softest, can puncture","Lock the front wheel off-road","Test the handle at your height","No bags on the handle","Measure your boot first"],
 NI,250,PINK,NAVY,NAVY,"#fff","Source for bags and brakes: RoSPA, the UK accident prevention charity.","Compare pram prices at babysorted.com",line="#fff",photo_h=680,title_fs=56)
render(ROOT+"/out/e",[cover,s2,s3,s4,s5,s6,s7,s8,s9,s10],pin,CSS,NAVY)
