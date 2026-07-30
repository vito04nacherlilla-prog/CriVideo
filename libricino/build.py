#!/usr/bin/env python3
# KRECA — libricino aziendale RICCO. Layout rigoroso e coordinato:
# header identico in alto, contenuto centrato, piè di pagina con numero su ogni pagina.
import math, base64, os
SCR = os.path.dirname(os.path.abspath(__file__))
ANTON = base64.b64encode(open(os.path.join(SCR,"anton.woff2"),"rb").read()).decode()
MONT  = base64.b64encode(open(os.path.join(SCR,"mont.woff2"),"rb").read()).decode()
LOGO  = base64.b64encode(open(os.path.join(SCR,"logo-kreca.png"),"rb").read()).decode()
TOTAL = 18

def blueprint():
    cx,cy,parts=100,100,[]
    for r in (30,52,74,92): parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}"/>')
    for a in range(0,360,5):
        rad=math.radians(a); lo=(a%30==0); r1,r2=74,(92 if lo else 84)
        parts.append(f'<line x1="{cx+r1*math.cos(rad):.1f}" y1="{cy+r1*math.sin(rad):.1f}" x2="{cx+r2*math.cos(rad):.1f}" y2="{cy+r2*math.sin(rad):.1f}"/>')
    t=[]
    for a in range(0,360,20):
        for off,r in ((-5,30),(-3,40),(3,40),(5,30)):
            rr=math.radians(a+off); t.append(f"{cx+r*math.cos(rr):.1f},{cy+r*math.sin(rr):.1f}")
    parts.append(f'<polygon points="{" ".join(t)}"/>'); parts.append(f'<circle cx="{cx}" cy="{cy}" r="12"/>')
    parts.append(f'<line x1="{cx}" y1="4" x2="{cx}" y2="196"/>'); parts.append(f'<line x1="4" y1="{cy}" x2="196" y2="{cy}"/>')
    return ('<svg class="bp" viewBox="0 0 200 200" fill="none" stroke="currentColor" stroke-width="0.8" vector-effect="non-scaling-stroke">'+"".join(parts)+'</svg>')
BP=blueprint()
def logo(cls=""): return f'<img class="logo-img {cls}" alt="KRECA — Officina Metalmeccanica" src="data:image/png;base64,{LOGO}">'
def rail(sez): return f'<div class="rail"><span class="sez">Sez</span><span class="sezn">{sez}</span></div>'
def head(sez,kick,title): return rail(sez)+f'<header class="phead"><span class="kick">{kick}</span><h2 class="ptitle">{title}</h2></header>'
def pfoot(n): return f'<div class="pfoot"><span class="pf-b">KRECA · Profilo aziendale</span><span class="pf-n">{n:02d} <i>/ {TOTAL}</i></span></div>'
def leaf(n,sez,kick,title,content,cls="",align="center"):
    return (f'<section class="leaf {cls}"><div class="crop"></div>{head(sez,kick,title)}'
            f'<div class="content {align}">{content}</div>{pfoot(n)}</section>')
def prest(items):
    return '<ul class="prest">'+"".join(f'<li><span class="pt">{t}</span><span class="pd">{d}</span></li>' for t,d in items)+'</ul>'
def norme(items):
    return '<div class="norme">'+"".join(f'<div class="nb"><span class="nk">{k}</span><span class="nv">{v}</span></div>' for k,v in items)+'</div>'
def nota(t): return f'<div class="nota"><span class="nl">Nota operativa</span><p>{t}</p></div>'
def lbl(t): return f'<span class="side-label block-label">{t}</span>'

P=[]  # pages

# 01 COVER
P.append(f'''<section class="leaf cover"><div class="crop"></div>
  <div class="cover-red"><div class="bpwrap">{BP}</div></div>
  <div class="cover-top">{logo("lg")}<div class="docmeta"><span>DOC · KRC / BR / 2026</span><span>Profilo aziendale — Rev. 06</span></div></div>
  <div class="cover-hero"><span class="eyebrow">General contractor · Puglia &amp; Basilicata · ISO 9001</span>
    <h1 class="htitle">Un solo<br>partner,<br><span class="hg">ogni opera.</span></h1>
    <p class="lead">Costruzioni metalliche, chiusure e sicurezza, facility e pronto intervento H24 —
    seguiti dall'inizio alla fine da un unico referente.</p></div>
  <div class="cover-foot">
    <div class="cf"><span class="cfk">Operativi dal</span><span class="cfv">2019</span></div>
    <div class="cf"><span class="cfk">Copertura</span><span class="cfv">Puglia · Basilicata</span></div>
    <div class="cf"><span class="cfk">Urgenze</span><span class="cfv">Pronto intervento H24</span></div>
    <div class="cf web"><span class="cfk">Web</span><span class="cfv">www.kreca.it</span></div></div>
</section>''')

# 02 INDICE
toc=[("01","Chi siamo","L'officina, la squadra, la filosofia"),("02","La nostra storia","Dal 2019 alla S.r.l."),
     ("03","Perché KRECA","Sei vantaggi concreti"),("04","Il metodo","Dal sopralluogo al collaudo"),
     ("05","Costruzioni metalliche","Carpenteria e strutture in acciaio"),("06","Chiusure &amp; sicurezza","Serramenti, facciate, blindature"),
     ("07","Facility &amp; logistica","Manutenzione e gestione continuativa"),("08","Pronto intervento H24","Fabbro e urgenze in tutta la regione"),
     ("09","Settori serviti","Retail, industria, condomìni, privati"),("10","Lavori recenti","Hanno scelto KRECA"),
     ("11","Zone servite","Puglia e Basilicata"),("12","Certificazioni &amp; norme","Qualità e conformità"),
     ("13","Glossario tecnico","I termini che contano"),("14","Domande frequenti","Le risposte più utili"),("15","Contatti","Parliamone")]
toc_html='<nav class="toc">'+"".join(f'<a class="trow"><span class="tn">{n}</span><span class="tt">{t}</span><span class="tdot"></span><span class="td">{d}</span></a>' for n,t,d in toc)+'</nav>'
P.append(leaf(2,"—","Indice","Cosa trovi<br>in questo profilo.",toc_html))

