// Screenshots real product cards from babysorted.com/catalog for "catalog" slides. Needs @supabase/supabase-js@2.45.4 unpacked to ./sb (the proxy blocks the floating @2 CDN URL).
const {chromium}=require('playwright');
const Q=[["egg3","egg 3 stroller carbonite","£703.20"],["metro3","ergobaby metro 3 natural beige","£219.90"],["snoozi","snoozi bassinet","£144.95"],["michair","icandy michair white","£169.00"],["oneair","babybjorn one air anthracite","Anthracite"],["pebble2","pebble 360 pro 2 twillic black","£179.00"]];
(async()=>{const b=await chromium.launch();
const c=await b.newContext({viewport:{width:1280,height:1600},deviceScaleFactor:2,locale:'en-GB'});
await c.route(/supabase-js@2\/dist/,r=>r.fulfill({path:__dirname+'/sb/package/dist/umd/supabase.js',contentType:'application/javascript'}));
const p=await c.newPage();
await p.goto('https://babysorted.com/catalog',{waitUntil:'networkidle',timeout:60000});
await p.getByText('United Kingdom').first().click().catch(()=>{});
await p.addStyleTag({content:'.bl-modal,.bl-modal-card,[class*=cookie],[class*=consent],[class*=mascot],[class*=float]{display:none!important}'});
for(const [k,q,price] of Q){
  await p.fill('#searchInput',q);await p.keyboard.press('Enter');
  await p.waitForTimeout(2500);
  await p.waitForFunction(()=>!/Loading products/.test(document.body.innerText),null,{timeout:60000}).catch(()=>{});
  await p.waitForTimeout(2500);
  await p.addStyleTag({content:'.bl-modal,.bl-modal-card,[class*=cookie],[class*=consent]{display:none!important}'});
  const cards=await p.$$('.product-card');let done=false;
  for(const el of cards){const t=await el.innerText();if(t.includes(price)&&(k!="oneair"||t.includes("£109.95"))){await el.scrollIntoViewIfNeeded();await p.waitForTimeout(800);await p.evaluate(()=>{document.querySelectorAll('body *').forEach(e=>{const cs=getComputedStyle(e);if(cs.position=='fixed'||cs.position=='sticky')e.remove()});document.body.style.overflow='auto'});await p.waitForTimeout(300);await el.screenshot({path:`cards/${k}.png`});console.log(k,'OK',t.replace(/\n/g,' / ').slice(0,140));done=true;break;}}
  if(!done)console.log(k,'NOT FOUND',cards.length);
}
await b.close();})();
