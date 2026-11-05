#!/usr/bin/env python3
"""StoichPath help site: privacy and support in twelve languages, one template."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
T = json.loads((ROOT / "copy.json").read_text())

CSS = """:root{color-scheme:light dark;--sheet:#fcfbf8;--well:#f2f0ea;--ink:#15171c;--ink2:#50545e;--cobalt:#2346d1;--rule:#e3e0d7;--strong:#c9c5b9}
@media(prefers-color-scheme:dark){:root{--sheet:#15181e;--well:#1c2027;--ink:#eceae4;--ink2:#a6aab3;--cobalt:#8da4ff;--rule:#262b34;--strong:#3a404c}}
*{box-sizing:border-box}body{margin:0;background:var(--sheet);color:var(--ink);font:17px/1.6 -apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif}
main{max-width:760px;margin:0 auto;padding:44px 22px 72px}.brand{font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--ink2);font-weight:600}
h1{font-size:40px;line-height:1.1;font-weight:700;margin:14px 0 8px}h2{font-size:13px;letter-spacing:.1em;text-transform:uppercase;font-weight:600;color:var(--ink2);margin:36px 0 8px;padding-top:12px;border-top:1px solid var(--strong)}
p,li{margin:8px 0}.lead{font-size:20px;color:var(--ink2)}nav{display:flex;gap:18px;margin:18px 0 30px;flex-wrap:wrap}
a{color:var(--cobalt);text-underline-offset:3px}.card{background:var(--well);border-radius:14px;padding:16px 20px;margin:14px 0}
code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:15px}
.rule{height:3px;width:56px;background:var(--cobalt);border-radius:2px;margin:26px 0}
footer{margin-top:40px;border-top:1px solid var(--rule);padding-top:16px;color:var(--ink2);font-size:14px}
.langs{display:flex;flex-wrap:wrap;gap:10px 16px;font-size:14px;list-style:none;padding:0}@media(max-width:600px){main{padding:30px 18px 56px}h1{font-size:32px}}"""


def page(lang, kind, t, html_lang):
    items = "".join(f"<h2>{h}</h2><p>{p}</p>" for h, p in t[kind]["sections"])
    faq = "".join(f'<div class="card"><p><strong>{q}</strong></p><p>{a}</p></div>' for q, a in t[kind].get("faq", []))
    return f"""<!doctype html>
<html lang="{html_lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>StoichPath — {t[kind]['title']}</title><style>{CSS}</style>
<link rel="canonical" href="https://hayriodabas.github.io/stoichpath-help/{lang}/{kind}.html"></head>
<body><main><div class="brand">StoichPath</div>
<nav><a href="privacy.html">{t['privacy']['title']}</a><a href="support.html">{t['support']['title']}</a><a href="../index.html">{t['languages']}</a></nav>
<h1>{t[kind]['title']}</h1><p class="lead">{t[kind]['lead']}</p><div class="rule"></div>{items}{faq}
<h2>{t['contact']}</h2><p><a href="mailto:hayriodabas@gmail.com">hayriodabas@gmail.com</a></p>
<footer><p>{t['updated']}</p><p>Hayri Odabaş</p></footer></main></body></html>
"""


def main():
    langs = T["languages"]
    for lang, t in T["pages"].items():
        d = ROOT / lang
        d.mkdir(exist_ok=True)
        html_lang = {"pt-BR": "pt-BR", "zh-Hans": "zh-Hans"}.get(lang, lang.split("-")[0] if lang != "en-US" else "en")
        for kind in ("privacy", "support"):
            (d / f"{kind}.html").write_text(page(lang, kind, t, html_lang), encoding="utf-8")
    links = "".join(f'<li><a href="{lang}/support.html">{name}</a> · <a href="{lang}/privacy.html">{T["pages"][lang]["privacy"]["title"]}</a></li>' for lang, name in langs.items())
    (ROOT / "index.html").write_text(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>StoichPath — Support</title><style>{CSS}</style>
<link rel="canonical" href="https://hayriodabas.github.io/stoichpath-help/"></head>
<body><main><div class="brand">StoichPath</div><h1>Support and privacy</h1><p class="lead">StoichPath is a bench for stoichiometry: write a reaction, give the amounts, and follow the path from grams to grams. Pick a language.</p>
<div class="rule"></div><ul class="langs">{links}</ul><footer><p>Hayri Odabaş · <a href="mailto:hayriodabas@gmail.com">hayriodabas@gmail.com</a></p></footer></main></body></html>
""", encoding="utf-8")
    print("pages:", len(T["pages"]) * 2 + 1)


if __name__ == "__main__":
    main()
