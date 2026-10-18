<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&pause=1000&color=4F8EF7&center=true&vCenter=true&width=720&lines=Hi%2C+I'm+Apoorv+Raj;Python+Software+Engineer;Backend%2C+REST+APIs+and+Applied+ML;Turning+Models+Into+Tested+Software" alt="Typing SVG" />

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-%230077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/apoorv-raj-1a35ba218)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-%234F8EF7?style=flat-square&logo=vercel&logoColor=white)](https://ai-engineer-portfolio-pi.vercel.app/)
[![Email](https://img.shields.io/badge/Email-Reach%20Out-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:apoorvrajmgr@gmail.com)
[![Mastodon](https://img.shields.io/badge/Mastodon-Follow-%232B90D9?style=flat-square&logo=mastodon&logoColor=white)](https://mastodon.social/@ApoorvRaj)

</div>

---

## About Me

I'm Apoorv — a Python software engineer who builds backend services, REST APIs and data-driven applications, and who likes taking machine-learning models the rest of the way: validated inputs, reliable data handling, automated tests and repeatable deployments.

- **Now:** AI Engineer (independent contractor, founding contributor) at **[Node2.io](https://www.node2.io)** — Python/FastAPI AI services for a PropTech SaaS, including an LLM booking assistant built with LangChain tool calling, a complaint-prioritisation engine, and resident/staff features in a Next.js + TypeScript app on PostgreSQL (Supabase)
- **Backend & data:** FastAPI, Pydantic validation, SQLAlchemy, schema design, constraints and Alembic migrations on PostgreSQL and SQLite
- **Applied ML:** XGBoost and TensorFlow models served behind tested APIs, with evaluation and explainability (SHAP) treated as part of the product
- **Research:** IEEE-published — *AI Narratives: Bridging Visual Content and Linguistic Expression* (CNN + Transformer image captioning), ICSPCRE 2024
- Open to software engineering and applied-AI roles, and to collaborating on research-driven projects

<sub>B.E. Computer Science & Engineering, Chandigarh University (2024) &nbsp;·&nbsp; Python for Data Science, AI & Development — IBM &nbsp;·&nbsp; AWS Cloud Technical Essentials — AWS</sub>

---

## Meet Me in 60 Seconds

<div align="center">

https://github.com/user-attachments/assets/ed85cead-67ed-4e3d-bc2c-a31d65dfed1f


  <img src="assets/introduction-poster.jpg" alt="Play: Apoorv Raj, a 58-second introduction. Python software engineer turning machine-learning models into tested, deployed software. Shows Fraud Radar, the Image Captioning System and Node2.io work." width="840" />
</a>

<sub>▶ Click to play (MP4, 1920×1080, 58 s, narrated, 7.7 MB) &nbsp;·&nbsp; <a href="video/narration-script.md">Read the script</a> &nbsp;·&nbsp; <a href="video/README.md">How it was made</a></sub>

</div>

---

## Selected Projects

### Fraud Radar — real-time card-fraud scoring with explanations

[Repository](https://github.com/apoorvrajdev/fraud-radar) · [Live demo](https://fraud-radar-lilac.vercel.app) · [24-second demo video](https://github.com/apoorvrajdev/fraud-radar#-product-demo)

A FastAPI service that scores card transactions by combining **6 deterministic business rules with an XGBoost model**, attaches a **SHAP attribution to every decision**, and lands flagged transactions in an analyst review queue with an append-only audit log. React + TypeScript dashboard for KPIs, flagged transactions and analyst decisions.

- Data layer on SQLAlchemy (SQLite in development, Postgres-compatible schemas) with exact decimal amounts, database constraints, versioned migrations and retry-safe ingestion via idempotency keys — a retried request is never stored twice
- Service-layer scoring latency p50 **3.7 ms**; **1,407 unit and integration tests**, `ruff` and `mypy --strict` in CI
- Evaluation reported honestly: PR-AUC **0.93** on a held-out fold of the project's own synthetic generator, and a separate PR-AUC **0.77** on 284,807 real anonymised transactions (ULB) on an isolated track. These measure how learnable the datasets are, not production fraud-detection effectiveness

### Image Captioning System — IEEE-published research, shipped as a tested app

[Repository](https://github.com/apoorvrajdev/image-captioning-system) · [Live app](https://image-captioning-system.vercel.app) · [27-second demo video](https://github.com/apoorvrajdev/image-captioning-system#-product-demo) · [Paper](https://doi.org/10.1109/ICSPCRE62303.2024.10675203)

The InceptionV3 + Transformer captioning model from my IEEE paper, rebuilt from a research notebook into an installable, typed Python package, a Dockerized FastAPI service on Hugging Face Spaces and a React app on Vercel. Greedy or beam-search decoding, with input validation and clear error responses at the API boundary.

- Retrained in TensorFlow on a 120,000-caption COCO 2017 sample with an image-level train/validation split, after finding and fixing a validation bug inherited from the original research code
- **563 pytest tests** (Python 3.10 and 3.11) and **27 Playwright end-to-end tests** run on every change; deployment passes only after the model loads and returns a real caption
- Evaluated with BLEU, METEOR, ROUGE-L and CIDEr; a pre-registered, blinded audit showed most of an apparent BLEU-4 gap against the paper came from the number of reference captions, not the model

---

## Tech Stack

**Languages**

![Python](https://img.shields.io/badge/Python-3670A0?style=flat-square&logo=python&logoColor=ffdd54)
![SQL](https://img.shields.io/badge/SQL-%2307405e?style=flat-square&logo=postgresql&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-%23007ACC?style=flat-square&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-%23323330?style=flat-square&logo=javascript&logoColor=%23F7DF1E)

**Backend & APIs**

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat-square&logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white)
![REST APIs](https://img.shields.io/badge/REST_APIs-%23009688?style=flat-square&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-%2320232a?style=flat-square&logo=react&logoColor=%2361DAFB)
![Next.js](https://img.shields.io/badge/Next.js-black?style=flat-square&logo=next.js&logoColor=white)

**Databases**

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-%23316192?style=flat-square&logo=postgresql&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-%2307405e?style=flat-square&logo=sqlite&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white)
![Alembic](https://img.shields.io/badge/Alembic-migrations-%23455A64?style=flat-square)

**Data & ML**

![pandas](https://img.shields.io/badge/pandas-%23150458?style=flat-square&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-EB6F2D?style=flat-square)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00?style=flat-square&logo=TensorFlow&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)

**Testing & Delivery**

![pytest](https://img.shields.io/badge/pytest-%23ffffff?style=flat-square&logo=pytest&logoColor=2f9fe3)
![Jest](https://img.shields.io/badge/Jest-%23C21325?style=flat-square&logo=jest&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat-square)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-%232088FF?style=flat-square&logo=githubactions&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-%232496ED?style=flat-square&logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![Vercel](https://img.shields.io/badge/Vercel-%23000000?style=flat-square&logo=vercel&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging_Face-Spaces-FFD21E?style=flat-square&logo=huggingface&logoColor=black)

---

## Experience & Education

- **Node2.io** — AI Engineer (Independent Contractor, Founding Contributor) · Jan 2026 – present · PropTech SaaS, remote with a Canada-based team
- **Freelance Software Developer** — independent client projects · 2024 – Dec 2025
- **Quicksilver Technologies Pvt. Ltd.** — ML Engineering Intern · May – Jul 2023 · Python data-processing scripts, debugging tools and unit tests for validation workflows
- **Chandigarh University** — B.E. Computer Science and Engineering, CGPA 7.66/10 · 2024
- **Publication** — [AI Narratives: Bridging Visual Content and Linguistic Expression](https://doi.org/10.1109/ICSPCRE62303.2024.10675203), IEEE ICSPCRE 2024

---

<div align="center">

## GitHub Stats

<img src="https://github-readme-streak-stats.herokuapp.com?user=apoorvrajdev&theme=tokyonight&hide_border=true&date_format=M%20j%5B%2C%20Y%5D" alt="GitHub Streak" />

</div>

---

<div align="center">

*"The model is the easy part — I build the tested software around it."*

</div>