# 03 CHI SIAMO
dati=[("Ragione sociale","KRECA S.r.l. — Officina Metalmeccanica"),("Forma giuridica","Società a responsabilità limitata"),
      ("Sede legale","Via Giotto 5, 70018 Rutigliano (BA)"),("Sede operativa","S.P. 240 delle Grotte Orientali 290, Rutigliano (BA)"),
      ("P.IVA / C.F.","09015760722"),("REA","BA-665535"),("Attiva dal","2019 — esperienza artigiana pregressa"),
      ("Settore","Lavorazione prodotti in metallo — ATECO 25")]
dati_rows="".join(f'<div class="drow"><dt>{k}</dt><dd>{v}</dd></div>' for k,v in dati)
chi=f'''<div class="two-col"><div class="col-main">
  <p><strong>KRECA S.r.l.</strong> è un'officina metalmeccanica e un general contractor per l'edilizia industriale e
  commerciale. Progettiamo, <strong>produciamo internamente nella nostra officina di Rutigliano (BA)</strong> e posiamo
  in opera: carpenteria e strutture in acciaio, serramenti e facciate, sistemi di chiusura e sicurezza.</p>
  <p>Affianchiamo alla produzione diretta un servizio completo di <strong>facility &amp; logistica</strong> per capannoni
  e poli logistici e un <strong>pronto intervento H24</strong> su accessi e chiusure. Il cliente ha così un
  <strong>unico interlocutore</strong> per l'intera opera — dalla struttura portante alle finiture, dalla manutenzione
  all'emergenza.</p>
  <p>Operiamo su tutta la <strong>Puglia e la Basilicata</strong> con squadre distribuite e reperibilità. Ogni lavoro è
  eseguito a norma, con marcatura CE e documentazione utile anche alle detrazioni fiscali.</p>
  <blockquote>Un solo partner, ogni opera. Dalla parola al preventivo, dalla posa alla manutenzione.</blockquote>
  </div><aside class="col-side">{lbl("Dati identificativi")}<dl class="dati">{dati_rows}</dl></aside></div>'''
P.append(leaf(3,"01","Chi siamo","Un'officina, un metodo,<br>un solo referente.",chi,cls="azienda"))

# 04 STORIA
tl=[("2019","Fondazione e radici","Nasce la ditta individuale KRECA di Jeliazkova Kremena, unendo la solida esperienza artigianale di Carmine nel settore metalmeccanico a una nuova visione operativa, focalizzata su carpenteria e manutenzioni industriali."),
    ("2020 — 2024","Espansione e fiducia","Consolidamento delle competenze nei poli logistici e industriali della Puglia. L'azienda si afferma come partner affidabile per grandi manutenzioni e strutture su misura, ampliando il parco clienti."),
    ("2025","Evoluzione in KRECA S.r.l.","Passaggio alla forma societaria di S.r.l. per rispondere alla crescente complessità dei progetti direzionali e industriali, mantenendo intatta la reattività e la passione delle origini familiari.")]
tl_html='<div class="timeline">'+"".join(f'<div class="tli"><span class="ty">{y}</span><div class="tlx"><h3>{t}</h3><p>{d}</p></div></div>' for y,t,d in tl)+'</div>'
P.append(leaf(4,"02","La nostra storia","Una crescita<br>costruita sul campo.",tl_html))

# 05 PERCHÉ
vals=[("01","Officina di produzione propria","Carpenteria e serramenti lavorati nella nostra officina di Rutigliano: controllo su qualità, materiali, finiture e tempi."),
      ("02","Interlocutore unico","Un solo referente per costruzioni, chiusure, facility e urgenze — anche nello stesso cantiere."),
      ("03","Certificati ISO 9001","Sistema di gestione qualità certificato e interventi a norma, con documentazione e attestazioni."),
      ("04","Pronto intervento H24","Squadre dedicate pronte a intervenire, con tempi di risposta rapidi in tutta la provincia."),
      ("05","Trasparenza sui costi","Preventivo chiaro prima di iniziare: nessuna sorpresa, tempi e prezzi definiti."),
      ("06","Copertura Puglia &amp; Basilicata","Presenza reale sul territorio, con squadre distribuite e reperibilità per gli interventi urgenti.")]
cards='<div class="vgrid">'+"".join(f'<article class="vcard"><span class="vn">{n}</span><h3>{t}</h3><p>{d}</p></article>' for n,t,d in vals)+'</div>'
nums=[("2019","Operativi dal"),("H24","Pronto intervento"),("≈60′","Intervento in provincia"),("ISO 9001","Qualità certificata")]
nums_html='<div class="statband">'+"".join(f'<div class="stat"><span class="sv">{v}</span><span class="sk">{k}</span></div>' for v,k in nums)+'</div>'
P.append(leaf(5,"03","Perché scegliere KRECA","Un solo partner,<br>ogni opera.",cards+nums_html))

# 06 METODO
steps=[("01","Sopralluogo e analisi","Veniamo da te: valutiamo esigenze, misure, impianti e vincoli tecnici del progetto."),
       ("02","Preventivo e progettazione","Soluzione su misura con disegni esecutivi e preventivo chiaro, senza sorprese."),
       ("03","Produzione in officina","Realizziamo strutture, serramenti e sistemi nella nostra officina, con materiali selezionati."),
       ("04","Posa, collaudo e assistenza","Installazione a regola d'arte, collaudo e — se vuoi — manutenzione programmata nel tempo.")]
steps_html='<div class="method">'+"".join(f'<article class="mstep"><span class="mn">{n}</span><h3>{t}</h3><p>{d}</p></article>' for n,t,d in steps)+'</div>'
met=(f'<p class="body intro">Un percorso in quattro passi, uguale per ogni commessa: chiaro, tracciato e con un unico '
     f'referente che segue il lavoro dall\'inizio alla fine.</p>{steps_html}'
     f'<div class="tline"><span>Trasparenza, nessuna sorpresa</span><b>Costi e tempi comunicati prima di iniziare.</b></div>')
P.append(leaf(6,"04","Il metodo","Dal sopralluogo<br>al collaudo.",met))

# 07 AREE INDEX
serv=[("05","Costruzioni metalliche","Carpenteria, strutture portanti, soppalchi, scale e accessi in acciaio."),
      ("06","Chiusure &amp; sicurezza","Serramenti, facciate continue, blindature, serrande e grate."),
      ("07","Facility &amp; logistica","Manutenzione tecnica e gestione continuativa per industria e logistica."),
      ("08","Pronto intervento H24","Fabbro e urgenze su serrature, serrande e accessi, in tutta la regione.")]
