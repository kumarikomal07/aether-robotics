"""Home page for Aether Robotics."""
from ui import (page, img, icon, btn, eyebrow, head_block, demo, hud, chips, checks,
                product_card, project_card, article_card, cta_band, logo_mark)
from data import AI_SERVICES, PRODUCTS, HOME_INDUSTRIES, PROJECTS, ARTICLES, TECH, RESEARCH

B = ""


def _hero():
    stats = [("5", "Illustrative Products", "cube"), ("7", "Illustrative Case Studies", "layers"),
             ("6", "AI Service Areas", "chip"), ("6", "Industries Explored", "users")]
    st = "".join(f'<li data-reveal style="--d:{.55 + i * .08:.2f}s">{icon(ic)}<div><b data-count="{n}">{n}</b><span>{l}</span></div></li>' for i, (n, l, ic) in enumerate(stats))
    quick = [("ai-solutions.html", "AI Solutions", "Custom AI systems, machine learning, vision and language.", "chip", "ae-wave"),
             ("robotics.html", "Robotics", "Robotic systems, autonomous solutions and process automation.", "arm", "ae-arm-close"),
             ("products.html", "Products &amp; Platforms", "Aether AI Core, RoboAssist, VisionX and more.", "layers", "ae-cubes"),
             ("industries.html", "Industries", "Practical applications across key enterprise sectors.", "factory", "ae-hq")]
    qc = "".join(f'''<a class="q-card" href="{h}" data-reveal data-glow style="--d:{.2 + i * .08:.2f}s">
  <div class="q-media">{img(B, im, "")}</div><span class="q-ic">{icon(ic)}</span>
  <h3>{t} {icon("arrow")}</h3><p>{s}</p></a>''' for i, (h, t, s, ic, im) in enumerate(quick))
    return f'''<section class="hero" data-hero>
  <div class="hero-bg" data-scene>
    <div class="hero-img" data-parallax=".12">{img(B, "ae-humanoid", "White humanoid robot with glowing cyan visor representing Aether Robotics", "", True)}</div>
    <svg class="orbit" viewBox="0 0 800 300" aria-hidden="true"><ellipse cx="400" cy="150" rx="390" ry="120"/><ellipse class="o2" cx="400" cy="150" rx="330" ry="96"/><circle class="o-dot" r="5"><animateMotion dur="9s" repeatCount="indefinite" path="M10,150 a390,120 0 1,0 780,0 a390,120 0 1,0 -780,0"/></circle></svg>
  </div>
  <div class="hero-shade" aria-hidden="true"></div><div class="grid-bg" aria-hidden="true"></div><canvas class="net" aria-hidden="true"></canvas>
  <div class="hud-rings" aria-hidden="true"><svg viewBox="0 0 200 200"><circle cx="100" cy="100" r="90" class="r1"/><circle cx="100" cy="100" r="70" class="r2"/><circle cx="100" cy="100" r="50" class="r3"/><circle cx="100" cy="100" r="22" class="r4"/></svg></div>
  <div class="hero-vert" aria-hidden="true"><span>2</span><span>0</span><span>2</span><span>0</span><em>SG</em></div>
  {hud("hud-hero")}
  <div class="wrap hero-in">
    <div class="hero-copy">
      {eyebrow("AI &middot; Robotics &middot; Intelligent Automation")}
      <h1 class="hero-title" data-split>Engineering Intelligence. <span class="grad">Empowering Tomorrow.</span></h1>
      <p class="hero-sub" data-reveal style="--d:.35s">We design AI systems, robotics and intelligent automation that help enterprises work smarter, safer and more efficiently, engineered in Singapore since 2020.</p>
      <div class="btn-row" data-reveal style="--d:.45s">{btn("ai-solutions.html", "Explore Solutions")}{btn("contact.html#enquiry", "Contact Us", "ghost", ic="chev-r")}</div>
    </div>
    <aside class="status-card" data-reveal="right" style="--d:.6s" aria-label="Illustrative system status interface">
      <div class="sc-l"><p class="sc-h">System Status</p><p class="sc-ok"><i></i><span data-typer="Operational|Vision model online|Fleet synced|Learning…">Operational</span></p>
        <svg class="sc-wave" viewBox="0 0 200 60" preserveAspectRatio="none" aria-hidden="true"><path d="M0 40 Q 25 5 50 30 T 100 30 T 150 30 T 200 22"/><path class="w2" d="M0 40 Q 25 5 50 30 T 100 30 T 150 30 T 200 22 V60 H0z"/></svg></div>
      <div class="sc-r" aria-hidden="true"><svg viewBox="0 0 120 80"><g class="bp"><path d="M10 74h100M18 74v-8h22v8M29 66V48l22-26 26 14 18 26v12"/><circle cx="29" cy="48" r="5"/><circle cx="51" cy="22" r="6"/><circle cx="77" cy="36" r="5"/><circle cx="95" cy="62" r="4"/></g></svg></div>
      <small>Illustrative interface</small>
    </aside>
    <ul class="hero-stats">{st}</ul>
    <p class="note-ill" data-reveal style="--d:.9s">{icon("alert")} Figures describe this website&#8217;s illustrative portfolio, not commercial results.</p>
  </div>
  <div class="wrap q-grid">{qc}</div>
  <a class="scroll-cue" href="#intro" aria-label="Scroll to introduction"><span></span></a>
</section>'''


