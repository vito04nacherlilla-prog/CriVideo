#!/usr/bin/env python3
# Interactive flip-book viewer for the KRECA booklet (self-contained HTML).
import os
SCR = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(SCR, "pages_b64.py")).read())   # defines PAGES (list of b64 jpg)

pages_js = "[" + ",".join('"data:image/jpeg;base64,%s"' % b for b in PAGES) + "]"
TITLES = ["Copertina","Indice","Chi siamo","La nostra storia","Perche KRECA","Il metodo",
 "Aree di servizio","Costruzioni metalliche","Chiusure & sicurezza","Facility & logistica",
 "Pronto intervento H24","Settori serviti","Lavori recenti","Zone servite","Certificazioni",
 "Glossario tecnico","Domande frequenti","Contatti"]
titles_js = "[" + ",".join('"%s"' % t for t in TITLES[:len(PAGES)]) + "]"

TEMPLATE = r"""<title>KRECA — Libricino · Anteprima sfogliabile</title>
<style>
:root{
  --ink:#08090B; --panel:#14161B; --green:#30D158; --green-deep:#1E9E43;
  --steel:#8B929C; --white:#F3F5F8; --line:rgba(139,146,156,.18);
}
*{box-sizing:border-box;margin:0}
html,body{height:100%}
body{background:radial-gradient(120% 90% at 50% -10%,#1a1d24 0%,#070809 62%,#050506 100%) fixed,#050506;
  color:var(--white);font-family:"Inter",system-ui,-apple-system,Segoe UI,Roboto,sans-serif;
  min-height:100dvh;display:flex;flex-direction:column;overflow:hidden}
.top{display:flex;align-items:center;justify-content:space-between;gap:12px;
  padding:14px clamp(12px,3vw,28px)}
.brand{display:flex;align-items:center;gap:10px;font-weight:800;letter-spacing:.02em;font-size:15px}
.brand .dot{width:11px;height:11px;background:var(--green);transform:rotate(45deg);flex:none;
  box-shadow:0 0 14px rgba(48,209,88,.6)}
.brand b{font-weight:800}.brand span{color:var(--steel);font-weight:600}
.top .btn{appearance:none;border:1px solid var(--line);background:rgba(255,255,255,.03);
  color:var(--white);font:inherit;font-weight:600;font-size:13px;letter-spacing:.02em;
  padding:8px 14px;border-radius:999px;cursor:pointer;display:inline-flex;align-items:center;gap:7px;
  transition:border-color .2s,background .2s}
.top .btn:hover{border-color:var(--green);background:rgba(48,209,88,.08)}
.top .btn svg{width:15px;height:15px}

.stage{flex:1;display:flex;align-items:center;justify-content:center;position:relative;
  padding:4px clamp(10px,4vw,60px);min-height:0}
.viewport{position:relative;perspective:2600px}
.book{position:relative;width:min(94vw, calc((100dvh - 180px) * 420/297));
  aspect-ratio:420/297;transform-style:preserve-3d;
  filter:drop-shadow(0 40px 60px rgba(0,0,0,.6))}
.half{position:absolute;top:0;height:100%;width:50%;overflow:hidden;background:#0c0d11}
.half.l{left:0} .half.r{left:50%}
.half img{width:100%;height:100%;object-fit:cover;display:block}
.half .empty{width:100%;height:100%;
  background:linear-gradient(90deg,#101216,#0a0b0e);
  box-shadow:inset -30px 0 50px -20px rgba(0,0,0,.7)}
/* centre gutter shading */
.gutter{position:absolute;top:0;left:50%;transform:translateX(-50%);width:9%;height:100%;
  pointer-events:none;z-index:6;
  background:linear-gradient(90deg,rgba(0,0,0,0) 0%,rgba(0,0,0,.34) 46%,rgba(0,0,0,.42) 50%,
    rgba(0,0,0,.34) 54%,rgba(0,0,0,0) 100%)}
/* turning leaf */
.leaf{position:absolute;top:0;left:50%;width:50%;height:100%;z-index:8;
  transform-style:preserve-3d;transform-origin:left center;transition:transform .72s cubic-bezier(.4,.02,.2,1);
  transform:rotateY(0deg);display:none}
.leaf.show{display:block}
.face{position:absolute;inset:0;overflow:hidden;backface-visibility:hidden;background:#0c0d11}
.face img{width:100%;height:100%;object-fit:cover;display:block}
.face.back{transform:rotateY(180deg)}
.face .sheen{position:absolute;inset:0;pointer-events:none;opacity:0;transition:opacity .72s ease}
.leaf.turning .face .sheen{opacity:1}
.face.front .sheen{background:linear-gradient(90deg,rgba(0,0,0,.5),rgba(0,0,0,0) 40%)}
.face.back .sheen{background:linear-gradient(270deg,rgba(0,0,0,.5),rgba(0,0,0,0) 40%)}

/* click zones */
.zone{position:absolute;top:0;height:100%;width:26%;z-index:7;cursor:pointer;
  display:flex;align-items:center;justify-content:center}
.zone.prev{left:0}.zone.next{right:0}
.zone .chev{width:46px;height:46px;border-radius:50%;background:rgba(8,9,11,.5);
  border:1px solid var(--line);display:flex;align-items:center;justify-content:center;
  opacity:0;transition:opacity .2s,transform .2s,border-color .2s;backdrop-filter:blur(4px)}
.zone:hover .chev{opacity:1}
.zone.prev:hover .chev{transform:translateX(-3px)}.zone.next:hover .chev{transform:translateX(3px)}
.zone .chev:hover{border-color:var(--green)}
.zone .chev svg{width:20px;height:20px;stroke:#fff}
.zone.disabled{cursor:default}.zone.disabled .chev{display:none}

/* bottom controls */
.controls{display:flex;flex-direction:column;align-items:center;gap:10px;padding:10px 16px 20px}
.caption{font-size:13.5px;color:var(--steel);font-weight:600;letter-spacing:.02em;min-height:18px;text-align:center}
.caption b{color:var(--white)}
.dots{display:flex;gap:9px;align-items:center}
.dots button{appearance:none;border:0;padding:0;width:9px;height:9px;border-radius:50%;
  background:rgba(139,146,156,.35);cursor:pointer;transition:transform .2s,background .2s}
.dots button.on{background:var(--green);transform:scale(1.35)}
.dots button:hover{background:var(--green)}

/* overview */
.overlay{position:fixed;inset:0;z-index:20;background:rgba(5,6,8,.92);backdrop-filter:blur(8px);
  display:none;flex-direction:column;padding:20px clamp(12px,4vw,40px)}
.overlay.open{display:flex}
.overlay h2{font-size:15px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;
  color:var(--steel);margin-bottom:16px;display:flex;align-items:center;justify-content:space-between}
.overlay h2 .x{cursor:pointer;color:var(--white);border:1px solid var(--line);border-radius:999px;
  padding:6px 12px;font-size:12px}
.grid{flex:1;overflow:auto;display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));
  gap:16px;align-content:start;padding-bottom:20px}
.thumb{cursor:pointer;border:1px solid var(--line);border-radius:6px;overflow:hidden;background:#0c0d11;
  transition:border-color .2s,transform .15s;position:relative}
.thumb:hover{border-color:var(--green);transform:translateY(-3px)}
.thumb img{width:100%;display:block;aspect-ratio:210/297;object-fit:cover}
.thumb .n{position:absolute;left:0;bottom:0;background:rgba(8,9,11,.8);color:#fff;
  font-size:11px;font-weight:700;padding:3px 8px;border-top-right-radius:5px}

/* fullscreen single page zoom */
.zoom{position:fixed;inset:0;z-index:30;background:rgba(5,6,8,.96);display:none;
  align-items:center;justify-content:center;padding:16px;cursor:zoom-out}
.zoom.open{display:flex}
.zoom img{max-width:100%;max-height:100%;object-fit:contain;border-radius:4px;
  box-shadow:0 30px 80px rgba(0,0,0,.7)}
.zoom .zx{position:absolute;top:16px;right:18px;color:#fff;border:1px solid var(--line);
  border-radius:999px;padding:8px 14px;font-size:13px;font-weight:600;cursor:pointer;background:rgba(8,9,11,.6)}

.hint{position:absolute;bottom:8px;left:50%;transform:translateX(-50%);font-size:12px;
  color:var(--steel);opacity:.8;pointer-events:none}
@media (max-width:640px){ .top .btn .lbl{display:none} .hint{display:none} }
@media (prefers-reduced-motion:reduce){ .leaf{transition:none !important} }
</style>

<div class="top">
  <div class="brand"><span class="dot"></span><b>KRECA</b><span>· Libricino · anteprima</span></div>
  <button class="btn" id="ovBtn">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>
    <span class="lbl">Tutte le pagine</span>
  </button>
</div>

<div class="stage">
  <div class="viewport">
    <div class="book" id="book">
      <div class="half l" id="halfL"></div>
      <div class="half r" id="halfR"></div>
      <div class="leaf" id="leaf">
        <div class="face front" id="ff"><img id="ffImg" alt=""><div class="sheen"></div></div>
        <div class="face back" id="fb"><img id="fbImg" alt=""><div class="sheen"></div></div>
      </div>
      <div class="gutter"></div>
      <div class="zone prev" id="zPrev"><div class="chev"><svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg></div></div>
      <div class="zone next" id="zNext"><div class="chev"><svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg></div></div>
    </div>
  </div>
  <div class="hint">Frecce ← →, clic sui lati, oppure scorri · tocca una pagina per ingrandirla</div>
</div>

<div class="controls">
  <div class="caption" id="caption"></div>
  <div class="dots" id="dots"></div>
</div>

<div class="overlay" id="overlay">
  <h2>Tutte le pagine <span class="x" id="ovClose">Chiudi ✕</span></h2>
  <div class="grid" id="grid"></div>
</div>

<div class="zoom" id="zoom"><span class="zx" id="zoomClose">Chiudi ✕</span><img id="zoomImg" alt=""></div>

<script>
const PAGES = /*PAGES*/;
const TITLES = /*TITLES*/;
// Build spreads: closed cover alone, then two-page spreads, back cover alone if leftover.
const SPREADS = [];
(function(){
  const cap = (l,r)=> l==null ? TITLES[r] : (TITLES[l]+" · "+TITLES[r]);
  SPREADS.push({L:null,R:0,cap:cap(null,0)});
  let i=1;
  for(; i+1 < PAGES.length; i+=2) SPREADS.push({L:i,R:i+1,cap:cap(i,i+1)});
  if(i < PAGES.length) SPREADS.push({L:PAGES.length-1,R:null,cap:TITLES[PAGES.length-1]});
})();
let s = 0, busy = false;
const $ = id => document.getElementById(id);
const halfL=$("halfL"), halfR=$("halfR"), leaf=$("leaf"),
      ffImg=$("ffImg"), fbImg=$("fbImg"),
      zPrev=$("zPrev"), zNext=$("zNext"), caption=$("caption"), dots=$("dots");

function pageHTML(idx){ return idx==null ? '<div class="empty"></div>'
  : '<img src="'+PAGES[idx]+'" alt="Pagina '+(idx+1)+'">'; }

function render(){
  halfL.innerHTML = pageHTML(SPREADS[s].L);
  halfR.innerHTML = pageHTML(SPREADS[s].R);
  caption.innerHTML = "<b>"+(s+1)+"</b> / "+SPREADS.length+" &nbsp;·&nbsp; "+SPREADS[s].cap;
  zPrev.classList.toggle("disabled", s===0);
  zNext.classList.toggle("disabled", s===SPREADS.length-1);
  [...dots.children].forEach((d,i)=>d.classList.toggle("on", i===s));
}

function go(dir){
  if(busy) return;
  const ns = s + dir;
  if(ns < 0 || ns >= SPREADS.length) return;
  const reduce = matchMedia("(prefers-reduced-motion:reduce)").matches;
  if(reduce){ s = ns; render(); return; }
  busy = true;
  if(dir > 0){
    // turn a leaf from right to left
    halfR.innerHTML = pageHTML(SPREADS[ns].R);        // reveal next right underneath
    ffImg.src = PAGES[SPREADS[s].R];                  // front = current right
    fbImg.src = SPREADS[ns].L!=null ? PAGES[SPREADS[ns].L] : "";
    $("fb").style.visibility = SPREADS[ns].L!=null ? "visible":"hidden";
    leaf.classList.add("show");
    leaf.style.transition="none"; leaf.style.transform="rotateY(0deg)";
    void leaf.offsetWidth;
    leaf.style.transition=""; leaf.classList.add("turning");
    leaf.style.transform="rotateY(-180deg)";
  } else {
    // turn a leaf from left to right
    halfL.innerHTML = pageHTML(SPREADS[ns].L);        // reveal prev left underneath
    ffImg.src = PAGES[SPREADS[ns].R];                 // front (lands on right) = prev right
    fbImg.src = SPREADS[s].L!=null ? PAGES[SPREADS[s].L] : "";
    $("fb").style.visibility = SPREADS[s].L!=null ? "visible":"hidden";
    leaf.classList.add("show");
    leaf.style.transition="none"; leaf.style.transform="rotateY(-180deg)";
    void leaf.offsetWidth;
    leaf.style.transition=""; leaf.classList.add("turning");
    leaf.style.transform="rotateY(0deg)";
  }
  const done = ()=>{
    leaf.removeEventListener("transitionend", done);
    s = ns; leaf.classList.remove("show","turning"); render(); busy=false;
  };
  leaf.addEventListener("transitionend", done);
}

function jump(ns){ if(ns===s) return; s=ns; render(); }

// dots
SPREADS.forEach((sp,i)=>{ const b=document.createElement("button");
  b.title=sp.cap; b.onclick=()=>jump(i); dots.appendChild(b); });

// nav events
zPrev.onclick=()=>go(-1); zNext.onclick=()=>go(1);
addEventListener("keydown",e=>{
  if($("overlay").classList.contains("open")||$("zoom").classList.contains("open")){
    if(e.key==="Escape"){ $("overlay").classList.remove("open"); $("zoom").classList.remove("open"); }
    return;
  }
  if(e.key==="ArrowRight"||e.key===" ") { e.preventDefault(); go(1); }
  if(e.key==="ArrowLeft") go(-1);
});
// swipe
let tx=null;
$("book").addEventListener("touchstart",e=>{tx=e.changedTouches[0].clientX},{passive:true});
$("book").addEventListener("touchend",e=>{ if(tx==null)return;
  const dx=e.changedTouches[0].clientX-tx; if(Math.abs(dx)>45) go(dx<0?1:-1); tx=null;});

// tap a page to zoom (ignore taps on nav chevrons)
$("book").addEventListener("click",e=>{
  if(busy) return;
  if(e.target.closest(".zone")) return;
  const img=e.target.closest(".half")?.querySelector("img");
  if(img){ $("zoomImg").src=img.src; $("zoom").classList.add("open"); }
});
$("zoom").onclick=()=>$("zoom").classList.remove("open");
$("zoomClose").onclick=()=>$("zoom").classList.remove("open");

// overview
const grid=$("grid");
PAGES.forEach((src,i)=>{ const d=document.createElement("div"); d.className="thumb";
  d.innerHTML='<img src="'+src+'"><span class="n">'+(i+1)+'</span>';
  d.onclick=()=>{ const idx=SPREADS.findIndex(sp=>sp.L===i||sp.R===i);
    jump(idx<0?0:idx); $("overlay").classList.remove("open"); };
  grid.appendChild(d); });
$("ovBtn").onclick=()=>$("overlay").classList.add("open");
$("ovClose").onclick=()=>$("overlay").classList.remove("open");

render();
</script>
"""

out = os.path.join(SCR, "viewer.html")
open(out, "w").write(TEMPLATE.replace("/*PAGES*/", pages_js).replace("/*TITLES*/", titles_js))
print("wrote", out, round(len(open(out).read())/1024), "KB")
