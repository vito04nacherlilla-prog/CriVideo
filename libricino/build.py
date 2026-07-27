#!/usr/bin/env python3
# Assembles the KRECA company booklet (single self-contained HTML file).
import math, base64, os, html

SCR = os.path.dirname(os.path.abspath(__file__))
ANTON = base64.b64encode(open(os.path.join(SCR, "anton.woff2"), "rb").read()).decode()
MONT  = base64.b64encode(open(os.path.join(SCR, "mont.woff2"), "rb").read()).decode()

# ---------------------------------------------------------------- blueprint motif
def blueprint(seed_rot=0):
    """A technical 'drawing' cluster: gear ring + protractor arcs + radial ticks."""
    cx, cy, parts = 100, 100, []
    # concentric circles
    for r in (30, 52, 74, 92):
        parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" />')
    # radial ticks around outer ring
    for a in range(0, 360, 5):
        rad = math.radians(a + seed_rot)
        long = (a % 30 == 0)
        r1 = 74; r2 = 92 if long else 84
        x1 = cx + r1*math.cos(rad); y1 = cy + r1*math.sin(rad)
        x2 = cx + r2*math.cos(rad); y2 = cy + r2*math.sin(rad)
        parts.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" />')
    # gear teeth (on r=30 ring)
    teeth = []
    for a in range(0, 360, 20):
        rad = math.radians(a)
        for off, r in ((-5, 30), (-3, 40), (3, 40), (5, 30)):
            rr = math.radians(a + off)
            teeth.append(f"{cx + r*math.cos(rr):.1f},{cy + r*math.sin(rr):.1f}")
    parts.append(f'<polygon points="{" ".join(teeth)}" />')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="12" />')
    # crosshair
    parts.append(f'<line x1="{cx}" y1="4" x2="{cx}" y2="196" />')
    parts.append(f'<line x1="4" y1="{cy}" x2="196" y2="{cy}" />')
    inner = "\n".join(parts)
    return (f'<svg class="bp" viewBox="0 0 200 200" aria-hidden="true" '
            f'fill="none" stroke="currentColor" stroke-width="0.8" '
            f'vector-effect="non-scaling-stroke">{inner}</svg>')

BP = blueprint()

# ---------------------------------------------------------------- logo
def logo(cls="logo"):
    return (f'<span class="{cls}">'
            '<svg class="mk" viewBox="0 0 48 48" aria-hidden="true">'
            '<path d="M11 3 H46 L37 45 H2 Z" fill="var(--red)"/>'
            '<g stroke="#fff" stroke-width="4.6" fill="none" stroke-linecap="butt">'
            '<path d="M17 13 V35"/><path d="M17 25 L30 13"/><path d="M17 24 L32 35"/>'
            '</g></svg>'
            '<span class="wm"><b>KRECA</b><i>officina metalmeccanica</i></span></span>')

# ---------------------------------------------------------------- helpers
def prest(items):
    lis = ""
    for t, d in items:
        lis += f'<li><span class="pt">{t}</span><span class="pd">{d}</span></li>'
    return f'<ul class="prest">{lis}</ul>'

def nota(txt):
    return f'<div class="nota"><span class="nl">Nota operativa</span><p>{txt}</p></div>'

def head(sez, kicker, title):
    return (f'<div class="rail"><span class="sez">SEZ</span>'
            f'<span class="sezn">{sez}</span></div>'
            f'<header class="phead"><span class="kick">{kicker}</span>'
            f'<h2 class="ptitle">{title}</h2></header>')

# ================================================================ PAGES
pages = []

# ---- COVER -------------------------------------------------------------
pages.append(f'''<section class="leaf cover">
  <div class="crop"></div>
  <div class="cover-red"><div class="bpwrap">{BP}</div></div>
  <div class="cover-top">
    {logo("logo lg")}
    <div class="docmeta">
      <span>DOC · KRC / BR / 2025</span>
      <span>PROFILO AZIENDALE — REV.05</span>
    </div>
  </div>
  <div class="cover-hero">
    <span class="eyebrow">KRECA S.r.l. — Profilo aziendale</span>
    <h1 class="htitle">Officina<br>metal<span class="hy">—</span><br>meccanica</h1>
    <p class="lead">General contractor metalmeccanico. Officina di produzione
      interna. Fornitura, posa e pronto intervento.</p>
  </div>
  <div class="cover-foot">
    <div class="cf"><span class="cfk">Operativi dal</span><span class="cfv">2019</span></div>
    <div class="cf"><span class="cfk">Area</span><span class="cfv">Puglia · Basilicata — 8 province</span></div>
    <div class="cf"><span class="cfk">Contatti</span><span class="cfv">080 875 5152 · +39 351 805 5489</span></div>
    <div class="cf web"><span class="cfk">Web</span><span class="cfv">www.kreca.it</span></div>
  </div>
</section>''')

