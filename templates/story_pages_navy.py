# Navy "story pages" layout (27 Nov 2026): navy bg, a white open-book card (two pages with a spine line) on the top half
# holding a book or a short keyword, a pink page-number badge, white text below. Used for: Parenting Tips #70 Reading to
# your baby. No prices.
# Facts: NHS "Baby and toddler play ideas" (start looking at books early; babies enjoy hearing you read before they talk;
# small babies like picture books; Bookstart Baby pack in the first year, usually from your health visitor);
# NHS Best Start in Life "First sounds 0-6 months" (face-to-face time; talk about what you're doing; fabric books with
# textures; watch what interests them) and "Listening and learning 6-12 months" (simple picture books, describe the pictures;
# mention what your baby is looking at; repeat songs and rhymes; copy them back; take turns; avoid screen time; libraries free).
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from extras import *
CSS=css(NAVY,"#fff",PINK,NAVY)+".t2{background:transparent;box-shadow:inset 0 0 0 3px #fff;color:#fff}"
NHS="Source: NHS"; BSL="Source: NHS Best Start in Life"
BF=b("bfs.png",800); SA=b("safari.png",700); SO=b("safari_open.png",900); BA=b("bath.png",700); AV=b("avery.png",800)
def book(inner,n):
    return f'''<div style="position:absolute;left:80px;right:80px;top:70px;height:540px;background:#fff;border-radius:28px 28px 40px 40px;box-shadow:0 22px 0 -8px {ROSE}"></div>
<div style="position:absolute;left:539px;top:90px;height:500px;width:2px;background:{NAVY};opacity:.12"></div>
<div style="position:absolute;left:80px;right:80px;top:70px;height:540px;display:flex;align-items:center;justify-content:center;text-align:center;color:{NAVY}">{inner}</div>
<div class="h" style="position:absolute;right:60px;top:40px;width:100px;height:100px;border-radius:50%;background:{PINK};color:{NAVY};font-size:50px;display:flex;align-items:center;justify-content:center">{n}</div>'''
def slide(inner,n,title,body,src=BSL):
    s=f'<div style="position:absolute;left:70px;right:70px;top:1190px;font-size:23px;font-weight:700;opacity:.75">{src}</div>' if src else ""
    return book(inner,n)+f'''<div style="position:absolute;left:70px;right:70px;top:690px"><div class="h" style="font-size:66px">{title}</div>
<div class="b" style="margin-top:16px;font-size:38px;opacity:.92">{body}</div></div>{s}'''
pimg=lambda s,h,w=820: f'<img src="{s}" style="max-height:{h}px;max-width:{w}px;object-fit:contain;filter:drop-shadow(0 14px 14px rgba(5,31,69,.18))">'
word=lambda a,c,fs=140: f'<div><div class="h" style="font-size:{fs}px">{a}</div><div style="font-weight:700;font-size:34px;opacity:.65;margin-top:10px">{c}</div></div>'
cover=hero_cover(baby(50,1080,800,.45,.5,1.0),'<div class="tags"><span class="tag t1">Parenting Tips</span><span class="tag t2">Play &amp; Development</span></div>',
 "Reading to your baby: start now","It’s never too early for a book.",f'<img src="{BF}" style="width:270px;border-radius:10px;{SH}">',1,card=NAVY,fg="#fff",pill_bg=PINK,pill_fg=NAVY,title_fs=74,pill="Swipe for 7 tips")
s2=slide(word("Day one","is not too early"),1,"It’s never too early","Even before babies can talk, they enjoy hearing you read. Even small babies like looking at picture books.",NHS)
s3=slide(pimg(BF,450,420),2,"Your face is the first picture","Hold your baby close, face to face, and talk about what you’re doing, from nappy changes to the walk to the shops.")
s4=slide(pimg(AV,470,520),3,"0–6 months: books to touch","Fabric books with different textures are a great start. Talk about how each page feels: soft, crinkly, bumpy.")
s5=slide(pimg(SO,400,760),4,"Name what they’re looking at","Watch what catches their eye and name it. From 6 months, look at simple picture books together and describe the pictures.")
s6=slide(word("Again!","same songs, same rhymes"),5,"Repeat, repeat, repeat","Sing the same songs and rhymes again and again. If your baby copies a sound, say it back to them.")
s7=slide(pimg(BA,430,520),6,"Take turns, like a chat","Say something, then pause so your baby can ‘answer’ with a coo or babble. Then it’s your turn again.")
s8=slide(word("Free","books and story times",150),7,"Books don’t have to cost a thing","Look out for a free Bookstart Baby pack in the first year, usually from your health visitor. Libraries are free, and some run baby story times.",NHS)
s9=hero_last(baby(13,1080,760,.5,.35,1.0),"Read, chat, repeat","Compare baby book and toy prices from UK shops in one place.",PINK,fg="#fff")
pin=pin_hero(baby(27,1000,660,.5,.35,1.0),pin_tags("Parenting Tips","Play &amp; Development"),"Reading to your baby: 6 easy habits",
 ["Start from day one","Face to face, talk all day","Touch-and-feel books first","Name what they look at","Repeat songs and rhymes","Take turns: pause for babble"],
 SA,300,NAVY,"#fff",PINK,NAVY,BSL+".","Compare baby book prices at babysorted.com",line="rgba(255,255,255,.2)",photo_h=660,title_fs=54)
render(ROOT+"/out/d",[cover,s2,s3,s4,s5,s6,s7,s8,s9],pin,CSS,"#fff")
