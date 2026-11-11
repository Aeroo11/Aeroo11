"""Grafik kontribusi GitHub beranimasi bergaya langit malam.

Pemakaian:
  GITHUB_TOKEN=... python scripts/kontribusi.py Aeroo11   # data asli (dipakai GitHub Actions)
  python scripts/kontribusi.py --demo                     # data acak untuk pratinjau
Output: assets/kontribusi.svg
"""
import json, os, random, sys, pathlib, urllib.request, datetime as dt

QUERY = """query($login:String!){user(login:$login){contributionsCollection{contributionCalendar{
 totalContributions weeks{contributionDays{date contributionCount weekday}}}}}}"""

def fetch(login, token):
    req = urllib.request.Request("https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": login}}).encode(),
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json", "User-Agent": "contribution-graph"})
    data = json.load(urllib.request.urlopen(req))
    if "errors" in data: raise SystemExit(data["errors"])
    cal = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    return [[(d["date"], d["contributionCount"], d["weekday"]) for d in w["contributionDays"]] for w in cal["weeks"]]

def demo():
    random.seed(7); start = dt.date.today() - dt.timedelta(days=364)
    start -= dt.timedelta(days=(start.weekday() + 1) % 7)
    weeks, d = [], start
    while d <= dt.date.today():
        wk = []
        for wd in range(7):
            if d > dt.date.today(): break
            burst = 1 + 3 * (abs((d - start).days % 90 - 45) < 12)
            wk.append((d.isoformat(), random.choice([0]*5 + [1, 2, 3, 5, 8]) * burst, wd)); d += dt.timedelta(days=1)
        weeks.append(wk)
    return weeks

def from_git(dirs, names):
    """Cadangan saat Actions tidak bisa jalan: hitung commit milik pemilik dari clone lokal."""
    import subprocess, collections
    cnt = collections.Counter()
    for d in dirs:
        out = subprocess.run(["git", "-C", d, "log", "--all", "--format=%an|%ae|%ad", "--date=short"],
                             capture_output=True, text=True).stdout
        for line in out.splitlines():
            an, ae, day = line.split("|")
            if an in names or ae in names: cnt[day] += 1
    today = dt.date.today(); start = today - dt.timedelta(days=364)
    start -= dt.timedelta(days=(start.weekday() + 1) % 7)
    weeks, d = [], start
    while d <= today:
        wk = []
        for wd in range(7):
            if d > today: break
            wk.append((d.isoformat(), cnt[d.isoformat()], wd)); d += dt.timedelta(days=1)
        weeks.append(wk)
    return weeks

def stats(weeks):
    days = [x for w in weeks for x in w]
    total = sum(c for _, c, _ in days)
    best = max(days, key=lambda x: x[1])
    longest = cur = 0
    for _, c, _ in days:
        cur = cur + 1 if c else 0; longest = max(longest, cur)
    cur = 0
    for _, c, _ in reversed(days[:-1] if days and days[-1][1] == 0 else days):
        if not c: break
        cur += 1
    return total, best, longest, cur

BULAN = "Jan Feb Mar Apr Mei Jun Jul Agu Sep Okt Nov Des".split()

def level(c, q):
    if c == 0: return 0
    return 1 + sum(c > t for t in q)