idx='<nav class="servindex">'+"".join(f'<a class="sidx"><span class="sidn">{n}</span><span class="sidt">{t}</span><span class="sidd">{d}</span></a>' for n,t,d in serv)+'</nav>'
aree=(f'<p class="body intro">Dalla struttura portante alla messa in sicurezza notturna: quattro aree coordinate che '
      f'coprono l\'intero ciclo di vita dell\'immobile industriale e commerciale.</p>{idx}')
P.append(leaf(7,"05—08","Aree di servizio","Quattro aree,<br>un unico partner.",aree))

def service(n,sez,title,intro,items,nrm=None,nota_txt=None,emergency=None):
    body=f'<p class="body intro">{intro}</p>'
    if emergency:
        body+=(f'<div class="emerg"><span class="el">Emergenza · attivazione diretta</span><a class="enum">{emergency}</a>'
               f'<span class="ed">Squadre pronte a intervenire entro ~60 minuti · H24 · Puglia e Basilicata</span></div>')
    body+=lbl("Cosa realizziamo")+prest(items)
    if nrm: body+=lbl("A norma di legge")+norme(nrm)
    if nota_txt: body+=nota(nota_txt)
    return leaf(n,sez,"Aree di servizio",title,body,cls="service")

P.append(service(8,"05","Costruzioni<br>metalliche.",
  "Progettiamo, produciamo in officina e posiamo strutture e manufatti in ferro e acciaio, su misura per contesti civili, commerciali e industriali. Ogni elemento nasce internamente — dal taglio alla saldatura MIG/MAG e TIG, dalle finiture al trattamento protettivo.",
  [("Carpenteria e strutture portanti","Travi, pilastri, telai e ossature in acciaio per capannoni, ampliamenti, tettoie e coperture."),
   ("Soppalchi industriali","Strutture autoportanti che recuperano superficie per stoccaggio, produzione o uffici senza ampliare l'edificio."),
   ("Scale, parapetti e passerelle","Scale interne ed esterne, scale antincendio, camminamenti e passerelle di servizio conformi."),
   ("Recinzioni, cancelli e manufatti su disegno","Recinzioni perimetrali, cancelli, staffe e manufatti sviluppati su disegno del cliente."),
   ("Lavorazioni per conto terzi","Taglio, piegatura, foratura, saldatura e assemblaggio per imprese e general contractor.")],
  nrm=[("Sicurezza strutturale","Calcoli e pratiche genio civile tramite rete di ingegneri partner."),
       ("Zincatura a caldo · EN ISO 1461","Trattamenti anticorrosivi presso impianti certificati per la massima durata."),
       ("Accessi sicuri · EN ISO 14122","Camminamenti, passerelle e scale di servizio a norma.")]))

P.append(service(9,"06","Chiusure<br>&amp; sicurezza.",
  "Gamma completa per l'involucro e la protezione: serramenti, facciate, vetrate e sistemi di sicurezza passiva. Produciamo internamente ferro e alluminio e ci avvaliamo di partner selezionati per PVC, vetro e componenti speciali — sempre con posa a regola d'arte.",
  [("Serramenti in alluminio a taglio termico","Alte prestazioni termiche e acustiche per complessi industriali, direzionali e residenziali."),
   ("Serramenti in PVC rinforzato e infissi su misura","Ottimo rapporto tra isolamento, durata e costo, con marcatura CE."),
   ("Vetrate panoramiche e facciate continue","Sistemi tutto vetro, scorrevoli minimali e facciate strutturali."),
   ("Carpenteria di sicurezza e porte blindate","Porte blindate di ultima generazione, inferriate e grate a snodo su misura."),
   ("Chiusure industriali, serrande &amp; grate","Serrande motorizzate, portoni sezionali e a libro, automazioni e ripristino strutturale.")],
  nrm=[("Antieffrazione · UNI EN 1627","Classi di resistenza certificate (RC2 / RC3) per i sistemi installati."),
       ("Tenuta agli agenti · UNI EN 13830","Prestazione e marcatura CE per facciate continue e serramenti esterni."),
       ("Compartimentazione · REI / EW","Chiusure tecniche e barriere tagliafuoco certificate per i luoghi di lavoro."),
       ("Tracciabilità di filiera · DoP","Certificati di Costanza della Prestazione e marcatura CE.")]))

P.append(service(10,"07","Facility<br>&amp; logistica.",
  "Per chi gestisce un capannone, un magazzino o un polo logistico la manutenzione è un costo continuo. Il nostro facility management la trasforma in un servizio ordinato e prevedibile: un unico referente per chiusure meccanizzate, carpenteria e interventi edili a norma.",
  [("Manutenzione di chiusure e portoni","Serrande motorizzate, portoni sezionali e automazioni: controlli, riparazioni e sostituzioni."),
   ("Strutture e carpenteria","Interventi su ringhiere, recinzioni, scale e strutture in acciaio con cedimenti o rischi."),
   ("Interventi edili a norma","Piccole opere edili, allestimenti e adeguamenti coordinati con la produzione in officina."),
   ("Contratti di facility management","Operatività continuativa per attività, capannoni e poli logistici, con reportistica dedicata.")],
  nota_txt="Processo in 4 fasi: sopralluogo e analisi · piano e preventivo · esecuzione con squadra dedicata · gestione continuativa con manutenzione programmata e referente unico nel tempo."))

P.append(service(11,"08","Pronto intervento<br>H24.",
  "Serrature bloccate, serrande o cancelli fuori uso, infissi e vetrine da mettere in sicurezza: la squadra d'urgenza di KRECA opera H24 in Puglia e Basilicata, con base operativa a Rutigliano. Costi trasparenti, comunicati prima di iniziare.",
  [("Sblocco e apertura","Serrande, cancelli motorizzati e serrature bloccate, preservando l'integrità del sistema."),
   ("Riparazione urgente","Motorizzazioni, serrature e componenti meccanici di porte, portoni e chiusure."),
   ("Messa in sicurezza post-effrazione","Chiusura provvisoria, sostituzione dei componenti e ripristino delle condizioni di sicurezza."),
   ("Urgenze su strutture e aziende","Riparazioni su ringhiere, scale e strutture; pronto intervento per capannoni e poli logistici.")],
  emergency="+39 351 805 5489"))