def _marquee():
    words = ["Artificial Intelligence", "Robotics Engineering", "Computer Vision", "Machine Learning", "Autonomous Systems", "Intelligent Automation", "Human-Machine Interaction"]
    row = "".join(f"<span>{w}</span><i>{logo_mark('mq')}</i>" for w in words)
    return f'<div class="marquee" aria-hidden="true"><div class="mq-track">{row}{row}</div></div>'


def _intro():
    return f'''<section class="sec intro" id="intro">
  <div class="wrap split-2">
    <div class="intro-media" data-reveal="left">
      <div class="frame" data-parallax=".06">{img(B, "ae-hq", "Aether Robotics headquarters building in Singapore at dusk")}</div>
      <div class="float-badge" data-reveal style="--d:.3s"><b class="astro">2020</b><span>Established in<br>Singapore</span></div>
      {hud()}
    </div>
    <div class="intro-copy">
      {eyebrow("Who we are")}
      <h2 class="sec-title" data-split>An engineering company built for the <span class="grad">intelligent era.</span></h2>
      <p class="lead" data-reveal style="--d:.15s">Aether Robotics brings together AI engineers, robotics specialists and software developers to build systems that perceive, decide and act in the real world.</p>
      <p data-reveal style="--d:.22s">From machine learning models that predict equipment issues to collaborative robots that support operators on the line, we take ideas from feasibility to dependable deployment, with safety, transparency and measurable value designed in from day one.</p>
      <ul class="pill-list" data-reveal style="--d:.3s"><li>{icon("brain")}AI Development</li><li>{icon("arm")}Robotics Engineering</li><li>{icon("flow")}Intelligent Automation</li><li>{icon("shield")}Ethical Technology</li></ul>
      <div class="btn-row" data-reveal style="--d:.38s">{btn("about.html", "About Aether", "ghost")}</div>
    </div>
  </div>
</section>'''


def _core():
    core = [("AI Development", "brain", "Custom AI systems that turn data into decisions and automate expert tasks.", "ai-solutions/ai-development.html", "ae-cubes"),
            ("Machine Learning", "chart", "Predictive models for forecasting, anomaly detection and optimisation.", "ai-solutions/machine-learning.html", "ae-wave"),
            ("Robotics Engineering", "arm", "Industrial arms, collaborative robots and autonomous mobile systems.", "robotics.html", "ae-arm-weld"),
            ("Intelligent Automation", "flow", "End-to-end process automation with people kept in the loop.", "ai-solutions/process-automation.html", "ae-status")]
    cards = "".join(f'''<a class="core-card" href="{h}" data-reveal data-glow style="--d:{i * .08:.2f}s">
  <div class="cc-media">{img(B, im, "")}</div><span class="idx astro">0{i + 1}</span>
  <span class="ic-box">{icon(ic)}</span><h3>{t}</h3><p>{s}</p><span class="more">Learn more {icon("arrow")}</span></a>''' for i, (t, ic, s, h, im) in enumerate(core))
    return f'''<section class="sec core">
  <div class="wrap">{head_block("Core solutions", "Four disciplines. <span class='grad'>One integrated team.</span>", "Our engineers combine software intelligence with physical robotics, so systems work end to end rather than in isolated pilots.", extra=btn("ai-solutions.html", "All Solutions", "ghost"))}
  <div class="core-grid">{cards}</div></div>
</section>'''


