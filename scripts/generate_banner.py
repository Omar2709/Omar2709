#!/usr/bin/env python3
"""Generate independent, GitHub-friendly architecture diagrams (stdlib only)."""
from pathlib import Path
from html import escape

BASE=Path(__file__).resolve().parents[1]
ASSETS=BASE/'assets'
ASSETS.mkdir(parents=True,exist_ok=True)

THEMES={
 'dark':dict(bg='#080F1F', panel='#101C31', inner='#13223A', border='#2B415A', text='#F0F7FF', muted='#B2C4D9', arrow='#729DB7', grid='#183149'),
 'light':dict(bg='#F8FBFF', panel='#FFFFFF', inner='#F0F6FD', border='#C7D8E9', text='#14263B', muted='#465E77', arrow='#7291B0', grid='#E3ECF6')
}
ACCENTS={'teamflow':'#1598D0','fastapi':'#8D72DC','integration':'#118F81'}

class Diagram:
 def __init__(self,key,theme,title,kicker,description):
  self.key=key; self.t=THEMES[theme]; self.accent=ACCENTS[key]; self.theme=theme
  self.z=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1180" height="470" viewBox="0 0 1180 470" role="img" aria-labelledby="title desc">',
          f'<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>',
          f'<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z" fill="{self.t["arrow"]}" /></marker><pattern id="grid" width="26" height="26" patternUnits="userSpaceOnUse"><path d="M26 0H0V26" fill="none" stroke="{self.t["grid"]}" stroke-width=".5" opacity=".5"/></pattern></defs>',
          f'<rect width="1180" height="470" rx="18" fill="{self.t["bg"]}"/>',
          f'<rect x="1" y="1" width="1178" height="468" rx="17" fill="none" stroke="{self.t["border"]}" stroke-width="2"/>',
          f'<rect x="20" y="90" width="1140" height="314" rx="10" fill="url(#grid)" stroke="{self.t["border"]}" stroke-width="1"/>',
          f'<rect x="20" y="20" width="6" height="50" rx="3" fill="{self.accent}"/>',
          f'<text x="42" y="37" fill="{self.accent}" font-family="Segoe UI,Arial,sans-serif" font-size="12" font-weight="700" letter-spacing="2.2">{escape(kicker)}</text>',
          f'<text x="42" y="67" fill="{self.t["text"]}" font-family="Segoe UI,Arial,sans-serif" font-size="27" font-weight="750">{escape(title)}</text>',
          f'<text x="1138" y="54" text-anchor="end" fill="{self.t["muted"]}" font-family="Consolas,monospace" font-size="12">ARCHITECTURE / V1</text>']
 def node(self,x,y,w,h,title,subtitle='',primary=False):
  panel=self.t['inner'] if primary else self.t['panel']
  stroke=self.accent if primary else self.t['border']
  self.z += [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{panel}" stroke="{stroke}" stroke-width="{1.7 if primary else 1.2}"/>']
  if primary:
   self.z += [f'<rect x="{x+11}" y="{y+11}" width="4" height="{h-22}" rx="2" fill="{self.accent}"/>']
  cx=x+w/2
  sy=y+(h/2-(4 if subtitle else -5))
  self.z += [f'<text x="{cx}" y="{sy}" text-anchor="middle" fill="{self.t["text"]}" font-family="Segoe UI,Arial,sans-serif" font-size="{18 if len(title)<21 else 15}" font-weight="700">{escape(title)}</text>']
  if subtitle:
   self.z += [f'<text x="{cx}" y="{sy+21}" text-anchor="middle" fill="{self.t["muted"]}" font-family="Segoe UI,Arial,sans-serif" font-size="13">{escape(subtitle)}</text>']
 def path(self,d,dash=False):
  dashstr=' stroke-dasharray="5 6"' if dash else ''
  self.z += [f'<path d="{d}" fill="none" stroke="{self.t["arrow"]}" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#arrow)"{dashstr}/>']
 def label(self,x,y,text,anchor='middle'):
  self.z += [f'<text x="{x}" y="{y}" text-anchor="{anchor}" fill="{self.t["muted"]}" font-family="Segoe UI,Arial,sans-serif" font-size="12" font-weight="550">{escape(text)}</text>']
 def footer(self,sub,badges):
  self.z += [f'<text x="41" y="440" fill="{self.t["muted"]}" font-family="Segoe UI,Arial,sans-serif" font-size="14">{escape(sub)}</text>']
  x=1140
  for badge in reversed(badges):
   w=len(badge)*7+22
   x-=w
   self.z += [f'<rect x="{x}" y="420" width="{w-7}" height="28" rx="6" fill="{self.t["panel"]}" stroke="{self.t["border"]}"/>',f'<text x="{x+(w-7)/2}" y="439" text-anchor="middle" fill="{self.t["text"]}" font-family="Segoe UI,Arial,sans-serif" font-size="12">{escape(badge)}</text>']
 def save(self):
  self.z.append('</svg>')
  p=ASSETS/f'architecture-{self.key}-{self.theme}.svg'
  p.write_text('\n'.join(self.z)+'\n',encoding='utf-8')
  return p

def make_team(theme):
 d=Diagram('teamflow',theme,'TeamFlow API','PROJECT 01  /  DJANGO + CELERY','Cliente HTTP atraviesa Gunicorn y DRF; PostgreSQL almacena datos. Redis sirve cache y broker de Celery; Beat programa trabajos y Worker escribe los resultados.')
 d.node(42,198,166,76,'Client','HTTP / JSON')
 d.node(267,198,207,76,'Gunicorn + DRF','JWT / roles / API',True)
 d.node(825,112,235,75,'PostgreSQL','Teams / tasks / events')
 d.node(554,198,210,76,'Redis','Cache + Celery broker',True)
 d.node(825,198,235,76,'Celery Worker','Background notifications')
 d.node(554,316,210,76,'Celery Beat','Periodic task scheduling')
 d.path('M208 236 H267')
 d.path('M474 236 H554')
 d.path('M764 236 H825')
 d.path('M380 198 V149 H825')
 d.path('M943 198 V187')
 d.path('M659 316 V274')
 d.label(516,183,'cache / enqueue')
 d.label(659,301,'scheduled jobs')
 d.footer('Responsabilidades separadas · ejecución local con Docker Compose',['DRF','Redis','Celery'])
 return d.save()

def make_fast(theme):
 d=Diagram('fastapi',theme,'FastAPI REST API','PROJECT 02  /  CONSISTENCY + MESSAGING','El contrato HTTP usa autenticación por API Keys y scopes. El servicio persiste Jobs, claves de idempotencia y Outbox en PostgreSQL; un publisher envía los eventos mediante adapter a SQS.')
 d.node(36,198,148,75,'Client','HTTP requests')
 d.node(228,198,192,75,'FastAPI','API Keys + scopes',True)
 d.node(466,198,170,75,'Services','Domain rules',True)
 d.node(715,123,182,79,'PostgreSQL','Jobs · Keys · Outbox')
 d.node(715,287,182,77,'Outbox Publisher','Retry / backoff')
 d.node(947,287,196,77,'Broker adapter','SQS via Boto3')
 d.node(947,123,196,79,'Amazon SQS','Message queue')
 d.path('M184 237 H228'); d.path('M420 237 H466'); d.path('M636 235 H674 V162 H715');d.path('M806 202 V287')
 d.path('M897 325 H947'); d.path('M1045 287 V202')
 d.label(775,270,'eligible events')
 d.footer('Un mismo request idempotente no debe crear dos Jobs',['SQLAlchemy','Outbox','SQS'])
 return d.save()

def make_integr(theme):
 d=Diagram('integration',theme,'Python Integration Service','PROJECT 03  /  HTTP INTEGRATIONS','FastAPI inyecta el VendorClient inicializado en lifespan, que depende de un Transport abstracto. HttpxTransport habla con APIs externas y FakeTransport facilita tests aislados.')
 d.node(36,196,146,78,'Client','GET /vendor/items')
 d.node(223,196,174,78,'FastAPI','Lifespan + DI',True)
 d.node(445,196,194,78,'VendorClient','Provider semantics',True)
 d.node(686,196,165,78,'Transport','Interface / port',True)
 d.node(896,196,232,78,'HttpxTransport','HTTPX client')
 d.node(896,107,232,65,'External API','Third-party service')
 d.node(445,315,194,72,'Resilience','Rate limits + retries')
 d.node(686,315,165,72,'FakeTransport','Isolated tests')
 d.path('M182 235 H223');d.path('M397 235 H445');d.path('M639 235 H686');d.path('M851 235 H896');d.path('M1012 196 V172')
 d.path('M542 315 V274',True);d.path('M768 315 V274',True)
 d.footer('Errores tipados, configuración validada y cierre determinista',['FastAPI','HTTPX','pytest'])
 return d.save()

if __name__=='__main__':
 for theme in THEMES:
  for f in (make_team,make_fast,make_integr):
   p=f(theme); print(p.name,p.stat().st_size)
