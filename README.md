# Aether Robotics — Website Template (Project 03)

A premium, futuristic multi-page static website for **Aether Robotics**, a Singapore-based AI & robotics engineering company (est. 2020). Plain HTML/CSS/JS with no runtime dependencies; pages are generated from a single content file by a small Python build script.

```bash
npm run dev        # serve at http://localhost:8000 (python3 http.server)
npm run build      # regenerate all HTML from tools/*.py
```

> Edit content in `tools/data.py`, layout/components in `tools/ui.py`, page templates in `tools/pages_*.py`, then run `npm run build`. Do not hand-edit generated `.html` files — they are overwritten.

## Pages (40)

| Section | URL | Notes |
|---|---|---|
| Home | `index.html` | 13 sections: hero with live "system status" card, marquee, intro, core solutions, auto-playing product tabs, AI capabilities, expanding industry panels, research, process timeline, projects, tech-stack marquee, insights, CTA |
| About | `about.html` | Overview, mission/vision, 6 values, expertise, philosophy, leadership placeholder |
| AI Solutions | `ai-solutions.html` + `ai-solutions/*.html` (6) | One reusable **service detail template** |
| Robotics | `robotics.html` | 4 capability blocks (anchor links used by nav dropdown), applications, engineering process, showcase |
| Products | `products.html` + `products/*.html` (5) | One reusable **product detail template**; all labelled illustrative |
| Industries | `industries.html` | 6 industries with sticky scroll-spy sub-nav |
| Research | `research.html` | 6 research areas, labelled as proposed (not achievements) |
| Projects | `projects.html` + `projects/*.html` (7) | Category filters; one **case study template**; all fictional & labelled |
| Insights | `insights.html` + `insights/*.html` (5) | Category filters, featured article, newsletter; one **article template** |
| Careers | `careers.html` | Culture, job categories (no live vacancies shown), application form with CV upload |
| Contact | `contact.html` | Enquiry form (Full name, Business email, Company, Phone, Interested solution, Project details), FAQs |
| Legal | `privacy-policy.html`, `terms.html`, `cookie-policy.html`, `cookie-preferences.html` | Singapore PDPA-oriented drafts with yellow `[To be confirmed: …]` markers |
| 404 | `404.html` | |

Contact form deep links: `contact.html?interest=robotics#enquiry`, `?type=partnership`, `?industry=logistics`.

## Brand tokens

| Token | Value |
|---|---|
| Background | `#040914` / surface `#0A1528` |
| Cyan (primary) | `#22D3EE` / `#5EEBFF` |
| Blue / Violet | `#2F7BFF` / `#8B5CF6` |
| Chromatic red (Astro effect) | `#FF3D5A` |
| Display font | **Astro** → fallback *Michroma* (Google Fonts) |
| Headings / body | *Outfit* / *Inter* |

**Astro font:** the display face is wired via `@font-face` in `css/styles.css`. Place a licensed copy at `assets/fonts/Astro.woff2` (and/or `Astro.woff`) and it is used automatically for the wordmark, eyebrows, numbers and the red/cyan chromatic "glitch" text. Until then Michroma is shown.

## Motion & effects

Loader with chromatic wordmark · word-by-word heading reveals · blur/slide scroll reveals · parallax backgrounds and Ken Burns zoom · mouse-reactive particle network · cursor glow and card spotlight · 3D tilt · magnetic buttons · animated orbit ring, HUD rings and blueprint arm · typing status text · counters · auto-playing product tabs with progress bars · expanding industry panels · drawn process timeline · dual-direction logo marquees · scroll progress ring. All motion respects `prefers-reduced-motion`.

## Go-live checklist

- [ ] Add licensed Astro font files to `assets/fonts/`
- [ ] Confirm domain, emails and add WhatsApp number in `tools/data.py` (`SITE`), then rebuild — WhatsApp buttons stay hidden while the number is empty
- [ ] Confirm HQ street address; replace the map placeholder on `contact.html` with a map embed
- [ ] Set form/newsletter endpoints and GA4 ID in the `CONFIG` block at the top of `js/main.js`
- [ ] Complete every `[To be confirmed: …]` in legal pages (entity name, UEN, DPO, providers, retention) and have them reviewed by Singapore counsel
- [ ] Add leadership profiles (About) and real vacancies (Careers) only when available
- [ ] Replace social `#` links in `tools/ui.py` footer
- [ ] Keep illustrative labels on products, case studies, statistics and research unless they become real and verifiable
- [ ] Update `sitemap.xml` domain (generated from `SITE["domain"]`)

## Content rules followed

No invented clients, awards, patents, certifications, partnerships or commercial results. Products are labelled *illustrative demo concepts*, case studies *fictional/illustrative*, home statistics *illustrative portfolio figures*, and research topics *proposed research areas*.
