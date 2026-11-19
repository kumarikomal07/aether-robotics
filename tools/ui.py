"""Shared layout and components for the Aether Robotics site generator."""
import json
from html import escape as esc
from data import SITE, AI_SERVICES, ROBOTICS, PRODUCTS, INDUSTRIES

# ---------------------------------------------------------------- icons (24px, stroke)
_P = {
    "brain": '<path d="M9.5 2A2.5 2.5 0 0 0 7 4.5v.3A3 3 0 0 0 4.5 8a3 3 0 0 0 .6 1.8A3 3 0 0 0 4 12.5a3 3 0 0 0 2 2.8V16a3 3 0 0 0 3 3h.5"/><path d="M14.5 2A2.5 2.5 0 0 1 17 4.5v.3A3 3 0 0 1 19.5 8a3 3 0 0 1-.6 1.8 3 3 0 0 1 1.1 2.7 3 3 0 0 1-2 2.8V16a3 3 0 0 1-3 3h-.5"/><path d="M12 2v20M9 8h1.5M13.5 8H15M8.5 13H10M14 13h1.5"/>',
    "chart": '<path d="M3 3v18h18"/><path d="m7 15 4-4 3 3 6-7"/><circle cx="20" cy="7" r="1"/>',
    "eye": '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/><path d="M12 9v.01"/>',
    "chat": '<path d="M21 12a8 8 0 0 1-11.6 7.1L3 21l1.9-6.4A8 8 0 1 1 21 12z"/><path d="M8 10h8M8 14h5"/>',
    "flow": '<rect x="3" y="3" width="6" height="6" rx="1.5"/><rect x="15" y="15" width="6" height="6" rx="1.5"/><path d="M9 6h5a3 3 0 0 1 3 3v6"/><path d="m14.5 12.5 2.5 2.5 2.5-2.5"/>',
    "flask": '<path d="M9 3h6M10 3v6L4.5 18.5A1.7 1.7 0 0 0 6 21h12a1.7 1.7 0 0 0 1.5-2.5L14 9V3"/><path d="M7 15h10"/>',
    "arm": '<path d="M4 21h8"/><path d="M6 21v-3h4v3"/><circle cx="8" cy="15" r="2"/><path d="m9.5 13.5 4-5"/><circle cx="15" cy="7" r="2"/><path d="m16.5 5.5 3-2M17 8.5l2.5 2.5M19.5 11l1.5-1"/>',
    "robot": '<rect x="5" y="8" width="14" height="11" rx="3"/><path d="M12 4v4M9 13h.01M15 13h.01M10 16.5h4M2 13v2M22 13v2"/><circle cx="12" cy="3.5" r="1"/>',
    "drone": '<circle cx="5" cy="5" r="2.5"/><circle cx="19" cy="5" r="2.5"/><circle cx="5" cy="19" r="2.5"/><circle cx="19" cy="19" r="2.5"/><rect x="9" y="9" width="6" height="6" rx="1.5"/><path d="M7 7l2 2M17 7l-2 2M7 17l2-2M17 17l-2-2"/>',
    "chip": '<rect x="5" y="5" width="14" height="14" rx="2"/><rect x="9" y="9" width="6" height="6" rx="1"/><path d="M9 2v3M15 2v3M9 19v3M15 19v3M2 9h3M2 15h3M19 9h3M19 15h3"/>',
    "factory": '<path d="M2 20V9l6 4V9l6 4V5h3l1 8h4v7z"/><path d="M6 17h2M11 17h2M16 17h2"/>',
    "health": '<path d="M9 3h6v6h6v6h-6v6H9v-6H3V9h6z"/>',
    "truck": '<path d="M1 4h14v12H1zM15 9h4l3 3v4h-7"/><circle cx="5.5" cy="18.5" r="2"/><circle cx="18.5" cy="18.5" r="2"/>',
    "building": '<rect x="4" y="2" width="16" height="20" rx="1.5"/><path d="M9 22v-4h6v4M8 6h.01M12 6h.01M16 6h.01M8 10h.01M12 10h.01M16 10h.01M8 14h.01M12 14h.01M16 14h.01"/>',
    "network": '<circle cx="12" cy="5" r="2.5"/><circle cx="5" cy="19" r="2.5"/><circle cx="19" cy="19" r="2.5"/><circle cx="12" cy="13" r="2"/><path d="M12 7.5V11M10.4 14.2 6.8 17.3M13.6 14.2l3.6 3.1M7.5 19h9"/>',
    "hand": '<path d="M18 11V6a2 2 0 0 0-4 0v5M14 10V4a2 2 0 0 0-4 0v6M10 10.5V6a2 2 0 0 0-4 0v8"/><path d="M18 8a2 2 0 1 1 4 0v6a8 8 0 0 1-8 8h-2c-2.8 0-4.5-.9-6-2.4l-3.6-3.6a2 2 0 0 1 2.8-2.8L7 15"/>',
    "spark": '<path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9z"/><path d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z"/>',
    "pulse": '<path d="M2 12h4l3-8 4 16 3-8h6"/>',
    "code": '<path d="M16 18l6-6-6-6M8 6l-6 6 6 6"/>',
    "cloud": '<path d="M17.5 19a4.5 4.5 0 0 0 .6-8.96A6 6 0 0 0 6.3 9.2 4 4 0 0 0 6.5 19z"/>',
    "layers": '<path d="M12 2 2 7l10 5 10-5-10-5z"/><path d="m2 17 10 5 10-5"/><path d="m2 12 10 5 10-5"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "arrow-l": '<path d="M19 12H5M11 6l-6 6 6 6"/>',
    "chev": '<path d="m6 9 6 6 6-6"/>',
    "chev-r": '<path d="m9 6 6 6-6 6"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "alert": '<path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/>',
    "target": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    "compass": '<circle cx="12" cy="12" r="10"/><path d="m16.2 7.8-2.1 6.3-6.3 2.1 2.1-6.3z"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
    "crosshair": '<circle cx="12" cy="12" r="9"/><path d="M12 1v5M12 18v5M1 12h5M18 12h5"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "calendar": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/>',
    "send": '<path d="m22 2-7 20-4-9-9-4z"/><path d="M22 2 11 13"/>',
    "upload": '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M17 8l-5-5-5 5M12 3v12"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "play": '<path d="m7 4 13 8-13 8z"/>',
    "zap": '<path d="M13 2 3 14h9l-1 8 10-12h-9z"/>',
    "settings": '<circle cx="12" cy="12" r="3"/><path d="M12 1v3M12 20v3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M1 12h3M20 12h3M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1"/>',
    "rocket": '<path d="M4.5 16.5c-1.5 1.3-2 5-2 5s3.7-.5 5-2c.7-.8.7-2.1-.1-2.9a2.2 2.2 0 0 0-2.9-.1z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.9A12.9 12.9 0 0 1 22 2c0 2.7-.8 7.5-6 11a22.4 22.4 0 0 1-4 2z"/><path d="M9 12H4s.6-3 2-4c1.6-1.1 5 0 5 0M12 15v5s3-.6 4-2c1.1-1.6 0-5 0-5"/>',
    "heart": '<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 21.2l8.8-8.8a5.5 5.5 0 0 0 0-7.8z"/>',
    "book": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V2H6.5A2.5 2.5 0 0 0 4 4.5z"/><path d="M4 19.5V22h16"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
    "share": '<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="m8.6 13.5 6.8 4M15.4 6.5l-6.8 4"/>',
    "lock": '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "file": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M16 13H8M16 17H8"/>',
    "briefcase": '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2M2 13h20"/>',
    "handshake": '<path d="m11 17 2 2a1 1 0 1 0 3-3"/><path d="m14 14 2.5 2.5a1 1 0 1 0 3-3l-3.9-3.9a3 3 0 0 0-4.2 0l-.9.9a1 1 0 1 1-3-3l2.8-2.8a5.8 5.8 0 0 1 7 .9L21 7.3"/><path d="m21 3 1 11h-2M3 3 2 14l6.5 6.5a1 1 0 1 0 3-3M3 4h8"/>',
    "menu": '<path d="M3 6h18M3 12h18M3 18h18"/>',
    "close": '<path d="M18 6 6 18M6 6l12 12"/>',
    "gauge": '<path d="M12 14 15.5 8.5"/><path d="M3.3 19a10 10 0 1 1 17.4 0z"/>',
    "cube": '<path d="M21 16V8l-9-5-9 5v8l9 5 9-5z"/><path d="m3.3 7 8.7 5 8.7-5M12 22V12"/>',
}
_FILL = {
    "linkedin": '<path d="M20.4 20.5h-3.6v-5.6c0-1.3 0-3-1.8-3s-2.1 1.4-2.1 2.9v5.7H9.3V9h3.4v1.6h.1c.5-.9 1.6-1.8 3.4-1.8 3.6 0 4.3 2.4 4.3 5.5zM5.3 7.4a2.1 2.1 0 1 1 0-4.2 2.1 2.1 0 0 1 0 4.2zM7.1 20.5H3.6V9h3.5zM22.2 0H1.8C.8 0 0 .8 0 1.7v20.6c0 .9.8 1.7 1.8 1.7h20.4c1 0 1.8-.8 1.8-1.7V1.7C24 .8 23.2 0 22.2 0z"/>',
    "x": '<path d="M18.2 2.3h3.4l-7.4 8.4 8.7 11.5h-6.8l-5.3-7-6.1 7H1.3l7.9-9L.9 2.3h7l4.8 6.4zm-1.2 17.9h1.9L7 4.2H5z"/>',
    "youtube": '<path d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.6 12 3.6 12 3.6s-7.5 0-9.4.5A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.5 9.4.5 9.4.5s7.5 0 9.4-.5a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8zM9.6 15.6V8.4l6.3 3.6z"/>',
    "github": '<path d="M12 .3a12 12 0 0 0-3.8 23.4c.6.1.8-.3.8-.6v-2c-3.3.7-4-1.6-4-1.6-.6-1.4-1.4-1.8-1.4-1.8-1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1 1.8 2.8 1.3 3.5 1 0-.8.4-1.3.7-1.6-2.7-.3-5.5-1.3-5.5-6 0-1.2.5-2.3 1.3-3.1-.2-.4-.6-1.6 0-3.2 0 0 1-.3 3.4 1.2a11.5 11.5 0 0 1 6 0C17.3 4.6 18.3 5 18.3 5c.7 1.6.2 2.8.1 3.2.8.8 1.3 1.9 1.3 3.1 0 4.6-2.8 5.6-5.5 5.9.5.4.9 1.1.9 2.2v3.3c0 .3.1.7.8.6A12 12 0 0 0 12 .3"/>',
    "whatsapp": '<path d="M17.5 14.4c-.3-.1-1.8-.9-2-1s-.5-.1-.7.1c-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5.3-.5c.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.1-.3-.2-.6-.3zM12 21.8c-1.8 0-3.5-.5-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 1 1 12 21.8zm8.4-18.3A11.8 11.8 0 0 0 1.7 17.7L0 24l6.4-1.7A11.8 11.8 0 0 0 23.8 12c0-3.2-1.2-6.2-3.4-8.5z"/>',
}