# 12 SETTORI
sett=[("Retail &amp; GDO","Negozi, punti vendita e grande distribuzione: serrande, vetrine, porte automatiche e sistemi di sicurezza, con pronto intervento H24 per non fermare l'attività."),
      ("Industria &amp; logistica","Capannoni e poli logistici: strutture portanti, portoni industriali, manutenzione e facility management continuativo."),
      ("Condomìni &amp; residenziale","Edifici e parti comuni: infissi, ringhiere, scale, cancelli, recinzioni e inferriate, a norma e con documentazione per le detrazioni."),
      ("Uffici &amp; direzionale","Facciate continue, serramenti a taglio termico, porte di sicurezza e allestimenti per spazi di lavoro."),
      ("Privati &amp; abitazioni","Case e ville: infissi termoacustici, chiusure civili, carpenteria metallica leggera e sistemi di sicurezza."),
      ("Banche &amp; uffici tecnici","Strutture portanti, accessi blindati e messa in sicurezza per sedi e sportelli d'ingresso.")]
sett_html='<div class="sectors">'+"".join(f'<article class="sect"><h3>{t}</h3><p>{d}</p></article>' for t,d in sett)+'</div>'
P.append(leaf(12,"09","Settori serviti","Un partner per<br>ogni contesto.",sett_html))

# 13 LAVORI
proj=[("Banco BPM","Monopoli (BA)","02 / 2026","Carpenteria","Strutture portanti dei portoni d'ingresso, serrate e messe in sicurezza."),
      ("Generali","Bari (BA)","11 / 2025","Manutenzione","Riparazioni di falegnameria e carpenteria per manutenzione straordinaria in sede."),
      ("Baglioni","Otranto (LE)","04 / 2026","Carpenteria","Pavimentazione gettata, recinzione perimetrale e porta metallica del vano quadro."),
      ("Polo logistico","Provincia di Bari","2025","Facility","Manutenzione programmata di serrande e portoni industriali in contratto continuativo.")]
proj_html='<div class="projects">'+"".join(f'<article class="proj"><div class="pjh"><span class="pjt">{tag}</span><span class="pjd">{date}</span></div><h3>{name}</h3><span class="pjl">{loc}</span><p>{desc}</p></article>' for name,loc,date,tag,desc in proj)+'</div>'
lav=f'<p class="body intro">In primo piano alcuni lavori dei nostri settori — carpenteria, serramenti, chiusure e sicurezza — per aziende, gruppi e privati.</p>{proj_html}'
P.append(leaf(13,"10","Lavori recenti","Hanno scelto<br>KRECA.",lav))

# 14 ZONE
puglia=["Rutigliano","Bari","Mola di Bari","Polignano a Mare","Conversano","Putignano","Monopoli","Triggiano","Noicattaro","Casamassima","Acquaviva delle Fonti","Gioia del Colle","Altamura","Gravina in Puglia","Bitonto","Modugno","Molfetta","Bisceglie","Trani","Andria","Barletta","Brindisi","Taranto","Lecce","Foggia"]
basil=["Matera","Potenza","Pisticci","Policoro","Bernalda","Ferrandina"]
def chips(l): return '<div class="chips">'+"".join(f'<span class="chip">{c}</span>' for c in l)+'</div>'
zon=(f'<p class="body intro">Base operativa a <strong>Rutigliano (BA)</strong>, squadre distribuite e reperibilità per gli '
     f'interventi urgenti su tutta l\'area di competenza.</p>'
     f'<div class="zone">{lbl("Puglia — provincia di Bari e oltre")}{chips(puglia)}</div>'
     f'<div class="zone">{lbl("Basilicata — Materano e Potentino")}{chips(basil)}</div>')
P.append(leaf(14,"11","Zone servite","Puglia e Basilicata,<br>sul territorio.",zon))

# 15 CERTIFICAZIONI
cert=[("ISO 9001","Sistema di gestione qualità certificato, applicato a ogni intervento."),
      ("D.Lgs 81/08","Pieno rispetto delle norme di sicurezza sul lavoro; patente a crediti INL."),
      ("Dichiarazioni di conformità","Impianti e opere consegnati a regola d'arte, con attestazione."),
      ("Marcatura CE","Serramenti e facciate con tracciabilità e Dichiarazione di Prestazione (DoP)."),
      ("Copertura assicurativa","Polizza RC verso Terzi con massimale di € 3.000.000."),
      ("Regolarità e mercati P.A.","DURC regolare, CCNL Metalmeccanica; iscrizione a MEPA ed EmPULIA.")]
cert_html="".join(f'<div class="crow2"><dt>{k}</dt><dd>{v}</dd></div>' for k,v in cert)
en=[("UNI EN 1627","Antieffrazione RC2/RC3"),("EN 356","Vetro di sicurezza"),("UNI EN 13830","Facciate continue"),
    ("EN ISO 1461","Zincatura a caldo"),("EN ISO 14122","Accessi e passerelle"),("REI / EW","Compartimentazione")]
en_html="".join(f'<span class="chip mono">{k}<i>{v}</i></span>' for k,v in en)
crt=(f'<div class="two-col wide"><div class="col-main">{lbl("Qualifiche e coperture")}<dl class="quals">{cert_html}</dl></div>'
     f'<aside class="col-side">{lbl("Norme tecniche di riferimento")}<div class="chips en">{en_html}</div>'
     f'<p class="foot-note">Documentazione amministrativa completa (visura, DURC, patente a crediti, polizza, DoP) disponibile in fase di qualifica fornitore.</p></aside></div>')
P.append(leaf(15,"12","Certificazioni &amp; norme","Qualità certificata,<br>opere a norma.",crt))

