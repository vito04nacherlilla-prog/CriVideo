# KRECA — Libricino aziendale (Profilo Aziendale)

Libricino aziendale in stile industriale per **KRECA S.r.l. — Officina Metalmeccanica**,
con i contenuti ripresi dal sito ufficiale e impaginati nella brand identity (verde `#30D158`
su nero) e nel logo ufficiale. Versione ricca, 18 pagine.

## File

- **`index.html`** — libricino completo, self-contained (font e logo incorporati). Aprilo nel
  browser per visualizzarlo o stamparlo (Ctrl/Cmd + P → A4).
- **`KRECA-Profilo-Aziendale.pdf`** — versione pronta per la stampa, 18 pagine A4.
- **`viewer.html`** — anteprima sfogliabile (doppie pagine, animazione di sfoglio, panoramica,
  zoom). Pagina web autonoma e condivisibile.
- **`KRECA-Libricino.mp4`** — video verticale 1080×1920 (~40s) che sfoglia tutte le pagine:
  formato ideale da inviare su WhatsApp.

## Struttura (18 pagine)

1. Copertina — *Un solo partner, ogni opera.*
2. Indice
3. `01` Chi siamo + dati identificativi
4. `02` La nostra storia (2019 → S.r.l. 2025)
5. `03` Perché KRECA — 6 vantaggi + numeri
6. `04` Il metodo — 4 step
7. `05–08` Aree di servizio (indice)
8. `05` Costruzioni metalliche
9. `06` Chiusure & sicurezza
10. `07` Facility & logistica
11. `08` Pronto intervento H24
12. `09` Settori serviti
13. `10` Lavori recenti (clienti)
14. `11` Zone servite (Puglia e Basilicata)
15. `12` Certificazioni & norme
16. `13` Glossario tecnico
17. `14` Domande frequenti
18. `15` Contatti

## Identità visiva

- **Colori (brand)** — verde `#30D158` (accento), nero `#08090B`, pannelli `#14161B`,
  testi `#C6CCD4` / `#8B929C`. Grandi fasce diagonali in verde profondo per mantenere leggibile
  il testo bianco.
- **Logo** — logo ufficiale KRECA (`logo-kreca.png`).
- **Type** — Anton (display) + Montserrat (testo), incorporati come woff2.
- **Motivo** — griglia tecnica, crocini di taglio, rail di sezione, cluster ingranaggio/goniometro.

## Rigenerare

- `python3 build.py` → `index.html` (legge `anton.woff2`, `mont.woff2`, `logo-kreca.png`).
- Il PDF si ottiene stampando l'HTML in A4 senza margini.
- `python3 build_viewer.py` → `viewer.html` (usa `pages_b64.py`, ricavato dagli screenshot delle pagine).