def icon(name, cls="ic"):
    if name in _FILL:
        return f'<svg class="{cls}" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">{_FILL[name]}</svg>'
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_P[name]}</svg>'


def logo_mark(uid="lm"):
    return (f'<svg class="logo-mark" viewBox="0 0 48 48" aria-hidden="true"><defs><linearGradient id="{uid}" x1="0" y1="1" x2="1" y2="0">'
            '<stop offset="0" stop-color="#1E6BFF"/><stop offset=".6" stop-color="#22D3EE"/><stop offset="1" stop-color="#7DF9FF"/></linearGradient></defs>'
            f'<path d="M4 42 21 6h7L11 42z" fill="url(#{uid})"/><path d="M28 6h-7l7 15 9.6 21H45z" fill="url(#{uid})" opacity=".92"/>'
            f'<path d="M14.5 34h20l-3.2-7H17.8z" fill="url(#{uid})" opacity=".7"/></svg>')


def logo(base, uid="lm"):
    return (f'<a class="logo" href="{base}index.html" aria-label="Aether Robotics home">{logo_mark(uid)}'
            '<span class="logo-text"><b>Aether</b><b>Robotics</b></span></a>')


# ---------------------------------------------------------------- images
_DIM = {"ae-humanoid": (1672, 941), "ai-abstract": (1600, 2000), "med-tech": (1600, 2000), "robot-arm-lab": (1600, 2400),
        "warehouse": (1600, 2133), "ai-chip": (1600, 900), "robot-hand": (1600, 900), "servers": (1600, 898),
        "drone": (1600, 1143), "vr-hmi": (1600, 1144), "robot-face": (1600, 1095)}


