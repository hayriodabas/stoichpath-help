#!/usr/bin/env python3
"""StoichPath help site: privacy and support in twelve languages, one template."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
T = json.loads((ROOT / "copy.json").read_text())

CSS = """:root{color-scheme:light dark;--paper:#f5eedf;--card:#fdf9f1;--ink:#1e2230;--ink2:#5c6170;--cobalt:#2447c9;--brass:#b08a2e;--rule:#dacfbb}
@media(prefers-color-scheme:dark){:root{--paper:#14171e;--card:#1e222b;--ink:#eee8da;--ink2:#a4a9b6;--cobalt:#7a95ff;--brass:#d6b259;--rule:#343a47}}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.6 -apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif}
main{max-width:760px;margin:0 auto;padding:44px 22px 72px}.brand{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--brass);font-weight:600}
h1{font-size:40px;line-height:1.1;font-weight:700;margin:14px 0 8px}h2{font-size:24px;line-height:1.2;font-weight:600;margin:34px 0 8px}
p,li{margin:8px 0}.lead{font-size:20px;color:var(--ink2)}nav{display:flex;gap:18px;margin:18px 0 30px;flex-wrap:wrap}
a{color:var(--cobalt);text-underline-offset:3px}.card{background:var(--card);border:1px solid var(--rule);border-radius:18px;padding:18px 22px;margin:14px 0}
code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:15px}
.rail{height:4px;background:var(--brass);border-radius:2px;margin:26px 0;position:relative}.rail::after{content:"";position:absolute;right:0;top:-6px;width:16px;height:16px;border-radius:50%;background:var(--cobalt)}
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
<h1>{t[kind]['title']}</h1><p class="lead">{t[kind]['lead']}</p><div class="rail"></div>{items}{faq}
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
<div class="rail"></div><ul class="langs">{links}</ul><footer><p>Hayri Odabaş · <a href="mailto:hayriodabas@gmail.com">hayriodabas@gmail.com</a></p></footer></main></body></html>
""", encoding="utf-8")
    print("pages:", len(T["pages"]) * 2 + 1)


if __name__ == "__main__":
    main()
