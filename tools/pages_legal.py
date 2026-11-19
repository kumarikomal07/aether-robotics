"""Legal & policy pages (Singapore PDPA-oriented drafts) and 404."""
from ui import page, icon, btn, hud, eyebrow
from data import SITE

B = ""
TBC = lambda t: f'<mark class="tbc">[To be confirmed: {t}]</mark>'  # noqa: E731


def _legal(path, title, intro, sections, updated="19 November 2026"):
    toc = "".join(f'<li><a href="#s{i + 1}">{h}</a></li>' for i, (h, _) in enumerate(sections))
    secs = "".join(f'<section id="s{i + 1}"><h2><span class="astro">{i + 1:02d}</span>{h}</h2>{b}</section>' for i, (h, b) in enumerate(sections))
    body = f'''<section class="phero legal-hero"><div class="grid-bg" aria-hidden="true"></div><canvas class="net" aria-hidden="true"></canvas>{hud("hud-hero")}
  <div class="wrap phero-in"><nav class="crumb" aria-label="Breadcrumb"><a href="index.html">Home</a>{icon("chev-r")}<span aria-current="page">{title}</span></nav>
  {eyebrow("Legal")}<h1 data-split>{title}</h1><p class="phero-sub" data-reveal>{intro}</p><p class="updated" data-reveal>Last updated: {updated}</p></div></section>
<section class="sec"><div class="wrap legal">
  <aside class="legal-toc glass"><p class="panel-h"><span class="dot"></span>Contents</p><ol>{toc}</ol></aside>
  <div class="prose legal-body"><div class="notice">{icon("alert")}<p><strong>Draft for legal review.</strong> This policy is a template prepared for a Singapore company. Items marked {TBC("…")} must be completed, and the full text reviewed by a qualified Singapore lawyer against actual company practices before publication.</p></div>{secs}</div>
</div></section>'''
    return page(path, title, intro, body, path, B)


CO = f'Aether Robotics {TBC("registered legal entity name and UEN")}'


def privacy():
    s = [("Who we are", f"<p>This website is operated by {CO}, a company established in Singapore in {SITE['founded']} (&#8220;Aether Robotics&#8221;, &#8220;we&#8221;, &#8220;us&#8221;). Our registered address is {TBC('registered office address')}.</p><p>Our Data Protection Officer can be contacted at {TBC('DPO email, e.g. dpo@aetherrobotics.sg')}.</p>"),
         ("Personal data we collect", "<ul><li><strong>Enquiries:</strong> name, business email, company name, phone number, interested solution and project details.</li><li><strong>Applications:</strong> name, contact details, CV and any information you provide.</li><li><strong>Newsletter:</strong> email address.</li><li><strong>Technical data:</strong> with consent, analytics data such as pages visited and device type.</li></ul>"),
         ("How we use personal data", "<p>We use personal data to respond to enquiries, assess job applications, send newsletters you request, operate and improve the website, and meet legal obligations. We collect, use and disclose personal data in accordance with the Personal Data Protection Act 2012 (PDPA).</p>"),
         ("Consent and withdrawal", f"<p>By submitting a form you consent to our use of your data for the purpose stated. You may withdraw consent at any time by emailing {TBC('DPO email')}. Withdrawal may affect our ability to respond to you.</p>"),
         ("Disclosure to third parties", f"<p>We may share data with service providers who help us operate the website, such as hosting, form processing and email providers {TBC('list providers')}. We do not sell personal data.</p>"),
         ("Overseas transfers", f"<p>Some providers may store data outside Singapore. Where this happens we take steps to ensure a standard of protection comparable to the PDPA. {TBC('transfer locations and safeguards')}</p>"),
         ("Retention", f"<p>We retain personal data only as long as needed for the purpose collected or for legal and business reasons. {TBC('retention periods for enquiries, applications and newsletter data')}</p>"),
         ("Security", "<p>We use reasonable security arrangements to protect personal data, including encrypted connections (HTTPS) and access controls.</p>"),
         ("Access and correction", f"<p>You may request access to or correction of your personal data by contacting our DPO at {TBC('DPO email')}. We may charge a reasonable fee for access requests as permitted by the PDPA.</p>"),
         ("Changes to this policy", "<p>We may update this policy. The latest version will always be published on this page with the date of the last update.</p>")]
    return _legal("privacy-policy.html", "Privacy Policy", "How Aether Robotics collects, uses and protects personal data under Singapore&#8217;s PDPA.", s)