# 16 GLOSSARIO
gloss=[("Classe RC2 / RC3 (EN 1627)","Misura quanto un infisso o un'inferriata resiste a un tentativo di scasso: la RC2 regge attrezzi manuali semplici per ≥3 minuti, la RC3 strumenti pesanti per ≥5."),
       ("Vetro stratificato antieffrazione","Lastre unite da fogli plastici (PVB): in caso di urto i frammenti restano incollati, mantenendo la barriera (EN 356)."),
       ("Cilindro europeo","Nucleo di cifratura sostituibile con perni in acciaio, anti-bumping e anti-trapano e chiavi a duplicazione protetta."),
       ("Defender antishock","Corazza in acciaio temperato sul cilindro: impedisce di strappare, forare o estrarre la serratura."),
       ("Molla di richiamo (serrande)","Bilancia il peso del manto e ne permette il sollevamento: la sua rottura è tra le cause più frequenti di fermo per i negozi."),
       ("Soppalco industriale","Struttura metallica autoportante che aggiunge un piano dentro un capannone, recuperando superficie utile."),
       ("Saldatura MIG/MAG e TIG","MIG/MAG a filo continuo, veloce; TIG con elettrodo di tungsteno, più lento ma con giunti puliti su materiali delicati."),
       ("Marcatura CE infissi","Garantisce la legalità del prodotto e l'accesso alle detrazioni fiscali.")]
gl_html='<div class="glossary">'+"".join(f'<div class="gitem"><h3>{t}</h3><p>{d}</p></div>' for t,d in gloss)+'</div>'
glo=f'<p class="body intro">Parliamo la stessa lingua: i termini più utili per scegliere con consapevolezza infissi, chiusure e sicurezza.</p>{gl_html}'
P.append(leaf(16,"13","Glossario tecnico","I termini<br>che contano.",glo))

# 17 FAQ
faq=[("Intervenite in urgenza, anche di notte?","Sì. La squadra di pronto intervento opera H24 in Puglia e Basilicata, con tempi di risposta rapidi in provincia e costi comunicati prima di iniziare."),
     ("Come funziona il preventivo?","Facciamo un sopralluogo, prendiamo le misure e ti proponiamo una soluzione con preventivo chiaro: tempi e costi definiti, senza sorprese."),
     ("Rilasciate documentazione per le detrazioni?","Sì. Lavorazioni a norma, marcatura CE e dichiarazioni di conformità: forniamo la documentazione utile anche alle detrazioni fiscali."),
     ("Producete internamente?","Sì. Carpenteria e serramenti nascono nella nostra officina di Rutigliano (BA): controlliamo qualità, materiali e tempi."),
     ("Seguite anche la manutenzione nel tempo?","Sì. Con i contratti di facility offriamo manutenzione programmata e un referente unico continuativo per capannoni e poli logistici."),
     ("Su quali zone operate?","Su tutta la Puglia e la Basilicata, con squadre distribuite sul territorio e reperibilità per le urgenze.")]
faq_html='<div class="faqs">'+"".join(f'<div class="faq"><h3>{q}</h3><p>{a}</p></div>' for q,a in faq)+'</div>'
P.append(leaf(17,"14","Domande frequenti","Le risposte<br>più utili.",faq_html))

# 18 CONTATTI / BACK
contacts=[("Telefono","080 875 5152"),("Mobile · H24","+39 351 805 5489"),("E-mail","info@kreca.it"),("PEC","kreca@pec.it"),
          ("Web","www.kreca.it"),("Social","IG @kreca_srl · FB /krecasrl"),("Sede legale","Via Giotto 5, 70018 Rutigliano (BA)"),
          ("Sede operativa","S.P. 240 Grotte Orientali 290, Rutigliano (BA)")]
crows="".join(f'<div class="crow"><dt>{k}</dt><dd>{v}</dd></div>' for k,v in contacts)
P.append(f'''<section class="leaf back"><div class="crop"></div>
  <div class="back-red"><div class="bpwrap">{BP}</div></div>
  <div class="back-top">{logo("lg")}<span class="docmeta"><span>18 / {TOTAL} — Contatti</span></span></div>
  <div class="back-hero"><span class="eyebrow">Un solo partner, ogni opera</span>
    <h1 class="htitle sm">Parliamone.<br>Dal preventivo<br>alla posa.</h1>
    <p class="lead2">Richiedi un sopralluogo o un preventivo: ti rispondiamo in fretta, anche su WhatsApp.</p></div>
  <div class="contacts">{crows}</div>
  <div class="back-foot"><span>KRECA S.r.l. — Officina Metalmeccanica</span><span>P.IVA 09015760722 · REA BA-665535 · ATECO 25</span></div>
</section>''')

BOOK="\n".join(P)

