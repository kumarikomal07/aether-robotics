"""Build the Aether Robotics static site.

Usage (from the project root):  python3 tools/build.py
Writes every HTML page, sitemap.xml and robots.txt into the project root.
Content: tools/data.py · layout/components: tools/ui.py · pages: tools/pages_*.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from data import SITE, AI_SERVICES, PRODUCTS, PROJECTS, ARTICLES  # noqa: E402
import pages_home as H  # noqa: E402
import pages_inner as P  # noqa: E402
import pages_detail as D  # noqa: E402
import pages_legal as L  # noqa: E402


def write(rel, html):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return rel


def main():
    out = [
        write("index.html", H.home()),
        write("about.html", P.about()),
        write("ai-solutions.html", P.ai_solutions()),
        write("robotics.html", P.robotics()),
        write("products.html", P.products()),
        write("industries.html", P.industries()),
        write("research.html", P.research()),
        write("projects.html", P.projects()),
        write("insights.html", P.insights()),
        write("careers.html", P.careers()),
        write("contact.html", P.contact()),
        write("privacy-policy.html", L.privacy()),
        write("terms.html", L.terms()),
        write("cookie-policy.html", L.cookie_policy()),
        write("cookie-preferences.html", L.cookie_prefs()),
        write("404.html", L.not_found()),
    ]
    out += [write(f"ai-solutions/{s['slug']}.html", D.service(s)) for s in AI_SERVICES]
    out += [write(f"products/{p['slug']}.html", D.product(p)) for p in PRODUCTS]
    out += [write(f"projects/{c['slug']}.html", D.case(c)) for c in PROJECTS]
    out += [write(f"insights/{a['slug']}.html", D.article(a)) for a in ARTICLES]

    urls = "".join(f"  <url><loc>{SITE['domain']}/{'' if r == 'index.html' else r}</loc><lastmod>2026-11-19</lastmod></url>\n" for r in out if r != "404.html")
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /tools/\n\nSitemap: {SITE['domain']}/sitemap.xml\n")
    print(f"Built {len(out)} pages.")


if __name__ == "__main__":
    main()
