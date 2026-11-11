"""Membuat assets/header.svg: lingkaran sihir AI beranimasi (SVG murni, tanpa aset eksternal)."""
import math, random, pathlib

random.seed(21)
W, H = 1200, 340
CX, CY, R = 250, 170, 128  # pusat lingkaran sihir
o = []
a = o.append

a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Efan Ramdhani - AI Engineer in training">')
a('''<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#05061a"/><stop offset=".6" stop-color="#0b0d2b"/><stop offset="1" stop-color="#140a2e"/>
  </linearGradient>
  <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="55"/></filter>
  <filter id="glow" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="2.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="soft" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="1.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <linearGradient id="title" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#b9a7ff"/><stop offset=".3" stop-color="#ffffff"/><stop offset=".5" stop-color="#9ff3ea"/>
    <stop offset=".7" stop-color="#ffffff"/><stop offset="1" stop-color="#b9a7ff"/>
    <animateTransform attributeName="gradientTransform" type="translate" values="-1 0;1 0" dur="6s" repeatCount="indefinite"/>
  </linearGradient>
  <radialGradient id="halo"><stop offset="0" stop-color="#7b5cff" stop-opacity=".45"/><stop offset=".6" stop-color="#2bc4b4" stop-opacity=".12"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>
  <linearGradient id="line" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7b5cff" stop-opacity="0"/><stop offset=".5" stop-color="#9ff3ea"/><stop offset="1" stop-color="#7b5cff" stop-opacity="0"/></linearGradient>
  <path id="ring" d="M {cx} {cy} m -{r} 0 a {r} {r} 0 1 1 {d} 0 a {r} {r} 0 1 1 -{d} 0"/>
  <clipPath id="frame"><rect width="{W}" height="{H}" rx="20"/></clipPath>
</defs>'''.replace('{cx}', str(CX)).replace('{cy}', str(CY)).replace('{r}', str(R - 14)).replace('{d}', str(2 * (R - 14)))
  .replace('{W}', str(W)).replace('{H}', str(H)))
a('''<style>
  .spin{transform-origin:%(cx)dpx %(cy)dpx;animation:spin 60s linear infinite}
  .spinr{transform-origin:%(cx)dpx %(cy)dpx;animation:spin 40s linear infinite reverse}
  .spinf{transform-origin:%(cx)dpx %(cy)dpx;animation:spin 18s linear infinite}
  @keyframes spin{to{transform:rotate(360deg)}}
  .aur{animation:drift 16s ease-in-out infinite alternate}
  @keyframes drift{from{transform:translate(0,0) scale(1)}to{transform:translate(120px,30px) scale(1.25)}}
  .tw{animation:tw 3s ease-in-out infinite}
  @keyframes tw{0%%,100%%{opacity:.15}50%%{opacity:.9}}
  .up{animation:up linear infinite}
  @keyframes up{0%%{transform:translateY(0);opacity:0}15%%{opacity:.9}100%%{transform:translateY(-260px);opacity:0}}
  .node{animation:fire 3s ease-in-out infinite}
  @keyframes fire{0%%,100%%{opacity:.35;r:4}12%%{opacity:1;r:6.5}30%%{opacity:.35;r:4}}
  .sig{stroke-dasharray:4 10;animation:flow 1.2s linear infinite}
  @keyframes flow{to{stroke-dashoffset:-14}}
  .breath{transform-origin:%(cx)dpx %(cy)dpx;animation:breath 4s ease-in-out infinite}
  @keyframes breath{0%%,100%%{opacity:.6;transform:scale(.96)}50%%{opacity:1;transform:scale(1.04)}}
  .line{opacity:0;animation:line 12s infinite}
  @keyframes line{0%%{opacity:0}2%%,30%%{opacity:1}33%%,100%%{opacity:0}}
  .l2{animation-delay:4s}.l3{animation-delay:8s}
  .type{animation:type 4s steps(30) infinite}
  @keyframes type{0%%{transform:scaleX(0)}45%%,100%%{transform:scaleX(1)}}
  .cur{animation:blink .9s steps(1) infinite}
  @keyframes blink{50%%{opacity:0}}
  .serif{font-family:Georgia,'Palatino Linotype','Book Antiqua',serif}
  .mono{font-family:'JetBrains Mono','Fira Code',Consolas,'Courier New',monospace}
</style>''' % {'cx': CX, 'cy': CY})

a(f'<g clip-path="url(#frame)"><rect width="{W}" height="{H}" fill="url(#bg)"/>')
# aurora
for cx, cy, r, col, d in [(300, 60, 220, '#5b3df5', 0), (820, 300, 260, '#1fb5a8', -5), (1100, 40, 200, '#8e44ff', -9), (600, 160, 160, '#2f6fe0', -3)]:
    a(f'<g class="aur" style="animation-delay:{d}s"><circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}" opacity=".33" filter="url(#blur)"/></g>')
# bintang
for _ in range(120):
    a(f'<circle class="tw" cx="{random.uniform(0, W):.0f}" cy="{random.uniform(0, H):.0f}" r="{random.choice([.5, .7, .9, 1.2])}" fill="#fff" '
      f'style="animation-delay:{random.uniform(0, 3):.2f}s;animation-duration:{random.uniform(2, 5):.1f}s"/>')
# partikel naik
for _ in range(34):
    x = random.uniform(20, W - 20)
    a(f'<circle class="up" cx="{x:.0f}" cy="{H + 10}" r="{random.choice([1, 1.4, 1.8])}" fill="{random.choice(["#9ff3ea", "#b9a7ff", "#ffffff"])}" filter="url(#soft)" '
      f'style="animation-duration:{random.uniform(7, 14):.1f}s;animation-delay:{-random.uniform(0, 14):.1f}s"/>')

