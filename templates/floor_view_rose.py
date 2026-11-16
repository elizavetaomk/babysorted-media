# Deeper-pink "floor view" Parenting Tips layout (18 Nov 2026): rose bg, white rounded card with a big fact chip,
# navy number badge overlapping the card, mint "do this" strip. Photo-led cover and last slide.
# Used for: #60 Baby-proofing before they crawl. Facts: NHS baby and toddler safety page.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css(ROSE,NAVY,NAVY,"#fff")+".t2{background:#fff;box-shadow:none}"
GT=b("gate.png",900); DATE="16 Nov 2026"
deco=star(36,30,26,"#fff")+star(1004,40,30,"#fff")
def chip(a,c): return f'<div style="text-align:center"><div class="h" style="font-size:150px;line-height:1">{a}</div><div class="h" style="font-size:42px;margin-top:14px">{c}</div></div>'
def spot(k,kick,title,body,do,inner,src="Source: NHS"):
    return deco+f'''<div style="position:absolute;left:60px;right:60px;top:70px;height:520px;background:#fff;border-radius:44px;display:flex;align-items:center;justify-content:center;overflow:hidden">{inner}</div>
<div class="h" style="position:absolute;left:40px;top:40px;width:130px;height:130px;border-radius:50%;background:{NAVY};color:#fff;font-size:68px;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 10px {ROSE}">{k}</div>
<div style="position:absolute;left:70px;right:70px;top:625px"><div class="kick">{kick}</div><div class="h" style="font-size:64px;margin-top:8px">{title}</div><div class="b" style="margin-top:12px;font-size:36px">{body}</div></div>
<div style="position:absolute;left:60px;right:60px;top:1040px;background:{MINT};border-radius:28px;padding:22px 30px;display:flex;justify-content:space-between;align-items:center;gap:20px"><div style="font-weight:800;font-size:31px;line-height:1.25">{do}</div><div style="flex:none;font-size:22px;font-weight:700;opacity:.65">{src}</div></div>'''
cover=hero_cover(baby(36,1080,800,.5,.3,1.15),'<div class="tags"><span class="tag t1">Parenting Tips</span><span class="tag t2">Kids Furniture</span></div>',"Baby-proofing before they crawl","6 jobs to do while they're still on their back.",f'<img src="{GT}" style="height:230px;{SH}">',1,card=ROSE,fg=NAVY,pill_bg=NAVY,pill_fg="#fff",title_fs=66)
s2=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="kick">START HERE</div><div class="h" style="font-size:86px;margin-top:8px">Get down on the floor and look around</div></div>
<div style="position:absolute;left:60px;right:60px;top:440px;background:#fff;border-radius:44px;padding:46px 50px">
<div class="b" style="font-size:40px">That's your baby's view. Cords, plugs, low shelves, the bin. Do it before they move, because once they crawl, they're fast.</div>
<div style="margin-top:28px;display:flex;gap:14px;flex-wrap:wrap"><span class="pill" style="background:{PINK}">hands and knees</span><span class="pill" style="background:{MINT}">10 minutes</span><span class="pill" style="background:{ROSE}">every room</span></div></div>
<div class="b" style="position:absolute;left:70px;right:70px;top:930px;font-size:38px">Then work through these 6 jobs. All of them come from NHS safety advice.</div>'''
gate=f'''<div style="display:flex;align-items:center;gap:30px"><img src="{GT}" style="height:400px;{SH}"><div><div class="h" style="font-size:58px">£25.95</div><div style="font-size:22px;font-weight:600;opacity:.7;line-height:1.3;margin-top:6px">BabyDan Multidan Metal<br>Safety Gate, white<br>Price on BabySorted, {DATE}</div></div></div>'''
S=[spot(1,"STAIRS","Gates at the top and the bottom","Fit gates that meet BS EN 1930:2011 at both ends of the stairs. Keep them up until your child is at least 2.","Check the label for BS EN 1930 before you buy.",gate),
spot(2,"WINDOWS","Blind and curtain cords","A loose loop can wrap around a child's neck. Tie cords up out of reach and fix them to a surface, with a cleat or a cord tidy.","Check every room, not just the nursery.",chip("Tie up","and fix to the wall")),
spot(3,"GADGETS","Button batteries","Swallowed, a small round battery can cause severe internal burns. Remotes, car keys, scales and light-up toys often use them.","Check every battery cover is screwed shut.",chip("Coin size","danger")),
spot(4,"KITCHEN","Hot drinks","A hot drink can still scald 15 minutes after it was made. Keep mugs well away from edges and little hands.","Put your mug down before you pick up your baby.",chip("15 min","still hot enough to scald")),
spot(5,"WINDOWS","Window catches","Fit locks or safety catches that stop windows opening more than 6.5cm. Move sofas, beds and low furniture away from windows.","Climbable furniture goes away from windows.",chip("6.5cm","max opening")),
spot(6,"OUT OF SIGHT","High up, out of sight","Medicines locked away or high up. Laundry capsules, cleaning products, nappy sacks and small magnets out of reach and sight.","Out of reach is not enough: out of sight too.",chip("High up","and out of sight"))]
s9=hero_last(baby(30,1080,700,.5,.4),"Choosing a stair gate? Compare prices first","Compare safety gate prices from UK shops in one place.",PINK,fg=NAVY,photo_h=700,note="Emergency: call 999. Urgent but not an emergency: NHS 111 (England, free from landlines and mobiles).")
pin=pin_hero(baby(31,1000,680,.5,.4),pin_tags("Parenting Tips","Kids Furniture"),"Baby-proofing before they crawl",["Gates at the top and bottom of stairs","Blind cords tied up and fixed","Button batteries locked away","Hot drinks well out of reach","Window catches: 6.5cm max","Medicines and capsules out of sight"],GT,240,ROSE,NAVY,NAVY,"#fff","Source: NHS. Stair gates to BS EN 1930:2011, until at least age 2.","Compare safety gate prices at babysorted.com",line="#fff",photo_h=680,title_fs=56)
render(ROOT+"/out/d",[cover,s2]+S+[s9],pin,CSS,NAVY)
