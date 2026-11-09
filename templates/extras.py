# Helpers added Nov 2026 for baby photos on covers and last slides. Baby source files stay in the private library, never in this repo.
import os,hashlib
from slide_lib import *
BABY=os.environ.get("BABY_DIR","")
def baby(n,w,h,cx=.5,cy=.5,zoom=1.0):
    """Crop photo baby_NN to w:h around (cx,cy); zoom>1 = tighter. Returns a data URI."""
    p=f"{BABY}/baby_{n:02d}.jpg"; im=Image.open(p).convert('RGB'); W,H=im.size
    r=w/h
    cw=min(W,H*r)/zoom; ch=cw/r
    x=max(0,min(W-cw,cx*W-cw/2)); y=max(0,min(H-ch,cy*H-ch/2))
    im=im.crop((int(x),int(y),int(x+cw),int(y+ch))).resize((w*2,h*2),Image.LANCZOS)
    f=io.BytesIO(); im.save(f,'JPEG',quality=90)
    return "data:image/jpeg;base64,"+base64.b64encode(f.getvalue()).decode()
def round_pic(src,x,y,w,h,r=40,ring=None):
    s=f"box-shadow:0 0 0 10px {ring};" if ring else ""
    return f'<img src="{src}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:{r}px;object-fit:cover;{s}">'
SH="filter:drop-shadow(0 18px 18px rgba(5,31,69,.20))"
def prod(name,h,extra=""):
    return f'<img src="{b(name)}" style="height:{h}px;max-width:100%;object-fit:contain;{SH};{extra}">'
def link_row(bg,fs=46):
    return f'''<div style="display:flex;align-items:center;gap:16px"><div class="h" style="font-size:{fs}px;background:{bg};color:{NAVY};padding:22px 30px;border-radius:24px;white-space:nowrap">babysorted.com/links</div>
<div style="background:{NAVY};color:#fff;font-weight:800;font-size:32px;padding:22px 26px;border-radius:24px;white-space:nowrap;box-shadow:0 0 0 3px #fff">Link in bio ↑</div></div>'''
# Photo-led cover and last slide (owner's request, 9 Nov 2026: bigger baby photos). The product sits inside the card, never on the photo.
def hero_cover(photo,tags,title,sub,prod,prod_h,card="#fff",fg=NAVY,pill_bg=NAVY,pill_fg="#fff",pill="Swipe before you buy",title_fs=76,photo_h=800):
    return f'''<img src="{photo}" style="position:absolute;left:0;top:0;width:1080px;height:{photo_h}px;object-fit:cover">
<div style="position:absolute;left:60px;top:{photo_h-110}px;background:{pill_bg};color:{pill_fg};font-weight:700;font-size:28px;padding:12px 24px;border-radius:40px">{pill}</div>
<div style="position:absolute;left:0;right:0;top:{photo_h-20}px;bottom:0;background:{card};border-radius:44px 44px 0 0"></div>
<div style="position:absolute;left:60px;top:{photo_h+20}px;width:{1080-120-(prod_h and 300)}px;color:{fg}">{tags}<div class="h" style="font-size:{title_fs}px;margin-top:18px">{title}</div><div style="font-size:32px;font-weight:600;opacity:.75;margin-top:12px">{sub}</div></div>
{f'<div style="position:absolute;right:50px;top:{photo_h+10}px;width:290px;height:{1350-photo_h-130}px;display:flex;align-items:center;justify-content:center">{prod}</div>' if prod else ''}'''
def hero_last(photo,title,body,link_bg,fg=NAVY,photo_h=760,note=""):
    nt=f'<div style="font-size:28px;font-weight:700;margin-bottom:14px;opacity:.85">{note}</div>' if note else ""
    return f'''<img src="{photo}" style="position:absolute;left:0;top:0;width:1080px;height:{photo_h}px;object-fit:cover;border-radius:0 0 44px 44px">
<div style="position:absolute;left:70px;right:70px;top:{photo_h+36}px;color:{fg}">{nt}<div class="h" style="font-size:66px">{title}</div>
<div class="b" style="margin-top:12px;font-size:34px">{body}</div>
<div style="margin-top:24px">{link_row(link_bg,42)}</div></div>'''