# ---- 01 L'AZIENDA ------------------------------------------------------
dati = [
    ("Ragione sociale", "KRECA S.r.l. — Officina Metalmeccanica"),
    ("Forma giuridica", "Società a responsabilità limitata"),
    ("Sede legale", "Via Giotto 5, 70018 Rutigliano (BA)"),
    ("Sede operativa", "S.P. 240 delle Grotte Orientali 290, Rutigliano (BA)"),
    ("P.IVA / C.F.", "09015760722"),
    ("REA", "BA-665535"),
    ("Attiva dal", "2019 — esperienza artigiana pregressa"),
    ("Area di competenza", "Puglia e Basilicata — 8 province"),
    ("Settore", "Lavorazione prodotti in metallo — ATECO 25"),
]
dati_rows = "".join(f'<div class="drow"><dt>{k}</dt><dd>{v}</dd></div>' for k, v in dati)
stats = [("2019", "Operativi dal"), ("8", "Province coperte"),
         ("2", "Regioni · PUG · BAS"), ("100%", "Produzione interna")]
stat_html = "".join(
    f'<div class="stat"><span class="sv">{v}</span><span class="sk">{k}</span></div>'
    for v, k in stats)
pages.append(f'''<section class="leaf azienda">
  <div class="crop"></div>
  {head("01", "L'azienda", "Officina metalmeccanica,<br>produzione interna e posa.")}
  <div class="body two-col">
    <div class="col-main">
      <p>KRECA S.r.l. è un'officina metalmeccanica specializzata nella lavorazione
      del ferro e dell'alluminio e nella realizzazione, fornitura e posa in opera di
      serramenti, sistemi di chiusura e soluzioni di sicurezza. Il cuore dell'azienda
      è la propria <strong>officina di produzione interna</strong>: carpenteria in
      ferro, serramenti in ferro e alluminio, cancelli, inferriate, persiane e
      manufatti su misura nascono internamente, con controllo dell'intero ciclo —
      dalla presa delle misure fino alla posa — senza dipendere da terzi per le
      lavorazioni principali.</p>
      <p>Accanto alla produzione diretta offriamo fornitura e posa per i prodotti che
      completano la gamma — serramenti in PVC, vetrate e zanzariere — selezionati
      presso partner qualificati e installati dalle nostre squadre. Il cliente trova
      così in KRECA un <strong>unico interlocutore</strong> per l'intera opera, dalle
      strutture portanti fino alle finiture.</p>
      <p>Operiamo su tutta la Puglia e la Basilicata — otto province — con squadre
      distribuite e reperibilità per gli interventi urgenti. Attivi dal 2019, nati da
      una consolidata esperienza artigiana nella lavorazione del metallo e strutturati
      in S.r.l. per commesse di maggiore complessità, come partner di gruppi industriali
      e società di facility management.</p>
      <blockquote>Una struttura decisionale snella, un interlocutore unico e la
      capacità di intervenire rapidamente su tutto il territorio di competenza.</blockquote>
    </div>
    <aside class="col-side">
      <span class="side-label">Dati identificativi</span>
      <dl class="dati">{dati_rows}</dl>
    </aside>
  </div>
  <div class="statband">{stat_html}</div>
</section>''')

# ---- 02 PERCHÉ ---------------------------------------------------------
vals = [
    ("01", "Officina di produzione propria",
     "Ferro e alluminio lavorati nella nostra officina: controllo su qualità, "
     "materiali, finiture e tempi di consegna, indipendenza dai fornitori terzi."),
    ("02", "Interlocutore unico",
     "Un solo referente per più categorie di intervento, anche nello stesso "
     "cantiere: meno coordinamento, tempi morti ridotti, responsabilità chiara."),
    ("03", "Copertura territoriale",
     "Operatività su 8 province tra Puglia e Basilicata con squadre distribuite: "
     "una presenza locale reale, non solo dichiarata."),
    ("04", "Pronto intervento",
     "Reperibilità e interventi urgenti su accessi e chiusure per la messa in "
     "sicurezza e il ripristino rapido della funzionalità."),
    ("05", "Struttura reattiva",
     "Decisioni rapide e comunicazione diretta con la titolarità: un referente "
     "unico segue la commessa dall'inizio alla fine."),
    ("06", "Esperienza nel facility",
     "Fornitore tecnico locale di gruppi di facility management, con reportistica, "
     "tempi di risposta e sicurezza allineati agli standard del committente."),
]
cards = "".join(
    f'<article class="vcard"><span class="vn">{n}</span>'
    f'<h3>{t}</h3><p>{d}</p></article>' for n, t, d in vals)
