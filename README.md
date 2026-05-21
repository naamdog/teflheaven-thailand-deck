# Teach Thailand — TEFL Heaven Programme Brochure

A 44-slide scroll-snap web brochure for **Teach Thailand by TEFL Heaven**, deployed at:

> 🔗 `https://teflheaven-thailand-deck.vercel.app/` *(set after deploy)*

Built with vanilla HTML + Tailwind via CDN + Google Fonts (Playfair Display, DM Sans, DM Mono). No build step. Drop `index.html` anywhere and it works.

---

## What's in here

```
teflheaven-thailand-deck/
├── index.html           ← the whole brochure (44 slides)
├── images/              ← drop your gpt-image-2 outputs here
├── image-prompts.csv    ← prompts for each image slot
├── vercel.json
├── README.md
└── .gitignore
```

---

## How the image slots work

Every image slot in the brochure is a `<div class="img-slot img-real" data-slot="FILENAME.jpg" style="background-image: url('images/FILENAME.jpg');">`.

- **When the file doesn't exist** → a clean grey-checker placeholder shows with the filename + a description of what image goes there.
- **When you drop the file into `/images/`** → the placeholder disappears and the real image appears.

### To add an image
1. Generate it from `image-prompts.csv` using ChatGPT Image 2.0
2. Save it as the exact filename in the `filename` column (e.g. `01-cover-bangkok-wat-arun.jpg`)
3. Drop it into the `/images/` folder
4. Push to git → Vercel auto-redeploys

That's it. No code changes needed.

---

## Persuasion architecture

This brochure was deliberately structured around three frameworks:

**Cialdini's 7 Principles** — Reciprocity, Commitment, Social Proof, Authority, Liking, Scarcity, Unity. Each section primarily activates one or two.

**Blair Warren's One-Sentence Persuasion** — *"People will do anything for those who encourage their dreams, justify their failures, allay their fears, confirm their suspicions, and help them throw rocks at their enemies."* All five levers are threaded through the deck.

**Russell Brunson's Attractive Character** — Mike Maitland is the founder character. His backstory (Koh Tao lanterns), parables ("feel the fear"), character flaws (didn't plan to stay, didn't build it for the business), and polarity ("not a holiday", "not a $19 weekend cert") run through the spine.

### Section map

| Section | Slides | Primary lever |
|---------|--------|---------------|
| **The Invitation** | 1–3 | Liking, dreams encouraged |
| **Part One — Why Thailand** | 4–6 | Dreams, parables |
| **Part Two — What's Included** | 7–15 | Reciprocity, Authority |
| **Part Three — Your Job & Life** | 16–22 | Authority, Unity |
| **Part Four — Are You Eligible?** | 23–27 | Commitment, allay fears, polarity |
| **Part Five — Why TEFL Heaven** | 28–34 | Social Proof, Authority, Unity, throwing rocks at enemies |
| **Part Six — The Numbers** | 35–39 | Scarcity, Commitment |
| **Part Seven — Your Next Step** | 40–44 | Commitment, Scarcity, CTA |

---

## Deploying

### Vercel (recommended)

```bash
# from this folder
npx vercel
# then for production
npx vercel --prod
```

Or connect via the Vercel dashboard → New Project → Import from GitHub.

### GitHub Pages (alternative)

Push to a repo, enable Pages on the `main` branch, root folder.

---

## Editing copy

All copy lives in `index.html`. Search for the slide ID (e.g. `s05`) to find that slide. The site uses Tailwind utility classes; brand colors are defined in the `tailwind.config` block at the top.

### Brand tokens

```css
ink   / brand-dark : #1a1a2e   (primary "blue" text)
amber              : #e8a020   (single accent color)
paper              : #ffffff   (clean white)
soft               : #f5f5f5   (card background)
```

### Fonts

```css
display : Playfair Display
sans    : DM Sans
mono    : DM Mono
```

---

## Navigation

- **Scroll** — smooth scroll-snap, one slide at a time
- **Arrow keys / Space / PageDown** — next slide
- **PageUp / Arrow Up / Arrow Left** — previous slide
- **Dot nav** — click any dot (right edge) to jump
- **Counter** — top-right shows `NN / 44`

---

## Print to PDF

`Cmd/Ctrl + P` → Save as PDF. Each slide becomes one landscape page (16:9 — set at `297mm × 167mm`).

---

## Credits

- Photography & branding: sourced from `teflheaven.com`
- Programme content: TEFL Heaven (Xplore Asia partner)
- Brochure design & build: this repo
- Image generation: ChatGPT Image 2.0 (`gpt-image-2`) via Runway API
