"""Top-level inner pages for Aether Robotics."""
from ui import (page, page_hero, img, icon, btn, eyebrow, head_block, demo, hud, chips, checks, flag, faq,
                service_card, product_card, project_card, article_card, cta_band, newsletter_form)
from data import (SITE, AI_SERVICES, ROBOTICS, PRODUCTS, INDUSTRIES, RESEARCH, PROJECTS, PROJECT_CATS,
                  TECH, ARTICLES, INSIGHT_CATS, CAREER_AREAS)

B = ""


def _hstats(items):
    return '<ul class="mini-stats" data-reveal style="--d:.35s">' + "".join(f"<li><b>{a}</b><span>{b}</span></li>" for a, b in items) + "</ul>"


# ---------------------------------------------------------------- about
def about():
    values = [("Innovation", "spark", "We explore new methods with curiosity, then prove them with evidence."),
              ("Intelligence", "brain", "We design systems that learn, adapt and explain their reasoning."),
              ("Precision", "crosshair", "Engineering discipline in every model, motion path and line of code."),
              ("Reliability", "shield", "Systems built to be monitored, maintained and trusted in production."),
              ("Ethical Technology", "heart", "Privacy, safety and human oversight are design requirements, not afterthoughts."),
              ("Collaboration", "handshake", "We work alongside operators, engineers and leaders, not around them.")]
    vals = "".join(f'<li class="val" data-reveal data-glow style="--d:{(i % 3) * .08:.2f}s"><span class="ic-box">{icon(ic)}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, ic, d) in enumerate(values))
    expertise = [("AI &amp; Machine Learning", "Model design, training, MLOps and responsible deployment.", "brain"),
                 ("Robotics Engineering", "Robot cells, cobots, mobile robots and motion planning.", "arm"),
                 ("Computer Vision", "Inspection, detection and vision-guided robotics.", "eye"),
                 ("Systems Integration", "PLC, MES, ERP and cloud connectivity for intelligent systems.", "layers")]
    ex = "".join(f'<li data-reveal style="--d:{i * .07:.2f}s"><span class="ic-box sm">{icon(ic)}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for i, (t, d, ic) in enumerate(expertise))
    phil = [("Problem first", "Every engagement starts from an operational problem and a decision that should change, never from a technology looking for a use."),
            ("People in the loop", "Automation should extend human judgement. We design clear hand-offs, overrides and explanations."),
            ("Simulate before you build", "Digital simulation de-risks robot cells, fleet sizes and model behaviour before hardware is purchased."),
            ("Measure honestly", "We report accuracy, limitations and uncertainty openly, so teams can trust what systems tell them.")]
    ph = "".join(f'<li data-reveal style="--d:{i * .08:.2f}s"><span class="astro">0{i + 1}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for i, (t, d) in enumerate(phil))
    body = page_hero(B, "About Aether Robotics", "Engineering intelligence with <span class='grad'>precision and purpose.</span>",
                     f"A Singapore-based AI and robotics engineering company, established in {SITE['founded']}, building intelligent systems that help enterprises work smarter, safer and more efficiently.",
                     [(None, "About")], "ae-hq") + f'''
<section class="sec">
  <div class="wrap split-2">
    <div>{eyebrow("Company overview")}<h2 class="sec-title" data-split>Founded in Singapore to make intelligent technology <span class="grad">practical.</span></h2>
      <p class="lead" data-reveal>Aether Robotics was established in {SITE["founded"]} in Singapore with a simple belief: AI and robotics create the most value when they are engineered as dependable systems, not one-off experiments.</p>
      <p data-reveal style="--d:.1s">Our multidisciplinary team brings together machine learning engineers, robotics specialists, software developers and applied researchers. We work with manufacturers, logistics operators, healthcare organisations, research institutions and technology companies to design, build and integrate AI and robotic solutions.</p>
      <p data-reveal style="--d:.15s">Singapore&#8217;s position as a hub for advanced manufacturing, logistics and research makes it an ideal base for engineering technology that serves the wider Asia-Pacific region.</p></div>
    <div class="about-media" data-reveal="right"><div class="frame">{img(B, "engineer-lab", "Engineers working with robotics equipment in a laboratory")}</div><div class="frame sm">{img(B, "ae-arm-close", "Robotic arm detail")}</div>{hud()}</div>
  </div>
</section>
<section class="sec mv">
  <div class="wrap mv-grid">
    <article class="mv-card glass" data-reveal="left">{hud()}<span class="ic-box">{icon("target")}</span><p class="eyebrow"><i></i>Mission</p><h2>To engineer intelligent systems that augment people and make operations safer, smarter and more efficient.</h2></article>
    <article class="mv-card glass" data-reveal="right">{hud()}<span class="ic-box">{icon("eye")}</span><p class="eyebrow"><i></i>Vision</p><h2>A future where AI and robotics are trusted partners in every industry, designed responsibly and accessible to organisations of every size.</h2></article>
  </div>
</section>
<section class="sec">
  <div class="wrap">{head_block("Core values", "The principles behind <span class='grad'>every system we build.</span>", "", True)}<ul class="grid-3 vals">{vals}</ul></div>
</section>
<section class="sec caps">
  <div class="caps-bg" data-parallax=".15">{img(B, "ae-status", "")}</div><div class="caps-shade" aria-hidden="true"></div>
  <div class="wrap split-2 caps-in">
    <div>{eyebrow("Our expertise")}<h2 class="sec-title" data-split>Deep expertise across <span class="grad">AI and robotics.</span></h2><p class="sec-sub" data-reveal>Software intelligence and physical engineering under one roof means fewer hand-offs and systems that work end to end.</p></div>
    <ul class="ex-list glass">{ex}</ul>
  </div>
</section>
<section class="sec">
  <div class="wrap">{head_block("Technology philosophy", "How we think about <span class='grad'>intelligent technology.</span>")}<ol class="phil">{ph}</ol></div>
</section>
<section class="sec">
  <div class="wrap">{head_block("Leadership &amp; engineering team", "The people behind <span class='grad'>Aether.</span>", "Team profiles will be published once details and consent have been confirmed.", True)}
    {flag("Leadership names, roles, photographs and biographies. This section intentionally shows no invented people.")}</div>
</section>''' + cta_band(B, "Discover Our", "AI &amp; Robotics Solutions", "See how our engineering disciplines come together to solve real operational problems.", "Discover Our Solutions", "ai-solutions.html", btn("contact.html#enquiry", "Contact Us", "ghost"))
    return page("about.html", "About Us", "Aether Robotics is a Singapore AI and robotics engineering company established in 2020. Our mission, vision, values and expertise.", body, "about.html", B, og_img="ae-hq")


# ---------------------------------------------------------------- AI solutions
def ai_solutions():
    cards = "".join(service_card(B, s, i) for i, s in enumerate(AI_SERVICES))
    how = [("Assess", "Use-case discovery, data audit and feasibility."), ("Prototype", "Rapid proof-of-concept with clear success measures."),
           ("Productionise", "Robust pipelines, APIs, integration and security."), ("Operate", "Monitoring, drift detection and retraining.")]
    hw = "".join(f'<li data-reveal style="--d:{i * .08:.2f}s"><span class="astro">0{i + 1}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(how))
    body = page_hero(B, "AI Solutions", "Artificial intelligence, <span class='grad'>engineered for production.</span>",
                     "Six AI service areas that take you from data and ideas to dependable, monitored systems that change how decisions are made.",
                     [(None, "AI Solutions")], "ae-wave", _hstats([("6", "Service areas"), ("4", "Delivery stages"), ("100%", "Human oversight by design")])) + f'''
<section class="sec">
  <div class="wrap">{head_block("Our AI services", "Choose a capability, <span class='grad'>or combine them.</span>", "Each service has its own detail page covering problems, capabilities, technologies and use cases.")}<div class="grid-3">{cards}</div></div>
</section>
<section class="sec">
  <div class="wrap">{head_block("How AI projects run", "A delivery model that <span class='grad'>reaches production.</span>", "", True)}<ol class="phase-row">{hw}</ol></div>
</section>
<section class="sec"><div class="wrap narrow">{head_block("FAQs", "Common questions about <span class='grad'>AI projects.</span>", "", True)}
{faq([("How much data do we need to start?", "It depends on the problem. Many projects start with existing operational data; where data is limited we use transfer learning, simulation or a short data-collection phase. A discovery workshop will tell you what is realistic."),
      ("Can AI run on our own infrastructure?", "Yes. We deploy on-premises, at the edge on embedded devices, or in the cloud, depending on latency, privacy and cost requirements."),
      ("How do you handle responsible AI?", "We document intended use and limitations, test for bias and robustness where relevant, add explainability and keep people in control of consequential decisions."),
      ("Do you support systems after launch?", "Yes. We offer monitoring, retraining and improvement support so models stay accurate as conditions change.")])}</div></section>''' + cta_band(B, "Have an AI idea?", "Let&#8217;s test it properly.", label="Discuss an AI Project", href="contact.html?interest=ai#enquiry")
    return page("ai-solutions.html", "AI Solutions", "AI development, machine learning, computer vision, NLP, intelligent automation and AI R&D services from Aether Robotics, Singapore.", body, "ai-solutions.html", B, og_img="ae-wave")


# ---------------------------------------------------------------- robotics
def robotics():
    blocks = ""
    for i, r in enumerate(ROBOTICS):
        rev = " rev" if i % 2 else ""
        blocks += f'''<article class="rb-block{rev}" id="{r["id"]}">
  <div class="rb-media" data-reveal="{"right" if i % 2 else "left"}"><div class="frame">{img(B, r["img"], r["name"])}</div><span class="rb-num astro">0{i + 1}</span>{hud()}</div>
  <div class="rb-copy"><span class="ic-box">{icon(r["icon"])}</span><h2 data-split>{r["name"]}</h2><p data-reveal>{r["text"]}</p>{checks(r["points"])}</div>
</article>'''
    apps = [("Manufacturing", "Welding, assembly, machine tending, inspection.", "factory"), ("Logistics", "Mobile robots, sorting, palletising.", "truck"),
            ("Healthcare", "Laboratory automation, supply delivery.", "health"), ("Research", "Robot test beds and simulation platforms.", "flask"),
            ("Industrial assets", "Drone and crawler inspection of hazardous sites.", "building"), ("Technology products", "Perception and control modules.", "chip")]
    ap = "".join(f'<li data-reveal data-glow style="--d:{(i % 3) * .07:.2f}s"><span class="ic-box sm">{icon(ic)}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d, ic) in enumerate(apps))
    caps = ["Mechanical and end-of-arm tooling design", "Robot simulation and offline programming", "ROS / ROS 2 software development",
            "Motion planning and control", "Vision-guided manipulation", "Safety risk assessment support", "PLC, MES and ERP integration", "Commissioning, training and support"]
    eng = [("Assess", "Task, site and safety assessment"), ("Simulate", "Digital cell and fleet simulation"), ("Build", "Hardware, software and tooling"),
           ("Commission", "Installation, testing and validation"), ("Support", "Monitoring, maintenance and improvement")]
    en = "".join(f'<li class="step" style="--i:{i}"><span class="step-n astro">0{i + 1}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(eng))
    rp = "".join(project_card(B, p, i) for i, p in enumerate([p for p in PROJECTS if p["cat"] == "Robotics"]))
    body = page_hero(B, "Robotics Solutions", "Robotics engineered for <span class='grad'>the real world.</span>",
                     "From industrial arms and collaborative robots to autonomous mobile systems, we design, program and integrate robotics that work safely alongside people.",
                     [(None, "Robotics")], "ae-arm-weld") + f'''
<section class="sec">
  <div class="wrap split-2">
    <div>{eyebrow("Robotics engineering")}<h2 class="sec-title" data-split>Intelligent machines, <span class="grad">integrated end to end.</span></h2></div>
    <div><p class="lead" data-reveal>Robotics projects succeed when mechanics, software, perception, safety and integration are engineered together. Our team covers all of them.</p>
    <p data-reveal style="--d:.1s">We focus on applications where robots take on repetitive, precise or hazardous work, while people remain in control of judgement, quality and exceptions. We describe expected benefits honestly and validate them through simulation and pilots before scale-up.</p></div>
  </div>
</section>
<section class="sec rb-list"><div class="wrap">{blocks}</div></section>
<section class="sec">
  <div class="wrap">{head_block("Applications", "Robotics applications <span class='grad'>across industries.</span>", "", True)}<ul class="grid-3 app-grid">{ap}</ul></div>
</section>
<section class="sec process">
  <div class="wrap split-2 top">
    <div>{eyebrow("Engineering capabilities")}<h2 class="sec-title" data-split>Everything a robot cell <span class="grad">needs to succeed.</span></h2>{checks(caps, "checks two")}</div>
    <div class="glass pad">{hud()}<p class="panel-h"><span class="dot"></span>Engineering process</p><ol class="steps vert" data-process><span class="steps-line" aria-hidden="true"><i></i></span>{en}</ol></div>
  </div>
</section>
<section class="sec">
  <div class="wrap">{head_block("Project showcase", "Illustrative <span class='grad'>robotics builds.</span>", "Fictional case studies, labelled as demos.", extra=btn("projects.html", "All Projects", "ghost"))}<div class="grid-3">{rp}</div></div>
</section>''' + cta_band(B, "Explore Robotics", "for Your Operations", label="Explore Robotics Solutions", href="contact.html?interest=robotics#enquiry")
    return page("robotics.html", "Robotics Solutions", "Industrial robotics, robotic arms, assistance systems, autonomous systems and intelligent robotics integration by Aether Robotics.", body, "robotics.html", B, og_img="ae-arm-weld")


# ---------------------------------------------------------------- products
def products():
    cards = "".join(product_card(B, p, i) for i, p in enumerate(PRODUCTS))
    rows = "".join(f'<tr><th scope="row">{p["name"]}</th><td>{p["tag"]}</td><td>{p["short"]}</td><td>{", ".join(p["applications"][:2])}</td></tr>' for p in PRODUCTS)
    body = page_hero(B, "Products &amp; Platforms", "Five platforms. <span class='grad'>One intelligent ecosystem.</span>",
                     "Illustrative product concepts that show how Aether&#8217;s AI and robotics capabilities can be packaged into reusable platforms.",
                     [(None, "Products")], "ae-cubes", f'<div data-reveal style="--d:.35s">{demo("All products are illustrative demo concepts, not commercially verified products")}</div>') + f'''
<section class="sec">
  <div class="wrap">{head_block("Product portfolio", "Explore the <span class='grad'>concepts.</span>", "Each product has its own page with purpose, features and use cases.")}<div class="grid-3 prod-grid">{cards}</div></div>
</section>
<section class="sec">
  <div class="wrap">{head_block("At a glance", "Compare the <span class='grad'>platforms.</span>", "", True)}
  <div class="table-wrap glass" data-reveal><table class="cmp"><thead><tr><th scope="col">Product</th><th scope="col">Category</th><th scope="col">Purpose</th><th scope="col">Example uses</th></tr></thead><tbody>{rows}</tbody></table></div></div>
</section>''' + cta_band(B, "Interested in a platform", "built around your needs?", label="Talk to Our Team", href="contact.html?interest=products#enquiry")
    return page("products.html", "Products & Platforms", "Aether AI Core, RoboAssist, VisionX, AutoFlow and NeuraSense: illustrative AI and robotics product concepts.", body, "products.html", B, og_img="ae-cubes")


# ---------------------------------------------------------------- industries
def industries():
    nav = "".join(f'<a href="#{d["id"]}" data-spy="{d["id"]}">{icon(d["icon"])}{d["short"]}</a>' for d in INDUSTRIES)
    blocks = ""
    for i, d in enumerate(INDUSTRIES):
        blocks += f'''<article class="ind-block{" rev" if i % 2 else ""}" id="{d["id"]}">
  <div class="ib-media" data-reveal="{"right" if i % 2 else "left"}"><div class="frame">{img(B, d["img"], d["name"])}</div><span class="rb-num astro">0{i + 1}</span>{hud()}</div>
  <div class="ib-copy"><span class="ic-box">{icon(d["icon"])}</span><h2 data-split>{d["name"]}</h2><p class="lead" data-reveal>{d["overview"]}</p>
    <div class="ib-cols" data-reveal style="--d:.1s">
      <div><h3>{icon("alert")}Common challenges</h3>{checks(d["challenges"], "checks warn")}</div>
      <div><h3>{icon("zap")}AI &amp; robotics applications</h3>{checks(d["applications"])}</div>
    </div>
    <div class="ib-sol" data-reveal style="--d:.15s"><h3>Proposed technology solutions</h3>{chips(d["solutions"])}</div>
    <div data-reveal style="--d:.2s">{btn(f"contact.html?industry={d['id']}#enquiry", "Discuss Your Industry Requirements", "ghost")}</div></div>
</article>'''
    body = page_hero(B, "Industries We Serve", "Industry problems, <span class='grad'>intelligent answers.</span>",
                     "How AI and robotics address the operational challenges of six sectors, from the factory floor to the research lab.",
                     [(None, "Industries")], "factory-robots") + f'''
<div class="subnav" data-subnav><div class="wrap"><nav aria-label="Industries">{nav}</nav></div></div>
<section class="sec ind-list"><div class="wrap">{blocks}</div></section>''' + cta_band(B, "Your industry,", "your requirements.", label="Discuss Your Requirements", href="contact.html#enquiry")
    return page("industries.html", "Industries We Serve", "AI and robotics for manufacturing, healthcare, logistics, research and education, industrial enterprises and technology companies.", body, "industries.html", B, og_img="factory-robots")


# ---------------------------------------------------------------- research
def research():
    areas = "".join(f'''<article class="ra-card glass" id="{k}" data-reveal data-glow style="--d:{(i % 3) * .08:.2f}s">
  <div class="ra-top"><span class="ic-box">{icon(ic)}</span><span class="status">Research area</span></div>
  <h3>{n}</h3><p>{t}</p><h4>Questions we are exploring</h4>{checks(q)}</article>''' for i, (k, n, ic, t, q) in enumerate(RESEARCH))
    hl = "".join(article_card(B, a, i) for i, a in enumerate(ARTICLES[2:5]))
    body = page_hero(B, "Research &amp; Innovation", "Researching the <span class='grad'>next frontier.</span>",
                     "Our research interests and future technology direction across machine learning, autonomy, perception and human-machine interaction.",
                     [(None, "Research")], "ae-humanoid") + f'''
<section class="sec">
  <div class="wrap split-2">
    <div>{eyebrow("AI research overview")}<h2 class="sec-title" data-split>Applied research with a <span class="grad">clear path to use.</span></h2></div>
    <div><p class="lead" data-reveal>Our research programme explores methods that could make AI and robotics more capable, efficient and trustworthy in industrial settings.</p>
    <p data-reveal style="--d:.1s">We evaluate ideas through structured experiments, simulation and prototypes, and share what we learn through technical articles. </p>
    <div class="notice" data-reveal style="--d:.15s">{icon("alert")}<p><strong>Transparency note:</strong> the areas below are <em>proposed research interests</em>. They are not completed research achievements, publications or patents.</p></div></div>
  </div>
</section>
<section class="sec"><div class="wrap">{head_block("Research areas", "Six areas we are <span class='grad'>exploring.</span>", "", True)}<div class="grid-3">{areas}</div></div></section>
<section class="sec"><div class="wrap">{head_block("Articles &amp; highlights", "Innovation <span class='grad'>highlights.</span>", "Articles from our engineering and research team.", extra=btn("insights.html", "All Insights", "ghost"))}<div class="grid-3">{hl}</div></div></section>''' + cta_band(B, "Interested in a", "research collaboration?", label="Propose a Collaboration", href="contact.html?type=partnership#enquiry")
    return page("research.html", "Research & Innovation", "Aether Robotics research interests: machine learning, neural networks, autonomous robotics, computer vision, human-machine interaction and emerging technology.", body, "research.html", B)


# ---------------------------------------------------------------- projects
def projects():
    f = '<button type="button" class="on" data-filter="all" aria-pressed="true">All</button>' + "".join(f'<button type="button" data-filter="{c}" aria-pressed="false">{c}</button>' for c in PROJECT_CATS)
    cards = "".join(project_card(B, p, i) for i, p in enumerate(PROJECTS))
    feat = PROJECTS[0]
    body = page_hero(B, "Projects &amp; Case Studies", "Ideas engineered into <span class='grad'>working systems.</span>",
                     "Illustrative AI and robotics case studies that show our approach to problems, solutions and implementation.",
                     [(None, "Projects")], "ae-arm-close", f'<div data-reveal style="--d:.35s">{demo("Fictional, illustrative case studies: no real clients or results")}</div>') + f'''
<section class="sec">
  <div class="wrap"><a class="feat-proj glass" href="projects/{feat["slug"]}.html" data-reveal>
    <div class="fp-media">{img(B, feat["img"], feat["title"])}</div>
    <div class="fp-body"><span class="tag">Featured · {feat["cat"]}</span><h2>{feat["title"]}</h2><p>{feat["summary"]} {feat["solution"]}</p>{chips(feat["tech"])}<span class="more">Read case study {icon("arrow")}</span></div></a></div>
</section>
<section class="sec">
  <div class="wrap">{head_block("All projects", "Filter by <span class='grad'>discipline.</span>")}
  <div class="filters" data-filters="proj" role="group" aria-label="Filter projects">{f}</div>
  <div class="grid-3 filter-grid" data-filter-grid="proj">{cards}</div><p class="empty" data-empty="proj" hidden>No projects in this category yet.</p></div>
</section>''' + cta_band(B, "Have a challenge", "worth engineering?", label="Start Your Project", href="contact.html?type=project#enquiry")
    return page("projects.html", "Projects & Case Studies", "Illustrative AI, robotics, automation and computer vision case studies from Aether Robotics.", body, "projects.html", B, og_img="ae-arm-close")


# ---------------------------------------------------------------- insights
def insights():
    f = '<button type="button" class="on" data-filter="all" aria-pressed="true">All</button>' + "".join(f'<button type="button" data-filter="{c}" aria-pressed="false">{c}</button>' for c in INSIGHT_CATS)
    a0 = ARTICLES[0]
    cards = "".join(article_card(B, a, i) for i, a in enumerate(ARTICLES[1:]))
    body = page_hero(B, "Insights &amp; AI Research Blog", "Ideas, analysis and <span class='grad'>engineering notes.</span>",
                     "Practical articles on artificial intelligence, robotics, machine learning, automation and emerging technologies.",
                     [(None, "Insights")], "ae-wave") + f'''
<section class="sec">
  <div class="wrap"><a class="feat-proj glass" href="insights/{a0["slug"]}.html" data-reveal>
    <div class="fp-media">{img(B, a0["img"], a0["title"])}</div>
    <div class="fp-body"><span class="tag">Featured · {a0["cat"]}</span><h2>{a0["title"]}</h2><p>{a0["summary"]}</p>
    <div class="meta"><span>{icon("calendar")}{a0["date_h"]}</span><span>{icon("clock")}{a0["read"]} min read</span></div><span class="more">Read article {icon("arrow")}</span></div></a></div>
</section>
<section class="sec">
  <div class="wrap">{head_block("Latest articles", "Browse by <span class='grad'>category.</span>")}
  <div class="filters" data-filters="art" role="group" aria-label="Filter articles">{f}</div>
  <div class="grid-3 filter-grid" data-filter-grid="art">{article_card(B, a0, 0)}{cards}</div><p class="empty" data-empty="art" hidden>New articles in this category are coming soon.</p></div>
</section>
<section class="sec"><div class="wrap"><div class="nl-band glass" data-reveal>{hud()}<div>{eyebrow("Newsletter")}<h2>Engineering notes, <span class="grad">monthly.</span></h2><p>Get new articles on AI and robotics delivered to your inbox.</p></div>{newsletter_form("blog")}</div></div></section>'''
    return page("insights.html", "Insights & AI Research Blog", "Articles on AI, robotics engineering, machine learning, intelligent automation, computer vision and emerging technologies.", body, "insights.html", B, og_img="ae-wave")


# ---------------------------------------------------------------- careers
def careers():
    why = [("Real-world impact", "Your work leaves the lab and runs on factory floors, warehouses and hospitals.", "rocket"),
           ("Multidisciplinary team", "Work daily with ML, robotics, embedded and software engineers.", "users"),
           ("Time to learn", "Dedicated learning time, conference budget and internal tech talks.", "book"),
           ("Responsible engineering", "Safety, ethics and honesty are part of how we build.", "shield")]
    wy = "".join(f'<li data-reveal data-glow style="--d:{i * .07:.2f}s"><span class="ic-box">{icon(ic)}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d, ic) in enumerate(why))
    cats = sorted(set(c for c, *_ in CAREER_AREAS), key=[c for c, *_ in CAREER_AREAS].index)
    f = '<button type="button" class="on" data-filter="all" aria-pressed="true">All</button>' + "".join(f'<button type="button" data-filter="{c}" aria-pressed="false">{c}</button>' for c in cats)
    areas = "".join(f'''<li class="job" data-cat="{c}" data-reveal style="--d:{(i % 3) * .06:.2f}s"><span class="ic-box sm">{icon(ic)}</span><div><small>{c}</small><h3>{n}</h3><p>{d}</p></div>
  <a class="btn btn-ghost btn-sm" href="#apply" data-area="{n}"><span>Register interest</span></a></li>''' for i, (c, ic, n, d) in enumerate(CAREER_AREAS))
    opts = "".join(f'<option value="{n}">{n}</option>' for _, _, n, _ in CAREER_AREAS)
    body = page_hero(B, "Careers", "Build the Future of <span class='grad'>Intelligent Technology.</span>",
                     "Join AI engineers, robotics specialists and technologists building systems that make a real difference.",
                     [(None, "Careers")], "engineer-2", f'<div class="btn-row" data-reveal style="--d:.35s">{btn("#apply", "Join Our Team")}{btn("#roles", "View Roles", "ghost")}</div>') + f'''
<section class="sec">
  <div class="wrap split-2">
    <div class="about-media" data-reveal="left"><div class="frame">{img(B, "team-tech", "Technology team collaborating")}</div><div class="frame sm">{img(B, "students-lab", "Engineers in a lab")}</div>{hud()}</div>
    <div>{eyebrow("Company culture")}<h2 class="sec-title" data-split>Curious minds, <span class="grad">engineering discipline.</span></h2>
    <p class="lead" data-reveal>We value clear thinking, careful engineering and kindness. Ideas are judged on evidence, not hierarchy.</p>
    <p data-reveal style="--d:.1s">Our engineering and innovation environment combines a hands-on robotics lab, simulation tools and modern MLOps infrastructure, so you can move from idea to experiment quickly and safely.</p>
    {flag("Benefits, working arrangements and lab facilities to be confirmed by HR.")}</div>
  </div>
</section>
<section class="sec"><div class="wrap">{head_block("Why work with Aether Robotics?", "Reasons engineers <span class='grad'>join us.</span>", "", True)}<ul class="grid-4 why">{wy}</ul></div></section>
<section class="sec" id="roles">
  <div class="wrap">{head_block("Current openings", "Roles &amp; <span class='grad'>job categories.</span>")}
  <div class="notice" data-reveal>{icon("alert")}<p><strong>No vacancies are currently advertised.</strong> Live openings will appear here once confirmed. Meanwhile, register your interest in one of our engineering areas below.</p></div>
  <div class="filters" data-filters="jobs" role="group" aria-label="Filter job categories">{f}</div>
  <ul class="jobs filter-grid" data-filter-grid="jobs">{areas}</ul></div>
</section>
<section class="sec" id="apply">
  <div class="wrap split-2 top">
    <div>{eyebrow("Apply")}<h2 class="sec-title" data-split>Register your <span class="grad">interest.</span></h2><p class="sec-sub" data-reveal>Tell us about yourself and the area you would like to work in. We will contact you when a suitable role opens.</p>
      {checks(["CV in PDF, DOC or DOCX, up to 5 MB", "We reply to every application", "Your data is handled under our Privacy Policy"])}</div>
    <form class="form glass" data-form="careers" novalidate>{hud()}
      <div class="row2"><div class="field"><label for="c-name">Full name *</label><input id="c-name" name="name" required autocomplete="name"></div>
      <div class="field"><label for="c-email">Email *</label><input id="c-email" type="email" name="email" required autocomplete="email"></div></div>
      <div class="row2"><div class="field"><label for="c-phone">Phone</label><input id="c-phone" type="tel" name="phone" autocomplete="tel"></div>
      <div class="field"><label for="c-area">Area of interest *</label><select id="c-area" name="area" required><option value="">Select an area</option>{opts}</select></div></div>
      <div class="field"><label for="c-link">LinkedIn or portfolio URL</label><input id="c-link" type="url" name="link" placeholder="https://"></div>
      <div class="field"><label for="c-msg">About you *</label><textarea id="c-msg" name="message" rows="4" minlength="20" required></textarea></div>
      <div class="field"><span class="lbl">CV / résumé *</span><label class="file">{icon("upload")}<span data-file-label>Click to upload or drag your file here</span><input type="file" name="cv" accept=".pdf,.doc,.docx" data-max="5" required></label></div>
      <label class="check"><input type="checkbox" name="consent" required><span>I agree to Aether Robotics processing my data for recruitment, as described in the <a href="privacy-policy.html">Privacy Policy</a>. *</span></label>
      <input type="text" name="website" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
      <button class="btn btn-primary" type="submit"><span>Submit Application</span><span class="btn-ic">{icon("send")}</span></button>
      <p class="form-msg" role="status" aria-live="polite"></p>
    </form>
  </div>
</section>'''
    return page("careers.html", "Careers", "Careers at Aether Robotics: AI engineering, robotics, software development and research roles in Singapore.", body, "careers.html", B, og_img="team-tech")


# ---------------------------------------------------------------- contact
def contact():
    interests = [("ai", "AI Solutions"), ("ml", "Machine Learning"), ("vision", "Computer Vision"), ("nlp", "Natural Language Processing"), ("automation", "Intelligent Automation"),
                 ("robotics", "Robotics Engineering"), ("products", "Products &amp; Platforms"), ("research", "Research Collaboration"), ("partnership", "Partnership"), ("other", "Other")]
    opts = "".join(f'<option value="{v}">{l}</option>' for v, l in interests)
    ways = [("General enquiries", "Questions about Aether Robotics and our capabilities.", "mail", f'<a href="mailto:{SITE["email"]}">{SITE["email"]}</a>'),
            ("AI &amp; robotics projects", "Scope a project with our engineers using the form.", "rocket", '<a href="#enquiry" data-type="project">Open project form</a>'),
            ("Partnerships", "Technology, research and integration partnerships.", "handshake", f'<a href="mailto:{SITE["partner_email"]}">{SITE["partner_email"]}</a>')]
    wy = "".join(f'<li class="way glass" data-reveal data-glow style="--d:{i * .08:.2f}s"><span class="ic-box">{icon(ic)}</span><h3>{t}</h3><p>{d}</p>{l}</li>' for i, (t, d, ic, l) in enumerate(ways))
    body = page_hero(B, "Contact Us", "Let&#8217;s Engineer <span class='grad'>What&#8217;s Next.</span>",
                     "Tell us about your challenge. Our AI and robotics engineers usually reply within one business day.",
                     [(None, "Contact")], "robot-hand") + f'''
<section class="sec"><div class="wrap"><ul class="grid-3 ways">{wy}</ul></div></section>
<section class="sec" id="enquiry">
  <div class="wrap split-2 top">
    <div>{eyebrow("Project enquiry")}<h2 class="sec-title" data-split>Tell us about <span class="grad">your project.</span></h2>
      <p class="sec-sub" data-reveal>Share as much as you can. We will respond with next steps, which is usually a short discovery call.</p>
      <div class="hq glass" data-reveal>{hud()}<h3>{icon("pin")}Singapore headquarters</h3><p>Full street address to be confirmed.</p>
        <ul class="ft-contact"><li>{icon("mail")}<a href="mailto:{SITE["email"]}">{SITE["email"]}</a></li><li>{icon("clock")}<span>Mon to Fri, 9:00 to 18:00 SGT</span></li><li class="wa">{icon("whatsapp")}<a href="#" data-wa>Chat on WhatsApp</a></li></ul>
        <div class="map-ph">{img(B, "ae-hq", "Aether Robotics headquarters (illustrative)")}<span>{icon("pin")}Office map will appear after address confirmation</span></div></div>
      {flag("Verified street address, phone number, WhatsApp number and map embed.")}</div>
    <form class="form glass" data-form="enquiry" novalidate>{hud()}
      <input type="hidden" name="type" value="general">
      <div class="row2"><div class="field"><label for="e-name">Full name *</label><input id="e-name" name="name" required autocomplete="name"></div>
      <div class="field"><label for="e-email">Business email *</label><input id="e-email" type="email" name="email" required autocomplete="email"></div></div>
      <div class="row2"><div class="field"><label for="e-company">Company name *</label><input id="e-company" name="company" required autocomplete="organization"></div>
      <div class="field"><label for="e-phone">Phone number</label><input id="e-phone" type="tel" name="phone" autocomplete="tel"></div></div>
      <div class="field"><label for="e-service">Interested solution *</label><select id="e-service" name="interest" required><option value="">Select a solution</option>{opts}</select></div>
      <div class="field"><label for="e-msg">Project details *</label><textarea id="e-msg" name="message" rows="5" minlength="20" required placeholder="Goals, current process, timelines, constraints…"></textarea></div>
      <label class="check"><input type="checkbox" name="consent" required><span>I agree to Aether Robotics using these details to respond to my enquiry, as described in the <a href="privacy-policy.html">Privacy Policy</a>. *</span></label>
      <input type="text" name="website" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
      <button class="btn btn-primary" type="submit"><span>Send Enquiry</span><span class="btn-ic">{icon("send")}</span></button>
      <p class="form-msg" role="status" aria-live="polite"></p>
    </form>
  </div>
</section>
<section class="sec"><div class="wrap narrow">{head_block("FAQs", "Before you <span class='grad'>get in touch.</span>", "", True)}
{faq([("What happens after I submit the form?", "An engineer reviews your enquiry and replies, usually within one business day, to arrange a short discovery call."),
      ("Do you work with organisations outside Singapore?", "Our headquarters is in Singapore. We can discuss projects elsewhere; on-site work depends on scope and location."),
      ("Can you sign an NDA before we share details?", "Yes. We are happy to sign a mutual NDA before detailed technical discussions."),
      ("Are your products available to buy?", "The five products on this website are illustrative demo concepts. We can discuss bespoke solutions built on similar ideas."),
      ("How do partnership enquiries work?", f"Email {SITE['partner_email']} or choose &#8216;Partnership&#8217; in the form, with a short description of the opportunity.")])}</div></section>'''
    return page("contact.html", "Contact Us", "Contact Aether Robotics in Singapore for AI and robotics project enquiries, partnerships and general questions.", body, "contact.html", B, og_img="ae-status")