pages.append(f'''<section class="leaf">
  <div class="crop"></div>
  {head("02", "Perché scegliere KRECA", "Un solo partner,<br>ogni opera.")}
  <p class="body intro">Il nostro valore per il committente si riassume in una
  promessa semplice — <em>un solo partner, ogni opera</em> — che si traduce in sei
  vantaggi concreti e verificabili.</p>
  <div class="vgrid">{cards}</div>
</section>''')

# ---- 03 SERVIZI INDEX --------------------------------------------------
serv = [
    ("3.1", "Costruzioni metalliche in ferro",
     "Carpenteria, strutture portanti, soppalchi, scale e manufatti su disegno."),
    ("3.2", "Serramenti e infissi",
     "Ferro e alluminio prodotti internamente; PVC, vetrate e zanzariere con partner."),
    ("3.3", "Chiusure e sicurezza",
     "Serrande, cancelli, portoni, porte blindate, serrature e automazioni."),
    ("3.4", "Manutenzione tecnica",
     "Ordinaria e straordinaria su elementi metallici, serramenti e chiusure."),
    ("3.5", "Pronto intervento",
     "Reperibilità e urgenze su accessi e chiusure, in tutta l'area di competenza."),
]
idx = "".join(
    f'<a class="sidx"><span class="sidn">{n}</span>'
    f'<span class="sidt">{t}</span><span class="sidd">{d}</span></a>'
    for n, t, d in serv)
pages.append(f'''<section class="leaf servcover">
  <div class="crop"></div>
  {head("03", "Aree di servizio", "Dalla progettazione<br>alla posa.")}
  <p class="body intro">Cinque aree di intervento coordinate da un unico
  interlocutore, dalla produzione in officina alla posa e alla manutenzione.</p>
  <nav class="servindex">{idx}</nav>
</section>''')

# ---- service detail template ------------------------------------------
def service(sez, num, title, intro, items, nota_txt=None, emergency=None):
    body = f'<p class="body intro">{intro}</p>'
    if emergency:
        body += (f'<div class="emerg"><span class="el">Attivazione diretta</span>'
                 f'<a class="enum">{emergency}</a>'
                 f'<span class="ed">Reperibilità · 8 province · Puglia e Basilicata</span></div>')
    body += '<span class="side-label prest-lbl">Prestazioni principali</span>'
    body += prest(items)
    if nota_txt:
        body += nota(nota_txt)
    return f'''<section class="leaf service">
  <div class="crop"></div>
  <span class="bignum">{num}</span>
  {head(sez, "Aree di servizio", title)}
  {body}
</section>'''

pages.append(service("03 · 3.1", "3.1", "Costruzioni metalliche<br>in ferro.",
    "Progettiamo, produciamo in officina e posiamo strutture e manufatti in ferro, "
    "su misura per contesti civili, commerciali e industriali. Ogni elemento nasce "
    "internamente — dal taglio alla saldatura, dalle finiture al trattamento "
    "protettivo — con controllo diretto in ogni fase.",
    [("Carpenteria e strutture portanti", "Travi, pilastri, telai e ossature in ferro per capannoni, ampliamenti, tettoie e coperture."),
     ("Soppalchi industriali e commerciali", "Su misura per magazzini, punti vendita e ambienti produttivi, calcolati sui carichi di esercizio."),
     ("Scale, parapetti, ringhiere e passerelle", "Interne ed esterne, conformi ai requisiti di sicurezza vigenti."),
     ("Telai, supporti e manufatti su disegno", "Su disegno del cliente o progettati internamente, per impiantistica e allestimenti."),
     ("Lavorazioni su misura per conto terzi", "Taglio, piegatura, foratura, saldatura e assemblaggio per imprese e general contractor.")],
    "Officina interna: tutte le lavorazioni sul ferro vengono eseguite in sede, "
    "garantendo continuità produttiva, controllo qualità e riduzione dei tempi."))

