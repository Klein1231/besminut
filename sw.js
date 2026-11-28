const C='besminut-v5';
self.addEventListener('install',e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(['./','index.html','manifest.webmanifest','icon-192.png','icon-512.png'])));self.skipWaiting()});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==C).map(x=>caches.delete(x)))));self.clients.claim()});
const put=(req,res)=>{if(res&&(res.ok||res.type==='opaque')){const cp=res.clone();caches.open(C).then(c=>c.put(req,cp))}return res};
self.addEventListener('fetch',e=>{const req=e.request;if(req.method!=='GET')return;const u=new URL(req.url);
 const fresh=req.mode==='navigate'||(u.origin===location.origin&&(u.pathname.endsWith('.html')||u.pathname.endsWith('/')||u.pathname.includes('/courses/')));
 if(fresh){e.respondWith(fetch(req).then(r=>put(req,r)).catch(()=>caches.match(req).then(r=>r||caches.match('index.html'))));return}
 e.respondWith(caches.match(req).then(r=>r||fetch(req).then(res=>put(req,res))))});
