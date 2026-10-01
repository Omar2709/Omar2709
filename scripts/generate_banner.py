#!/usr/bin/env python3
"""Genera los dos banners SVG animados del perfil. Solo requiere Python 3.10+."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)

THEMES = {
    "dark": {
        "bg": "#080F1F", "top": "#101B30", "panel": "#0E1A2D", "panel2": "#12243A", "line": "#29415B",
        "text": "#F1F7FF", "muted": "#9AAFC7", "accent": "#5EEAD4", "cyan": "#38BDF8", "blue": "#60A5FA", "gold": "#FFCF77",
        "pill": "#162A41", "shadow": "#020712"
    },
    "light": {
        "bg": "#F3F7FC", "top": "#FFFFFF", "panel": "#FFFFFF", "panel2": "#EDF5FB", "line": "#C7D9EA",
        "text": "#10253B", "muted": "#536F8C", "accent": "#087F70", "cyan": "#0575BB", "blue": "#205DAE", "gold": "#B67612",
        "pill": "#E7F1F9", "shadow": "#CBD8E5"
    },
}


def text(x, y, value, size=16, weight=400, color=None, family="mono", other=""):
    fonts = {"mono": "'SFMono-Regular',Consolas,'Liberation Mono',monospace", "sans": "Inter,Segoe UI,Helvetica,Arial,sans-serif"}
    attrs = f' x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" font-family="{fonts[family]}" fill="{color}" {other}'
    return f"<text{attrs}>{escape(value)}</text>"


def generate(theme, c):
    out = [f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 398" width="1180" height="398" role="img" aria-labelledby="title desc">
<title id="title">Omar López — Backend Engineer</title><desc id="desc">Terminal animada con identidad profesional y diagrama API, datos y eventos.</desc>
<defs>
  <linearGradient id="base" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c['bg']}"/><stop offset="1" stop-color="{c['top']}"/></linearGradient>
  <filter id="shade" x="-20%" y="-30%" width="150%" height="170%"><feDropShadow dx="0" dy="6" stdDeviation="10" flood-color="{c['shadow']}" flood-opacity=".35"/></filter>
  <clipPath id="corners"><rect x="1" y="1" width="1178" height="396" rx="18"/></clipPath>
</defs>
<style>
  .cursor {{ animation: blink 1.2s steps(1) infinite; }}
  .packet {{ animation: flow 4.5s linear infinite; }}
  .packet2 {{ animation: flow 4.5s linear infinite; animation-delay: -2.2s; }}
  .pulse {{ animation: glow 3s ease-in-out infinite; }}
  .pulse2 {{ animation: glow 3s ease-in-out infinite; animation-delay: -1.5s; }}
  .logline {{ animation: appear 9s ease-in-out infinite; }}
  @keyframes blink {{ 0%,47% {{opacity:1}} 48%,100% {{opacity:0}} }}
  @keyframes flow {{ from {{stroke-dashoffset:52}} to {{stroke-dashoffset:0}} }}
  @keyframes glow {{ 0%,100% {{opacity:.28}} 45%,60% {{opacity:1}} }}
  @keyframes appear {{0%,15% {{opacity:.35}} 16%,65% {{opacity:1}} 66%,100% {{opacity:.35}}}}
  @media (prefers-reduced-motion: reduce) {{ .cursor,.packet,.packet2,.pulse,.pulse2,.logline {{animation:none}} }}
</style>
<g clip-path="url(#corners)">
<rect width="1180" height="398" fill="url(#base)"/>
<rect x="22" y="20" width="1136" height="358" rx="14" fill="{c['panel']}" stroke="{c['line']}" filter="url(#shade)"/>
<path d="M22 65H1158" stroke="{c['line']}"/>
<circle cx="45" cy="43" r="5" fill="#FF605C"/><circle cx="64" cy="43" r="5" fill="#FFBE2F"/><circle cx="83" cy="43" r="5" fill="#2ACA44"/>
''']
    out += [text(590,48, "omar@github: ~/profile  —  ./build.sh", 13, 500, c['muted'], other='text-anchor="middle"')]
    out += [f'<path d="M730 84V355" stroke="{c["line"]}"/>']
    out += [text(60,105,"~/profile/README.md",14,600,c['accent'])]
    out += [text(60,166,"OMAR LÓPEZ",45,800,c['text'],"sans",'letter-spacing="2"')]
    out += [text(61,208,"BACKEND ENGINEER",24,700,c['cyan'],"mono")]
    out += [f'<rect x="61" y="227" width="10" height="23" rx="1" fill="{c["accent"]}" class="cursor"/>']
    out += [text(82,246,"Python · FastAPI · Django · PostgreSQL",17,500,c['muted'])]
    out += [f'<rect x="61" y="274" width="211" height="35" rx="17" fill="{c["pill"]}" stroke="{c["line"]}"/>']
    out += [text(78,296,"API ARCHITECTURE",13,650,c['accent'])]
    out += [f'<rect x="281" y="274" width="225" height="35" rx="17" fill="{c["pill"]}" stroke="{c["line"]}"/>']
    out += [text(299,296,"DISTRIBUTED SYSTEMS",13,650,c['blue'])]
    out += [text(62,344,"> build · test · observe · iterate",14,400,c['muted'])]
    out += [text(760,108,"SYSTEM TOPOLOGY",14,700,c['muted'],other='letter-spacing="1.6"')]
    # grid right panel
    for x in range(773,1134,24):
        for y in range(137,335,24):
            out += [f'<circle cx="{x}" cy="{y}" r=".85" fill="{c["muted"]}" opacity=".18"/>']
    nodes=[(758,163,108,76,"01","API","FastAPI"),(899,163,108,76,"02","DATA","Postgres"),(1040,163,105,76,"03","EVENTS","SQS / Redis")]
    for x,y,w,h,num,name,sub in nodes:
        out += [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{c["panel2"]}" stroke="{c["line"]}"/>']
        out += [text(x+11,y+21,num,12,600,c['muted'])]
        out += [text(x+11,y+46,name,16,700,c['text'])]
        out += [text(x+11,y+64,sub,11,450,c['cyan'])]
    # animated connections, no JavaScript/network dependencies
    out += [f'<path d="M867 201H896M1009 201H1036" fill="none" stroke="{c["line"]}" stroke-width="3" stroke-linecap="round"/>']
    out += [f'<path class="packet" d="M867 201H896M1009 201H1036" fill="none" stroke="{c["accent"]}" stroke-width="3" stroke-dasharray="10 52" stroke-linecap="round"/>']
    out += [f'<path d="M810 241v29h281v-29" fill="none" stroke="{c["line"]}" stroke-width="1.7" stroke-dasharray="4 5"/>']
    out += [f'<circle class="pulse" cx="810" cy="270" r="4" fill="{c["accent"]}"/><circle class="pulse2" cx="1091" cy="270" r="4" fill="{c["cyan"]}"/>']
    out += [f'<rect x="759" y="292" width="385" height="42" rx="7" fill="{c["panel2"]}" stroke="{c["line"]}"/>']
    out += [text(773,317,"$",14,700,c['accent'])]
    out += [text(792,317,"request  >  validate  >  publish",13,500,c['text'],other='class="logline"')]
    out += [text(1119,355,"COLOMBIA  ·  GITHUB",11,500,c['muted'],other='text-anchor="end"')]
    out += ['</g></svg>']
    file=ASSETS/f"banner-{theme}.svg"
    file.write_text(''.join(out),encoding="utf-8")
    print(f"{file.name}: {file.stat().st_size:,} bytes")


if __name__=="__main__":
    for k,v in THEMES.items():generate(k,v)
