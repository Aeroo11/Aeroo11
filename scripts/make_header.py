"""Membuat assets/header.svg: perpustakaan sihir di malam hari (SVG murni, gambar orisinal, animasi halus)."""
import random, pathlib

random.seed(5)
W, H = 1200, 400
o = []
a = o.append

a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Efan Ramdhani - AI Engineer in training">')
a(f'''<defs>
  <linearGradient id="wall" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#0d0a0b"/><stop offset=".6" stop-color="#17110f"/><stop offset="1" stop-color="#0b0808"/>
  </linearGradient>
  <linearGradient id="wood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2b1d16"/><stop offset="1" stop-color="#160e0a"/></linearGradient>
  <linearGradient id="night" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0b1633"/><stop offset="1" stop-color="#1f3466"/></linearGradient>
  <linearGradient id="beam" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#b9cdf5" stop-opacity=".28"/><stop offset="1" stop-color="#b9cdf5" stop-opacity="0"/>
  </linearGradient>
  <radialGradient id="vig" r=".8"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".75"/></radialGradient>
  <radialGradient id="bflame" cx=".5" cy=".65" r=".6"><stop offset="0" stop-color="#ffffff"/><stop offset=".4" stop-color="#cfe6ff"/><stop offset=".8" stop-color="#5a8fe6"/><stop offset="1" stop-color="#2a5bc4" stop-opacity="0"/></radialGradient>
  <radialGradient id="bhalo"><stop offset="0" stop-color="#8fbaf0" stop-opacity=".3"/><stop offset="1" stop-color="#8fbaf0" stop-opacity="0"/></radialGradient>
  <radialGradient id="bookglow"><stop offset="0" stop-color="#cfe0ff" stop-opacity=".35"/><stop offset="1" stop-color="#cfe0ff" stop-opacity="0"/></radialGradient>
  <linearGradient id="silver" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#9aa8c4"/><stop offset=".4" stop-color="#e9edf6"/><stop offset=".5" stop-color="#ffffff"/>
    <stop offset=".6" stop-color="#e9edf6"/><stop offset="1" stop-color="#9aa8c4"/>
    <animateTransform attributeName="gradientTransform" type="translate" values="-1 0;1 0" dur="9s" repeatCount="indefinite"/>
  </linearGradient>
  <linearGradient id="page" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#cfd2da"/><stop offset="1" stop-color="#eef0f4"/></linearGradient>
  <linearGradient id="pageR" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#eef0f4"/><stop offset="1" stop-color="#cfd2da"/></linearGradient>
  <filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="1.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="blur6"><feGaussianBlur stdDeviation="6"/></filter>
  <clipPath id="frame"><rect width="{W}" height="{H}" rx="18"/></clipPath>
</defs>''')
a('''<style>
  .dust{animation:dust linear infinite}
  @keyframes dust{0%{transform:translate(0,0);opacity:0}20%{opacity:.8}80%{opacity:.6}100%{transform:translate(40px,150px);opacity:0}}
  .flame{animation:flick .5s ease-in-out infinite alternate;transform-box:fill-box;transform-origin:50% 100%}
  @keyframes flick{from{transform:scale(1,1)}to{transform:scale(.88,1.1)}}
  .float{animation:float 6s ease-in-out infinite}
  @keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
  .turn{transform-box:fill-box;transform-origin:0% 50%;animation:turn 9s ease-in-out infinite}
  @keyframes turn{0%,55%{transform:scaleX(1)}75%,100%{transform:scaleX(-1)}}
  .turn2{animation:fade2 9s ease-in-out infinite}
  @keyframes fade2{0%,74%{opacity:1}76%,100%{opacity:0}}
  .rise{animation:rise 7s ease-out infinite}
  @keyframes rise{0%{transform:translate(0,0);opacity:0}20%{opacity:.9}100%{transform:translate(var(--dx),-70px);opacity:0}}
  .sub{opacity:0;animation:sub 15s infinite}
  @keyframes sub{0%{opacity:0}5%,30%{opacity:1}35%,100%{opacity:0}}
  .s2{animation-delay:5s}.s3{animation-delay:10s}
  .tw{animation:tw 4s ease-in-out infinite}
  @keyframes tw{0%,100%{opacity:.3}50%{opacity:1}}
  .serif{font-family:Georgia,'Palatino Linotype','Book Antiqua',serif}
</style>''')
a(f'<g clip-path="url(#frame)"><rect width="{W}" height="{H}" fill="url(#wall)"/>')

