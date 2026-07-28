#!/usr/bin/env python3
# KRECA square advert tile for the San Rocco festival poster.
import math, base64, os

SCR = os.path.dirname(os.path.abspath(__file__))
ANTON = base64.b64encode(open(os.path.join(SCR, "anton.woff2"), "rb").read()).decode()
MONT  = base64.b64encode(open(os.path.join(SCR, "mont.woff2"), "rb").read()).decode()

def blueprint():
    cx, cy, parts = 100, 100, []
    for r in (30, 52, 74, 92):
        parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" />')
    for a in range(0, 360, 5):
        rad = math.radians(a); long = (a % 30 == 0)
        r1 = 74; r2 = 92 if long else 84
        parts.append(f'<line x1="{cx+r1*math.cos(rad):.1f}" y1="{cy+r1*math.sin(rad):.1f}" '
                     f'x2="{cx+r2*math.cos(rad):.1f}" y2="{cy+r2*math.sin(rad):.1f}" />')
    teeth = []
    for a in range(0, 360, 20):
        for off, r in ((-5, 30), (-3, 40), (3, 40), (5, 30)):
            rr = math.radians(a + off)
            teeth.append(f"{cx+r*math.cos(rr):.1f},{cy+r*math.sin(rr):.1f}")
    parts.append(f'<polygon points="{" ".join(teeth)}" />')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="12" />')
    parts.append(f'<line x1="{cx}" y1="4" x2="{cx}" y2="196" />')
    parts.append(f'<line x1="4" y1="{cy}" x2="196" y2="{cy}" />')
    return ('<svg class="bp" viewBox="0 0 200 200" fill="none" stroke="currentColor" '
            'stroke-width="0.8" vector-effect="non-scaling-stroke">' + "".join(parts) + '</svg>')

def logo():
    return ('<span class="logo">'
            '<svg class="mk" viewBox="0 0 48 48" aria-hidden="true">'
            '<path d="M11 3 H46 L37 45 H2 Z" fill="var(--red)"/>'
            '<g stroke="#fff" stroke-width="4.6" fill="none">'
            '<path d="M17 13 V35"/><path d="M17 25 L30 13"/><path d="M17 24 L32 35"/>'
            '</g></svg>'
            '<span class="wm"><b>KRECA</b><i>officina metalmeccanica</i></span></span>')

SERVICES = [
    "Carpenteria e strutture in ferro",
    "Serramenti e infissi · ferro, alluminio, PVC",
    "Cancelli, serrande e inferriate",
    "Porte blindate e sistemi di sicurezza",
    "Manutenzione tecnica e chiusure",
    "Pronto intervento su accessi e chiusure",
]
serv = "".join(f'<li>{s}</li>' for s in SERVICES)

