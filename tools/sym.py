# IEC-style schematic symbols for lesson SVGs (single-line / ladder diagrams, P&ID)
from lib import T,TL,B,A,P
def L(x1,y1,x2,y2,c='ln'):return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{c}"/>'
def R(x,y,w,h,c='bx',r=3):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" class="{c}"/>'
def C(x,y,r,c='bx'):return f'<circle cx="{x}" cy="{y}" r="{r}" class="{c}"/>'
def TR(x,y,s,c=''):return f'<text x="{x}" y="{y}" text-anchor="end" class="{c}">{s}</text>'
# --- electrical (vertical, top→bottom) ---
def no_v(x,y,h=24,lab='',c='ln'):
    """normally-open contact, vertical, from y to y+h"""
    a=y+h*0.3;b=y+h*0.7
    return L(x,y,x,a,c)+L(x,b,x,y+h,c)+L(x,b,x-8,a+1,c)+(TL(x+6,y+h/2+4,lab,'t-s') if lab else '')
def nc_v(x,y,h=24,lab='',c='ln'):
    a=y+h*0.3;b=y+h*0.7
    return L(x,y,x,a,c)+L(x,b,x,y+h,c)+L(x,b,x+8,a-1,c)+L(x,a,x+10,a,c)+(TL(x+12,y+h/2+4,lab,'t-s') if lab else '')
def breaker_v(x,y,h=30,lab='QF',c='ln'):
    a=y+h*0.3;b=y+h*0.7
    return L(x,y,x,a,c)+L(x,b,x,y+h,c)+L(x,b,x-9,a+1,c)+L(x-4,a-4,x+4,a+4,c)+L(x-4,a+4,x+4,a-4,c)+TL(x+8,y+h/2+4,lab,'t-s t-b')
def coil(x,y,lab,c='bxa'):return R(x-14,y,28,18,c)+TL(x+18,y+13,lab,'t-s t-b')
def motor(x,y,r=17,c='bx'):return C(x,y,r,c)+T(x,y-1,'M','t-b')+T(x,y+11,'3~','t-s')
def thermal_v(x,y,h=26,lab='KK'):
    m=y+h/2
    return L(x,y,x,m-7)+f'<path d="M{x} {m-7} l-5 3 l10 4 l-10 4 l5 3" class="ln"/>'+L(x,m+7,x,y+h)+TL(x+9,m+4,lab,'t-s t-b')
def slashes(x,y,n=3):return ''.join(L(x-5,y+4-i*5,x+5,y-2-i*5) for i in range(n))
# --- hydraulic (P&ID-like, horizontal pipe) ---
def valve_h(x,y,s=7):  # gate valve: two triangles (bow-tie)
    return f'<polygon points="{x-s},{y-s} {x},{y} {x-s},{y+s}" class="bx"/><polygon points="{x+s},{y-s} {x},{y} {x+s},{y+s}" class="bx"/>'
def check_h(x,y,s=7):  # check valve: bow-tie, one side filled (flow →)
    return f'<polygon points="{x-s},{y-s} {x},{y} {x-s},{y+s}" class="soft"/><polygon points="{x+s},{y-s} {x},{y} {x+s},{y+s}" class="bx"/>'+L(x,y-s,x,y+s)
def pump_h(x,y,r=12,c='bx'):  # centrifugal pump: circle + triangle pointing to discharge (right)
    return C(x,y,r,c)+f'<polygon points="{x-6},{y-8} {x+9},{y} {x-6},{y+8}" class="ln"/>'
def inst(x,y,lab,c='bx'):return C(x,y,11,c)+T(x,y+4,lab,'t-s t-b')
# --- power symbols (single-line) ---
def trafo_v(x,y,lab=''):  # transformer: two overlapping circles, vertical
    return C(x,y,11,'bx')+C(x,y+14,11,'bx')+(TL(x+16,y+11,lab,'t-s') if lab else '')
def gen(x,y,r=15,c='bx'):return C(x,y,r,c)+T(x,y+1,'G','t-b')+T(x,y+12,'~','t-s')
def bus(x1,x2,y,c='lna'):return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" class="{c}" style="stroke-width:3.5"/>'
def meter_v(x,y,lab='Wh'):return R(x-13,y,26,20,'bx')+T(x,y+14,lab,'t-s t-b')
def ground(x,y):return L(x,y,x,y+6)+L(x-8,y+6,x+8,y+6)+L(x-5,y+10,x+5,y+10)+L(x-2,y+14,x+2,y+14)