def _products():
    tabs = "".join(f'<button class="pt-tab{" on" if i == 0 else ""}" type="button" role="tab" aria-selected="{"true" if i == 0 else "false"}" aria-controls="pp-{p["slug"]}" id="pt-{p["slug"]}" data-tab="{i}"><span class="ic-box sm">{icon(p["icon"])}</span><span><strong>{p["name"]}</strong><small>{p["tag"]}</small></span><i class="bar"></i></button>' for i, p in enumerate(PRODUCTS))
    panes = "".join(f'''<div class="pt-pane{" on" if i == 0 else ""}" role="tabpanel" id="pp-{p["slug"]}" aria-labelledby="pt-{p["slug"]}" {"" if i == 0 else "hidden"}>
  <div class="pt-img">{img(B, p["img"], p["name"] + " illustrative visual")}</div>
  <div class="pt-info">{demo()}<h3>{p["name"]}</h3><p>{p["short"]}</p>{checks([f[0] for f in p["features"][:4]])}{btn("products/" + p["slug"] + ".html", "Explore Product")}</div>
</div>''' for i, p in enumerate(PRODUCTS))
    return f'''<section class="sec products">
  <div class="glow-orb o1" aria-hidden="true"></div>
  <div class="wrap">{head_block("Featured products", "Platforms for an <span class='grad'>intelligent enterprise.</span>", "Five illustrative product concepts that show how our AI and robotics capabilities can be packaged into reusable platforms.", extra=btn("products.html", "View All Products", "ghost"))}
  <div class="ptabs" data-tabs data-autoplay="6500"><div class="pt-list" role="tablist" aria-label="Products">{tabs}</div><div class="pt-stage">{panes}{hud()}</div></div>
  <p class="note-ill center">{icon("alert")} All five products are illustrative demo concepts, not commercially released or verified products.</p></div>
</section>'''


def _capabilities():
    caps = [("Predictive Analytics", "chart", "Forecast demand, failures and performance from historical and live data.", 92),
            ("Computer Vision", "eye", "Detect, inspect and measure objects in images and video streams.", 88),
            ("Natural Language Processing", "chat", "Understand, search and summarise documents, tickets and speech.", 84),
            ("Intelligent Systems", "network", "Combine models, rules and robotics into systems that act autonomously.", 90)]
    rows = "".join(f'''<li class="cap" data-reveal style="--d:{i * .1:.2f}s"><span class="ic-box sm">{icon(ic)}</span><div><h3>{t}</h3><p>{s}</p>
  <div class="meter" aria-hidden="true"><i style="--v:{v}%"></i></div></div></li>''' for i, (t, ic, s, v) in enumerate(caps))
    return f'''<section class="sec caps">
  <div class="caps-bg" data-parallax=".15">{img(B, "ae-wave", "")}</div><div class="caps-shade" aria-hidden="true"></div>
  <div class="wrap split-2 caps-in">
    <div>{eyebrow("AI capabilities")}<h2 class="sec-title" data-split>Intelligence that <span class="grad">sees, predicts</span> and understands.</h2>
      <p class="sec-sub" data-reveal style="--d:.15s">Our capability areas cover the full journey from raw data to automated action. Each is delivered with explainability, monitoring and human oversight built in.</p>
      <div class="btn-row" data-reveal style="--d:.25s">{btn("ai-solutions.html", "Discuss an AI Project")}</div></div>
    <div class="caps-panel glass" data-tilt>{hud()}<p class="panel-h"><span class="dot"></span>Capability focus <small>illustrative emphasis</small></p><ul class="cap-list">{rows}</ul></div>
  </div>
</section>'''


def _industries():
    panels = "".join(f'''<a class="ind-panel{" on" if i == 0 else ""}" href="industries.html#{d["id"]}" data-reveal style="--d:{i * .07:.2f}s">
  {img(B, d["img"], d["name"])}<div class="ip-shade"></div>
  <span class="ip-num astro">0{i + 1}</span>
  <div class="ip-body"><span class="ic-box sm">{icon(d["icon"])}</span><h3>{d["short"]}</h3><p>{d["overview"]}</p><span class="more">Explore {icon("arrow")}</span></div></a>''' for i, d in enumerate(HOME_INDUSTRIES))
    return f'''<section class="sec inds">
  <div class="wrap">{head_block("Industries we transform", "Where intelligent technology <span class='grad'>creates real value.</span>", "AI and robotics applied to the operational challenges of five demanding sectors.", extra=btn("industries.html", "All Industries", "ghost"))}
  <div class="ind-panels" data-panels>{panels}</div></div>
</section>'''