CSS = """
:root{--ink:#0C0D10;--red:#DA2128;--red-deep:#9E121A;--red-ink:#F04A50;
  --steel:#A6AEBB;--white:#F3F5F8;--line:rgba(166,174,187,.16);--line2:rgba(166,174,187,.34)}
*{box-sizing:border-box;margin:0}
body{background:#0a0b0e;display:flex;justify-content:center;padding:clamp(10px,3vw,40px)}
.tile{position:relative;overflow:hidden;width:min(760px,94vw);aspect-ratio:1/1;
  container-type:size;color:var(--white);font-family:"Mont",system-ui,sans-serif;
  background:linear-gradient(155deg,#15171c 0%,#0e1014 60%,#0b0c0f 100%);
  box-shadow:0 30px 70px -30px rgba(0,0,0,.85);display:flex;flex-direction:column;
  padding:7cqw 7cqw 0}
.tile::before{content:"";position:absolute;inset:0;opacity:.5;pointer-events:none;
  background:linear-gradient(var(--line) 1px,transparent 1px) 0 0/100% 6cqw,
            linear-gradient(90deg,var(--line) 1px,transparent 1px) 0 0/6cqw 100%}
.tile>*{position:relative;z-index:2}
/* red corner + gear */
.corner{position:absolute;z-index:1;right:-22%;top:-30%;width:70%;height:70%;
  background:linear-gradient(135deg,var(--red),var(--red-deep));transform:skewX(-14deg)}
.bpwrap{position:absolute;z-index:1;right:-6cqw;top:-4cqw;width:46cqw;color:#fff;
  opacity:.16;transform:none}.bp{width:100%;height:auto;display:block}
/* header */
.head{display:flex;justify-content:space-between;align-items:flex-start}
.logo{display:inline-flex;align-items:center;gap:2.2cqw}
.logo .mk{width:8cqw;height:8cqw;flex:none;filter:drop-shadow(0 2px 6px rgba(0,0,0,.4))}
.logo .wm{display:flex;flex-direction:column;line-height:1}
.logo .wm b{font-family:"Anton";font-weight:400;font-size:6.4cqw;letter-spacing:.12em;color:#fff}
.logo .wm i{font-style:normal;font-weight:600;font-size:1.75cqw;letter-spacing:.32em;
  text-transform:uppercase;color:var(--steel);margin-top:.6cqw}
.pill{font-weight:700;font-size:1.7cqw;letter-spacing:.16em;text-transform:uppercase;
  color:#fff;background:rgba(0,0,0,.28);border:1px solid rgba(255,255,255,.35);
  padding:1.2cqw 2cqw;white-space:nowrap}
/* hero */
.hero{margin-top:7cqw}
.kick{font-weight:600;font-size:2cqw;letter-spacing:.26em;text-transform:uppercase;color:var(--steel);
  display:flex;align-items:center;gap:1.6cqw}
.kick::before{content:"";width:5cqw;height:2px;background:var(--red)}
.hero h1{font-family:"Anton";font-weight:400;text-transform:uppercase;line-height:.92;
  font-size:10.6cqw;margin:2.4cqw 0 0;letter-spacing:.004em;text-wrap:balance}
.claim{font-weight:600;font-size:2.9cqw;color:var(--red-ink);margin-top:2.2cqw;letter-spacing:.01em}
/* services */
.serv{margin-top:5.5cqw}
.slab{font-weight:700;font-size:1.85cqw;letter-spacing:.24em;text-transform:uppercase;
  color:var(--red-ink);padding-bottom:1.8cqw;border-bottom:1px solid var(--line2);margin-bottom:2.6cqw}
.serv ul{list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:2.2cqw 5cqw}
.serv li{font-weight:500;font-size:2.4cqw;line-height:1.25;color:#E7EAEF;
  display:flex;align-items:baseline;gap:1.8cqw}
.serv li::before{content:"";width:1.9cqw;height:1.9cqw;flex:none;background:var(--red);
  transform:rotate(45deg);translate:0 .1cqw}
/* footer */
.foot{margin-top:auto;margin-left:-7cqw;margin-right:-7cqw;
  background:linear-gradient(135deg,var(--red),var(--red-deep));padding:4cqw 7cqw;
  display:flex;flex-direction:column;gap:2cqw}
.addr{display:flex;gap:6cqw;flex-wrap:wrap}
.addr .a{display:flex;flex-direction:column;gap:.5cqw}
.addr .k{font-weight:700;font-size:1.55cqw;letter-spacing:.18em;text-transform:uppercase;color:rgba(255,255,255,.78)}
.addr .v{font-weight:600;font-size:2cqw;color:#fff;line-height:1.25}
.contacts{display:flex;align-items:center;gap:2.4cqw;flex-wrap:wrap;
  border-top:1px solid rgba(255,255,255,.28);padding-top:2.6cqw}
.contacts .c{display:flex;align-items:baseline;gap:1.4cqw}
.contacts .cl{font-weight:700;font-size:1.5cqw;letter-spacing:.16em;text-transform:uppercase;color:rgba(255,255,255,.8)}
.contacts .cv{font-family:"Anton";font-weight:400;font-size:3.4cqw;color:#fff;letter-spacing:.01em}
.contacts .web{margin-left:auto;font-family:"Anton";font-size:3.2cqw;color:#fff;letter-spacing:.02em}
@page{size:160mm 160mm;margin:0}
@media print{body{padding:0;background:#fff}.tile{width:160mm;height:160mm;box-shadow:none}}
"""

FONTS = (f'@font-face{{font-family:"Anton";font-weight:400;font-display:swap;'
         f'src:url(data:font/woff2;base64,{ANTON}) format("woff2")}}'
         f'@font-face{{font-family:"Mont";font-weight:300 800;font-display:swap;'
         f'src:url(data:font/woff2;base64,{MONT}) format("woff2")}}')

HTML = f"""<title>KRECA — Riquadro San Rocco</title>
<style>{FONTS}{CSS}</style>
<main>
<div class="tile">
  <div class="corner"></div>
  <div class="bpwrap">{blueprint()}</div>
  <div class="head">{logo()}<span class="pill">Rutigliano · BA</span></div>
  <div class="hero">
    <span class="kick">General contractor metalmeccanico</span>
    <h1>Officina<br>metalmeccanica</h1>
    <p class="claim">Un solo partner, ogni opera — dalla progettazione alla posa.</p>
  </div>
  <div class="serv">
    <div class="slab">I nostri servizi</div>
    <ul>{serv}</ul>
  </div>
  <div class="foot">
    <div class="addr">
      <div class="a"><span class="k">Sede operativa</span>
        <span class="v">S.P. 240 delle Grotte Orientali 290<br>70018 Rutigliano (BA)</span></div>
      <div class="a"><span class="k">E-mail</span>
        <span class="v">info@kreca.it</span></div>
    </div>
    <div class="contacts">
      <span class="c"><span class="cl">Tel</span><span class="cv">080 875 5152</span></span>
      <span class="c"><span class="cl">Cell</span><span class="cv">+39 351 805 5489</span></span>
      <span class="web">www.kreca.it</span>
    </div>
  </div>
</div>
</main>"""

out_dir = "/home/user/CriVideo/san-rocco"
os.makedirs(out_dir, exist_ok=True)
open(os.path.join(out_dir, "kreca-riquadro.html"), "w").write(HTML)
print("wrote", os.path.join(out_dir, "kreca-riquadro.html"), len(HTML))