def src(name):
    return f"{name}.jpg" if name.startswith("ae-") else f"{name}.webp"


def img(base, name, alt, cls="", eager=False):
    w, h = _DIM.get(name, (1752, 897) if name.startswith("ae-") else (1600, 1067))
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    c = f' class="{cls}"' if cls else ""
    return f'<img{c} src="{base}assets/img/{src(name)}" alt="{esc(alt)}" {load} decoding="async" width="{w}" height="{h}">'


# ---------------------------------------------------------------- primitives
def btn(href, label, kind="primary", arrow=True, extra="", ic="arrow"):
    a = f'<span class="btn-ic">{icon(ic)}</span>' if arrow else ""
    return f'<a class="btn btn-{kind}" href="{href}" {extra}><span>{label}</span>{a}</a>'


def eyebrow(t, d=0):
    return f'<p class="eyebrow" data-reveal style="--d:{d}s"><i></i>{t}</p>'


def head_block(eb, title, sub="", center=False, extra=""):
    c = " center" if center else ""
    s = f'<p class="sec-sub" data-reveal style="--d:.15s">{sub}</p>' if sub else ""
    return f'<div class="sec-head{c}"><div>{eyebrow(eb)}<h2 class="sec-title" data-split>{title}</h2>{s}</div>{extra}</div>'


