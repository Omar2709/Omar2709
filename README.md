<div align="center">

<!-- BANNER: conserva ambos SVG en la carpeta assets/ del repositorio. -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg" />
  <img src="assets/banner-dark.svg" width="100%" alt="Omar López — Backend Engineer | Python, FastAPI, Django y sistemas distribuidos" />
</picture>

<br />

<a href="https://github.com/Omar2709">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=21&duration=2900&pause=1200&color=2786DE&center=true&vCenter=true&width=850&height=45&lines=Backend+Engineer+%7C+Python+%26+FastAPI;Django+REST+Framework+%7C+PostgreSQL;API+Design+%7C+Integrations+%7C+Distributed+Systems;AWS+Serverless+%7C+Docker+%7C+CI%2FCD" alt="Especialidades: ingeniería backend, APIs y sistemas distribuidos" />
</a>

<br />

<a href="https://omar-lopez-portafolio.netlify.app/">
  <img src="https://img.shields.io/badge/Portafolio-Visitar-1664C0?style=for-the-badge&logo=netlify&logoColor=white" alt="Portafolio" />
</a>
<a href="https://www.linkedin.com/in/omar-l%C3%B3pez-8a0009269/">
  <img src="https://img.shields.io/badge/LinkedIn-Conectar-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
</a>
<a href="https://github.com/Omar2709?tab=repositories">
  <img src="https://img.shields.io/badge/GitHub-Repositorios-24292E?style=for-the-badge&logo=github&logoColor=white" alt="Repositorios" />
</a>

<br /><br />

<img src="https://komarev.com/ghpvc/?username=Omar2709&label=Visitas+al+perfil&color=1664c0&style=flat-square" alt="Contador de visitas del perfil" />

</div>

---

## 👨‍💻 Sobre mí

Soy **Omar López**, ingeniero de sistemas de Colombia 🇨🇴 y **Backend Engineer enfocado en Python**. Trabajo con **Django, Django REST Framework y FastAPI** para diseñar APIs, servicios e integraciones que sean mantenibles y fáciles de probar.

Me interesan los problemas que aparecen más allá de un CRUD: **autenticación y autorización, integridad transaccional, idempotencia, mensajería, procesamiento asíncrono y resiliencia**. Mi enfoque combina diseño de software, pruebas automatizadas y decisiones de arquitectura justificadas.

- 🧩 **Backend:** Python, Django REST Framework, FastAPI, APIs REST e integraciones.
- 🏗️ **Arquitectura:** separación de responsabilidades, modelado de dominio y patrones para sistemas distribuidos.
- ⚙️ **Infraestructura:** PostgreSQL, Redis, Celery, Docker, GitHub Actions y servicios de AWS.
- 🌱 **Explorando:** Go, concurrencia, observabilidad y arquitectura orientada a eventos.

## 🛠️ Tecnologías

<div align="center">

**Backend y lenguajes**

<img src="https://skillicons.dev/icons?i=python,django,fastapi,go&perline=4" alt="Python, Django, FastAPI y Go" />

**Datos, mensajería y cloud**

<img src="https://skillicons.dev/icons?i=postgres,mysql,redis,firebase,aws&perline=5" alt="PostgreSQL, MySQL, Redis, Firebase y AWS" />

**Herramientas y calidad**

<img src="https://skillicons.dev/icons?i=docker,linux,git,github,githubactions,postman,vscode&perline=7" alt="Docker, Linux, Git, GitHub, GitHub Actions, Postman y VS Code" />

<sub>También trabajo con SQLAlchemy, Alembic, Celery, Amazon SQS, HTTPX, pytest, Ruff y CI/CD.</sub>

</div>

---

## 🚀 Proyectos destacados

Proyectos que demuestran **arquitectura, seguridad, persistencia e integraciones**. Los diagramas resumen las decisiones principales de cada implementación; haz clic en ellos para ampliarlos. El código y las pruebas están disponibles públicamente.

### 👥 [TeamFlow API](https://github.com/Omar2709/teamflow-api) — Django, equipos y procesamiento asíncrono

API colaborativa con **JWT, roles por equipo, aislamiento de recursos, PostgreSQL, caché con Redis y tareas con Celery**. Incluye contratos OpenAPI, controles de consultas y pruebas automatizadas.

<a href="assets/architecture-teamflow-dark.svg" title="Ampliar arquitectura de TeamFlow API">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/architecture-teamflow-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="assets/architecture-teamflow-light.svg" />
    <img src="assets/architecture-teamflow-dark.svg" width="100%" alt="Arquitectura de TeamFlow: cliente, Gunicorn y Django REST, PostgreSQL, Redis como caché y broker, Celery Worker y Celery Beat." />
  </picture>