def terms():
    s = [("Acceptance", f"<p>By using this website you agree to these Terms. The website is operated by {CO}.</p>"),
         ("Use of the website", "<p>You agree not to misuse the website, attempt unauthorised access, introduce malicious code or use automated tools that place an unreasonable load on it.</p>"),
         ("Illustrative content", "<p>Products (Aether AI Core, RoboAssist, VisionX, AutoFlow and NeuraSense), case studies, statistics and research areas shown on this website are <strong>illustrative demo concepts</strong>. They do not represent commercially available products, real clients, actual results or completed research.</p>"),
         ("Intellectual property", "<p>Content, design, logos and text on this website belong to Aether Robotics or its licensors. You may view and print pages for personal or internal business use only.</p>"),
         ("No professional advice", "<p>Website content is general information and is not engineering, safety, legal or investment advice. Projects are subject to separate written agreements.</p>"),
         ("Limitation of liability", f"<p>To the extent permitted by law, Aether Robotics is not liable for losses arising from use of this website. {TBC('liability wording reviewed by counsel')}</p>"),
         ("Third-party links", "<p>Links to external sites are provided for convenience. We are not responsible for their content or practices.</p>"),
         ("Governing law", "<p>These Terms are governed by the laws of Singapore, and the courts of Singapore have exclusive jurisdiction.</p>"),
         ("Contact", f"<p>Questions about these Terms can be sent to <a href=\"mailto:{SITE['email']}\">{SITE['email']}</a>.</p>")]
    return _legal("terms.html", "Terms & Conditions", "The terms that apply when you use the Aether Robotics website.", s)


def cookie_policy():
    s = [("What cookies are", "<p>Cookies are small files stored on your device. We also use browser local storage to remember your cookie choices.</p>"),
         ("Cookies we use", """<div class="table-wrap"><table class="cmp"><thead><tr><th>Name</th><th>Type</th><th>Purpose</th><th>Duration</th></tr></thead><tbody>
<tr><td>ae_consent</td><td>Essential (local storage)</td><td>Remembers your cookie choices</td><td>12 months</td></tr>
<tr><td>_ga, _ga_*</td><td>Analytics (optional)</td><td>Google Analytics 4 usage statistics, loaded only after consent</td><td>Up to 2 years</td></tr></tbody></table></div>"""),
         ("Your choices", "<p>Optional cookies are off until you accept them. You can change your choice at any time on the <a href=\"cookie-preferences.html\">Cookie Preferences</a> page or in your browser settings.</p>"),
         ("Third-party content", f"<p>Fonts are served by Google Fonts. A map embed may be added after the office address is confirmed. {TBC('final list of third-party services')}</p>"),
         ("Contact", f"<p>Questions: <a href=\"mailto:{SITE['email']}\">{SITE['email']}</a>.</p>")]
    return _legal("cookie-policy.html", "Cookie Policy", "Which cookies this website uses and how you can control them.", s)


def cookie_prefs():
    body = f'''<section class="phero legal-hero"><div class="grid-bg" aria-hidden="true"></div>{hud("hud-hero")}
  <div class="wrap phero-in"><nav class="crumb" aria-label="Breadcrumb"><a href="index.html">Home</a>{icon("chev-r")}<span aria-current="page">Cookie Preferences</span></nav>
  {eyebrow("Legal")}<h1 data-split>Cookie Preferences</h1><p class="phero-sub" data-reveal>Choose which optional cookies we may use. Essential cookies are always on.</p></div></section>
<section class="sec"><div class="wrap narrow">
<form class="prefs glass" data-prefs>{hud()}
  <div class="pref"><div><h2>Essential</h2><p>Required for the website to work, including remembering these choices.</p></div><span class="always">Always on</span></div>
  <label class="pref"><div><h2>Analytics</h2><p>Google Analytics 4 helps us understand how the website is used. Loaded only with consent.</p></div><span class="switch"><input type="checkbox" name="analytics"><i></i></span></label>
  <label class="pref"><div><h2>Marketing</h2><p>Not currently used. Reserved for future campaign measurement, which would be disclosed first.</p></div><span class="switch"><input type="checkbox" name="marketing"><i></i></span></label>
  <div class="btn-row"><button class="btn btn-primary" type="submit"><span>Save Preferences</span></button><button class="btn btn-ghost" type="button" data-consent="accept"><span>Accept all</span></button><button class="btn btn-ghost" type="button" data-consent="reject"><span>Reject optional</span></button></div>
  <p class="form-msg" role="status" aria-live="polite"></p>
</form><p class="small-note">See our <a href="cookie-policy.html">Cookie Policy</a> for details.</p></div></section>'''
    return page("cookie-preferences.html", "Cookie Preferences", "Manage optional cookies on the Aether Robotics website.", body, "cookie-preferences.html", B)


def not_found():
    body = f'''<section class="nf"><div class="grid-bg" aria-hidden="true"></div><canvas class="net" aria-hidden="true"></canvas>{hud("hud-hero")}
  <div class="wrap nf-in"><p class="astro chroma nf-code" data-text="404">404</p><h1>Signal lost.</h1><p>The page you are looking for has moved or does not exist.</p>
  <div class="btn-row center">{btn("/index.html", "Back to Home")}{btn("/contact.html", "Contact Us", "ghost")}</div></div></section>'''
    return page("404.html", "Page Not Found", "The page you requested could not be found.", body, "", "/")