def demo(text="Illustrative demo concept"):
    return f'<span class="demo">{icon("alert")}{text}</span>'


def chips(items, cls="chips"):
    return f'<ul class="{cls}">' + "".join(f"<li>{t}</li>" for t in items) + "</ul>"


def checks(items, cls="checks"):
    return f'<ul class="{cls}">' + "".join(f'<li>{icon("check")}<span>{t}</span></li>' for t in items) + "</ul>"


def hud(cls=""):
    """Decorative HUD corner brackets + tick ruler (pure decoration)."""
    return (f'<div class="hud {cls}" aria-hidden="true"><span class="hc tl"></span><span class="hc tr"></span><span class="hc bl"></span><span class="hc br"></span>'
            '<span class="ruler"></span><span class="hud-dots"><i></i><i></i><i></i></span></div>')


def flag(text):
    return f'<div class="flag">{icon("alert")}<p><strong>To confirm before launch:</strong> {text}</p></div>'


def faq(items):
    return "".join(f'<details class="faq" data-reveal style="--d:{i * .05:.2f}s"><summary><span>{q}</span><i>{icon("plus")}</i></summary><div class="faq-a"><p>{a}</p></div></details>' for i, (q, a) in enumerate(items))


# ---------------------------------------------------------------- nav
ABOUT_DD = [("about.html", "About Aether", "Our story, mission and values", "compass"), ("careers.html", "Careers", "Build the future with us", "briefcase"),
            ("contact.html", "Contact", "Talk to our engineers", "mail")]


def _dd(base, items, wide=False, all_href=None, all_label=None, did="dd"):
    lis = "".join(f'<li><a href="{base}{h}"><span class="dd-ic">{icon(ic)}</span><span><strong>{n}</strong><small>{s}</small></span></a></li>' for h, n, s, ic in items)
    al = f'<a class="dd-all" href="{base}{all_href}">{all_label} {icon("arrow")}</a>' if all_href else ""
    return f'<div class="dd{" dd-wide" if wide else ""}" id="{did}"><ul>{lis}</ul>{al}</div>'


