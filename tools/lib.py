import math,base64
def T(x,y,s,c=''):return f'<text x="{x}" y="{y}" text-anchor="middle" class="{c}">{s}</text>'
def B(x,y,w,h,lines,c='bx',tc='',r=6,lh=15):
    o=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" class="{c}"/>';ls=lines.split('\n');y0=y+h/2-(len(ls)-1)*lh/2+4.5
    for i,l in enumerate(ls):o+=T(x+w/2,round(y0+i*lh,1),l,tc)
    return o
def A(x1,y1,x2,y2,c='ln',hd='hd',dash=False,two=False):
    a=math.atan2(y2-y1,x2-x1);L,W=8,4.5
    def head(xe,ye,ang):
        bx,by=xe-L*math.cos(ang),ye-L*math.sin(ang);px,py=-math.sin(ang)*W,math.cos(ang)*W
        return (bx,by),f'<polygon points="{xe},{ye} {bx+px:.1f},{by+py:.1f} {bx-px:.1f},{by-py:.1f}" class="{hd}"/>'
    (bx,by),h1=head(x2,y2,a);sx,sy,h0=x1,y1,''
    if two:(sx,sy),h0=head(x1,y1,a+math.pi)
    return f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{bx:.1f}" y2="{by:.1f}" class="{c}{" dash" if dash else ""}"/>'+h1+h0
def S(w,h,body,lab):return f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{lab}">{body}</svg>'
def F(svg,cap):return f'<figure>{svg}<figcaption>{cap}</figcaption></figure>'
def IMG(p,alt,cap):return f'<figure><img src="data:image/jpeg;base64,{base64.b64encode(open(p,"rb").read()).decode()}" alt="{alt}"><figcaption>{cap}</figcaption></figure>'
def CHECK(q,a):return f'<aside class="check"><p class="q">{q}</p><div class="a">{a}</div></aside>'
def AN(t):return f'<aside class="analogy"><p>{t}</p></aside>'
def PF(t):return f'<aside class="pitfall"><p>{t}</p></aside>'
def LEAD(t):return f'<p class="lead">{t}</p>'
def P(pts,c='ln',hd='hd',dash=False):
    """elbow arrow through points, head at the last point"""
    d='M'+' L'.join(f'{x} {y}' for x,y in pts[:-1]);(x1,y1),(x2,y2)=pts[-2],pts[-1]
    a=math.atan2(y2-y1,x2-x1);bx,by=x2-8*math.cos(a),y2-8*math.sin(a);px,py=-math.sin(a)*4.5,math.cos(a)*4.5
    return f'<path d="{d} L{bx:.1f} {by:.1f}" class="{c}{" dash" if dash else ""}"/><polygon points="{x2},{y2} {bx+px:.1f},{by+py:.1f} {bx-px:.1f},{by-py:.1f}" class="{hd}"/>'
def TL(x,y,s,c=''):return f'<text x="{x}" y="{y}" text-anchor="start" class="{c}">{s}</text>'
import re as _re
def DC(s):
    """decimal comma: replace '.' only between digits"""
    return _re.sub(r'(?<=\d)\.(?=\d)',',',s)
