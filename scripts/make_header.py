"""Membuat assets/header.svg: langit malam penyihir yang beranimasi (SVG murni, tanpa aset eksternal)."""
import random, pathlib
random.seed(11)
W, H = 1200, 380
out = []
a = out.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Efan Ramdhani - AI Engineer in training">')
a('''<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#0b0820"/><stop offset=".55" stop-color="#1c1240"/><stop offset="1" stop-color="#3a1d4f"/>
  </linearGradient>
  <linearGradient id="gold" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#7f93b3"/><stop offset=".35" stop-color="#d6e2f3"/>
    <stop offset=".5" stop-color="#ffffff"/><stop offset=".65" stop-color="#d6e2f3"/><stop offset="1" stop-color="#7f93b3"/>
    <animateTransform attributeName="gradientTransform" type="translate" values="-1 0;1 0" dur="4s" repeatCount="indefinite"/>
  </linearGradient>
  <radialGradient id="moonGlow"><stop offset="0" stop-color="#cfe3ff" stop-opacity=".55"/><stop offset="1" stop-color="#cfe3ff" stop-opacity="0"/></radialGradient>
  <radialGradient id="flame"><stop offset="0" stop-color="#ffffff"/><stop offset=".5" stop-color="#9fd8ff"/><stop offset="1" stop-color="#3a7bd5" stop-opacity="0"/></radialGradient>
  <linearGradient id="trail" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff"/></linearGradient>
  <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<style>
  .tw{animation:tw 3s ease-in-out infinite}
  @keyframes tw{0%,100%{opacity:.25}50%{opacity:1}}
  .win{animation:win 4s ease-in-out infinite}
  @keyframes win{0%,100%{opacity:.95}45%{opacity:.55}55%{opacity:1}}
  .candle{animation:bob 5s ease-in-out infinite}
  @keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
  .fl{animation:fl .35s ease-in-out infinite alternate;transform-box:fill-box;transform-origin:50% 100%}
  @keyframes fl{from{transform:scaleY(1) scaleX(1)}to{transform:scaleY(1.18) scaleX(.85)}}
  .sub{opacity:0;animation:sub 12s infinite}
  @keyframes sub{0%{opacity:0;transform:translateY(8px)}4%,29%{opacity:1;transform:translateY(0)}33%,100%{opacity:0;transform:translateY(-8px)}}
  .s2{animation-delay:4s}.s3{animation-delay:8s}
  .shoot{animation:shoot 7s ease-in infinite}
  @keyframes shoot{0%,70%{transform:translate(0,0);opacity:0}72%{opacity:1}85%{transform:translate(-420px,190px);opacity:0}100%{opacity:0}}
  .spark{animation:spark 2.2s ease-out infinite}
  @keyframes spark{0%{opacity:0;transform:translate(0,0) scale(.4)}20%{opacity:1}100%{opacity:0;transform:translate(var(--dx),var(--dy)) scale(1.2)}}
  .title{font-family:Georgia,'Palatino Linotype','Book Antiqua',serif;font-weight:700;letter-spacing:3px}
  .serif{font-family:Georgia,'Palatino Linotype',serif}
</style>''')
a(f'<rect width="{W}" height="{H}" rx="18" fill="url(#sky)"/>')
# bintang
for _ in range(110):
    x, y = random.uniform(10, W-10), random.uniform(8, H*0.72)
    r = random.choice([.6, .8, 1, 1.2, 1.6])
    a(f'<circle class="tw" cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="#fff" style="animation-delay:{random.uniform(0,3):.2f}s;animation-duration:{random.uniform(2,4.5):.1f}s"/>')