def render(weeks, login):
    total, best, longest, cur = stats(weeks)
    nz = sorted(c for w in weeks for _, c, _ in w if c)
    q = [nz[int(len(nz) * f)] for f in (.25, .5, .75)] if nz else [1, 2, 3]
    CELL, GAP = 13, 3; X0, Y0 = 70, 92
    W = X0 + len(weeks) * (CELL + GAP) + 50; H = Y0 + 7 * (CELL + GAP) + 120
    ink = ["#3b5583", "#1f4f80", "#2f7fc0", "#5fb6ec", "#d4f3ff"]
    o = []; a = o.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Aktivitas kontribusi: {total} kontribusi dalam 12 bulan terakhir">')
    a('''<defs>
 <filter id="paper" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".8" numOctaves="3" seed="4"/>
  <feColorMatrix values="0 0 0 0 .55  0 0 0 0 .65  0 0 0 0 .9  0 0 0 .05 0"/><feComposite in2="SourceGraphic" operator="in"/><feBlend in="SourceGraphic" mode="screen"/></filter>
 <radialGradient id="vig" r=".75"><stop offset=".6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".55"/></radialGradient>
 <radialGradient id="orb"><stop offset="0" stop-color="#ffffff"/><stop offset=".5" stop-color="#bfe8ff"/><stop offset="1" stop-color="#4f9fe0"/></radialGradient>
 <filter id="glow" x="-80%" y="-80%" width="260%" height="260%"><feGaussianBlur stdDeviation="2.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
 <path id="foot" d="M0 -4.2c1.6 0 2.4 1.6 2.2 3.4-.2 1.6-1 2.2-1 3.6 0 1-.6 1.6-1.3 1.6S-1.4 4-1.4 3c0-1.6-.9-2.4-.9-4.2C-2.3-2.8-1.4-4.2 0-4.2z"/>
</defs>
<style>
 .t{font-family:Georgia,'Palatino Linotype','Book Antiqua',serif;fill:#dbe6f5}
 .star{opacity:.25;animation:tw 3.5s ease-in-out infinite}
 @keyframes tw{0%,100%{opacity:.15}50%{opacity:.7}}
 .hot{animation:pulse 2.4s ease-in-out infinite}
 @keyframes pulse{0%,100%{opacity:.75}50%{opacity:1}}
 .fp{opacity:0;animation:fp 14s linear infinite}
 @keyframes fp{0%{opacity:0}1%{opacity:.85}12%{opacity:.85}20%{opacity:0}100%{opacity:0}}
 .ink{stroke-dasharray:900;stroke-dashoffset:900;animation:draw 3s ease-out forwards}
 @keyframes draw{to{stroke-dashoffset:0}}
 .cell{opacity:0;animation:appear .5s ease-out forwards}
 @keyframes appear{to{opacity:1}}
 .wing{animation:flap .12s ease-in-out infinite alternate;transform-box:fill-box}
 .wl{transform-origin:100% 100%}.wr{transform-origin:0% 100%}
 @keyframes flap{from{transform:rotate(-25deg)}to{transform:rotate(20deg)}}
</style>''')
    # perkamen
    a(f'<rect x="4" y="4" width="{W-8}" height="{H-8}" rx="10" fill="#0d1328" filter="url(#paper)"/>')
    a(f'<rect x="4" y="4" width="{W-8}" height="{H-8}" rx="10" fill="url(#vig)"/>')
    rnd = random.Random(3)
    for _ in range(70):
        a(f'<circle class="star" cx="{rnd.uniform(20, W-20):.0f}" cy="{rnd.uniform(20, H-20):.0f}" r="{rnd.choice([.5,.7,1])}" fill="#fff" style="animation-delay:{rnd.uniform(0,3):.1f}s"/>')
    a(f'<rect x="14" y="14" width="{W-28}" height="{H-28}" rx="6" fill="none" stroke="#5f7fb0" stroke-width="1.2" stroke-dasharray="2 4" opacity=".6"/>')
    a(f'<text class="t" x="{W/2}" y="46" text-anchor="middle" font-size="24" font-weight="700" letter-spacing="2">AKTIVITAS KONTRIBUSI</text>')
    a(f'<text class="t" x="{W/2}" y="68" text-anchor="middle" font-size="13" font-style="italic" opacity=".8">Kontribusi GitHub {login} dalam 12 bulan terakhir</text>')
    # kompas
    cx, cy = W - 58, 52
    a(f'<g opacity=".75" transform="translate({cx} {cy})"><circle r="20" fill="none" stroke="#8fb0dc"/><polygon points="0,-18 4,0 0,18 -4,0" fill="#bcd3f0"/><polygon points="-18,0 0,-4 18,0 0,4" fill="#5f7fb0"/>'
      f'<text class="t" y="-23" text-anchor="middle" font-size="9">U</text>'
      '<animateTransform attributeName="transform" type="rotate" additive="sum" values="-8;8;-8" dur="6s" repeatCount="indefinite"/></g>')
    # label hari & bulan
    for wd, nm in ((1, "Sen"), (3, "Rab"), (5, "Jum")):
        a(f'<text class="t" x="{X0-8}" y="{Y0 + wd*(CELL+GAP) + 10}" text-anchor="end" font-size="10" opacity=".75">{nm}</text>')
    last = None
    for i, w in enumerate(weeks):
        m = int(w[0][0][5:7])
        if m != last and i < len(weeks) - 2:
            a(f'<text class="t" x="{X0 + i*(CELL+GAP)}" y="{Y0-8}" font-size="10" opacity=".75">{BULAN[m-1]}</text>'); last = m
    # sel kontribusi
    for i, w in enumerate(weeks):
        for date, c, wd in w:
            x = X0 + i*(CELL+GAP); y = Y0 + wd*(CELL+GAP); lv = level(c, q)
            delay = f"animation-delay:{i*0.025:.2f}s"
            tip = f"<title>{date}: {c} kontribusi</title>"
            if lv == 0:
                a(f'<rect class="cell" style="{delay}" x="{x+1}" y="{y+1}" width="{CELL-2}" height="{CELL-2}" rx="3" fill="none" stroke="{ink[0]}" stroke-width="1">{tip}</rect>')
            elif lv < 4:
                a(f'<rect class="cell" style="{delay}" x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="3" fill="{ink[lv]}">{tip}</rect>')
            else:
                a(f'<g class="cell" style="{delay}"><rect class="hot" x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="3" fill="{ink[4]}" filter="url(#glow)" style="animation-delay:{(i%7)*.3:.1f}s">{tip}</rect></g>')
    # jejak kaki: mengikuti hari tersibuk tiap minggu
    pts = []
    for i, w in enumerate(weeks):
        wd = max(w, key=lambda d: d[1])[2] if any(d[1] for d in w) else 3
        pts.append((X0 + i*(CELL+GAP) + CELL/2, Y0 + wd*(CELL+GAP) + CELL/2))
    n = len(pts)
    for i in range(n - 1):
        (x1, y1), (x2, y2) = pts[i], pts[i+1]
        import math
        ang = math.degrees(math.atan2(y2-y1, x2-x1)) + 90
        for k, side in ((0, -1), (1, 1)):
            f = (k + .5) / 2; px = x1 + (x2-x1)*f; py = y1 + (y2-y1)*f
            nx, ny = math.cos(math.radians(ang)), math.sin(math.radians(ang))
            d = (i*2 + k) / (2*n) * 14 * .8
            a(f'<use href="#foot" class="fp" fill="#cfe0f5" style="animation-delay:{d:.2f}s" transform="translate({px+nx*3*side:.1f} {py+ny*3*side:.1f}) rotate({ang:.0f}) scale(1.1)"/>')
    # bola emas bersayap
    path = "M{} {} ".format(X0-20, Y0+20) + " ".join(
        f"Q{X0 + (j+.5)*(W-X0-60)/6:.0f} {Y0 + (-30 if j%2 else 7*(CELL+GAP)+30)} {X0 + (j+1)*(W-X0-60)/6:.0f} {Y0 + 3.5*(CELL+GAP):.0f}" for j in range(6))
    a(f'<g><g filter="url(#glow)"><ellipse class="wing wl" cx="-7" cy="-3" rx="7" ry="3" fill="#e8f6ff" opacity=".9"/>'
      f'<ellipse class="wing wr" cx="7" cy="-3" rx="7" ry="3" fill="#e8f6ff" opacity=".9"/><circle r="5" fill="url(#orb)"/></g>'
      f'<animateMotion dur="11s" repeatCount="indefinite" path="{path} Q{W/2} {Y0-60} {X0-20} {Y0+20}"/></g>')
    # segel statistik
    yb = Y0 + 7*(CELL+GAP) + 30
    seals = [(f"{total}", "total kontribusi"), (f"{longest} hari", "streak terpanjang"),
             (f"{cur} hari", "streak saat ini"), (f"{best[1]}", f"rekor harian · {best[0]}")]
    sw = (W - 2*X0) / len(seals)
    for k, (big, small) in enumerate(seals):
        sx = X0 + sw*k + 26
        a(f'<g transform="translate({sx} {yb+22})"><circle r="17" fill="#1b3358"/><circle r="13" fill="none" stroke="#8fb0dc" stroke-dasharray="3 2"/>'
          f'<text x="0" y="5" text-anchor="middle" font-size="14" fill="#cfe8ff" font-family="Georgia,serif">&#10022;</text></g>')
        a(f'<text class="t" x="{sx+26}" y="{yb+18}" font-size="17" font-weight="700">{big}</text>')
        a(f'<text class="t" x="{sx+26}" y="{yb+35}" font-size="11" opacity=".8">{small}</text>')
    # legenda
    lx = W - 230; ly = H - 30
    a(f'<text class="t" x="{lx-8}" y="{ly+10}" font-size="10" text-anchor="end" opacity=".75">sedikit</text>')
    for k in range(5):
        if k == 0: a(f'<rect x="{lx+k*16+1}" y="{ly+1}" width="11" height="11" rx="3" fill="none" stroke="{ink[0]}"/>')
        else: a(f'<rect x="{lx+k*16}" y="{ly}" width="13" height="13" rx="3" fill="{ink[k] if k<4 else ink[4]}"/>')
    a(f'<text class="t" x="{lx+86}" y="{ly+10}" font-size="10" opacity=".75">banyak</text>')
    a(f'<text class="t" x="{X0}" y="{ly+10}" font-size="10" font-style="italic" opacity=".6">diperbarui {dt.date.today().isoformat()}</text>')
    a('</svg>')
    return "\n".join(o)

if __name__ == "__main__":
    login = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else "Aeroo11"
    if "--demo" in sys.argv: weeks = demo()
    elif "--from-git" in sys.argv:
        dirs = sys.argv[sys.argv.index("--from-git") + 1:]
        weeks = from_git(dirs, set(os.environ.get("AUTHOR_NAMES", login).split(",")))
    else: weeks = fetch(login, os.environ["GITHUB_TOKEN"])
    out = pathlib.Path(__file__).resolve().parent.parent / "assets" / "kontribusi.svg"
    out.write_text(render(weeks, login)); print("ditulis:", out)
