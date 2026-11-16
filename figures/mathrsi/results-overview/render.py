from pathlib import Path
from html import escape
import json
P=Path(__file__).parent
D=json.loads((P/'data.json').read_text())
COL=['#4C5BD4','#0E9384','#D9822B','#D9467A','#0EA5E9','#65A30D']
def render(lang):
 z=lang=='zh'; a=[]
 def t(x,y,s,size=17,color='#3D4655',weight=400,anchor='start'):
  a.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}">{escape(str(s))}</text>')
 def line(x,y,X,Y,c='#D3D8E0',w=1):a.append(f'<line x1="{x}" y1="{y}" x2="{X}" y2="{Y}" stroke="{c}" stroke-width="{w}"/>')
 def rect(x,y,w,h,c):a.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{c}"/>')
 for i,key in enumerate(['pb','ecc','dd','e86','q6','he']):
  x=32+(i%2)*450;y=32+(i//2)*300;c=COL[i]
  t(x,y+21,D[key]['name'][lang],22,c,650)
  if key=='pb':
   t(x,y+50,'逐点 + 统一下界' if z else 'Pointwise + uniform bounds',18,'#0B1220',550)
   line(x+20,y+167,x+386,y+167)
   for j,g in enumerate(D[key]['gains']):
    bx=x+30+j*46;h=g*2.2;rect(bx,y+167-h,20,h,c);t(bx+10,y+159-h,'+'+str(g),15,c,600,'middle');t(bx+10,y+190,str(5+j),15,anchor='middle')
   t(x,y+218,'k = 5–12 · '+('相对指定参考界的增益' if z else 'gains over stated references'),16)
   t(x,y+246,'统一定理：所有 k ≥ 12' if z else 'Uniform theorem: every k ≥ 12',18,c,550)
  elif key=='ecc':
   t(x,y+50,'4 个精确值 · 1 个收紧区间' if z else '4 exact values · 1 narrower interval',18,'#0B1220',550)
   for j,r in enumerate(D[key]['rows']):
    yy=y+84+j*31;t(x,yy,r[0],17);t(x+120,yy,r[1],17,'#667085');t(x+215,yy,'→',18);t(x+250,yy,r[2],19,c,650);t(x+340,yy,('开放' if z else 'open') if j==4 else ('文献*' if z else 'lit.*') if j==3 else '',15)
   t(x,y+256,'* 文献定理推论' if z else '* Literature corollary',15)
  elif key=='dd':
   t(x,y+50,'各组参数下的最佳构造' if z else 'Our best constructions by setting',18,'#0B1220',550)
   for j,r in enumerate(D[key]['settings']):
    yy=y+92+j*40;t(x,yy,r['parameter'],18);t(x+370,yy,f"{r['vertices']:,}",25,c,650,'end')
   t(x,y+256,'顶点数 · 四组展示参数' if z else 'Vertices · four showcased settings',16)
  elif key=='e86':
   t(x,y+50,'无四圈超立方体的渐近边密度' if z else 'Asymptotic C₄-free cube edge density',17,'#0B1220',550)
   t(x,y+96,'0.60318 → < 0.59155154',25,c,650)
   X=lambda v:x+20+(v-.5)/.11*360
   line(X(.5),y+162,X(.61),y+162,'#667085',2)
   for v in [.5,.59155154,.60318]:
    xx=X(v);line(xx,y+154,xx,y+170,c,2)
   t(X(.5),y+193,'0.5',16,anchor='middle');t(X(.59155154),y+146,'新 / new' if z else 'new',16,c,600,'end');t(X(.60318)+4,y+193,'参考' if z else 'prior',16,anchor='middle')
   t(x,y+246,'猜想值：1/2' if z else 'Conjecture: 1/2',18)
  elif key=='q6':
   t(x,y+56,'Q₆ 中每一个匹配' if z else 'Every matching in Q₆',21,'#0B1220',600)
   t(x,y+82,'均可扩展为 Hamilton 圈' if z else 'extends to a Hamilton cycle',19,c,600)
   t(x,y+126,'Q₇ 中每个至少 57 边的匹配' if z else 'Every Q₇ matching with ≥57 edges',20,'#0B1220',600)
   t(x,y+152,'均可扩展为 Hamilton 圈，' if z else 'extends to a Hamilton cycle containing',18,c,600)
   t(x,y+178,'且保留匹配的每一条指定边。' if z else 'every prescribed matching edge.',18,c,600)
   t(x,y+218,'完整 Q₇ 猜想仍开放' if z else 'Full Q₇ conjecture remains open',17)
   t(x,y+256,'亦含任意维 ≤6 方向推论（引用结果）' if z else 'Also ≤6 directions in Qₙ (imported results)',15)
  else:
   t(x,y+50,'凸七边形的强制阈值上界' if z else 'Upper bound for the convex 7-gon threshold',17,'#0B1220',550)
   t(x,y+110,'ES(7) ≤ 77',32,c,650)
   t(x,y+151,'上界：78 → 77' if z else 'Upper bound: 78 → 77',20)
   t(x,y+213,'工作稿 · 待独立审阅' if z else 'Working manuscript · review pending',19,c,650)
  if i<4:line(x,y+280,x+398,y+280,'#E4E7EC')
 return '<svg xmlns="http://www.w3.org/2000/svg" width="900" height="934" viewBox="0 0 900 934" role="img"><title>'+('MathRSI 六领域成果' if z else 'MathRSI results across six domains')+'</title><rect width="900" height="934" fill="white"/><g font-family="Arial, PingFang SC, Microsoft YaHei, sans-serif">'+''.join(a)+'</g></svg>'
if __name__=='__main__':
 import argparse
 parser=argparse.ArgumentParser(description='Generate bilingual SVG overviews; optionally render PNG previews.')
 parser.add_argument('--png',action='store_true',help='Also export PNGs using Playwright Chromium')
 args=parser.parse_args()
 for lang in ['en','zh']:
  (P/f'results-overview.{lang}.svg').write_text(render(lang))
 if args.png:
  from playwright.sync_api import sync_playwright
  with sync_playwright() as p:
   browser=p.chromium.launch()
   for lang in ['en','zh']:
    page=browser.new_page(viewport={'width':900,'height':934},device_scale_factor=1)
    page.goto((P/f'results-overview.{lang}.svg').resolve().as_uri());page.screenshot(path=str(P/f'results-overview.{lang}.png'));page.close()
   browser.close()