# ===== lingkaran sihir =====
a(f'<circle cx="{CX}" cy="{CY}" r="{R + 40}" fill="url(#halo)" class="breath"/>')
a(f'<g filter="url(#soft)" stroke="#b9a7ff" fill="none">')
a(f'<circle cx="{CX}" cy="{CY}" r="{R}" stroke-width="1.6" opacity=".85"/>')
a(f'<circle cx="{CX}" cy="{CY}" r="{R - 26}" stroke-width="1" opacity=".6"/>')
a('</g>')
# cincin rune (istilah AI) berputar
runes = " ✦ ATTENTION ✦ EMBEDDING ✦ GRADIENT ✦ BACKPROP ✦ TRANSFORMER ✦ INFERENCE ✦ TOKENS"
a(f'<g class="spin"><text class="mono" font-size="11.5" letter-spacing="2.2" fill="#cfc4ff" filter="url(#soft)">'
  f'<textPath href="#ring" textLength="{2 * math.pi * (R - 14) - 8:.0f}">{runes}</textPath></text></g>')
# tanda-tanda kecil di cincin luar
a('<g class="spinr">')
for k in range(24):
    ang = math.radians(k * 15)
    x1, y1 = CX + (R + 4) * math.cos(ang), CY + (R + 4) * math.sin(ang)
    x2, y2 = CX + (R + (14 if k % 3 == 0 else 8)) * math.cos(ang), CY + (R + (14 if k % 3 == 0 else 8)) * math.sin(ang)
    a(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#9ff3ea" stroke-width="{1.6 if k % 3 == 0 else 1}" opacity=".8"/>')
a('</g>')
# heksagram berputar berlawanan
r6 = R - 30
tri = lambda off: " ".join(f"{CX + r6 * math.cos(math.radians(off + 120 * i)):.1f},{CY + r6 * math.sin(math.radians(off + 120 * i)):.1f}" for i in range(3))
a(f'<g class="spinr" fill="none" stroke="#7b5cff" stroke-width="1.4" filter="url(#soft)" opacity=".9">'
  f'<polygon points="{tri(-90)}"/><polygon points="{tri(90)}"/>'
  f'<circle cx="{CX}" cy="{CY}" r="{r6 * 0.5:.0f}" stroke="#9ff3ea" stroke-dasharray="2 6"/></g>')
# titik-titik bersinar di sudut heksagram
a('<g class="spinf">')
for k in range(6):
    ang = math.radians(-90 + 60 * k)
    a(f'<circle cx="{CX + r6 * math.cos(ang):.1f}" cy="{CY + r6 * math.sin(ang):.1f}" r="3" fill="#ffffff" filter="url(#glow)"/>')
a('</g>')
# jaringan saraf di tengah: forward pass
layers = [3, 4, 3]
pos = []
for li, n in enumerate(layers):
    x = CX - 38 + li * 38
    pos.append([(x, CY + (j - (n - 1) / 2) * 22) for j in range(n)])
for li in range(len(layers) - 1):
    for (x1, y1) in pos[li]:
        for (x2, y2) in pos[li + 1]:
            a(f'<line x1="{x1}" y1="{y1:.0f}" x2="{x2}" y2="{y2:.0f}" stroke="#9ff3ea" stroke-width=".8" opacity=".35"/>')
            a(f'<line class="sig" x1="{x1}" y1="{y1:.0f}" x2="{x2}" y2="{y2:.0f}" stroke="#ffffff" stroke-width="1" opacity=".55" style="animation-delay:{li * .4}s"/>')
for li, layer in enumerate(pos):
    for (x, y) in layer:
        a(f'<circle class="node" cx="{x}" cy="{y:.0f}" r="4" fill="#e9fffc" filter="url(#glow)" style="animation-delay:{li * .45:.2f}s"/>')

# ===== teks =====
TX = 450
a(f'<text x="{TX}" y="118" class="mono" font-size="14" letter-spacing="5" fill="#9ff3ea" opacity=".9">✦ AI ENGINEER · DATA WIZARD ✦</text>')
a(f'<text x="{TX - 4}" y="190" class="serif" font-size="74" font-weight="700" letter-spacing="2" fill="url(#title)" filter="url(#soft)">Efan Ramdhani</text>')
a(f'<rect x="{TX}" y="208" width="520" height="1.5" fill="url(#line)"/>')
lines = ["merapal model dari data yang jujur", "membangun pipeline yang mengukur dirinya", "mahasiswa ITS · belajar LLM &amp; MLOps"]
for i, t in enumerate(lines):
    w = len(t.replace("&amp;", "&")) * 9.6 + 4
    a(f'<g class="line l{i + 1}"><clipPath id="c{i}"><rect class="type" x="{TX + 28}" y="228" width="{w:.0f}" height="28" style="transform-origin:{TX + 28}px 0;animation-delay:{i * 4}s"/></clipPath>'
      f'<text x="{TX}" y="248" class="mono" font-size="16" fill="#7b5cff">&gt;_</text>'
      f'<text x="{TX + 28}" y="248" class="mono" font-size="16" fill="#e6e1ff" clip-path="url(#c{i})">{t}</text></g>')
a(f'<text x="{TX}" y="300" class="mono" font-size="12" fill="#8c86b8" letter-spacing="1.5">Python · DuckDB · dbt · Next.js · Docker</text>')
a('</g>')
a(f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="20" fill="none" stroke="#3a2f7a" opacity=".8"/>')
a('</svg>')

pathlib.Path(__file__).resolve().parent.parent.joinpath('assets/header.svg').write_text('\n'.join(o))
print('ok')