def header(base, active):
    ai = [(f"ai-solutions/{s['slug']}.html", s["name"], s["short"], s["icon"]) for s in AI_SERVICES]
    rb = [(f"robotics.html#{r['id']}", r["name"], r["text"][:64].rsplit(" ", 1)[0] + "…", r["icon"]) for r in ROBOTICS]
    pr = [(f"products/{p['slug']}.html", p["name"], p["tag"] + " · illustrative concept", p["icon"]) for p in PRODUCTS]
    menu = [
        ("index.html", "Home", None),
        ("about.html", "About", _dd(base, ABOUT_DD, did="dd-about")),
        ("ai-solutions.html", "AI Solutions", _dd(base, ai, True, "ai-solutions.html", "All AI solutions", "dd-ai")),
        ("robotics.html", "Robotics", _dd(base, rb, False, "robotics.html", "Robotics overview", "dd-rob")),
        ("products.html", "Products", _dd(base, pr, False, "products.html", "All products & platforms", "dd-prod")),
        ("industries.html", "Industries", None),
        ("research.html", "Research", None),
        ("projects.html", "Projects", None),
        ("insights.html", "Insights", None),
        ("contact.html", "Contact", None),
    ]
    items = []
    for href, label, dd in menu:
        on = active == href or (active.startswith(href.replace(".html", "/")) if href != "index.html" else False)
        cur = ' class="active" aria-current="page"' if on else ""
        if dd:
            did = dd.split('id="', 1)[1].split('"', 1)[0]
            items.append(f'<li class="has-dd"><a href="{base}{href}"{cur}>{label}</a><button class="dd-btn" type="button" aria-expanded="false" aria-controls="{did}" aria-label="Show {label} menu">{icon("chev")}</button>{dd}</li>')
        else:
            items.append(f'<li><a href="{base}{href}"{cur}>{label}</a></li>')
    return f'''<header class="site-header" data-header>
  <div class="wrap hdr">
    {logo(base, "lm-h")}
    <nav class="nav" id="nav" aria-label="Main"><ul class="nav-list">{"".join(items)}</ul>
      <div class="nav-foot">{btn(base + "ai-solutions.html", "Explore Our Technology")}<p><a href="mailto:{SITE["email"]}">{SITE["email"]}</a></p></div>
    </nav>
    <a class="btn btn-outline btn-sm hdr-cta" href="{base}ai-solutions.html"><span>Explore Our Technology</span><span class="btn-ic">{icon("arrow")}</span></a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav" aria-label="Open menu"><span></span><span></span><span></span></button>
  </div>
</header>'''


def newsletter_form(uid, label="Email address for newsletter"):
    return f'''<form class="nl-form" data-newsletter novalidate>
  <label class="sr-only" for="nl-{uid}">{label}</label>
  <input id="nl-{uid}" type="email" name="email" placeholder="Your work email" autocomplete="email" required>
  <input type="text" name="website" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
  <button type="submit" aria-label="Subscribe">{icon("send")}</button>
  <p class="form-msg" role="status" aria-live="polite"></p>
</form>'''


def footer(base):
    quick = [("about.html", "About Us"), ("industries.html", "Industries"), ("research.html", "Research & Innovation"), ("projects.html", "Projects"),
             ("insights.html", "Insights"), ("careers.html", "Careers"), ("contact.html", "Contact")]
    q = "".join(f'<li><a href="{base}{h}">{l}</a></li>' for h, l in quick)
    svc = "".join(f'<li><a href="{base}ai-solutions/{s["slug"]}.html">{s["name"]}</a></li>' for s in AI_SERVICES)
    svc += f'<li><a href="{base}robotics.html">Robotics Engineering</a></li>'
    prod = "".join(f'<li><a href="{base}products/{p["slug"]}.html">{p["name"]}</a></li>' for p in PRODUCTS)
    soc = "".join(f'<a href="#" aria-label="Aether Robotics on {n} (link to be added)" data-social>{icon(k)}</a>' for k, n in [("linkedin", "LinkedIn"), ("x", "X"), ("youtube", "YouTube"), ("github", "GitHub")])
    return f'''<footer class="site-footer">
  <div class="ft-word" aria-hidden="true"><span class="astro chroma" data-text="AETHER">AETHER</span></div>
  <div class="wrap ft-top">
    <div class="ft-brand">{logo(base, "lm-f")}<p>A Singapore-based AI and robotics engineering company, established in {SITE["founded"]}, designing intelligent systems, robotics and automation for enterprises.</p><div class="social">{soc}</div></div>
    <div class="ft-nl"><h3>Engineering notes, monthly</h3><p>AI and robotics insights from our engineers. No spam, unsubscribe any time.</p>{newsletter_form("foot")}</div>
  </div>
  <div class="wrap ft-grid">
    <div><h3>Company</h3><ul>{q}</ul></div>
    <div><h3>AI &amp; Robotics</h3><ul>{svc}</ul></div>
    <div><h3>Products <small>(illustrative)</small></h3><ul>{prod}</ul></div>
    <div><h3>Contact</h3><ul class="ft-contact">
      <li>{icon("pin")}<span>Singapore headquarters<br><em>Full address to be confirmed</em></span></li>
      <li>{icon("mail")}<a href="mailto:{SITE["email"]}">{SITE["email"]}</a></li>
      <li>{icon("handshake")}<a href="mailto:{SITE["partner_email"]}">{SITE["partner_email"]}</a></li>
      <li class="wa">{icon("whatsapp")}<a href="#" data-wa>Chat on WhatsApp</a></li></ul></div>
  </div>
  <div class="wrap ft-bottom">
    <p>&copy; <span data-year>2026</span> Aether Robotics. All rights reserved. Products, projects and figures shown are illustrative.</p>
    <ul><li><a href="{base}privacy-policy.html">Privacy Policy</a></li><li><a href="{base}terms.html">Terms &amp; Conditions</a></li><li><a href="{base}cookie-policy.html">Cookie Policy</a></li><li><a href="{base}cookie-preferences.html">Cookie Preferences</a></li></ul>
  </div>
</footer>'''


