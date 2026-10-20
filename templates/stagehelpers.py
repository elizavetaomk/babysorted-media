NAVY="#051F45"
def stage(inner,gap=40):
    return f'<div class="stage" style="position:absolute;left:0;right:0;top:0;height:600px;padding:70px 60px 50px;display:flex;align-items:center;justify-content:center;gap:{gap}px">{inner}</div>'
def pic(src,h):
    return f'<img src="data:image/png;base64,{src}" style="height:{h}px;max-height:100%;max-width:100%;object-fit:contain;filter:drop-shadow(0 24px 24px rgba(5,31,69,.18))">'
ticks="".join(f'<div style="position:absolute;left:6px;top:{k*5}%;width:{60 if k%5==0 else 32}px;height:4px;background:{NAVY};opacity:.7"></div>' for k in range(21))
RULER_I=(f'<div style="display:flex;align-items:center;gap:18px;height:100%"><div class="h" style="font-size:52px">cm</div>'
         f'<div style="position:relative;width:70px;height:440px;max-height:100%"><div style="position:absolute;left:0;top:0;bottom:0;width:6px;background:{NAVY};border-radius:3px"></div>{ticks}</div></div>')
def ARR_I(flip):
    return f'<svg style="flex:none;transform:scaleX({-1 if flip else 1})" width="130" height="104" viewBox="0 0 150 120"><path d="M10 60 H110 M80 25 L120 60 L80 95" fill="none" stroke="{NAVY}" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/></svg>'
I_SIZE=(f'<div style="text-align:center"><div class="h" style="font-size:190px">i-Size</div>'
        f'<div style="display:inline-block;margin-top:24px;background:{NAVY};color:#fff;font-weight:800;font-size:48px;padding:14px 34px;border-radius:40px">= R129</div></div>')
