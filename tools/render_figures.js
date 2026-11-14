const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:400,height:2600}});
await p.route('**/fonts.g*/**',r=>r.abort());await p.goto('http://localhost:8767/index.html');await p.evaluate(()=>localStorage.clear());await p.reload();await p.waitForTimeout(1500);
await p.click('.row-main:has-text("Ғимараттың")');let n=0;
for(const name of ['2-сабақ']){await p.click(`.row-main:has-text("${name}")`);await p.waitForTimeout(300);
 for(let k=0;k<12;k++){for(const f of await p.$$('#lvc figure')){await f.screenshot({path:`fg-${n++}.png`})}await p.keyboard.press('ArrowRight');await p.waitForTimeout(120)}
 await p.keyboard.press('Escape');await p.waitForTimeout(500)}
console.log(n);await b.close()})();
