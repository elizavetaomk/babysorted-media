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
