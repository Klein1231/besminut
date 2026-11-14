import json, os
from PIL import Image, ImageDraw
out='/mnt/user-data/outputs/besminut'
src=open('app.html',encoding='utf-8').read()
head='''<!doctype html>
<html lang="kk">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#D9731F">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Бес минут">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon-192.png">
<link rel="apple-touch-icon" href="icon-192.png">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}[hidden]{display:none!important}img{max-width:100%}</style>
'''
body=src.replace('<div id="app"></div>','</head>\n<body>\n<div id="app"></div>',1)
open(f'{out}/index.html','w',encoding='utf-8').write(head+body+'\n</body>\n</html>\n')
json.dump({"name":"Бес минут","short_name":"Бес минут","start_url":"./","scope":"./","display":"standalone",
 "background_color":"#E8EEEC","theme_color":"#D9731F","lang":"kk",
 "icons":[{"src":"icon-192.png","sizes":"192x192","type":"image/png"},{"src":"icon-512.png","sizes":"512x512","type":"image/png","purpose":"any maskable"}]},
 open(f'{out}/manifest.webmanifest','w',encoding='utf-8'),ensure_ascii=False,indent=1)
open(f'{out}/sw.js','w').write('''const C='besminut-v3';
self.addEventListener('install',e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(['./','index.html','manifest.webmanifest','icon-192.png','icon-512.png'])));self.skipWaiting()});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==C).map(x=>caches.delete(x)))));self.clients.claim()});
const put=(req,res)=>{if(res&&(res.ok||res.type==='opaque')){const cp=res.clone();caches.open(C).then(c=>c.put(req,cp))}return res};
self.addEventListener('fetch',e=>{const req=e.request;if(req.method!=='GET')return;const u=new URL(req.url);
 const fresh=req.mode==='navigate'||(u.origin===location.origin&&(u.pathname.endsWith('.html')||u.pathname.endsWith('/')||u.pathname.includes('/courses/')));
 if(fresh){e.respondWith(fetch(req).then(r=>put(req,r)).catch(()=>caches.match(req).then(r=>r||caches.match('index.html'))));return}
 e.respondWith(caches.match(req).then(r=>r||fetch(req).then(res=>put(req,res))))});
''')
for s in (192,512):
    im=Image.new('RGB',(s,s),'#D9731F'); d=ImageDraw.Draw(im)
    u=s/24; pts=[(13,2),(4,14),(11,14),(10,22),(19,10),(12,10)]
    cx=s*0.5-12*u*0.62; cy=s*0.5-12*u*0.62
    d.polygon([(cx+x*u*0.62,cy+y*u*0.62) for x,y in pts],fill='#1A0E03')
    im.save(f'{out}/icon-{s}.png')
print(os.listdir(out))

import hashlib,glob
packs=[]
for f in sorted(glob.glob(f'{out}/courses/*/*.json')):
    rel=os.path.relpath(f,out).replace(os.sep,'/')
    if rel.endswith('index.json') or rel.endswith('glossary.json') or rel.endswith('syllabus.json'):continue
    packs.append({"path":rel,"v":hashlib.sha1(open(f,'rb').read()).hexdigest()[:12]})
os.makedirs(f'{out}/courses',exist_ok=True)
json.dump({"packs":packs},open(f'{out}/courses/index.json','w'),indent=1)
print('packs',len(packs))