pages.append(service("03 · 3.2", "3.2", "Serramenti<br>e infissi.",
    "Gamma completa per aperture interne ed esterne, in ambito residenziale, "
    "commerciale e direzionale. Produciamo internamente i serramenti in ferro e in "
    "alluminio — a freddo o a taglio termico; per PVC, vetrate e zanzariere ci "
    "avvaliamo di partner selezionati, con posa a regola d'arte.",
    [("Alluminio a taglio termico", "Elevato isolamento termico e acustico, per abitazioni, uffici ed edifici a uso pubblico."),
     ("Alluminio a freddo", "Ottimo rapporto tra resistenza, leggerezza e durata dove non serve il taglio termico."),
     ("Serramenti e opere in ferro", "Infissi, telai, finestrature e chiusure in ferro su misura, realizzati internamente."),
     ("Infissi in PVC · fornitura e posa", "Serramenti in PVC di qualità, tramite partner qualificati e posa certificata."),
     ("Vetrate e superfici vetrate", "Facciate continue, scorrevoli e sistemi minimali; posa curata direttamente da KRECA."),
     ("Zanzariere · persiane e scuri", "Zanzariere a rullo, plissettate e scorrevoli; persiane e scuri in ferro o alluminio su misura.")]))

pages.append(service("03 · 3.3", "3.3", "Chiusure<br>e sicurezza.",
    "Realizziamo, forniamo e installiamo sistemi di chiusura, protezione e sicurezza "
    "per accessi e aperture, in ambienti privati, commerciali e a uso pubblico. "
    "Copriamo l'intero ciclo, dalla misura sul posto alla messa a punto finale.",
    [("Serrande, tapparelle e avvolgibili", "Commerciali e industriali, manuali o motorizzate; installazione, manutenzione e sostituzione."),
     ("Cancelli e inferriate", "Pedonali e carrabili, grate di sicurezza fisse o apribili, in ferro su misura."),
     ("Portoni", "Industriali e sezionali per accessi civili e produttivi, manuali o automatizzati."),
     ("Porte blindate di ultima generazione", "Installazione a norma e taratura di tutti gli accessori per la massima protezione."),
     ("Serrature, cilindri e automazioni", "Serrature meccaniche ed elettroniche, cilindri europei, sistemi master-key e automazioni per cancelli e portoni.")]))

pages.append(service("03 · 3.4", "3.4", "Manutenzione<br>tecnica.",
    "Manutenzione tecnica di elementi metallici, serramenti e sistemi di chiusura di "
    "immobili, capannoni industriali e poli logistici. Operiamo in appalto diretto o "
    "in subappalto per gruppi di facility management, con operatività continuativa e "
    "reportistica dedicata.",
    [("Ordinaria e straordinaria", "Interventi programmati e non su carpenteria, serramenti, portoni, cancelli e chiusure."),
     ("Ripristino e sostituzione componenti", "Componenti usurati o non conformi, adeguamento e ripristino della piena funzionalità."),
     ("Interventi programmati e su chiamata", "Squadre dedicate e pianificazione dei fermi, con minimo impatto sull'attività del committente.")],
    "Attivi come fornitore tecnico locale per gruppi di facility management: "
    "standard di reportistica, sicurezza e tempi di risposta allineati al committente."))

pages.append(service("03 · 3.5", "3.5", "Pronto intervento<br>accessi e chiusure.",
    "Servizio di reperibilità e intervento urgente su tutta l'area di competenza, per "
    "la messa in sicurezza e il ripristino della funzionalità di accessi e chiusure a "
    "seguito di guasti, blocchi o effrazioni.",
    [("Apertura e sblocco", "Serrande, cancelli motorizzati e serrature bloccate, preservando l'integrità del sistema ove possibile."),
     ("Riparazione urgente", "Motorizzazioni, serrature e componenti meccanici di porte, portoni e sistemi di chiusura."),
     ("Messa in sicurezza post-effrazione", "Chiusura provvisoria, sostituzione dei componenti danneggiati e ripristino delle condizioni di sicurezza.")],
    emergency="+39 351 805 5489"))

# ---- 04·05 COLLABORAZIONE + QUALIFICHE --------------------------------
quals = [
    ("Mercati elettronici P.A.", "Iscrizione a MEPA e a EmPULIA."),
    ("Patente a crediti", "Patente a crediti INL — art. 27 D.Lgs. 81/2008, con dotazione conforme ai requisiti di legge."),
    ("Copertura assicurativa", "Polizza RC verso Terzi, massimale € 3.000.000 — Generali Italia."),
    ("Regolarità contributiva", "DURC regolare. Applicazione del CCNL Metalmeccanica."),
    ("Sistema qualità", "Conforme a UNI EN ISO 9001 — in corso di certificazione."),
]
qrows = "".join(f'<div class="qrow"><dt>{k}</dt><dd>{v}</dd></div>' for k, v in quals)
pages.append(f'''<section class="leaf">
  <div class="crop"></div>
  {head("04 · 05", "Collaborazione · Qualifiche", "Come lavoriamo<br>e le nostre garanzie.")}
  <div class="body two-col wide">
    <div class="col-main">
      <span class="side-label">04 — Modalità di collaborazione</span>
      <p>KRECA opera sia in appalto diretto sia come impresa esecutrice in subappalto
      per general contractor e società di facility management. In quest'ultima veste
      mette a disposizione la propria officina e le proprie squadre come
      <strong>fornitore tecnico locale</strong>, garantendo continuità operativa e
      rispetto degli standard richiesti in materia di tempi, reportistica e sicurezza.</p>
      <p>Per esigenze di volume superiori alla capacità diretta, l'azienda si avvale di
      una rete selezionata di collaboratori e imprese partner, che coordina restando
      <strong>unico responsabile</strong> nei confronti del committente.</p>
    </div>
    <aside class="col-side">
      <span class="side-label">05 — Qualifiche, iscrizioni e coperture</span>
      <dl class="quals">{qrows}</dl>
    </aside>
  </div>
  <p class="foot-note">La documentazione amministrativa completa — visura camerale,
  DURC, patente a crediti, polizza assicurativa e autocertificazioni di legge — è
  disponibile e viene fornita in fase di qualifica fornitore.</p>
</section>''')