# bulan
a('<circle cx="1040" cy="78" r="90" fill="url(#moonGlow)"/><circle cx="1040" cy="78" r="38" fill="#e9eff9"/><circle cx="1056" cy="68" r="34" fill="#1a1140" opacity=".92"/>')
# bintang jatuh
a('<g class="shoot"><line x1="980" y1="40" x2="1060" y2="2" stroke="url(#trail)" stroke-width="2" transform="rotate(180 1020 21)"/><circle cx="980" cy="40" r="2.4" fill="#fff" filter="url(#glow)"/></g>')
# kastil (siluet orisinal)
base = H - 40
castle = ['<g fill="#0a0716">']
towers = [(70,60,150,'c'),(150,40,110,'c'),(205,85,70,'f'),(300,34,190,'c'),(345,90,95,'f'),(450,46,140,'c'),(510,70,80,'f'),(600,30,215,'c'),(640,120,105,'f'),(780,40,160,'c'),(830,80,90,'f'),(930,52,130,'c'),(990,70,70,'f'),(1080,38,120,'c')]
wins = []
for x,w,h,kind in towers:
    h = int(h*0.55)
    top = base - h
    castle.append(f'<rect x="{x}" y="{top}" width="{w}" height="{h+80}"/>')
    if kind == 'c':
        castle.append(f'<polygon points="{x-6},{top} {x+w/2},{top-w*1.25} {x+w+6},{top}"/>')
        castle.append(f'<line x1="{x+w/2}" y1="{top-w*1.25}" x2="{x+w/2}" y2="{top-w*1.25-14}" stroke="#0a0716" stroke-width="2"/>')
    else:
        for i in range(int(w//14)):
            castle.append(f'<rect x="{x+i*14+2}" y="{top-9}" width="8" height="9"/>')
    for _ in range(random.randint(1,3)):
        wx = x + random.uniform(6, max(7, w-14)); wy = top + random.uniform(10, max(11, h-14))
        wins.append(f'<rect class="win" x="{wx:.0f}" y="{wy:.0f}" width="6" height="10" rx="3" fill="#8fd3ff" style="animation-delay:{random.uniform(0,4):.1f}s"/>')
castle.append('</g>')
a('<path d="M0 %d Q300 %d 600 %d T1200 %d V%d H0Z" fill="#120c26"/>' % (base+10, base-20, base+5, base-5, H))
out += castle + wins
a(f'<rect x="0" y="{base+20}" width="{W}" height="{H-base-20}" fill="#0a0716"/>')
# lilin melayang
for i,(cx,cy) in enumerate([(90,60),(215,110),(330,40),(1150,200),(960,170),(720,30)]):
    a(f'<g class="candle" style="animation-delay:{i*.7:.1f}s"><rect x="{cx-4}" y="{cy}" width="8" height="26" rx="2" fill="#e3e9f3"/>'
      f'<ellipse class="fl" cx="{cx}" cy="{cy-7}" rx="4.5" ry="8" fill="url(#flame)"/><circle cx="{cx}" cy="{cy-6}" r="12" fill="#8fd3ff" opacity=".15"/></g>')
# judul
a('<text x="600" y="150" text-anchor="middle" class="title" font-size="68" fill="url(#gold)" filter="url(#glow)">EFAN RAMDHANI</text>')
a('<line x1="390" y1="173" x2="810" y2="173" stroke="#9fb4d6" stroke-width="1" opacity=".6"/><circle cx="600" cy="173" r="3" fill="#d6e2f3"/>')
subs = ['AI Engineer in training', 'Data Wizard  ·  ITS', 'Merapal pipeline, melatih model']
for i,s in enumerate(subs):
    a(f'<text x="600" y="212" text-anchor="middle" class="serif sub s{i+1}" font-size="26" fill="#d3def0" font-style="italic">{s}</text>')
# tongkat sihir + percikan
a('<g transform="translate(355 268) rotate(-22)"><rect x="0" y="-3" width="120" height="6" rx="3" fill="#5a3a22"/><rect x="0" y="-4" width="34" height="8" rx="3" fill="#3d2616"/></g>')
for i in range(10):
    dx, dy = random.uniform(-40,40), random.uniform(-45,10)
    a(f'<circle class="spark" cx="466" cy="223" r="{random.choice([1.5,2,2.5])}" fill="#bfe6ff" filter="url(#glow)" style="--dx:{dx:.0f}px;--dy:{dy:.0f}px;animation-delay:{i*.22:.2f}s"/>')
a('</svg>')
pathlib.Path(__file__).resolve().parent.parent.joinpath('assets/header.svg').write_text('\n'.join(out))
print('ok')
