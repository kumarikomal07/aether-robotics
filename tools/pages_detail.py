"""Reusable detail-page templates: service, product, case study, article."""
from html import escape as esc
from ui import (page, page_hero, img, icon, btn, eyebrow, head_block, demo, hud, chips, checks,
                service_card, product_card, project_card, article_card, cta_band, newsletter_form)
from data import SITE, AI_SERVICES, PRODUCTS, PROJECTS, ARTICLES

B = "../"


def _pager(items, cur, key, title_key, folder):
    i = [x[key] for x in items].index(cur[key])
    p, n = items[i - 1], items[(i + 1) % len(items)]
    return f'''<nav class="pager wrap" aria-label="More {folder}">
  <a href="{p[key]}.html" class="glass"><small>{icon("arrow-l")} Previous</small><b>{p[title_key]}</b></a>
  <a href="{n[key]}.html" class="glass nx"><small>Next {icon("arrow")}</small><b>{n[title_key]}</b></a></nav>'''


def service(s):
    tech = "".join(f'<li data-reveal style="--d:{i * .04:.2f}s"><span>{t}</span></li>' for i, t in enumerate(s["tech"]))
    ben = "".join(f'<li class="ben glass" data-reveal data-glow style="--d:{i * .07:.2f}s"><span class="astro">0{i + 1}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(s["benefits"]))
    others = "".join(service_card(B, x, i) for i, x in enumerate([x for x in AI_SERVICES if x["slug"] != s["slug"]][:3]))
    side = f'<div class="phero-side glass" data-reveal="right" style="--d:.4s">{hud()}<p class="panel-h"><span class="dot"></span>Service snapshot</p><ul><li><small>Capabilities</small><b>{len(s["capabilities"])}</b></li><li><small>Core technologies</small><b>{len(s["tech"])}</b></li><li><small>Example use cases</small><b>{len(s["usecases"])}</b></li></ul></div>'
    body = page_hero(B, "AI Solutions", s["name"], s["short"], [("ai-solutions.html", "AI Solutions"), (None, s["name"])], s["img"],
                     f'<div class="btn-row" data-reveal style="--d:.35s">{btn(B + "contact.html?interest=ai#enquiry", "Discuss an AI Project")}</div>', side) + f'''
<section class="sec">
  <div class="wrap split-2">
    <div class="about-media" data-reveal="left"><div class="frame">{img(B, s["img"], s["name"] + " visual")}</div>{hud()}</div>
    <div>{eyebrow("Overview &amp; purpose")}<h2 class="sec-title" data-split>What this service <span class="grad">delivers.</span></h2><p class="lead" data-reveal>{s["overview"]}</p>
      <h3 class="mini-h" data-reveal>Business problems it addresses</h3>{checks(s["problems"], "checks warn")}</div>
  </div>
</section>
<section class="sec">
  <div class="wrap">{head_block("Key capabilities", "Capabilities &amp; <span class='grad'>applications.</span>")}
  <ol class="cap-grid">{"".join(f'<li data-reveal data-glow style="--d:{(i % 3) * .07:.2f}s"><span class="astro">0{i + 1}</span><p>{c}</p></li>' for i, c in enumerate(s["capabilities"]))}</ol></div>
</section>
<section class="sec">
  <div class="wrap split-2 top">
    <div>{eyebrow("Technologies involved")}<h2 class="sec-title" data-split>Built on <span class="grad">proven tools.</span></h2><ul class="tech-chips">{tech}</ul></div>
    <div class="glass pad" data-reveal>{hud()}<p class="panel-h"><span class="dot"></span>Potential use cases</p>{checks(s["usecases"])}<p class="small-note">{icon("alert")} Example scenarios for illustration.</p></div>
  </div>
</section>
<section class="sec"><div class="wrap">{head_block("Benefits", "Why it <span class='grad'>matters.</span>", "", True)}<ul class="grid-4 bens">{ben}</ul></div></section>
<section class="sec"><div class="wrap">{head_block("Related services", "Explore other <span class='grad'>AI services.</span>")}<div class="grid-3">{others}</div></div></section>
{_pager(AI_SERVICES, s, "slug", "name", "services")}''' + cta_band(B, "Discuss an", "AI Project", label="Discuss an AI Project", href="contact.html?interest=ai#enquiry")
    schema = {"@context": "https://schema.org", "@type": "Service", "name": s["name"], "description": s["short"], "provider": {"@type": "Organization", "name": SITE["name"]}, "areaServed": "SG"}
    return page(f"ai-solutions/{s['slug']}.html", s["name"], s["overview"][:155], body, f"ai-solutions/{s['slug']}.html", B, schema, s["img"])


def product(p):
    feats = "".join(f'<li class="feat glass" data-reveal data-glow style="--d:{(i % 3) * .07:.2f}s"><span class="ic-box sm">{icon("check")}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(p["features"]))
    apps = "".join(f'<li data-reveal style="--d:{i * .06:.2f}s"><span class="astro">0{i + 1}</span>{a}</li>' for i, a in enumerate(p["applications"]))
    others = "".join(product_card(B, x, i) for i, x in enumerate([x for x in PRODUCTS if x["slug"] != p["slug"]][:3]))
    body = page_hero(B, p["tag"], p["name"], p["short"], [("products.html", "Products"), (None, p["name"])], p["img"],
                     f'<div data-reveal style="--d:.3s">{demo("Illustrative demo concept, not a commercially verified product")}</div><div class="btn-row" data-reveal style="--d:.4s">{btn("#features", "Explore Features")}{btn(B + "contact.html?interest=products#enquiry", "Talk to Us", "ghost")}</div>') + f'''
<section class="sec">
  <div class="wrap split-2">
    <div class="prod-stage" data-reveal="left" data-tilt><div class="frame">{img(B, p["img"], p["name"] + " illustrative product visual")}</div><span class="ps-label glass">{icon(p["icon"])}{p["name"]}</span>{hud()}</div>
    <div>{eyebrow("Product introduction")}<h2 class="sec-title" data-split>Meet <span class="grad">{p["name"]}.</span></h2><p class="lead" data-reveal>{p["intro"]}</p>
      <h3 class="mini-h" data-reveal>Purpose &amp; functionality</h3><p data-reveal>{p["purpose"]}</p></div>
  </div>
</section>
<section class="sec" id="features"><div class="wrap">{head_block("Key features", "What it is <span class='grad'>designed to do.</span>")}<ul class="grid-3 feats">{feats}</ul></div></section>
<section class="sec caps">
  <div class="caps-bg" data-parallax=".15">{img(B, "ae-wave", "")}</div><div class="caps-shade" aria-hidden="true"></div>
  <div class="wrap split-2 caps-in"><div>{eyebrow("Applications &amp; use cases")}<h2 class="sec-title" data-split>Where it <span class="grad">fits.</span></h2><p class="sec-sub" data-reveal>Example applications for the concept. Any real deployment would be scoped and validated with you.</p></div>
  <ol class="app-list glass">{apps}</ol></div>
</section>
<section class="sec"><div class="wrap">{head_block("More platforms", "Other illustrative <span class='grad'>products.</span>")}<div class="grid-3">{others}</div></div></section>
{_pager(PRODUCTS, p, "slug", "name", "products")}''' + cta_band(B, "Explore", f"{p['name']} for your team", label="Explore Product", href="contact.html?interest=products#enquiry")
    return page(f"products/{p['slug']}.html", f"{p['name']} (Illustrative Concept)", p["intro"][:155], body, f"products/{p['slug']}.html", B, None, p["img"])


def case(c):
    ap = "".join(f'<li class="step" style="--i:{i}"><span class="step-n astro">0{i + 1}</span><p>{a}</p></li>' for i, a in enumerate(c["approach"]))
    others = "".join(project_card(B, x, i) for i, x in enumerate([x for x in PROJECTS if x["slug"] != c["slug"]][:3]))
    facts = f'<ul class="facts glass" data-reveal>{hud()}<li><small>Category</small><b>{c["cat"]}</b></li><li><small>Sector</small><b>{c["industry"]}</b></li><li><small>Type</small><b>Illustrative case study</b></li><li><small>Stack</small><b>{", ".join(c["tech"][:3])}</b></li></ul>'
    body = page_hero(B, f"Case study · {c['cat']}", c["title"], c["summary"], [("projects.html", "Projects"), (None, c["title"])], c["img"],
                     f'<div data-reveal style="--d:.35s">{demo("Fictional, illustrative case study: not a real client or result")}</div>') + f'''
<section class="sec"><div class="wrap">{facts}</div></section>
<section class="sec">
  <div class="wrap split-2 top">
    <div><div class="frame" data-reveal="left">{img(B, c["img"], c["title"] + " demonstration")}</div></div>
    <div class="case-text">
      <div data-reveal>{eyebrow("Background")}<p class="lead">{c["background"]}</p></div>
      <div data-reveal>{eyebrow("The challenge")}<p>{c["challenge"]}</p></div>
      <div data-reveal>{eyebrow("Proposed solution")}<p>{c["solution"]}</p></div>
      <div data-reveal>{eyebrow("Technologies used")}{chips(c["tech"])}</div>
    </div>
  </div>
</section>
<section class="sec process"><div class="wrap">{head_block("Implementation approach", "How it would be <span class='grad'>delivered.</span>", "", True)}<ol class="steps" data-process><span class="steps-line" aria-hidden="true"><i></i></span>{ap}</ol></div></section>
<section class="sec">
  <div class="wrap split-2 top">
    <div class="glass pad" data-reveal>{hud()}<p class="panel-h"><span class="dot"></span>Intended outcomes <small>qualitative, illustrative</small></p>{checks(c["outcomes"])}</div>
    <div class="glass pad" data-reveal style="--d:.1s">{hud()}<p class="panel-h"><span class="dot"></span>Learnings</p><p class="lead">{c["learnings"]}</p></div>
  </div>
</section>
<section class="sec"><div class="wrap">{head_block("More case studies", "Other illustrative <span class='grad'>projects.</span>")}<div class="grid-3">{others}</div></div></section>
{_pager(PROJECTS, c, "slug", "title", "projects")}''' + cta_band(B, "Start Your", "Project", label="Start Your Project", href="contact.html?type=project#enquiry")
    return page(f"projects/{c['slug']}.html", f"{c['title']} (Illustrative Case Study)", c["summary"], body, f"projects/{c['slug']}.html", B, None, c["img"])


def article(a):
    url = f"{SITE['domain']}/insights/{a['slug']}.html"
    rel = "".join(article_card(B, x, i) for i, x in enumerate([x for x in ARTICLES if x["slug"] != a["slug"]][:3]))
    hero = f'''<section class="phero art-hero">
  <div class="phero-bg" data-parallax=".2">{img(B, a["img"], "", "kb", True)}</div><div class="phero-shade" aria-hidden="true"></div><div class="grid-bg" aria-hidden="true"></div>
  <div class="wrap phero-in narrow">
    <nav class="crumb" aria-label="Breadcrumb"><a href="{B}index.html">Home</a>{icon("chev-r")}<a href="{B}insights.html">Insights</a>{icon("chev-r")}<span aria-current="page">{a["cat"]}</span></nav>
    <span class="tag" data-reveal>{a["cat"]}</span><h1 data-split>{a["title"]}</h1>
    <div class="meta" data-reveal style="--d:.2s"><span>{icon("users")}Aether Robotics Engineering Team</span><span>{icon("calendar")}<time datetime="{a["date"]}">{a["date_h"]}</time></span><span>{icon("clock")}{a["read"]} min read</span></div>
  </div><div class="scan" aria-hidden="true"></div>
</section>'''
    share = f'''<div class="share"><span>Share</span>
  <a href="https://www.linkedin.com/sharing/share-offsite/?url={url}" target="_blank" rel="noopener" aria-label="Share on LinkedIn">{icon("linkedin")}</a>
  <a href="https://twitter.com/intent/tweet?url={url}&amp;text={esc(a["title"])}" target="_blank" rel="noopener" aria-label="Share on X">{icon("x")}</a>
  <button type="button" data-copy="{url}" aria-label="Copy link">{icon("share")}</button></div>'''
    body = hero + f'''
<section class="sec art-sec"><div class="wrap art-layout">
  <article class="prose" data-reveal>{a["body"]}{share}</article>
  <aside class="art-side"><div class="glass pad">{hud()}<p class="panel-h"><span class="dot"></span>Newsletter</p><p>Monthly engineering notes on AI and robotics.</p>{newsletter_form("art")}</div>
  <div class="glass pad"><p class="panel-h"><span class="dot"></span>Need help?</p><p>Talk to our engineers about applying these ideas.</p>{btn(B + "contact.html#enquiry", "Contact Us")}</div></aside>
</div></section>
<section class="sec"><div class="wrap">{head_block("Keep reading", "Related <span class='grad'>articles.</span>")}<div class="grid-3">{rel}</div></div></section>'''
    schema = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": a["title"], "datePublished": a["date"], "description": a["summary"],
              "image": f"{SITE['domain']}/assets/img/{a['img']}", "author": {"@type": "Organization", "name": SITE["name"]}, "mainEntityOfPage": url}
    return page(f"insights/{a['slug']}.html", a["title"], a["summary"], body, f"insights/{a['slug']}.html", B, schema, a["img"])
