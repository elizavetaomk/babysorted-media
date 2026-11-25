# White "swing tag" layout (25 Nov 2026): white bg, a deeper-pink swing tag (hole + string) carrying the label wording,
# product on the right, navy text below. Used for: #56 What "from birth" really means on a pushchair.
# Facts: The Lullaby Trust product guide (pram: completely lie-flat for sleep, not just reclined; mattress firm, flat, waterproof;
# carry cots BS EN 1466), The Lullaby Trust car seats page (not for long sleeps; take baby out on arrival, firm flat surface).
# Catalog: Stokke YOYO5 6+ needs the newborn pack to be used from birth; Joolz Aer2 "from birth to 22kg", lie-flat seat (maker).
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css("#fff",NAVY,NAVY,"#fff")+f".t2{{background:{ROSE};box-shadow:none}}"
DATE="22 Nov 2026"; LT="Source: The Lullaby Trust, the UK safer baby sleep charity"
AE=b("aer2.png",900); YO=b("yoyo.png",800); YN=b("yoyonb.png",700); IS=b("isnug.png",700)
def tag(text,fs=64,w=560,rot=-6):
    return f'''<div style="position:relative;transform:rotate({rot}deg);width:{w}px">
<svg width="170" height="90" style="position:absolute;left:-120px;top:20px"><path d="M10 10 C60 0,110 70,165 50" fill="none" stroke="{NAVY}" stroke-width="5" stroke-linecap="round"/></svg>
<div style="background:{ROSE};border-radius:28px 28px 28px 28px;clip-path:polygon(16% 0,100% 0,100% 100%,16% 100%,0 50%);padding:40px 40px 40px 150px;position:relative">
<div style="position:absolute;left:62px;top:50%;width:40px;height:40px;margin-top:-20px;border-radius:50%;background:#fff"></div>
<div class="h" style="font-size:{fs}px;line-height:1.02">{text}</div></div></div>'''
def slide(kick,tg,title,body,img=None,h=380,src=None,tfs=64):
    s=f'<div style="position:absolute;left:70px;right:70px;top:1180px;font-size:22px;font-weight:700;opacity:.75">{src}</div>' if src else ""
    pic=f'<img src="{img}" style="max-height:{h}px;max-width:400px;object-fit:contain;{SH}">' if img else ""
    return f'''<div style="position:absolute;left:70px;top:70px" class="kick">{kick}</div>
<div style="position:absolute;left:150px;top:200px">{tag(tg,tfs,560 if img else 760)}</div>
<div style="position:absolute;right:50px;top:110px;width:420px;height:560px;display:flex;align-items:center;justify-content:center">{pic}</div>
<div style="position:absolute;left:70px;right:70px;top:720px"><div class="h" style="font-size:60px">{title}</div><div class="b" style="margin-top:16px;font-size:35px">{body}</div></div>{s}'''
cover=hero_cover(baby(16,1080,800,.5,.55,1.0),f'<div class="tags"><span class="tag t1">Tips</span><span class="tag t2">Pushchairs</span></div>',"What ‘from birth’ really means on a pushchair","Two words that don’t mean the same on every box.",f'<img src="{AE}" style="height:330px;{SH}">',1,card="#fff",fg=NAVY,title_fs=66)
def col(img,h,lab,sub): return f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;text-align:center"><img src="{img}" style="max-height:{h}px;max-width:95%;object-fit:contain;{SH}"><div class="h" style="margin-top:22px;background:{ROSE};font-size:30px;padding:12px 20px;border-radius:20px;line-height:1.1">{lab}</div><div style="font-size:24px;font-weight:600;opacity:.7;margin-top:8px">{sub}</div></div>'
s2=f'''<div style="position:absolute;left:70px;top:70px" class="kick">THREE SET-UPS</div>
<div style="position:absolute;left:40px;right:40px;top:130px;height:560px;display:flex;gap:20px">{col(AE,380,"Lie-flat seat","seat lies fully flat")}{col(YN,330,"Carrycot or newborn pack","often sold extra")}{col(IS,270,"Car seat on the frame","for short trips")}</div>
<div style="position:absolute;left:70px;right:70px;top:740px"><div class="h" style="font-size:60px">Same two words, three different set-ups</div><div class="b" style="margin-top:16px;font-size:35px">‘From birth’ can mean any of these. Check which one the box means before you pay.</div></div>'''
flat=f'''<div style="display:flex;flex-direction:column;gap:46px;align-items:flex-start">
<div style="display:flex;align-items:center;gap:26px"><svg width="300" height="70"><line x1="10" y1="35" x2="290" y2="35" stroke="{NAVY}" stroke-width="16" stroke-linecap="round"/></svg><div class="h" style="font-size:46px">✓</div></div>
<div style="display:flex;align-items:center;gap:26px"><svg width="300" height="110"><line x1="10" y1="95" x2="290" y2="15" stroke="{NAVY}" stroke-width="16" stroke-linecap="round" opacity=".35"/></svg><div class="h" style="font-size:46px;opacity:.4">✗</div></div></div>'''
s3=f'''<div style="position:absolute;left:70px;top:70px" class="kick">1 · FOR SLEEP</div>
<div style="position:absolute;left:150px;top:200px">{tag("Flat, not just reclined",60,520)}</div>
<div style="position:absolute;right:70px;top:150px;width:380px;height:500px;display:flex;align-items:center;justify-content:center">{flat}</div>
<div style="position:absolute;left:70px;right:70px;top:720px"><div class="h" style="font-size:60px">Reclined is not the same as lie-flat</div><div class="b" style="margin-top:16px;font-size:35px">If your baby sleeps in the pushchair, they need to lie completely flat, not just reclined. Check the seat goes all the way.</div></div>
<div style="position:absolute;left:70px;right:70px;top:1180px;font-size:22px;font-weight:700;opacity:.75">{LT}.</div>'''
def pr(img,h,p,n): return f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;text-align:center"><img src="{img}" style="max-height:{h}px;max-width:95%;object-fit:contain;{SH}"><div class="h" style="font-size:52px;margin-top:14px">{p}</div><div style="font-size:24px;font-weight:700;opacity:.75;line-height:1.25">{n}</div></div>'
s4=f'''<div style="position:absolute;left:70px;top:70px" class="kick">2 · CHECK THE BOX</div>
<div style="position:absolute;left:60px;right:60px;top:130px;height:560px;display:flex;gap:30px;align-items:flex-end">{pr(YO,380,"£379.00","On its own:<br>from 6 months")}<div class="h" style="font-size:80px;align-self:center">→</div>{pr(YN,340,"£479.00","With newborn pack:<br>from birth")}</div>
<div style="position:absolute;left:70px;right:70px;top:740px"><div class="h" style="font-size:60px">Some only work from birth with an extra</div><div class="b" style="margin-top:16px;font-size:35px">Stokke YOYO5: the seat is 6 months+. From birth you need the newborn pack, about £100 more.</div></div>
<div style="position:absolute;left:70px;right:70px;top:1180px;font-size:22px;font-weight:700;opacity:.75">Prices on BabySorted, {DATE}.</div>'''
s5=slide("3 · TRAVEL SYSTEMS","Short trips only","A car seat on wheels isn’t a bed","Car seats aren’t made for long sleeps. When you arrive, lift your baby out and lay them on a firm, flat surface.",IS,300,LT+".",tfs=60)
s6=slide("4 · CARRYCOT AT HOME","BS EN 1466","Using the carrycot as a bed?","Look for BS EN 1466 on the label. Keep the mattress firm, flat and waterproof, with no extra padding.",YN,330,LT+".",tfs=66)
s7=slide("5 · READ THE WHOLE LINE","From birth to 22kg","The weight limit tells you more","‘From birth’ is only half the label. Check the weight limit, when to move on, and read the instructions before your first walk.",AE,400,None,tfs=58)
s8=hero_last(baby(51,1080,760,.5,.45),"Found the right one? Compare prices","Compare pushchair prices from UK shops in one place.",ROSE,fg=NAVY)
pin=pin_hero(baby(45,1000,660,.5,.35,1.1),pin_tags("Tips","Pushchairs"),"‘From birth’ on a pushchair",
 ["Lie-flat seat, carrycot or car seat?","For sleep: flat, not just reclined","Some need a newborn pack, extra","Car seat: short trips, not long naps","Carrycot as a bed? BS EN 1466","Check the weight limit too"],
 AE,300,"#fff",NAVY,ROSE,NAVY,"Source: The Lullaby Trust, the UK safer baby sleep charity.","Compare pushchair prices at babysorted.com",line=PINK,photo_h=660,title_fs=56)
render(ROOT+"/out/b",[cover,s2,s3,s4,s5,s6,s7,s8],pin,CSS,NAVY)
