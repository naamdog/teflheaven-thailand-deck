# /images/

Drop your ChatGPT Image 2.0 outputs here. Filenames must match the `filename` column in `../image-prompts.csv` exactly.

## What goes where

| Slide | Filename | Notes |
|-------|----------|-------|
| 01 — Cover | `01-cover-bangkok-wat-arun.jpg` | Full-bleed hero (16:9) |
| 03 — Founder | `03-mike-portrait.jpg` | Portrait of Mike (3:4 portrait) |
| 05 — Why Thailand | `05-night-market.jpg` | Photo (3:2) |
| 06a — Day in Life | `06a-tuktuk.jpg` | Photo (16:9) |
| 06b — Day in Life | `06b-beach.jpg` | Photo (1:1) |
| 06c — Day in Life | `06c-rooftop.jpg` | Photo (1:1) |
| 09 — Orientation Week | `09-orientation-temple.jpg` | Photo (4:5 portrait) |
| 10 — TESOL Course | `10-tesol-classroom.jpg` | Photo (4:5 portrait) |
| 11 — Accreditation | `11a-tquk.png`, `11b-trinity.png`, `11c-ofqual.png` | Real logos preferred over generation |
| 17 — Map | `17-map-illustration.png` | Hand-drawn map illustration (4:3) |
| 18 — Schools | `18a-school-government.jpg`, `18b-school-private.jpg` | Photos (16:10) |
| 20 — Accommodation | `20a-huahin-accom.jpg`, `20b-bangkok-apt.jpg` | Photos (16:10) |
| 30 — Team | `30a-mike.jpg`, `30b-team-2.jpg`, `30c-team-3.jpg`, `30d-team-4.jpg` | Square portraits (1:1) for circular crop |
| 31 — Testimonials | `31a-teacher-A.jpg`, `31b-teacher-B.jpg`, `31c-teacher-C.jpg` | Square portraits (1:1) |
| 43 — Apply | `43-island-sunset.jpg` | Full-bleed sunset (16:9) |
| 43 — Apply | `43-qr.png` | Generate real QR for `teflheaven.com/apply` |

## File format

- **Photos** → `.jpg`, sRGB color profile, quality 85
- **Illustrations & logos** → `.png` with transparency
- **Target resolution** → 2560×1440 for full-bleed; 1600×1200 for cards; 1024×1024 for portraits

## Generation

Use `../image-prompts.csv` as the source. Each row has the exact prompt to feed gpt-image-2 (or whatever pipeline you've set up via Cowork + Runway). The `filename` column is the exact name to save to.