# ===== jendela gotik =====
WX, WW, WT, WB = 495, 210, 22, 205
mid = WX + WW / 2
arch = f'M{WX} {WB} V{WT + 80} Q{WX} {WT + 10} {mid} {WT} Q{WX + WW} {WT + 10} {WX + WW} {WT + 80} V{WB} Z'
a(f'<path d="{arch}" fill="url(#night)"/>')
for _ in range(26):
    a(f'<circle class="tw" cx="{random.uniform(WX + 8, WX + WW - 8):.0f}" cy="{random.uniform(WT + 30, WB - 60):.0f}" r="{random.choice([.6, .9, 1.2])}" fill="#fff" '
      f'style="animation-delay:{random.uniform(0, 4):.1f}s"/>')
a(f'<circle cx="{WX + 150}" cy="{WT + 70}" r="22" fill="#eef2fb"/><circle cx="{WX + 150}" cy="{WT + 70}" r="40" fill="#cfdcf7" opacity=".15"/>')
lead = []
for k in range(1, 4):
    x = WX + WW * k / 4
    lead.append(f'<line x1="{x:.0f}" y1="{WT + 8}" x2="{x:.0f}" y2="{WB}"/>')
for y in range(WT + 60, WB, 36):
    lead.append(f'<line x1="{WX}" y1="{y}" x2="{WX + WW}" y2="{y}"/>')
a(f'<g stroke="#1a120e" stroke-width="3">{"".join(lead)}</g>')
a(f'<path d="{arch}" fill="none" stroke="#2b1d16" stroke-width="12"/><path d="{arch}" fill="none" stroke="#3a281e" stroke-width="3"/>')
a(f'<rect x="{WX - 16}" y="{WB}" width="{WW + 32}" height="12" fill="#2b1d16"/>')
a(f'<polygon points="{WX + 10},{WB} {WX + WW - 10},{WB} {mid + 230},{H} {mid - 190},{H}" fill="url(#beam)"/>')
for _ in range(40):
    x = random.uniform(WX + 10, WX + WW); y = random.uniform(WB - 10, WB + 120)
    a(f'<circle class="dust" cx="{x:.0f}" cy="{y:.0f}" r="{random.choice([.7, 1, 1.3])}" fill="#e3ebfb" '
      f'style="animation-duration:{random.uniform(9, 16):.1f}s;animation-delay:{-random.uniform(0, 16):.1f}s"/>')

# ===== rak buku =====
COLORS = ["#5a1f24", "#4a191d", "#1f3b2d", "#18301f", "#1d2a4a", "#16213b", "#3a2440", "#3b2a1e", "#2c2f36", "#432a22"]