# ---- BACK / CONTATTI ---------------------------------------------------
contacts = [
    ("Telefono", "080 875 5152"),
    ("Mobile", "+39 351 805 5489"),
    ("E-mail", "info@kreca.it"),
    ("PEC", "kreca@pec.it"),
    ("Web", "www.kreca.it"),
    ("Social", "IG @kreca_srl · FB /krecasrl"),
    ("Sede legale", "Via Giotto 5, 70018 Rutigliano (BA)"),
    ("Sede operativa", "S.P. 240 Grotte Orientali 290, Rutigliano (BA)"),
]
crows = "".join(f'<div class="crow"><dt>{k}</dt><dd>{v}</dd></div>' for k, v in contacts)
pages.append(f'''<section class="leaf back">
  <div class="crop"></div>
  <div class="back-red"><div class="bpwrap">{BP}</div></div>
  <div class="back-top">{logo("logo lg")}
    <span class="docmeta"><span>SEZ · 06 — Contatti</span></span></div>
  <div class="back-hero">
    <span class="eyebrow">Un solo partner, ogni opera</span>
    <h1 class="htitle sm">Dalla<br>progettazione<br>alla posa.</h1>
  </div>
  <div class="contacts">{crows}</div>
  <div class="back-foot">
    <span>KRECA S.r.l. — Officina Metalmeccanica</span>
    <span>P.IVA 09015760722 · REA BA-665535 · ATECO 25</span>
  </div>
</section>''')

BOOK = "\n".join(pages)