def chrome_extras(base):
    return f'''<a class="wa-float" href="#" data-wa aria-label="Chat with Aether Robotics on WhatsApp" hidden>{icon("whatsapp")}</a>
<button class="to-top" type="button" aria-label="Back to top"><svg viewBox="0 0 40 40" aria-hidden="true"><circle class="tt-track" cx="20" cy="20" r="18"/><circle class="tt-bar" cx="20" cy="20" r="18"/></svg>{icon("arrow")}</button>
<div class="cookie" role="dialog" aria-live="polite" aria-label="Cookie consent" hidden data-cookie>
  <div class="cookie-in"><div><strong>Cookies on this site</strong><p>We use essential cookies to run this website and, only with your consent, analytics cookies to understand how it is used. Read our <a href="{base}cookie-policy.html">Cookie Policy</a>.</p></div>
  <div class="cookie-btns"><a class="btn btn-ghost btn-sm" href="{base}cookie-preferences.html"><span>Preferences</span></a><button class="btn btn-ghost btn-sm" type="button" data-consent="reject"><span>Reject optional</span></button><button class="btn btn-primary btn-sm" type="button" data-consent="accept"><span>Accept all</span></button></div></div>
</div>
<script>window.AE_SITE={json.dumps({"whatsapp": SITE["whatsapp"]})};</script>
<script src="{base}js/main.js" defer></script>'''


def page(path, title, desc, body, active="", base="", schema=None, og_img="ae-humanoid"):
    url = SITE["domain"] + "/" + (path if path != "index.html" else "")
    org = {"@context": "https://schema.org", "@type": "Organization", "name": SITE["name"], "url": SITE["domain"] + "/",
           "logo": SITE["domain"] + "/assets/favicon.svg", "foundingDate": SITE["founded"], "email": SITE["email"],
           "address": {"@type": "PostalAddress", "addressLocality": "Singapore", "addressCountry": "SG"}}
    ld = [org] + ([schema] if schema else [])
    full = title if "Aether" in title else f"{title} | Aether Robotics"
    return f'''<!doctype html>
<html lang="en-SG">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#050A16">
<meta property="og:type" content="{"article" if schema and schema.get("@type") == "BlogPosting" else "website"}">
<meta property="og:site_name" content="Aether Robotics">
<meta property="og:title" content="{esc(full)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE["domain"]}/assets/img/{src(og_img)}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{base}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&amp;family=Michroma&amp;family=Outfit:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}css/styles.css">
<script>document.documentElement.classList.add("js")</script>
<script type="application/ld+json">{json.dumps(ld if len(ld) > 1 else org)}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="progress" aria-hidden="true"></div>
<div class="cursor-glow" aria-hidden="true"></div>
<div class="loader" aria-hidden="true"><span class="astro chroma" data-text="AETHER">AETHER</span><i></i></div>
{header(base, active)}
<main id="main">
{body}
</main>
{footer(base)}
{chrome_extras(base)}
</body>
</html>
'''


