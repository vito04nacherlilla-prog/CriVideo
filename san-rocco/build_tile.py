#!/usr/bin/env python3
# KRECA square advert tile for the San Rocco poster.
# Optimised for legibility when the tile is printed SMALL on a shared poster:
# few words, large bold type, high contrast, prominent contacts.
import math, base64, os

SCR = os.path.dirname(os.path.abspath(__file__))
ANTON = base64.b64encode(open(os.path.join(SCR, "anton.woff2"), "rb").read()).decode()
MONT  = base64.b64encode(open(os.path.join(SCR, "mont.woff2"), "rb").read()).decode()
LOGO  = base64.b64encode(open(os.path.join(SCR, "logo-kreca.png"), "rb").read()).decode()

def blueprint():
    cx, cy, parts = 100, 100, []
    for r in (30, 52, 74, 92):
        parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" />')
    for a in range(0, 360, 5):
        rad = math.radians(a); long = (a % 30 == 0)
        r1, r2 = 74, (92 if long else 84)
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
            'stroke-width="0.9" vector-effect="non-scaling-stroke">' + "".join(parts) + '</svg>')

# Few, short items — each fits one line so it can be set large.
SERVICES = [
    "Carpenteria e strutture in ferro",
    "Serramenti e infissi in alluminio",
    "Cancelli, serrande e porte blindate",
    "Manutenzione e pronto intervento",
]
serv = "".join(f'<li>{s}</li>' for s in SERVICES)

CSS = """
:root{--ink:#08090B;--panel:#14161B;
  --green:#30D158;--green-deep:#1E9E43;--green-dark:#0F5A2A;--green-ink:#5FE084;
  --text:#EAEDF1;--white:#FFFFFF;
  --line:rgba(139,146,156,.14)}
*{box-sizing:border-box;margin:0}
body{background:#050506;display:flex;justify-content:center;padding:clamp(10px,3vw,40px)}
.tile{position:relative;overflow:hidden;width:min(760px,94vw);aspect-ratio:1/1;
  container-type:size;color:var(--white);font-family:"Mont",system-ui,sans-serif;
  background:linear-gradient(155deg,#14161B 0%,#0c0d11 58%,#08090B 100%);
  box-shadow:0 30px 70px -30px rgba(0,0,0,.85);display:flex;flex-direction:column;
  padding:6.5cqw 7cqw 0}
.tile::before{content:"";position:absolute;inset:0;opacity:.45;pointer-events:none;
  background:linear-gradient(var(--line) 1px,transparent 1px) 0 0/100% 7cqw,
            linear-gradient(90deg,var(--line) 1px,transparent 1px) 0 0/7cqw 100%}
.tile>*{position:relative;z-index:2}
/* deep-green corner + gear */
.corner{position:absolute;z-index:1;right:-24%;top:-40%;width:60%;height:50%;
  background:linear-gradient(150deg,var(--green-deep) 0%,var(--green-dark) 100%);
  transform:skewX(-14deg)}
.bpwrap{position:absolute;z-index:1;right:-5cqw;top:-3cqw;width:42cqw;color:#fff;opacity:.13}
.bp{width:100%;height:auto;display:block}
/* header */
.head{display:flex;align-items:flex-start}
.logo-img{width:54cqw;height:auto;display:block;filter:drop-shadow(0 3px 10px rgba(0,0,0,.5))}
/* hero */
.hero{margin-top:4cqw}
.hero h1{font-family:"Anton";font-weight:400;text-transform:uppercase;line-height:.9;
  font-size:11cqw;color:#fff;letter-spacing:.004em;text-wrap:balance}
.claim{font-weight:700;font-size:3.05cqw;color:var(--green);margin-top:2cqw;letter-spacing:.005em}
/* services — large, high contrast, single column */
.serv{margin-top:3.2cqw}
.slab{font-family:"Anton";font-weight:400;text-transform:uppercase;font-size:3.1cqw;
  color:var(--green);letter-spacing:.03em;padding-bottom:1.2cqw;
  border-bottom:2px solid var(--green);margin-bottom:2.2cqw;display:inline-block}
.serv ul{list-style:none;display:flex;flex-direction:column;gap:2.3cqw}
.serv li{font-weight:600;font-size:3.15cqw;line-height:1.1;color:var(--white);
  display:flex;align-items:center;gap:2.4cqw}
.serv li::before{content:"";width:2.6cqw;height:2.6cqw;flex:none;background:var(--green);
  transform:rotate(45deg)}
/* footer — bright green band, ink text, big contacts */
.foot{margin-top:auto;margin-left:-7cqw;margin-right:-7cqw;color:var(--ink);
  background:linear-gradient(135deg,var(--green) 0%,#28C24F 100%);padding:3.8cqw 7cqw;
  display:flex;flex-direction:column;gap:2.6cqw}
.addr{font-weight:700;font-size:2.7cqw;line-height:1.3;color:var(--ink);letter-spacing:.005em}
.addr .em{display:block;font-weight:600;margin-top:.6cqw}
.contacts{display:flex;align-items:center;gap:3cqw;flex-wrap:wrap;
  border-top:2px solid rgba(8,9,11,.32);padding-top:3cqw}
.contacts .c{display:flex;align-items:baseline;gap:1.6cqw}
.contacts .cl{font-weight:800;font-size:2cqw;letter-spacing:.1em;text-transform:uppercase;color:rgba(8,9,11,.72)}
.contacts .cv{font-family:"Anton";font-weight:400;font-size:4.6cqw;color:var(--ink);letter-spacing:.005em}
.contacts .web{margin-left:auto;font-family:"Anton";font-size:4cqw;color:var(--ink);letter-spacing:.01em}
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
  <div class="head">
    <img class="logo-img" alt="KRECA — Officina Metalmeccanica"
         src="data:image/png;base64,{LOGO}">
  </div>
  <div class="hero">
    <h1>Officina<br>metalmeccanica</h1>
    <p class="claim">Un solo partner, ogni opera.</p>
  </div>
  <div class="serv">
    <span class="slab">Servizi</span>
    <ul>{serv}</ul>
  </div>
  <div class="foot">
    <div class="addr">S.P. 240 delle Grotte Orientali 290 — 70018 Rutigliano (BA)
      <span class="em">info@kreca.it · www.kreca.it</span></div>
    <div class="contacts">
      <span class="c"><span class="cl">Tel</span><span class="cv">080 875 5152</span></span>
      <span class="c"><span class="cl">Cell</span><span class="cv">+39 351 805 5489</span></span>
    </div>
  </div>
</div>
</main>"""

out_dir = "/home/user/CriVideo/san-rocco"
os.makedirs(out_dir, exist_ok=True)
open(os.path.join(out_dir, "kreca-riquadro.html"), "w").write(HTML)
print("wrote", os.path.join(out_dir, "kreca-riquadro.html"), len(HTML))