CSS=r"""
:root{--ink:#08090B;--panel:#14161B;--panel-2:#1B1F27;--panel-3:#232833;
 --red:#30D158;--red-deep:#1E9E43;--red-ink:#57DD78;--fill1:#166B39;--fill2:#07330F;
 --steel:#8B929C;--steel-dim:#5A626E;--white:#F3F5F8;
 --line:rgba(139,146,156,.16);--line-strong:rgba(139,146,156,.32);
 --pad:8cqw}
*{box-sizing:border-box}html,body{margin:0}
body{background:radial-gradient(120% 80% at 50% -10%,#1a1d24 0%,#0a0b0e 60%) fixed,#0a0b0e;
 color:var(--white);font-family:"Mont",system-ui,sans-serif;-webkit-font-smoothing:antialiased;padding:clamp(14px,4vw,56px) 0 64px}
.stack{display:flex;flex-direction:column;align-items:center;gap:clamp(18px,3.4vw,40px)}
.leaf{position:relative;overflow:hidden;width:min(820px,94vw);aspect-ratio:210/297;container-type:size;
 background:linear-gradient(160deg,#14161B 0%,#0c0d11 62%,#08090B 100%);color:var(--white);
 box-shadow:0 40px 80px -30px rgba(0,0,0,.85),0 2px 0 rgba(255,255,255,.03) inset;
 padding:var(--pad) var(--pad) 5cqw;display:flex;flex-direction:column}
.leaf::before{content:"";position:absolute;inset:0;pointer-events:none;opacity:.5;
 background:linear-gradient(var(--line) 1px,transparent 1px) 0 0/100% 5.6cqw,
 linear-gradient(90deg,var(--line) 1px,transparent 1px) 0 0/5.6cqw 100%}
.leaf>*{position:relative;z-index:2}
.crop{position:absolute;inset:0;z-index:3;pointer-events:none}
.crop::before,.crop::after{content:"";position:absolute;width:3cqw;height:3cqw}
.crop::before{top:3.2cqw;left:3.2cqw;border-top:1px solid var(--steel-dim);border-left:1px solid var(--steel-dim)}
.crop::after{bottom:3.2cqw;right:3.2cqw;border-bottom:1px solid var(--steel-dim);border-right:1px solid var(--steel-dim)}
/* rail */
.rail{position:absolute;top:0;right:0;height:100%;width:var(--pad);z-index:4;display:flex;flex-direction:column;
 align-items:center;gap:1.2cqw;padding-top:var(--pad);border-left:1px solid var(--line)}
.rail .sez{writing-mode:vertical-rl;font-size:1.5cqw;letter-spacing:.42em;text-transform:uppercase;color:var(--steel);font-weight:600}
.rail .sezn{font-family:"Anton";color:var(--red);font-size:4cqw;line-height:1;text-align:center}
/* header */
.phead{margin-bottom:0}
.kick{font-size:1.8cqw;display:flex;align-items:center;gap:1.4cqw;font-weight:600;text-transform:uppercase;letter-spacing:.24em;color:var(--steel);margin-bottom:2cqw}
.kick::before{content:"";width:4cqw;height:2px;background:var(--red);flex:none}
.ptitle{font-family:"Anton";font-weight:400;text-transform:uppercase;line-height:.92;letter-spacing:.005em;font-size:7.4cqw;color:var(--white)}
h1,h2,h3{font-family:"Anton";font-weight:400;text-transform:uppercase;line-height:.95;letter-spacing:.005em;margin:0}
/* content zone */
.content{flex:1;min-height:0;display:flex;flex-direction:column;justify-content:center;padding-top:3cqw}
.content.center{justify-content:center}
.content.start{justify-content:flex-start}
.body{font-size:2.3cqw;line-height:1.6;color:#C6CCD4}
.body p{margin:0 0 1.5cqw}.body strong{color:var(--white);font-weight:600}
.intro{font-size:2.5cqw;line-height:1.5;color:#DFE3E9;max-width:64cqw;margin:0 0 3.6cqw}
blockquote{margin:2.6cqw 0 0;padding-left:3cqw;border-left:3px solid var(--red);font-weight:600;font-size:2.15cqw;line-height:1.4;color:var(--white)}
.side-label{display:block;font-size:1.65cqw;padding-bottom:1.5cqw;margin-bottom:2.2cqw;border-bottom:1px solid var(--line-strong);
 color:var(--red-ink);text-transform:uppercase;letter-spacing:.22em;font-weight:600}
.block-label{margin-top:.4cqw}
/* footer */
.pfoot{display:flex;justify-content:space-between;align-items:center;padding-top:2.6cqw;border-top:1px solid var(--line);
 font-size:1.45cqw;letter-spacing:.2em;text-transform:uppercase;color:var(--steel);font-weight:600}
.pf-n{font-family:"Anton";font-weight:400;letter-spacing:.06em;font-size:2.2cqw;color:var(--red)}
.pf-n i{font-style:normal;color:var(--steel-dim);font-size:1.7cqw}
/* cover */
.cover{padding:0;justify-content:space-between}
.cover-red{position:absolute;z-index:1;right:-16%;bottom:-16%;width:88%;height:78%;
 background:linear-gradient(135deg,var(--fill1),var(--fill2));transform:skewX(-14deg);transform-origin:bottom right;
 box-shadow:-20px 0 60px -20px rgba(30,158,67,.4)}
.bpwrap{position:absolute;color:#fff;opacity:.15;pointer-events:none}
.cover-red .bpwrap{right:5%;bottom:7%;width:56cqw;transform:skewX(14deg)}
.bp{width:100%;height:auto;display:block}
.cover-top{display:flex;justify-content:space-between;align-items:flex-start;padding:8cqw 8cqw 0}
.docmeta{display:flex;flex-direction:column;align-items:flex-end;gap:.7cqw;font-size:1.5cqw;letter-spacing:.18em;text-align:right;text-transform:uppercase;color:var(--steel);font-weight:600}
.cover-hero{padding:0 8cqw;margin-top:auto;margin-bottom:2cqw;z-index:3}
.eyebrow{font-size:1.9cqw;display:block;margin-bottom:3cqw;color:var(--steel);text-transform:uppercase;letter-spacing:.24em;font-weight:600}
.htitle{font-family:"Anton";font-weight:400;text-transform:uppercase;line-height:.9;font-size:15cqw;color:var(--white)}
.htitle .hg{color:var(--red)}
.htitle.sm{font-size:11cqw}
.lead{font-weight:500;font-size:2.45cqw;line-height:1.4;color:#E7EAEF;max-width:50cqw;margin:3.4cqw 0 0}
.lead2{font-weight:500;font-size:2.15cqw;line-height:1.4;color:#E7EAEF;max-width:50cqw;margin:2.6cqw 0 0}
.cover-foot{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--line-strong);background:rgba(8,9,11,.62);z-index:3}
.cf{padding:3.2cqw 2.2cqw;border-right:1px solid var(--line);display:flex;flex-direction:column;gap:1cqw}
.cf:last-child{border-right:0}.cfk{font-size:1.4cqw;letter-spacing:.2em;text-transform:uppercase;color:var(--steel);font-weight:600}
.cfv{font-weight:600;font-size:1.9cqw;color:var(--white)}.cf.web .cfv{color:var(--red-ink)}
.logo-img{width:44cqw;height:auto;display:block;filter:drop-shadow(0 3px 10px rgba(0,0,0,.5))}
/* TOC */
.toc{display:flex;flex-direction:column;border-top:1px solid var(--line-strong)}
.trow{display:grid;grid-template-columns:auto auto 1fr auto;align-items:baseline;gap:2.6cqw;padding:2.1cqw 0;border-bottom:1px solid var(--line)}
.tn{font-family:"Anton";color:var(--red);font-size:2.9cqw;line-height:1;width:5cqw}
.tt{font-family:"Anton";text-transform:uppercase;color:var(--white);font-size:3.1cqw;line-height:1}
.tdot{height:1px;border-bottom:1px dotted var(--steel-dim);transform:translateY(-.5cqw)}
.td{font-size:1.7cqw;color:var(--steel);text-align:right}
/* two-col */
.two-col{display:grid;grid-template-columns:1.5fr 1fr;gap:5.5cqw;align-items:start}
.two-col.wide{grid-template-columns:1fr 1fr}
.azienda .ptitle{font-size:6.4cqw}.azienda .body{font-size:2.1cqw;line-height:1.5}.azienda .body p{margin-bottom:1.2cqw}
.azienda blockquote{font-size:2cqw}
.dati,.quals{display:flex;flex-direction:column;margin:0}
.drow,.crow2{display:flex;flex-direction:column;gap:.5cqw;padding:1.4cqw 0;border-bottom:1px solid var(--line)}
.drow dt,.crow2 dt{font-size:1.4cqw;letter-spacing:.18em;text-transform:uppercase;color:var(--steel);font-weight:600}
.drow dd,.crow2 dd{margin:0;font-weight:500;font-size:1.85cqw;line-height:1.3;color:var(--white)}
.crow2 dd{font-weight:400;color:#C6CCD4}
/* timeline */
.timeline{position:relative;padding-left:7cqw}
.timeline::before{content:"";position:absolute;left:1.4cqw;top:1.4cqw;bottom:1.4cqw;width:2px;background:linear-gradient(var(--red),var(--red-deep))}
.tli{position:relative;display:block}
.tli+.tli{margin-top:4.6cqw}
.tli::before{content:"";position:absolute;left:-5.6cqw;top:.2cqw;width:2.8cqw;height:2.8cqw;border-radius:50%;background:var(--ink);border:2px solid var(--red);box-shadow:0 0 12px rgba(48,209,88,.5)}
.tli .ty{font-family:"Anton";color:var(--red);font-size:3.4cqw;display:block;margin-bottom:1cqw}
.tli h3{font-size:3cqw;color:var(--white);margin:0 0 1.2cqw}
.tli p{margin:0;font-size:2.05cqw;line-height:1.5;color:#C6CCD4;max-width:64cqw}
/* value cards */
.vgrid{display:grid;grid-template-columns:1fr 1fr;border-top:1px solid var(--line-strong);border-left:1px solid var(--line-strong)}
.vcard{padding:3cqw 3.2cqw;border-right:1px solid var(--line-strong);border-bottom:1px solid var(--line-strong)}
.vcard .vn{font-family:"Anton";font-size:3cqw;color:var(--red);display:block;margin-bottom:1cqw}
.vcard h3{font-size:2.5cqw;color:var(--white);margin:0 0 1.2cqw;line-height:1.02}
.vcard p{margin:0;font-size:1.8cqw;line-height:1.45;color:#C4C9D3}
.statband{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--line-strong);margin-top:3.4cqw}
.stat{padding:3cqw 1cqw 0;display:flex;flex-direction:column;gap:.7cqw;border-right:1px solid var(--line)}
.stat:last-child{border-right:0}
.sv{font-family:"Anton";font-size:6cqw;color:var(--red);line-height:.9}.sk{font-size:1.4cqw;letter-spacing:.14em;text-transform:uppercase;color:var(--steel);font-weight:600}
/* method */
.method{display:grid;grid-template-columns:1fr 1fr;gap:3cqw}
.mstep{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--red);padding:3cqw 3.2cqw}
.mn{font-family:"Anton";color:var(--red);font-size:3.4cqw;display:block;margin-bottom:1cqw}
.mstep h3{font-size:2.6cqw;color:var(--white);margin:0 0 1.2cqw}
.mstep p{margin:0;font-size:1.9cqw;line-height:1.45;color:#C6CCD4}
.tline{margin-top:3.4cqw;display:flex;flex-direction:column;gap:.9cqw;border-top:1px solid var(--line-strong);padding-top:2.6cqw}
.tline span{font-size:1.6cqw;letter-spacing:.22em;text-transform:uppercase;color:var(--red-ink);font-weight:600}
.tline b{font-family:"Anton";font-weight:400;text-transform:uppercase;font-size:3.4cqw;color:var(--white)}
/* services index */
.servindex{display:flex;flex-direction:column;border-top:1px solid var(--line-strong)}
.sidx{display:grid;grid-template-columns:auto 1fr auto;align-items:center;gap:3.4cqw;padding:3.4cqw 0;border-bottom:1px solid var(--line)}
.sidn{font-family:"Anton";font-size:5.2cqw;color:var(--red);line-height:.8;width:8cqw}
.sidt{font-family:"Anton";text-transform:uppercase;font-size:3.6cqw;color:var(--white);line-height:1}
.sidd{font-size:1.7cqw;color:var(--steel);max-width:30cqw;text-align:right;line-height:1.35}
/* service detail */
.prest{list-style:none;margin:0;padding:0;display:flex;flex-direction:column}
.prest li{padding:1.5cqw 0;border-bottom:1px solid var(--line)}
.prest li:first-child{padding-top:0}
.prest .pt{font-weight:700;font-size:2.1cqw;color:var(--white);display:flex;align-items:baseline;gap:1.6cqw}
.prest .pt::before{content:"";width:1.6cqw;height:1.6cqw;flex:none;background:var(--red);transform:rotate(45deg);translate:0 -.05cqw}
.prest .pd{display:block;font-size:1.82cqw;line-height:1.4;color:#C4C9D3;padding-left:3.2cqw;margin-top:.5cqw}
.norme{display:grid;grid-template-columns:1fr 1fr;gap:1.6cqw}
.nb{background:var(--panel);border:1px solid var(--line);padding:1.8cqw 2cqw;display:flex;flex-direction:column;gap:.6cqw}
.nb .nk{font-size:1.5cqw;letter-spacing:.1em;text-transform:uppercase;color:var(--red-ink);font-weight:700}
.nb .nv{font-size:1.78cqw;line-height:1.35;color:#C6CCD4}
.nota{margin-top:2.8cqw;background:var(--panel-2);border-left:3px solid var(--red);padding:2.6cqw 3cqw;display:flex;flex-direction:column;gap:1cqw}
.nota .nl{font-size:1.5cqw;letter-spacing:.2em;text-transform:uppercase;color:var(--steel);font-weight:600}.nota p{margin:0;font-size:1.9cqw;line-height:1.42;color:#D5D9E0}
.emerg{display:flex;flex-direction:column;gap:.9cqw;background:linear-gradient(135deg,var(--red),#26BE4C);color:var(--ink);padding:2.8cqw 3.2cqw;margin:0 0 3cqw}
.emerg .el{color:rgba(8,9,11,.72);font-size:1.5cqw;letter-spacing:.16em;text-transform:uppercase;font-weight:700}
.emerg .enum{font-family:"Anton";font-size:6.6cqw;line-height:.9;color:var(--ink)}
.emerg .ed{font-weight:600;font-size:1.68cqw;color:rgba(8,9,11,.85)}
/* sectors */
.sectors{display:grid;grid-template-columns:1fr 1fr;gap:2.4cqw}
.sect{background:var(--panel);border:1px solid var(--line);border-top:3px solid var(--red);padding:2.6cqw 2.8cqw}
.sect h3{font-size:2.4cqw;color:var(--white);margin:0 0 1cqw;line-height:1.04}
.sect p{margin:0;font-size:1.76cqw;line-height:1.4;color:#C4C9D3}
/* projects */
.projects{display:grid;grid-template-columns:1fr 1fr;gap:2.6cqw}
.proj{background:var(--panel);border:1px solid var(--line);padding:2.6cqw 2.8cqw;display:flex;flex-direction:column;gap:1cqw}
.pjh{display:flex;justify-content:space-between;align-items:center}
.pjt{font-size:1.4cqw;color:var(--red-ink);border:1px solid var(--red-deep);border-radius:999px;padding:.5cqw 1.4cqw;letter-spacing:.14em;text-transform:uppercase;font-weight:700}
.pjd{font-size:1.5cqw;letter-spacing:.1em;color:var(--steel);font-weight:600}
.proj h3{font-family:"Anton";text-transform:uppercase;font-size:3.2cqw;color:var(--white);margin:.4cqw 0 0}
.pjl{font-size:1.7cqw;color:var(--red-ink);font-weight:600}
.proj p{margin:.4cqw 0 0;font-size:1.82cqw;line-height:1.4;color:#C4C9D3}
/* zones */
.zone+.zone{margin-top:3cqw}
.chips{display:flex;flex-wrap:wrap;gap:1.4cqw}
.chip{font-size:1.82cqw;font-weight:500;color:#DCE0E6;background:var(--panel);border:1px solid var(--line);padding:1.1cqw 1.8cqw}
.chip.mono{display:flex;flex-direction:column;gap:.3cqw;font-family:"Anton";letter-spacing:.02em;color:var(--white);font-size:2cqw}
.chip.mono i{font-family:"Mont";font-style:normal;font-weight:600;font-size:1.3cqw;color:var(--steel);text-transform:uppercase;letter-spacing:.1em}
.foot-note{margin-top:2.6cqw;font-size:1.55cqw;line-height:1.5;color:var(--steel)}
/* glossary */
.glossary{display:grid;grid-template-columns:1fr 1fr;gap:2.6cqw 4cqw}
.gitem h3{font-size:2.1cqw;color:var(--white);margin:0 0 .8cqw;line-height:1.06}
.gitem p{margin:0;font-size:1.7cqw;line-height:1.42;color:#C4C9D3}
/* faq */
.faqs{display:flex;flex-direction:column}
.faq{padding:2.4cqw 0;border-bottom:1px solid var(--line)}
.faq:first-child{padding-top:0}
.faq h3{font-size:2.5cqw;color:var(--white);margin:0 0 1cqw;display:flex;gap:1.6cqw;align-items:baseline}
.faq h3::before{content:"?";font-family:"Anton";color:var(--red);font-size:2.6cqw;line-height:.9}
.faq p{margin:0;font-size:1.92cqw;line-height:1.45;color:#C6CCD4;padding-left:4.2cqw}
/* back */
.back{padding:0;justify-content:flex-start}
.back-red{position:absolute;z-index:1;right:-20%;left:auto;top:-24%;width:66%;height:48%;background:linear-gradient(150deg,var(--fill1),var(--fill2));transform:skewX(-14deg)}
.back-red .bpwrap{right:4%;top:14%;left:auto;width:42cqw;transform:skewX(14deg)}
.back-top{display:flex;justify-content:space-between;align-items:flex-start;padding:8cqw 8cqw 0;z-index:3}
.back .docmeta{color:#F3F5F8}
.back-hero{padding:0 8cqw;margin-top:7cqw;z-index:3}
.back-hero .eyebrow{color:var(--red)}
.back .htitle.sm{font-size:11cqw;margin-top:2cqw}
.contacts{margin-top:auto;padding:0 8cqw;display:grid;grid-template-columns:1fr 1fr;column-gap:6cqw;z-index:3}
.crow{display:flex;flex-direction:column;gap:.4cqw;padding:1.5cqw 0;border-bottom:1px solid var(--line)}
.crow dt{font-size:1.4cqw;letter-spacing:.18em;text-transform:uppercase;color:var(--steel);font-weight:600}
.crow dd{margin:0;font-weight:500;font-size:1.95cqw;color:var(--white)}
.back-foot{margin-top:4cqw;padding:3cqw 8cqw;display:flex;justify-content:space-between;border-top:1px solid var(--line-strong);font-size:1.45cqw;letter-spacing:.12em;text-transform:uppercase;color:var(--steel);z-index:3}
@media(hover:hover){.sidx:hover{padding-left:2cqw}.vcard:hover,.sect:hover,.proj:hover{background:var(--panel-2)}}
@page{size:A4;margin:0}
@media print{body{background:#fff;padding:0}.stack{gap:0}.leaf{width:210mm;height:297mm;box-shadow:none;break-after:page;page-break-after:always}.leaf:last-child{break-after:auto}.crop{display:none}}
"""
FONTS=(f'@font-face{{font-family:"Anton";font-weight:400;font-display:swap;src:url(data:font/woff2;base64,{ANTON}) format("woff2")}}'
       f'@font-face{{font-family:"Mont";font-weight:300 800;font-display:swap;src:url(data:font/woff2;base64,{MONT}) format("woff2")}}')
HTML=f"""<title>KRECA — Profilo Aziendale</title>
<style>{FONTS}{CSS}</style>
<main class="stack">
{BOOK}
</main>"""
out=os.path.join(SCR,"index.html"); open(out,"w").write(HTML)
print("wrote",out,round(len(HTML)/1024),"KB ·",len(P),"pagine")
