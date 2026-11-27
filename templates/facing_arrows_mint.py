# Mint "facing arrows" layout (27 Nov 2026): mint bg, product large on the top half next to a navy arrow badge that shows
# which way the seat faces, white text card at the bottom. Used for: #61 Parent-facing vs forward-facing seats. No prices.
# Buying advice is ours (no source label). Facts with labels: The Lullaby Trust product guide (babies safest sleeping flat on
# their backs; advises against sleep in a seated or inclined position, such as pushchairs) and summer safety page (don't
# cover prams with blankets or cloths: too hot and you can't see them; use a clip-on sunshade).
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css(MINT,NAVY,NAVY,"#fff")+".t2{background:#fff;box-shadow:none}"
LT="Source: The Lullaby Trust, the UK safer baby sleep charity"
VF=b("vtx_f.png",700); VP=b("vtx_p.png",900); VW=b("vtx_w.png",900); RF=b("reef.png",700); MX=b("mixx.png",800)
def arrow(label,flip=False):
    return f'''<div style="display:flex;flex-direction:column;align-items:center;gap:14px"><svg width="150" height="110" viewBox="0 0 150 110" style="transform:scaleX({-1 if flip else 1})"><path d="M10 55 H118 M84 18 L126 55 L84 92" fill="none" stroke="{NAVY}" stroke-width="18" stroke-linecap="round" stroke-linejoin="round"/></svg>
<div class="h" style="background:{NAVY};color:#fff;font-size:28px;padding:12px 22px;border-radius:30px;white-space:nowrap">{label}</div></div>'''
def top(inner): return f'<div style="position:absolute;left:50px;right:50px;top:50px;height:640px;display:flex;align-items:center;justify-content:center;gap:30px">{inner}</div>'
def slide(inner,title,body,src=""):
    s=f'<div style="font-size:23px;font-weight:700;opacity:.7;margin-top:18px">{src}</div>' if src else ""
    return top(inner)+f'''<div style="position:absolute;left:50px;right:50px;top:720px;bottom:120px;background:#fff;border-radius:40px;padding:42px 46px">
<div class="h" style="font-size:62px">{title}</div><div class="b" style="margin-top:16px;font-size:37px">{body}</div>{s}</div>'''
pimg=lambda s,h: f'<img src="{s}" style="height:{h}px;max-width:620px;object-fit:contain;{SH}">'
word=lambda a,c: f'<div style="text-align:center"><div class="h" style="font-size:150px">{a}</div><div style="font-weight:700;font-size:34px;opacity:.7;margin-top:8px">{c}</div></div>'
cover=hero_cover(baby(45,1080,800,.5,.33,1.0),'<div class="tags"><span class="tag t1">Comparison</span><span class="tag t2">Pushchairs</span></div>',
 "Parent-facing or forward-facing?","Which way should your baby look?",f'<img src="{VF}" style="height:400px;{SH}">',1,card=MINT,title_fs=72,pill="Swipe before you buy")
s2=slide(pimg(VP,560)+arrow("FACING YOU",True),"Parent-facing: you see them","You can watch their face, chat, and spot a lost dummy or a hot, sweaty head straight away. Handy in the early months.")
s3=slide(arrow("FACING OUT")+pimg(VW,560),"Forward-facing: they see the world","Curious older babies often want to see what’s coming. Some parents switch once their baby sits up and takes it all in.")
s4=slide(pimg(RF,560)+f'<div class="h" style="background:{NAVY};color:#fff;font-size:30px;padding:14px 26px;border-radius:30px;white-space:nowrap">⇄ SWAP TEST</div>',"Can the seat swap both ways?","Not every seat reverses. If you want both views, choose a reversible seat and try the swap in the shop: one click, or a wrestle?")
s5=slide(pimg(MX,580),"Does it fold with the seat on?","Some fold with the seat facing either way, some only one way, some need the seat off first. It decides how fast you get into the car.")
s6=slide(pimg(VP,560),"Check the recline both ways","Lie the seat back in each direction. Naps happen facing out too, so look for a comfy recline either way.")
s7=slide(word("Lie flat","for sleep in the early months"),"Little babies: flat for sleep","Babies are safest sleeping flat on their backs. The Lullaby Trust advises against sleep sitting up or tilted, as in a pushchair seat.",LT)
s8=slide(word("No cover","use a clip-on sunshade"),"Either way: never cover the pram","A blanket or muslin over the pram can make your baby too hot and stops you seeing them. Use a clip-on sunshade instead.",LT)
s9=hero_last(baby(31,1080,760,.5,.38,1.0),"Facing you or the world?","Compare pushchair prices from UK shops in one place.","#fff")
pin=pin_hero(baby(48,1000,660,.55,.5,1.0),pin_tags("Comparison","Pushchairs"),"Parent-facing vs forward-facing",
 ["Facing you: easy to check on them","Facing out: for curious older babies","Try the seat swap in the shop","Check the fold with the seat on","Check the recline both ways","Never cover the pram"],
 VP,250,MINT,NAVY,NAVY,"#fff",LT+" (point 6).","Compare pushchair prices at babysorted.com",line="#fff",photo_h=660,title_fs=54)
render(ROOT+"/out/c",[cover,s2,s3,s4,s5,s6,s7,s8,s9],pin,CSS,NAVY)