def _research():
    items = "".join(f'<li data-reveal style="--d:{i * .06:.2f}s"><span class="ic-box sm">{icon(ic)}</span><div><h3>{n}</h3><p>{t.split(".")[0]}.</p></div></li>' for i, (_, n, ic, t, _p) in enumerate(RESEARCH[:4]))
    return f'''<section class="sec research">
  <div class="wrap split-2 rs-in">
    <div class="rs-media" data-reveal="left"><div class="frame tall">{img(B, "ae-arm-close", "Close-up of a white robotic arm joint with cyan illumination")}</div>
      <div class="rs-chip glass" data-reveal style="--d:.3s"><span class="dot"></span><div><b>Research areas</b><small>Proposed focus, not completed achievements</small></div></div>{hud()}</div>
    <div>{eyebrow("Research &amp; innovation")}<h2 class="sec-title" data-split>Exploring what comes <span class="grad">next in autonomy.</span></h2>
      <p class="sec-sub" data-reveal style="--d:.15s">Our applied research explores emerging methods in machine learning, perception and human-robot collaboration, and tests whether they are ready for real-world use.</p>
      <ul class="rs-list">{items}</ul>
      <div class="btn-row" data-reveal>{btn("research.html", "Our Research Areas", "ghost")}</div></div>
  </div>
</section>'''


def _process():
    steps = [("Discover", "search", "Understand goals, constraints, data and the operational environment."),
             ("Design", "compass", "Architect the AI, robotics and integration approach, and simulate it."),
             ("Develop", "code", "Build models, software and robot cells in iterative, tested sprints."),
             ("Integrate", "layers", "Connect with existing systems, train teams and validate safety."),
             ("Optimize", "gauge", "Monitor performance, retrain models and improve continuously.")]
    s = "".join(f'<li class="step" style="--i:{i}"><span class="step-n astro">0{i + 1}</span><span class="step-ic">{icon(ic)}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, ic, d) in enumerate(steps))
    return f'''<section class="sec process">
  <div class="wrap">{head_block("Our development process", "From discovery to <span class='grad'>continuous optimisation.</span>", "A structured, five-stage engineering process that keeps risk low and value visible at every step.", True)}
  <ol class="steps" data-process><span class="steps-line" aria-hidden="true"><i></i></span>{s}</ol></div>
</section>'''


def _projects():
    cards = "".join(project_card(B, p, i) for i, p in enumerate(PROJECTS[:3]))
    return f'''<section class="sec projects">
  <div class="wrap">{head_block("Featured projects", "Illustrative builds that show <span class='grad'>how we engineer.</span>", "Fictional case studies demonstrating our approach. They do not describe real clients or results.", extra=btn("projects.html", "All Projects", "ghost"))}
  <div class="grid-3">{cards}</div></div>
</section>'''


def _stack():
    rows = []
    for k in range(2):
        logos = [l for g in (TECH if k == 0 else TECH[::-1]) for l in g[2]]
        seq = "".join(f'<span class="tech"><img src="assets/logos/{f}.svg" alt="" width="28" height="28" loading="lazy">{n}</span>' for n, f in logos)
        rows.append(f'<div class="mq-row{" rev" if k else ""}"><div class="mq-track">{seq}{seq}</div></div>')
    groups = "".join(f'<li data-reveal style="--d:{i * .06:.2f}s"><span class="ic-box sm">{icon(ic)}</span><div><h3>{g}</h3><p>{", ".join(n for n, _ in ls)}</p></div></li>' for i, (g, ic, ls) in enumerate(TECH))
    return f'''<section class="sec stack">
  <div class="wrap">{head_block("Technology stack", "Proven tools. <span class='grad'>Engineered together.</span>", "We select mature, well-supported frameworks for AI, robotics and deployment, so systems stay maintainable long after launch.", True)}</div>
  <div class="logo-marquee" aria-label="Technologies we use">{"".join(rows)}</div>
  <div class="wrap"><ul class="stack-groups">{groups}</ul></div>
</section>'''


def _insights():
    cards = "".join(article_card(B, a, i) for i, a in enumerate(ARTICLES[:3]))
    return f'''<section class="sec">
  <div class="wrap">{head_block("Latest insights", "Notes from our <span class='grad'>engineering desk.</span>", "Practical perspectives on AI, robotics and intelligent automation.", extra=btn("insights.html", "All Insights", "ghost"))}
  <div class="grid-3">{cards}</div></div>
</section>'''


def home():
    body = _hero() + _marquee() + _intro() + _core() + _products() + _capabilities() + _industries() + _research() + _process() + _projects() + _stack() + _insights() + cta_band(B)
    schema = {"@context": "https://schema.org", "@type": "WebSite", "name": "Aether Robotics", "url": "https://www.aetherrobotics.sg/"}
    return page("index.html", "Aether Robotics | AI & Robotics Engineering, Singapore",
                "Aether Robotics is a Singapore AI and robotics engineering company designing AI systems, robotics and intelligent automation for enterprises.",
                body, "index.html", B, schema)
