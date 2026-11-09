# Rose "swap cards" layout: deeper-pink bg; each mistake slide = product on a white card with a navy "MISTAKE" sticker,
# then a mint "DO THIS INSTEAD" strip. Used for: 5 feeding gear mistakes new parents make (9 Nov 2026). Facts: NHS.
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css(ROSE,NAVY,NAVY,"#fff")+".t2{background:#fff;box-shadow:none}"
deco=star(36,30,26,"#fff")+star(1000,40,30,"#fff")
ST=b("ster2.png",1000); CUP=b("cup.png",900); BR=b("brush.png",900); BO=b("bibs.png",1000)
DATE="9 Nov 2026"
def sticker(k): return f'<div style="position:absolute;left:60px;top:60px;background:{NAVY};color:#fff;border-radius:22px;padding:14px 24px;transform:rotate(-4deg);font-weight:800;font-size:30px;letter-spacing:.05em;z-index:2">MISTAKE {k} OF 5</div>'
def mis(k,title,body,instead,vis,src,price=""):
    pr=f'<div style="position:absolute;right:34px;bottom:26px;text-align:right"><div class="h" style="font-size:46px">{price[0]}</div><div style="font-size:21px;font-weight:600;opacity:.7;max-width:330px">{price[1]}<br>Price on BabySorted, {DATE}</div></div>' if price else ""
    return deco+sticker(k)+f'''<div style="position:absolute;left:60px;right:60px;top:60px;height:520px;background:#fff;border-radius:44px;display:flex;align-items:center;justify-content:center;overflow:hidden">{vis}{pr}</div>
<div style="position:absolute;left:70px;right:70px;top:615px"><div class="h" style="font-size:66px">{title}</div><div class="b" style="margin-top:14px;font-size:38px">{body}</div></div>
<div style="position:absolute;left:60px;right:60px;top:1010px;background:{MINT};border-radius:30px;padding:22px 30px"><div style="font-weight:800;font-size:24px;letter-spacing:.06em;opacity:.6">DO THIS INSTEAD</div><div class="h" style="font-size:38px;margin-top:6px;line-height:1.15">{instead}</div></div>
<div style="position:absolute;left:70px;right:70px;top:1210px;font-size:26px;font-weight:700;opacity:.6">{src}</div>'''
img=lambda s,h,x="": f'<img src="{s}" style="height:{h}px;max-width:88%;object-fit:contain;{SH};{x}">'
cover=star(980,60,36,"#fff")+star(1000,560,24,"#fff")+f'''<div style="position:absolute;left:70px;right:70px;top:70px"><div class="tags"><span class="tag t1">Tips</span><span class="tag t2">Nursing &amp; Feeding</span></div>
<div class="h" style="font-size:100px;margin-top:28px">5 feeding gear mistakes new parents make</div>
<div style="font-size:44px;font-weight:700;margin-top:18px">Buy less at first. Here's why.</div></div>
<div style="position:absolute;left:60px;right:60px;top:600px;height:610px;background:#fff;border-radius:44px;overflow:hidden">
<img src="{baby(7,440,570,.38,.55,1.15)}" style="position:absolute;left:20px;top:20px;width:440px;height:570px;border-radius:32px;object-fit:cover">
<img src="{ST}" style="position:absolute;left:540px;top:45px;height:370px;{SH}"><img src="{CUP}" style="position:absolute;right:60px;bottom:35px;height:235px;{SH}"></div>
<div style="position:absolute;left:100px;top:1110px;background:{NAVY};color:#fff;font-weight:700;font-size:30px;padding:14px 26px;border-radius:40px">Swipe before you buy</div>'''
s2=deco+f'''<div style="position:absolute;left:70px;right:70px;top:80px"><div class="kick">START HERE</div></div>
<div style="position:absolute;left:60px;right:60px;top:140px;background:#fff;border-radius:44px;padding:44px 50px"><div class="h" style="font-size:150px;line-height:.7;color:{ROSE}">“</div><div class="h" style="font-size:74px;margin-top:-6px">There's no evidence that 1 type of teat or bottle is better than any other.</div><div style="font-size:32px;font-weight:700;opacity:.6;margin-top:22px">Source: NHS</div></div>
<div style="position:absolute;left:60px;right:60px;top:720px;background:{NAVY};color:#fff;border-radius:34px;padding:44px 50px"><div class="h" style="font-size:66px">So the fancy kit can wait.</div><div class="b" style="font-size:40px;margin-top:16px">Here are 5 places parents overspend, or buy the wrong thing, in the first year.</div></div>'''
s3=mis(1,"Paying extra for a “special” bottle","The NHS says simple bottles that are easy to clean are likely to be best. Start with a few and see how your baby gets on.","Buy a small starter set, not a cupboard full.",img(BO,430,"margin-right:300px"),"Source: NHS",("£23.96","BIBS glass bottles, 2 pack"))
F1=f'''<div style="text-align:center"><div class="h" style="font-size:200px;line-height:.9">1</div><div class="h" style="font-size:52px">formula for the first year</div><div style="margin-top:22px"><span class="pill" style="background:{MINT}">First infant formula</span></div></div>'''
s4=mis(2,"Stocking up on follow-on or “hungry baby” milk","First infant formula is the only formula your baby needs in year one. Switching to follow-on at 6 months has no benefits. Hungry baby milk: no evidence babies settle or sleep longer.","Ask your midwife or health visitor before you switch.",F1,"Source: NHS")
s5=mis(3,"Thinking the dishwasher sterilises","A dishwasher cleans bottles, but it doesn't sterilise them. Keep sterilising bottles and teats until your baby is at least 12 months old.","Wash, rinse, then sterilise. Every feed, for a year.",img(ST,420,"margin-right:300px"),"Source: NHS",("£89.99","Momcozy steriliser and dryer"))
s6=mis(4,"Using the kitchen brush","Keep one clean brush only for bottles. Check teats and bottles often for tears and cracks. And never clean teats with salt: it can be dangerous for your baby.","One brush, bottles only. Bin damaged teats.",img(BR,440,"margin-right:300px"),"Source: NHS",("£2.49","Jane bottle brush with sponge"))
s7=mis(5,"Buying a “non-spill” valve cup","From about 6 months, an open cup or a free-flow cup without a valve helps your baby learn to sip. It's better for teeth. From age 1, move away from bottles.","Look for an open or free-flow cup.",img(CUP,380,"margin-right:300px"),"Source: NHS",("£12.80","Mamas &amp; Papas 3-in-1 cup, works as an open cup"))
s8=star(36,30,26,"#fff")+f'''{round_pic(baby(13,960,560,.5,.4),60,60,960,560,44)}
<div style="position:absolute;left:70px;right:70px;top:650px"><div class="h" style="font-size:78px">Buying bottles? Compare prices first</div>
<div class="b" style="margin-top:18px;font-size:38px">Compare feeding gear prices from UK shops in one place.</div>
<div style="margin-top:30px">{link_row("#fff")}</div>
<div style="margin-top:20px;font-size:32px;font-weight:700;opacity:.6">Save this post for later</div></div>'''
L=[("A “special” bottle","No evidence one type is better. Keep it simple."),("Follow-on or hungry baby milk","First infant formula is all year one needs."),("Dishwasher = sterile?","No. Sterilise until at least 12 months."),("The kitchen brush","One brush for bottles only. Never salt on teats."),("Valve “non-spill” cups","Open or free-flow cup from about 6 months.")]
ls="".join(f'<div style="display:flex;align-items:center;gap:20px;padding:15px 0;border-top:{"0" if i==0 else f"3px solid {ROSE}"}"><div class="h" style="flex:none;width:58px;height:58px;border-radius:50%;background:{NAVY};color:#fff;font-size:30px;display:flex;align-items:center;justify-content:center">{i+1}</div><div><div class="h" style="font-size:35px">{a}</div><div style="font-size:26px;font-weight:500;opacity:.85;margin-top:2px">{c}</div></div></div>' for i,(a,c) in enumerate(L))
pin=f'''{star(920,44,30,"#fff")}<div style="position:absolute;left:60px;right:60px;top:56px"><div class="tags"><span class="tag t1" style="font-size:24px">Tips</span><span class="tag t2" style="font-size:24px">Nursing &amp; Feeding</span></div>
<div class="h" style="font-size:72px;margin-top:20px">5 feeding gear mistakes new parents make</div></div>
<div style="position:absolute;left:60px;right:60px;top:360px;height:330px;background:#fff;border-radius:34px;display:flex;align-items:center;justify-content:center;gap:60px"><img src="{ST}" style="height:270px;{SH}"><img src="{CUP}" style="height:200px;{SH}"><img src="{BR}" style="height:270px;{SH}"></div>
<div style="position:absolute;left:60px;right:60px;top:715px;background:#fff;border-radius:34px;padding:12px 34px 14px">{ls}</div>
<div style="position:absolute;left:60px;right:60px;top:1300px;background:{NAVY};color:#fff;border-radius:24px;padding:16px 26px;font-size:26px;font-weight:600;line-height:1.3">Thinking of switching formula? Ask your midwife or health visitor first. Source: NHS.</div>
<div style="position:absolute;left:60px;right:60px;bottom:30px;display:flex;justify-content:space-between;align-items:center"><div class="brand" style="font-size:34px">BabySorted</div><div style="font-weight:700;font-size:25px">Compare feeding gear prices at babysorted.com</div></div>'''
render(ROOT+"/out/a",[cover,s2,s3,s4,s5,s6,s7,s8],pin,CSS,NAVY)
