"""Membuat assets/header.svg: kastil sihir di tepi danau pada malam hari (SVG murni, gambar orisinal)."""
import math, random, pathlib

random.seed(9)
W, H = 1200, 420
LAKE = 318          # garis permukaan danau
o = []
a = o.append

a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Efan Ramdhani - AI Engineer in training">')
a(f'''<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#03050f"/><stop offset=".45" stop-color="#0a1430"/><stop offset="1" stop-color="#1d2f57"/>
  </linearGradient>
  <linearGradient id="lake" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#0f1c3a"/><stop offset="1" stop-color="#02040b"/>
  </linearGradient>
  <radialGradient id="moonglow"><stop offset="0" stop-color="#dfe9ff" stop-opacity=".55"/><stop offset=".35" stop-color="#9fb8ef" stop-opacity=".18"/><stop offset="1" stop-color="#9fb8ef" stop-opacity="0"/></radialGradient>
  <radialGradient id="moon" cx=".42" cy=".4"><stop offset="0" stop-color="#ffffff"/><stop offset=".7" stop-color="#e3eaf7"/><stop offset="1" stop-color="#b9c6de"/></radialGradient>
  <linearGradient id="silver" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#8fa3c7"/><stop offset=".35" stop-color="#e8eefa"/><stop offset=".5" stop-color="#ffffff"/>
    <stop offset=".65" stop-color="#e8eefa"/><stop offset="1" stop-color="#8fa3c7"/>
    <animateTransform attributeName="gradientTransform" type="translate" values="-1 0;1 0" dur="5s" repeatCount="indefinite"/>
  </linearGradient>
  <linearGradient id="spell" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#ffffff" stop-opacity="0"/><stop offset=".3" stop-color="#cfe6ff"/><stop offset="1" stop-color="#ffffff"/>
  </linearGradient>
  <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="1.3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="mist" x="-30%" y="-100%" width="160%" height="300%"><feGaussianBlur stdDeviation="14"/></filter>
  <filter id="ripple" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.004 0.09" numOctaves="2" seed="3">
      <animate attributeName="baseFrequency" values="0.004 0.09;0.004 0.12;0.004 0.09" dur="7s" repeatCount="indefinite"/>
    </feTurbulence>
    <feDisplacementMap in="SourceGraphic" scale="9" xChannelSelector="R" yChannelSelector="G"/>
    <feGaussianBlur stdDeviation=".8"/>
  </filter>
  <clipPath id="frame"><rect width="{W}" height="{H}" rx="20"/></clipPath>
  <clipPath id="above"><rect width="{W}" height="{LAKE}"/></clipPath>
</defs>''')
a('''<style>
  .tw{animation:tw 3s ease-in-out infinite}
  @keyframes tw{0%,100%{opacity:.2}50%{opacity:1}}
  .win{animation:win 5s ease-in-out infinite}
  @keyframes win{0%,100%{opacity:.9}40%{opacity:.45}60%{opacity:1}}
  .mist{animation:mist 22s ease-in-out infinite alternate}
  @keyframes mist{from{transform:translateX(-80px)}to{transform:translateX(120px)}}
  .owl{animation:owl 16s linear infinite}
  @keyframes owl{0%{transform:translate(380px,200px) scale(.8);opacity:0}6%{opacity:1}
    45%{transform:translate(860px,118px) scale(1.5)}94%{opacity:1}100%{transform:translate(1260px,40px) scale(1.1);opacity:0}}
  .wing{animation:flap .45s ease-in-out infinite alternate;transform-box:fill-box;transform-origin:50% 100%}
  @keyframes flap{from{transform:scaleY(1)}to{transform:scaleY(-.55)}}
  .cast{stroke-dasharray:1200;stroke-dashoffset:1200;animation:cast 7s ease-in-out infinite}
  @keyframes cast{0%{stroke-dashoffset:1200;opacity:1}40%{stroke-dashoffset:0;opacity:1}75%{stroke-dashoffset:0;opacity:.9}100%{stroke-dashoffset:0;opacity:0}}
  .spark{animation:spark 2.4s ease-out infinite}
  @keyframes spark{0%{opacity:0;transform:translate(0,0)}15%{opacity:1}100%{opacity:0;transform:translate(var(--dx),var(--dy))}}
  .bolt{animation:bolt 4s infinite}
  @keyframes bolt{0%,88%,100%{opacity:.85}90%{opacity:.2}92%{opacity:1}94%{opacity:.3}96%{opacity:1}}
  .sub{opacity:0;animation:sub 12s infinite}
  @keyframes sub{0%{opacity:0}3%,30%{opacity:1}33%,100%{opacity:0}}
  .s2{animation-delay:4s}.s3{animation-delay:8s}
  .type{animation:type 4s steps(28) infinite}
  @keyframes type{0%{transform:scaleX(0)}40%,100%{transform:scaleX(1)}}
  .shoot{animation:shoot 9s ease-in infinite}
  @keyframes shoot{0%,78%{transform:translate(0,0);opacity:0}80%{opacity:1}90%{transform:translate(-300px,140px);opacity:0}100%{opacity:0}}
  .serif{font-family:Georgia,'Palatino Linotype','Book Antiqua',serif}
</style>''')
a(f'<g clip-path="url(#frame)">')
a(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')

# bintang
for _ in range(150):
    x, y = random.uniform(0, W), random.uniform(0, LAKE - 40)
    a(f'<circle class="tw" cx="{x:.0f}" cy="{y:.0f}" r="{random.choice([.5, .7, .9, 1.3])}" fill="#fff" '
      f'style="animation-delay:{random.uniform(0, 3):.1f}s;animation-duration:{random.uniform(2, 5):.1f}s"/>')
a('<g class="shoot"><line x1="700" y1="30" x2="770" y2="-3" stroke="url(#spell)" stroke-width="1.6" transform="rotate(180 735 13)"/>'
  '<circle cx="700" cy="30" r="2" fill="#fff" filter="url(#soft)"/></g>')

# bulan
MX, MY = 860, 112
a(f'<circle cx="{MX}" cy="{MY}" r="150" fill="url(#moonglow)"/><circle cx="{MX}" cy="{MY}" r="56" fill="url(#moon)"/>')
for dx, dy, r in [(-16, -10, 9), (14, 12, 6), (-4, 22, 4), (20, -18, 5)]:
    a(f'<circle cx="{MX + dx}" cy="{MY + dy}" r="{r}" fill="#c6d1e6" opacity=".55"/>')

# ===== kastil =====
def castle(ox, base, scale, fill, lit):
    s = []
    p = s.append
    # (x relatif, lebar, tinggi badan, tinggi atap)
    towers = [(0, 26, 70, 46), (34, 18, 105, 52), (60, 40, 60, 0), (104, 22, 140, 64), (132, 30, 90, 40),
              (170, 16, 170, 78), (192, 34, 110, 0), (232, 24, 150, 60), (262, 44, 75, 0), (312, 20, 120, 56),
              (338, 28, 85, 44), (372, 14, 135, 58), (392, 36, 60, 0), (434, 22, 95, 46)]
    wins = []
    for tx, tw, th, rh in towers:
        x = ox + tx * scale; w = tw * scale; h = th * scale; top = base - h
        p(f'<rect x="{x:.1f}" y="{top:.1f}" width="{w:.1f}" height="{h + 4:.1f}"/>')
        if rh:
            r = rh * scale
            p(f'<path d="M{x - 3 * scale:.1f} {top:.1f} Q{x + w / 2:.1f} {top - r * .35:.1f} {x + w / 2:.1f} {top - r:.1f} Q{x + w / 2:.1f} {top - r * .35:.1f} {x + w + 3 * scale:.1f} {top:.1f}Z"/>')
            p(f'<line x1="{x + w / 2:.1f}" y1="{top - r:.1f}" x2="{x + w / 2:.1f}" y2="{top - r - 9 * scale:.1f}" stroke="{fill}" stroke-width="{1.4 * scale:.1f}"/>')
        else:
            for i in range(int(tw // 8)):
                p(f'<rect x="{x + i * 8 * scale + scale:.1f}" y="{top - 5 * scale:.1f}" width="{5 * scale:.1f}" height="{5 * scale:.1f}"/>')
        if lit:
            for _ in range(random.randint(1, 3) if h > 60 * scale else 1):
                wx = x + random.uniform(.25, .65) * w; wy = top + random.uniform(.15, .75) * h
                wins.append(f'<path class="win" d="M{wx:.1f} {wy + 7 * scale:.1f}v-{4 * scale:.1f}a{1.8 * scale:.1f} {1.8 * scale:.1f} 0 0 1 {3.6 * scale:.1f} 0v{4 * scale:.1f}z" '
                            f'fill="#cfe2ff" style="animation-delay:{random.uniform(0, 5):.1f}s"/>')
    # jembatan berlengkung
    bx = ox + 262 * scale; by = base - 40 * scale
    p(f'<path d="M{bx - 60 * scale:.1f} {by:.1f} h{150 * scale:.1f} v{8 * scale:.1f} ' +
      " ".join(f'h-{6 * scale:.1f} a{9 * scale:.1f} {12 * scale:.1f} 0 0 0 -{18 * scale:.1f} 0' for _ in range(6)) + ' Z"/>')
    return f'<g fill="{fill}">' + "".join(s) + '</g>' + "".join(wins)

CX0 = 590
cliff = (f'<path d="M{CX0 - 40} {LAKE} L{CX0 - 10} {LAKE - 40} L{CX0 + 30} {LAKE - 52} L{CX0 + 90} {LAKE - 60} L{CX0 + 200} {LAKE - 66} '
         f'L{CX0 + 330} {LAKE - 62} L{CX0 + 450} {LAKE - 70} L{CX0 + 520} {LAKE - 50} L{CX0 + 560} {LAKE - 30} L{CX0 + 600} {LAKE} Z" fill="#05070f"/>')
far = castle(CX0 + 40, LAKE - 50, .9, "#16244a", False)
near = castle(CX0 + 20, LAKE - 58, 1.15, "#05070f", True)
scene = f'<g opacity=".9">{far}</g>{near}{cliff}'
a(f'<g clip-path="url(#above)">{scene}</g>')

# danau + pantulan
a(f'<rect x="0" y="{LAKE}" width="{W}" height="{H - LAKE}" fill="url(#lake)"/>')
a(f'<g filter="url(#ripple)" opacity=".45"><g transform="translate(0 {2 * LAKE}) scale(1 -1)">{scene}'
  f'<circle cx="{MX}" cy="{MY}" r="56" fill="#dfe9ff" opacity=".7"/></g></g>')
for i in range(9):
    w = random.uniform(30, 90)
    a(f'<rect class="tw" x="{MX - w / 2 + random.uniform(-25, 25):.0f}" y="{LAKE + 12 + i * 9}" width="{w:.0f}" height="1.4" fill="#e3ecff" opacity=".6" '
      f'style="animation-delay:{i * .35:.2f}s"/>')
a(f'<rect x="0" y="{LAKE}" width="{W}" height="1" fill="#6f86b8" opacity=".45"/>')
# kabut
for y, op, d in [(LAKE - 18, .22, 0), (LAKE + 10, .18, -8)]:
    a(f'<g class="mist" style="animation-delay:{d}s"><ellipse cx="{W / 2}" cy="{y}" rx="{W * .55:.0f}" ry="18" fill="#b8c8e8" opacity="{op}" filter="url(#mist)"/></g>')

# burung hantu
a('<g class="owl"><g transform="translate(0 0)">'
  '<path class="wing" d="M0 0 C-10 -12 -26 -12 -34 -2 C-24 -6 -12 -3 0 0Z" fill="#05070f"/>'
  '<path class="wing" d="M0 0 C10 -12 26 -12 34 -2 C24 -6 12 -3 0 0Z" fill="#05070f"/>'
  '<ellipse cx="0" cy="2" rx="6" ry="8" fill="#05070f"/><path d="M-5 -5 l2 -5 l3 4 l3 -4 l2 5z" fill="#05070f"/></g></g>')

# ===== judul & mantra =====
TX = 70
a(f'<g class="bolt" filter="url(#glow)"><path d="M{TX + 4} 70 l-14 26 h11 l-9 22 l22 -30 h-11 l10 -18z" fill="#e8eefa"/></g>')
a(f'<text x="{TX + 32}" y="112" class="serif" font-size="66" font-weight="700" letter-spacing="1.5" fill="url(#silver)" filter="url(#soft)">Efan Ramdhani</text>')
subs = ["AI Engineer in training", "Fakultas Sihir Data · ITS", "merapal model, bukan sekadar kode"]
for i, s in enumerate(subs):
    w = len(s) * 12.5
    a(f'<g class="sub s{i + 1}"><clipPath id="cl{i}"><rect class="type" x="{TX + 34}" y="132" width="{w:.0f}" height="34" '
      f'style="transform-origin:{TX + 34}px 0;animation-delay:{i * 4}s"/></clipPath>'
      f'<text x="{TX + 34}" y="158" class="serif" font-size="24" font-style="italic" fill="#c9d6ee" clip-path="url(#cl{i})">{s}</text></g>')
# tongkat + pita mantra
a(f'<g transform="translate({TX - 12} 262) rotate(-32)"><rect x="0" y="-3.5" width="118" height="7" rx="3.5" fill="#3a2a22"/>'
  '<rect x="0" y="-4.5" width="36" height="9" rx="4" fill="#24170f"/><circle cx="12" cy="0" r="1.6" fill="#5a4334"/><circle cx="22" cy="0" r="1.6" fill="#5a4334"/></g>')
TIPX, TIPY = TX - 12 + 118 * math.cos(math.radians(-32)), 262 + 118 * math.sin(math.radians(-32))
a(f'<path class="cast" d="M{TIPX:.0f} {TIPY:.0f} C {TIPX + 80:.0f} {TIPY - 70:.0f}, {TIPX + 160:.0f} {TIPY + 40:.0f}, {TIPX + 260:.0f} {TIPY - 10:.0f} '
  f'S {TIPX + 420:.0f} {TIPY - 60:.0f}, {TIPX + 500:.0f} {TIPY - 20:.0f}" fill="none" stroke="url(#spell)" stroke-width="3" stroke-linecap="round" filter="url(#glow)"/>')
for i in range(14):
    a(f'<circle class="spark" cx="{TIPX:.0f}" cy="{TIPY:.0f}" r="{random.choice([1.2, 1.8, 2.4])}" fill="#e6f1ff" filter="url(#soft)" '
      f'style="--dx:{random.uniform(-30, 50):.0f}px;--dy:{random.uniform(-50, 20):.0f}px;animation-delay:{i * .17:.2f}s"/>')
a('</g>')
a(f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="20" fill="none" stroke="#2a3a66" opacity=".8"/>')
a('</svg>')

pathlib.Path(__file__).resolve().parent.parent.joinpath('assets/header.svg').write_text('\n'.join(o))
print('ok')