</a>

[**Código y documentación ↗**](https://github.com/Omar2709/teamflow-api) · [**Pruebas por módulo ↗**](https://github.com/Omar2709/teamflow-api/tree/main/apps) · [**Pipeline CI ↗**](https://github.com/Omar2709/teamflow-api/actions/workflows/ci.yml)

[![TeamFlow CI](https://github.com/Omar2709/teamflow-api/actions/workflows/ci.yml/badge.svg)](https://github.com/Omar2709/teamflow-api/actions/workflows/ci.yml)

### ⚡ [FastAPI REST API](https://github.com/Omar2709/fastapi-rest-api) — consistencia y mensajería

API centrada en **API Keys y scopes, idempotencia HTTP y Transactional Outbox**. Separa servicios, dominio y adaptadores; un publisher publica eventos mediante el adaptador de **Amazon SQS**, con lógica de reintentos y fallos terminales.

<a href="assets/architecture-fastapi-dark.svg" title="Ampliar arquitectura de FastAPI REST API">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/architecture-fastapi-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="assets/architecture-fastapi-light.svg" />
    <img src="assets/architecture-fastapi-dark.svg" width="100%" alt="Arquitectura de FastAPI REST API: cliente, autenticación y scopes, servicios, PostgreSQL con Jobs e idempotencia y Outbox Publisher conectado mediante adaptador a Amazon SQS." />
  </picture>
</a>

[**Código y documentación ↗**](https://github.com/Omar2709/fastapi-rest-api) · [**Pruebas ↗**](https://github.com/Omar2709/fastapi-rest-api/tree/main/tests) · [**Pipeline CI ↗**](https://github.com/Omar2709/fastapi-rest-api/actions/workflows/ci.yml)

[![FastAPI CI](https://github.com/Omar2709/fastapi-rest-api/actions/workflows/ci.yml/badge.svg)](https://github.com/Omar2709/fastapi-rest-api/actions/workflows/ci.yml)

### 🔌 [Python Integration Service](https://github.com/Omar2709/python-integration-service) — integraciones resilientes

Servicio con **inyección de dependencias, abstracción de transporte y HTTPX**. Separa semántica de proveedores y transporte, valida respuestas, gestiona excepciones y utiliza dobles de prueba para aislar integraciones externas.

<a href="assets/architecture-integration-dark.svg" title="Ampliar arquitectura de Python Integration Service">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/architecture-integration-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="assets/architecture-integration-light.svg" />
    <img src="assets/architecture-integration-dark.svg" width="100%" alt="Arquitectura de Python Integration Service: cliente, FastAPI con inyección de dependencias, VendorClient, interfaz de transporte, HttpxTransport y API externa; políticas de resiliencia y FakeTransport para pruebas." />
  </picture>
</a>

[**Código y documentación ↗**](https://github.com/Omar2709/python-integration-service) · [**Pruebas ↗**](https://github.com/Omar2709/python-integration-service/tree/main/tests) · [**Pipeline CI ↗**](https://github.com/Omar2709/python-integration-service/actions/workflows/ci.yml)

[![Integration CI](https://github.com/Omar2709/python-integration-service/actions/workflows/ci.yml/badge.svg)](https://github.com/Omar2709/python-integration-service/actions/workflows/ci.yml)

<sub>Los diagramas son vistas simplificadas de las arquitecturas documentadas; cada repositorio contiene los detalles y sus pruebas.</sub>

---

## 💼 Experiencia y formación

**Backend Developer — Efficode** · *Febrero de 2022 – actualidad*

Desarrollo de APIs y servicios backend con Python; trabajo con persistencia, integraciones, pruebas, procesamiento asíncrono y despliegue. Para consultar mi experiencia completa, visita mi [portafolio](https://omar-lopez-portafolio.netlify.app/) o [LinkedIn](https://www.linkedin.com/in/omar-l%C3%B3pez-8a0009269/).

**Ingeniería de Sistemas** · Universidad de La Guajira

---

## 🐍 Actividad en GitHub

<div align="center">

<!-- Esta animación utiliza tu workflow existente: .github/workflows/snake.yml -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Omar2709/Omar2709/output/github-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Omar2709/Omar2709/output/github-snake.svg" />
  <img src="https://raw.githubusercontent.com/Omar2709/Omar2709/output/github-snake.svg" alt="Animación del historial de contribuciones de Omar en GitHub" width="100%" />
</picture>

<br />

<sub>Building reliable backend systems, one architectural decision at a time.</sub>

</div>