def shelf(x0, x1, y0, y1, row_h=64):
    a(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" fill="url(#wood)"/>')
    y = y0 + 10
    while y + row_h <= y1:
        x = x0 + 10
        while x < x1 - 14:
            if random.random() < .06:
                x += random.uniform(8, 20); continue
            w = random.uniform(9, 20); h = random.uniform(row_h * .62, row_h * .9)
            if x + w > x1 - 10: break
            col = random.choice(COLORS); top = y + row_h - h
            lean = random.random() < .05
            g = f' transform="rotate({random.choice([-8, 8])} {x + w / 2:.0f} {y + row_h:.0f})"' if lean else ''
            a(f'<g{g}><rect x="{x:.1f}" y="{top:.1f}" width="{w:.1f}" height="{h:.1f}" rx="1.2" fill="{col}"/>'
              f'<rect x="{x:.1f}" y="{top + 6:.1f}" width="{w:.1f}" height="1.3" fill="#9aa3b5" opacity=".45"/>'
              f'<rect x="{x:.1f}" y="{top + h - 8:.1f}" width="{w:.1f}" height="1.3" fill="#9aa3b5" opacity=".45"/>'
              f'<rect x="{x:.1f}" y="{top:.1f}" width="{w * .25:.1f}" height="{h:.1f}" fill="#fff" opacity=".04"/></g>')
            x += w + random.uniform(.5, 2)
        a(f'<rect x="{x0}" y="{y + row_h}" width="{x1 - x0}" height="8" fill="#2f2018"/><rect x="{x0}" y="{y + row_h}" width="{x1 - x0}" height="1.5" fill="#4a3426"/>')
        y += row_h + 8
    a(f'<rect x="{x0}" y="{y0}" width="10" height="{y1 - y0}" fill="#24180f"/><rect x="{x1 - 10}" y="{y0}" width="10" height="{y1 - y0}" fill="#24180f"/>')

shelf(0, 420, 0, H)
shelf(W - 420, W, 0, H)
# tangga perpustakaan
a('<g stroke="#3d2a1f" stroke-width="5" stroke-linecap="round"><line x1="330" y1="40" x2="300" y2="400"/><line x1="372" y1="40" x2="342" y2="400"/></g>')
a('<g stroke="#3d2a1f" stroke-width="4">' + "".join(f'<line x1="{328 - i * 2.4:.0f}" y1="{70 + i * 30}" x2="{370 - i * 2.4:.0f}" y2="{70 + i * 30}"/>' for i in range(11)) + '</g>')

# lilin kecil di rak
for i, (cx, cy) in enumerate([(120, 136), (250, 280), (900, 208), (1080, 352), (1130, 64)]):
    a(f'<g transform="translate({cx} {cy})"><circle cx="0" cy="-16" r="24" fill="url(#bhalo)"/>'
      f'<rect x="-4" y="-14" width="8" height="18" rx="1.5" fill="#d9dde6"/>'
      f'<ellipse class="flame" cx="0" cy="-20" rx="3.4" ry="7" fill="url(#bflame)" filter="url(#soft)" style="animation-delay:{i * .13:.2f}s"/></g>')

# vignette + area gelap di belakang judul agar terbaca
a(f'<rect width="{W}" height="{H}" fill="url(#vig)"/>')
a(f'<ellipse cx="{W / 2}" cy="262" rx="270" ry="62" fill="#000000" opacity=".6" filter="url(#blur6)"/>')

# ===== judul =====
a(f'<text x="{W / 2}" y="262" text-anchor="middle" class="serif" font-size="58" font-weight="700" letter-spacing="2" fill="url(#silver)">Efan Ramdhani</text>')
a(f'<line x1="{W / 2 - 150}" y1="280" x2="{W / 2 + 150}" y2="280" stroke="#9aa8c4" stroke-width=".8" opacity=".6"/>')
for i, s in enumerate(["AI Engineer in training", "mahasiswa ITS · data &amp; machine learning", "setiap jawaban dimulai dari membaca"]):
    a(f'<text x="{W / 2}" y="306" text-anchor="middle" class="serif sub s{i + 1}" font-size="19" font-style="italic" fill="#c5cede">{s}</text>')

# ===== buku terbuka melayang =====
BX, BY = W / 2, 352
a(f'<g class="float"><ellipse cx="{BX}" cy="{BY + 2}" rx="90" ry="26" fill="url(#bookglow)"/>')
a(f'<path d="M{BX} {BY - 18} Q{BX - 30} {BY - 26} {BX - 62} {BY - 20} L{BX - 62} {BY + 10} Q{BX - 30} {BY + 4} {BX} {BY + 12} Z" fill="url(#page)"/>')
a(f'<path d="M{BX} {BY - 18} Q{BX + 30} {BY - 26} {BX + 62} {BY - 20} L{BX + 62} {BY + 10} Q{BX + 30} {BY + 4} {BX} {BY + 12} Z" fill="url(#pageR)"/>')
for k in range(4):
    a(f'<line x1="{BX - 54}" y1="{BY - 12 + k * 6}" x2="{BX - 10}" y2="{BY - 10 + k * 6}" stroke="#8c93a3" stroke-width=".8" opacity=".6"/>')
    a(f'<line x1="{BX + 10}" y1="{BY - 10 + k * 6}" x2="{BX + 54}" y2="{BY - 12 + k * 6}" stroke="#8c93a3" stroke-width=".8" opacity=".6"/>')
a(f'<g class="turn2"><path class="turn" d="M{BX} {BY - 18} Q{BX + 30} {BY - 26} {BX + 62} {BY - 20} L{BX + 62} {BY + 10} Q{BX + 30} {BY + 4} {BX} {BY + 12} Z" fill="#f4f5f8" stroke="#c8ccd6" stroke-width=".5"/></g>')
a(f'<path d="M{BX - 64} {BY + 10} Q{BX - 30} {BY + 6} {BX} {BY + 15} Q{BX + 30} {BY + 6} {BX + 64} {BY + 10} L{BX + 64} {BY + 14} Q{BX + 30} {BY + 10} {BX} {BY + 19} Q{BX - 30} {BY + 10} {BX - 64} {BY + 14} Z" fill="#4a191d"/>')
for i in range(7):
    a(f'<circle class="rise" cx="{BX + random.uniform(-40, 40):.0f}" cy="{BY - 18}" r="{random.choice([1, 1.4])}" fill="#e3ecff" filter="url(#soft)" '
      f'style="--dx:{random.uniform(-25, 25):.0f}px;animation-delay:{i:.0f}s"/>')
a('</g></g>')
a(f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="18" fill="none" stroke="#2b1d16"/>')
a('</svg>')

pathlib.Path(__file__).resolve().parent.parent.joinpath('assets/header.svg').write_text('\n'.join(o))
print('ok')