def page_hero(base, eb, title, sub, crumbs, image, extra="", side=""):
    """crumbs: list of (href or None, label)."""
    cr = "".join((f'<a href="{base}{h}">{l}</a>' if h else f'<span aria-current="page">{l}</span>') + ("" if i == len(crumbs) - 1 else icon("chev-r")) for i, (h, l) in enumerate(crumbs))
    return f'''<section class="phero">
  <div class="phero-bg" data-parallax=".2">{img(base, image, "", "kb", True)}</div>
  <div class="phero-shade" aria-hidden="true"></div><div class="grid-bg" aria-hidden="true"></div><canvas class="net" aria-hidden="true"></canvas>
  {hud("hud-hero")}
  <div class="wrap phero-in{" has-side" if side else ""}">
    <div class="phero-copy">
      <nav class="crumb" aria-label="Breadcrumb"><a href="{base}index.html">Home</a>{icon("chev-r")}{cr}</nav>
      {eyebrow(eb)}
      <h1 data-split>{title}</h1>
      <p class="phero-sub" data-reveal style="--d:.25s">{sub}</p>{extra}
    </div>{side}
  </div>
  <div class="scan" aria-hidden="true"></div>
</section>'''


# ---------------------------------------------------------------- cards
def service_card(base, s, i):
    return f'''<a class="svc-card" href="{base}ai-solutions/{s["slug"]}.html" data-reveal data-glow style="--d:{(i % 3) * .08:.2f}s">
  <div class="svc-media">{img(base, s["img"], "")}</div>
  <span class="ic-box">{icon(s["icon"])}</span><span class="idx">0{i + 1}</span>
  <h3>{s["name"]}</h3><p>{s["short"]}</p>
  <span class="more">Explore service {icon("arrow")}</span>
</a>'''


def product_card(base, p, i):
    return f'''<a class="prod-card" href="{base}products/{p["slug"]}.html" data-reveal data-tilt style="--d:{(i % 3) * .08:.2f}s">
  <div class="pc-media">{img(base, p["img"], p["name"] + " illustrative concept visual")}<span class="tag">{p["tag"]}</span></div>
  <div class="pc-body"><span class="ic-box sm">{icon(p["icon"])}</span><h3>{p["name"]}</h3><p>{p["short"]}</p>
  <div class="pc-foot">{demo("Illustrative concept")}<span class="circ">{icon("arrow")}</span></div></div>
</a>'''


def project_card(base, p, i):
    return f'''<a class="proj-card" href="{base}projects/{p["slug"]}.html" data-cat="{p["cat"]}" data-reveal style="--d:{(i % 3) * .08:.2f}s">
  <div class="pj-media">{img(base, p["img"], p["title"] + " illustrative case study")}<span class="tag">{p["cat"]}</span><span class="demo-dot">Illustrative case study</span></div>
  <div class="pj-body"><small>{p["industry"]}</small><h3>{p["title"]}</h3><p>{p["summary"]}</p><span class="more">View case study {icon("arrow")}</span></div>
</a>'''


def article_card(base, a, i):
    return f'''<a class="art-card" href="{base}insights/{a["slug"]}.html" data-cat="{a["cat"]}" data-reveal style="--d:{(i % 3) * .08:.2f}s">
  <div class="ac-media">{img(base, a["img"], a["title"])}<span class="tag">{a["cat"]}</span></div>
  <div class="ac-body"><div class="meta"><span>{icon("calendar")}<time datetime="{a["date"]}">{a["date_h"]}</time></span><span>{icon("clock")}{a["read"]} min read</span></div>
  <h3>{a["title"]}</h3><p>{a["summary"]}</p><span class="more">Read article {icon("arrow")}</span></div>
</a>'''


def cta_band(base, title="Ready to Build the Future", accent="With Intelligent Technology?", sub="Tell us about the problem you want to solve. Our AI and robotics engineers will help you scope a practical, safe path from idea to deployment.", label="Start a Conversation", href="contact.html#enquiry", second=None):
    s = second or btn(base + "ai-solutions.html", "Explore Solutions", "ghost")
    return f'''<section class="cta-wrap"><div class="wrap">
  <div class="cta" data-reveal="zoom">
    <div class="cta-art" aria-hidden="true">{img(base, "ae-humanoid", "")}</div>
    <div class="grid-bg" aria-hidden="true"></div>{hud()}
    <div class="cta-txt">{eyebrow("Start a project")}<h2 data-split>{title} <span class="grad">{accent}</span></h2>
    <p data-reveal style="--d:.2s">{sub}</p><div class="btn-row" data-reveal style="--d:.3s">{btn(base + href, label)}{s}</div></div>
  </div></div></section>'''
