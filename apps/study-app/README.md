# Ham Radio General Class Study App

An offline-capable PWA for studying the FCC General Class (Element 3) amateur radio exam.

## Features

- **429 questions** — the complete 2023–2027 FCC question pool
- **Flashcard mode** — flip through questions one at a time with instant answer reveal
- **Practice exam mode** — timed 35-question exams drawn randomly from the pool (passing = 26/35)
- **Progress tracking** — per-question correct/incorrect counts stored in `localStorage`
- **Weak-spot focus** — filter to questions you've gotten wrong most
- **Offline support** — service worker caches the app after first load; no internet required
- **Installable PWA** — "Add to Home Screen" on Android/iOS or install from desktop Chrome/Edge

## Usage

Open `index.html` directly in a browser — no build step, no server required. Works from the filesystem or served over HTTP/HTTPS.

For GitHub Pages, the app is available at:
`https://<user>.github.io/general-study-guide/apps/study-app/`

## Files

| File | Purpose |
|------|---------|
| `index.html` | Single-file app (HTML + CSS) |
| `app.js` | All 429 FCC Element 3 questions and app logic (JS) |
| `sw.js` | Service worker for offline caching |
| `manifest.json` | PWA manifest (name, icons, display mode) |
| `icon-192.png` | App icon (192×192) |
| `icon-512.png` | App icon (512×512) |

## Question Pool

Questions sourced from the [NCVEC 2023–2027 General pool](http://www.ncvec.org/page.php?id=364). Valid through **June 30, 2027**.
