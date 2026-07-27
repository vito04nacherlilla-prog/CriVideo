# KRECA — Libricino aziendale (Profilo Aziendale)

Libricino aziendale in stile industriale per **KRECA S.r.l. — Officina Metalmeccanica**,
realizzato a partire dai contenuti del profilo aziendale e ispirato allo stile della
brochure di riferimento (rosso / grafite), portato a un livello superiore.

## File

- **`index.html`** — libricino completo, self-contained (font incorporati, nessuna
  risorsa esterna). Aprilo nel browser per visualizzarlo o stamparlo (Ctrl/Cmd + P → A4).
- **`KRECA-Profilo-Aziendale.pdf`** — versione pronta per la stampa, 11 pagine A4.

## Struttura (11 pagine)

1. Copertina — *Officina Metalmeccanica*
2. `SEZ 01` L'azienda + dati identificativi
3. `SEZ 02` Perché scegliere KRECA — 6 vantaggi
4. `SEZ 03` Aree di servizio (indice)
5. `3.1` Costruzioni metalliche in ferro
6. `3.2` Serramenti e infissi
7. `3.3` Chiusure e sicurezza
8. `3.4` Manutenzione tecnica
9. `3.5` Pronto intervento
10. `SEZ 04·05` Modalità di collaborazione + qualifiche
11. Contatti (retro)

## Identità visiva

- **Colori** — grafite `#0C0D10`, rosso segnale `#DA2128`, acciaio `#A6AEBB`.
- **Type** — Anton (display condensato) + Montserrat (testo), incorporati come woff2.
- **Motivo** — griglia tecnica "blueprint", crocini di taglio, rail di sezione,
  cluster ingranaggio/goniometro sulle fasce rosse.

## Rigenerare

I contenuti e lo stile sono assemblati da `build.py` (nella cartella di lavoro della
sessione). Per rigenerare `index.html` basta rieseguire lo script; il PDF si ottiene
stampando l'HTML in formato A4 senza margini.