# ================================================================ CSS
CSS = """
:root{
  --ink:#0C0D10; --panel:#14161B; --panel-2:#1B1F27; --panel-3:#232833;
  --red:#DA2128; --red-deep:#9E121A; --red-ink:#F04A50;
  --steel:#A6AEBB; --steel-dim:#767E8C; --steel-fade:rgba(166,174,187,.16);
  --paper:#EEF1F4; --on-paper:#14161B;
  --white:#F3F5F8;
  --line:rgba(166,174,187,.16); --line-strong:rgba(166,174,187,.34);
}
*{box-sizing:border-box}
html,body{margin:0}
body{
  background:
    radial-gradient(120% 80% at 50% -10%, #202531 0%, #0a0b0e 60%) fixed,
    #0a0b0e;
  color:var(--white);
  font-family:"Mont",system-ui,sans-serif;
  -webkit-font-smoothing:antialiased;
  padding:clamp(14px,4vw,56px) 0 64px;
}
.stack{display:flex;flex-direction:column;align-items:center;gap:clamp(18px,3.4vw,40px)}

/* ---------------- LEAF (a page) ---------------- */
.leaf{
  position:relative; overflow:hidden;
  width:min(820px,94vw); aspect-ratio:210/297;
  container-type:size;
  background:linear-gradient(160deg,#14161b 0%,#0e1014 62%,#0b0c0f 100%);
  color:var(--white);
  box-shadow:0 40px 80px -30px rgba(0,0,0,.85), 0 2px 0 rgba(255,255,255,.03) inset;
  padding:9cqw 8.4cqw;
  display:flex; flex-direction:column;
}
.leaf::before{ /* blueprint grid ambience */
  content:""; position:absolute; inset:0; pointer-events:none; opacity:.5;
  background:
    linear-gradient(var(--line) 1px,transparent 1px) 0 0/100% 5.2cqw,
    linear-gradient(90deg,var(--line) 1px,transparent 1px) 0 0/5.2cqw 100%;
  -webkit-mask-image:linear-gradient(#000,#000);
}
.leaf>*{position:relative;z-index:2}

/* crop marks */
.crop{position:absolute;inset:0;z-index:3;pointer-events:none}
.crop::before,.crop::after{content:"";position:absolute;width:3.4cqw;height:3.4cqw}
.crop::before{top:3cqw;left:3cqw;border-top:1px solid var(--steel-dim);border-left:1px solid var(--steel-dim)}
.crop::after{bottom:3cqw;right:3cqw;border-bottom:1px solid var(--steel-dim);border-right:1px solid var(--steel-dim)}

/* ---------------- shared type ---------------- */
.eyebrow,.kick,.side-label,.docmeta,.sez,.cfk,.sk,.nl,.el,.prest-lbl{
  font-family:"Mont",sans-serif;font-weight:600;text-transform:uppercase;
  letter-spacing:.24em;color:var(--steel);
}
h1,h2,h3,.bignum,.htitle,.ptitle{
  font-family:"Anton","Mont",sans-serif;font-weight:400;
  text-transform:uppercase;line-height:.92;text-wrap:balance;
  letter-spacing:.005em;
}
.body{font-size:2.35cqw;line-height:1.62;color:#D5D9E0;font-weight:400}
.body p{margin:0 0 1.5cqw}
.body strong{color:var(--white);font-weight:600}
.body em{font-style:normal;color:var(--red-ink);font-weight:600}

/* ---------------- page header + rail ---------------- */
.rail{position:absolute;top:0;right:0;height:100%;width:8.4cqw;z-index:4;
  display:flex;flex-direction:column;align-items:center;justify-content:flex-start;
  gap:1.4cqw;padding-top:9cqw;border-left:1px solid var(--line)}
.rail .sez{writing-mode:vertical-rl;font-size:1.5cqw;letter-spacing:.5em}
.rail .sezn{font-family:"Anton",sans-serif;color:var(--red);font-size:5cqw;line-height:1}
.phead{margin-bottom:3.4cqw}
.kick{font-size:1.85cqw;display:block;margin-bottom:2cqw}
.kick::before{content:"";display:inline-block;width:4cqw;height:2px;background:var(--red);
  vertical-align:middle;margin-right:1.4cqw;transform:translateY(-.3cqw)}
.ptitle{font-size:8.6cqw;color:var(--white)}
.ptitle br{line-height:.9}

/* ---------------- COVER ---------------- */
.cover{padding:0;justify-content:space-between}
.cover-red{position:absolute;z-index:1;right:-14%;bottom:-16%;width:96%;height:80%;
  background:linear-gradient(135deg,var(--red) 0%,var(--red-deep) 100%);
  transform:skewX(-14deg);transform-origin:bottom right;
  box-shadow:-20px 0 60px -20px rgba(218,33,40,.5)}
.bpwrap{position:absolute;color:#fff;opacity:.16;pointer-events:none}
.cover-red .bpwrap{right:6%;bottom:8%;width:62cqw;transform:skewX(14deg)}
.bp{width:100%;height:auto;display:block}
.cover-top{display:flex;justify-content:space-between;align-items:flex-start;
  padding:8cqw 8cqw 0}
.docmeta{display:flex;flex-direction:column;align-items:flex-end;gap:.7cqw;
  font-size:1.55cqw;letter-spacing:.18em;text-align:right}
.cover-hero{padding:0 8cqw;margin-top:auto;margin-bottom:2cqw;position:relative;z-index:3}
.eyebrow{font-size:2cqw;display:block;margin-bottom:3cqw;color:var(--steel)}
.htitle{font-size:18cqw;color:var(--white);letter-spacing:.004em}
.htitle .hy{color:var(--red);-webkit-text-fill-color:var(--red)}
.htitle.sm{font-size:13cqw}
.lead{font-family:"Mont";font-weight:500;font-size:2.7cqw;line-height:1.4;
  color:#E7EAEF;max-width:44cqw;margin:4cqw 0 0}
.cover-foot{display:grid;grid-template-columns:repeat(4,1fr);
  border-top:1px solid var(--line-strong);background:rgba(9,10,13,.6);
  backdrop-filter:blur(2px);position:relative;z-index:3}
.cf{padding:3.4cqw 2.4cqw;border-right:1px solid var(--line);display:flex;
  flex-direction:column;gap:1cqw}
.cf:last-child{border-right:0}
.cfk{font-size:1.5cqw;letter-spacing:.2em}
.cfv{font-family:"Mont";font-weight:600;font-size:2cqw;color:var(--white)}
.cf.web .cfv{color:var(--red-ink)}

/* ---------------- LOGO ---------------- */
.logo{display:inline-flex;align-items:center;gap:2cqw}
.logo .mk{width:6.4cqw;height:6.4cqw;flex:none;filter:drop-shadow(0 2px 6px rgba(0,0,0,.4))}
.logo .wm{display:flex;flex-direction:column;line-height:1}
.logo .wm b{font-family:"Anton",sans-serif;font-weight:400;font-size:5cqw;
  letter-spacing:.14em;color:var(--white)}
.logo .wm i{font-style:normal;font-family:"Mont";font-weight:600;font-size:1.4cqw;
  letter-spacing:.34em;text-transform:uppercase;color:var(--steel);margin-top:.5cqw}

/* ---------------- body columns ---------------- */
.two-col{display:grid;grid-template-columns:1.55fr 1fr;gap:6cqw;align-items:start}
.two-col.wide{grid-template-columns:1fr 1fr}
.intro{font-size:2.7cqw;line-height:1.5;color:#E7EAEF;max-width:62cqw;margin-bottom:4cqw}
blockquote{margin:3cqw 0 0;padding-left:3cqw;border-left:3px solid var(--red);
  font-family:"Mont";font-weight:600;font-size:2.5cqw;line-height:1.4;color:var(--white)}
.side-label{display:block;font-size:1.7cqw;padding-bottom:1.6cqw;margin-bottom:2cqw;
  border-bottom:1px solid var(--line-strong);color:var(--red-ink)}

/* dati / quals / contacts definition rows */
.dati,.quals,.contacts{margin:0;display:flex;flex-direction:column}
.drow,.qrow,.crow{display:flex;flex-direction:column;gap:.5cqw;padding:1.7cqw 0;
  border-bottom:1px solid var(--line)}
.drow dt,.qrow dt,.crow dt{font-size:1.5cqw;letter-spacing:.2em;text-transform:uppercase;
  color:var(--steel);font-weight:600}
.drow dd,.qrow dd,.crow dd{margin:0;font-family:"Mont";font-weight:500;
  font-size:2cqw;line-height:1.35;color:var(--white)}
.qrow dd{font-weight:400;color:#D5D9E0}

/* azienda page — denser to fit portrait height */
.azienda .ptitle{font-size:7.2cqw}
.azienda .phead{margin-bottom:2.6cqw}
.azienda .body{font-size:2.12cqw;line-height:1.5}
.azienda .body p{margin-bottom:1.15cqw}
.azienda blockquote{font-size:2.15cqw;margin-top:2.2cqw}
.azienda .two-col{gap:5cqw}
.azienda .drow,.azienda .qrow{padding:1.35cqw 0}
.azienda .drow dd{font-size:1.9cqw}

/* stat band */
.statband{margin-top:auto;display:grid;grid-template-columns:repeat(4,1fr);
  border-top:1px solid var(--line-strong)}
.stat{padding:3.2cqw 1cqw 0;display:flex;flex-direction:column;gap:.8cqw;
  border-right:1px solid var(--line)}
.stat:last-child{border-right:0}
.sv{font-family:"Anton",sans-serif;font-size:7.4cqw;color:var(--red);line-height:.9}
.sk{font-size:1.5cqw;letter-spacing:.16em}

/* ---------------- value cards (02) ---------------- */
.vgrid{display:grid;grid-template-columns:1fr 1fr;gap:0;
  border-top:1px solid var(--line-strong);border-left:1px solid var(--line-strong)}
.vcard{padding:3.6cqw 3.4cqw;border-right:1px solid var(--line-strong);
  border-bottom:1px solid var(--line-strong);position:relative;min-height:24cqw}
.vcard .vn{font-family:"Anton",sans-serif;font-size:3.4cqw;color:var(--red);
  display:block;margin-bottom:1.4cqw}
.vcard h3{font-size:3cqw;color:var(--white);margin:0 0 1.6cqw;line-height:1}
.vcard p{margin:0;font-size:1.95cqw;line-height:1.5;color:#C9CED7}

/* ---------------- services index (03) ---------------- */
.servindex{display:flex;flex-direction:column;border-top:1px solid var(--line-strong)}
.sidx{display:grid;grid-template-columns:auto 1fr auto;align-items:center;
  gap:3.4cqw;padding:3.4cqw 0;border-bottom:1px solid var(--line);
  transition:padding .25s ease}
.sidn{font-family:"Anton",sans-serif;font-size:6cqw;color:var(--red);line-height:.8}
.sidt{font-family:"Anton",sans-serif;text-transform:uppercase;font-size:4cqw;
  color:var(--white);line-height:1}
.sidd{font-size:1.85cqw;color:var(--steel);max-width:30cqw;text-align:right;line-height:1.35}

/* ---------------- service detail ---------------- */
.service{overflow:hidden}
.bignum{position:absolute;z-index:1;top:3cqw;right:6cqw;
  font-family:"Anton",sans-serif;font-size:34cqw;line-height:1;
  color:rgba(218,33,40,.10);letter-spacing:-.02em;pointer-events:none}
.prest-lbl{margin-top:1cqw}
.prest{list-style:none;margin:0;padding:0;display:flex;flex-direction:column}
.prest li{display:grid;grid-template-columns:1fr;gap:.7cqw;padding:2.2cqw 0;
  border-bottom:1px solid var(--line)}
.prest .pt{font-family:"Mont";font-weight:700;font-size:2.35cqw;color:var(--white);
  display:flex;align-items:baseline;gap:1.6cqw}
.prest .pt::before{content:"";width:1.8cqw;height:1.8cqw;flex:none;
  background:var(--red);transform:rotate(45deg);translate:0 -.1cqw}
.prest .pd{font-size:2cqw;line-height:1.45;color:#C4C9D3;padding-left:3.4cqw}
.nota{margin-top:auto;background:var(--panel-2);border-left:3px solid var(--red);
  padding:2.8cqw 3cqw;display:flex;flex-direction:column;gap:1.2cqw}
.nota .nl{font-size:1.55cqw}
.nota p{margin:0;font-size:2cqw;line-height:1.45;color:#D5D9E0}

/* emergency block (3.5) */
.emerg{display:flex;flex-direction:column;gap:1cqw;background:var(--red);
  color:#fff;padding:3cqw 3.4cqw;margin:0 0 4cqw}
.emerg .el{color:rgba(255,255,255,.8);font-size:1.6cqw}
.emerg .enum{font-family:"Anton",sans-serif;font-size:8cqw;line-height:.9;color:#fff;
  letter-spacing:.01em}
.emerg .ed{font-family:"Mont";font-weight:600;font-size:1.8cqw;color:rgba(255,255,255,.9)}

/* collaborazione footnote */
.foot-note{margin-top:auto;font-size:1.7cqw;line-height:1.5;color:var(--steel);
  border-top:1px solid var(--line);padding-top:2.4cqw}

/* ---------------- BACK ---------------- */
.back{padding:0;justify-content:flex-start}
.back-red{position:absolute;z-index:1;left:-16%;top:-18%;width:92%;height:74%;
  background:linear-gradient(135deg,var(--red) 0%,var(--red-deep) 100%);
  transform:skewX(-14deg)}
.back-red .bpwrap{left:8%;top:14%;width:56cqw;transform:skewX(14deg)}
.back-top{display:flex;justify-content:space-between;align-items:flex-start;
  padding:8cqw 8cqw 0;position:relative;z-index:3}
.back-hero{padding:0 8cqw;margin-top:8cqw;position:relative;z-index:3}
.back-hero .eyebrow{color:#fff;opacity:.85}
.back .htitle.sm{font-size:14cqw;margin-top:2cqw}
.contacts{margin-top:auto;padding:0 8cqw;display:grid;grid-template-columns:1fr 1fr;
  column-gap:6cqw;position:relative;z-index:3}
.back-foot{margin-top:5cqw;padding:3cqw 8cqw;display:flex;justify-content:space-between;
  border-top:1px solid var(--line-strong);font-size:1.55cqw;letter-spacing:.14em;
  text-transform:uppercase;color:var(--steel);position:relative;z-index:3}

/* ---------------- hover (screen only) ---------------- */
@media(hover:hover){
  .sidx:hover{padding-left:2cqw}
  .vcard:hover{background:var(--panel-2)}
}

/* ---------------- PRINT ---------------- */
@page{size:A4;margin:0}
@media print{
  body{background:#fff;padding:0}
  .stack{gap:0}
  .leaf{width:210mm;height:297mm;box-shadow:none;break-after:page;page-break-after:always}
  .leaf:last-child{break-after:auto}
  .crop{display:none}
}
"""

FONTS = f"""
@font-face{{font-family:"Anton";font-style:normal;font-weight:400;font-display:swap;
  src:url(data:font/woff2;base64,{ANTON}) format("woff2");}}
@font-face{{font-family:"Mont";font-style:normal;font-weight:300 800;font-display:swap;
  src:url(data:font/woff2;base64,{MONT}) format("woff2");}}
"""

HTML = f"""<title>KRECA — Profilo Aziendale</title>
<style>{FONTS}{CSS}</style>
<main class="stack">
{BOOK}
</main>"""

out = os.path.join(SCR, "index.html")
open(out, "w").write(HTML)
print("wrote", out, len(HTML), "bytes")
