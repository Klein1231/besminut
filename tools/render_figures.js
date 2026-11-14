// usage: node tools/render_figures.js "<course name substring>" "<lesson title substring>" [outprefix] [maxParts]
const {chromium}=require('playwright');
(async()=>{const [course,lesson,pre='fg',maxp='16']=process.argv.slice(2);
const b=await chromium.launch();const p=await b.newPage({viewport:{width:400,height:2600}});
await p.route('**/fonts.g*/**',r=>r.abort());
await p.route('**/index.html',async r=>{const res=await r.fetch();let t=await res.text();t=t.replace("location.protocol!=='https:'||",'');r.fulfill({response:res,body:t})}); // local http: allow auto-sync
await p.goto('http://localhost:8767/index.html');await p.waitForTimeout(3500); // fresh context = empty storage
await p.click(`.row-main:has-text("${course}")`);await p.waitForTimeout(300);let n=0;
await p.click(`.row-main:has-text("${lesson}")`);await p.waitForTimeout(400);
for(let k=0;k<+maxp;k++){for(const f of await p.$$('#lvc figure')){await f.screenshot({path:`${pre}-${String(k+1).padStart(2,'0')}-${n++}.png`})}await p.keyboard.press('ArrowRight');await p.waitForTimeout(150)}
console.log(n);await b.close()})();
