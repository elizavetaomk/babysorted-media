from playwright.sync_api import sync_playwright
import base64, os, io
from PIL import Image
PINK="#F1D3DF"; NAVY="#051F45"; ROSE="#E6B6C9"; MINT="#DDF5E3"
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def b(name,maxw=1100):
    p=f"{ROOT}/cut/{name}"; im=Image.open(p)
    if im.width>maxw: im=im.resize((maxw,int(im.height*maxw/im.width)),Image.LANCZOS)
    f=io.BytesIO()
    if name.endswith('.png'): im.save(f,'PNG'); m='image/png'
    else: im.convert('RGB').save(f,'JPEG',quality=92); m='image/jpeg'
    return f"data:{m};base64,"+base64.b64encode(f.getvalue()).decode()
def star(x,y,s,c,o=1): return f'<svg style="position:absolute;left:{x}px;top:{y}px;opacity:{o}" width="{s}" height="{s}" viewBox="0 0 20 20"><path d="M10 0l2.6 7.4L20 10l-7.4 2.6L10 20l-2.6-7.4L0 10l7.4-2.6z" fill="{c}"/></svg>'
def css(bg,fg,tag1bg,tag1fg,w=1080,h=1350):
    return f"""*{{margin:0;padding:0;box-sizing:border-box}} body{{width:{w}px;height:{h}px;background:{bg};font-family:Inter;color:{fg};position:relative;overflow:hidden}}
.h{{font-weight:800;letter-spacing:-0.035em;line-height:1.05}}
.tags{{display:flex;gap:14px}} .tag{{font-weight:700;font-size:28px;padding:9px 22px;border-radius:30px}}
.t1{{background:{tag1bg};color:{tag1fg}}} .t2{{background:transparent;box-shadow:inset 0 0 0 3px {fg}}}
.kick{{font-weight:800;font-size:28px;letter-spacing:.06em;opacity:.6}}
.foot{{position:absolute;left:70px;right:70px;bottom:50px;display:flex;justify-content:space-between;align-items:center}}
.brand{{font-weight:800;font-size:36px;letter-spacing:-0.03em}}
.pill{{display:inline-block;font-weight:800;font-size:30px;padding:13px 24px;border-radius:24px;white-space:nowrap}}
.b{{font-size:37px;font-weight:500;line-height:1.36}}
.c{{color:{NAVY}}}"""
def foot(i,n,fg):
    d="".join(f'<div style="width:{40 if j==i else 14}px;height:14px;border-radius:7px;background:{fg};opacity:{1 if j==i else .25}"></div>' for j in range(n))
    return f'<div class="foot"><div class="brand">BabySorted</div><div style="display:flex;gap:12px">{d}</div></div>'
def render(out,bodies,pin,CSS,fg,PINCSS=None):
    os.makedirs(out,exist_ok=True); n=len(bodies)
    with sync_playwright() as p:
        br=p.chromium.launch(); pg=br.new_page(viewport=dict(width=1080,height=1350))
        ov=[]
        for i,bd in enumerate(bodies):
            pg.set_content(f"<html><head><style>{CSS}</style></head><body>{bd}{foot(i,n,fg)}</body></html>"); pg.wait_for_timeout(350)
            r=pg.evaluate("""()=>{const f=document.querySelector('.foot').getBoundingClientRect().top;let w=[];document.querySelectorAll('body *').forEach(e=>{if(e.closest('.foot')||e.tagName=='svg'||e.closest('svg')||e.tagName=='IMG')return;const r=e.getBoundingClientRect();if(e.children.length==0&&e.textContent.trim()&&(r.bottom>f-4||r.right>1080||r.left<0))w.push(e.textContent.slice(0,40)+' b='+Math.round(r.bottom))
            if(e.children.length==0 && e.scrollWidth>e.clientWidth+1 && getComputedStyle(e).display!='inline') w.push('OVERX '+e.textContent.slice(0,40))});return w}""")
            if r: ov.append((i+1,r))
            pg.screenshot(path=f"{out}/slide_{i+1}.png")
        pg2=br.new_page(viewport=dict(width=1000,height=1500),device_scale_factor=2)
        pg2.set_content(f"<html><head><style>{(PINCSS or CSS).replace('width:1080px;height:1350px','width:1000px;height:1500px')}</style></head><body>{pin}</body></html>"); pg2.wait_for_timeout(350)
        pg2.screenshot(path=f"{out}/pin.png"); br.close()
    if ov: print('OVERFLOW',ov)
    W=Image.new('RGB',(1800,920),'#bbb')
    for k in range(n): W.paste(Image.open(f'{out}/slide_{k+1}.png').resize((352,440)),((k%5)*360,(k//5)*460))
    W.save(f'{out}/preview.png')
    Image.open(f'{out}/pin.png').resize((667,1000)).save(f'{out}/pinp.png')
