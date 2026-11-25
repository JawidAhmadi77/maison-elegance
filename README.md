# Maison Élégance

A luxury fine-dining restaurant platform: a Django REST backend and a
React + TypeScript frontend, kept fully separate and talking over a
versioned API.

Maison Élégance is a **demonstration brand**. The name, address, menu,
prices and reviews in the seed data are editable sample content, marked
as such in the product, ready to be replaced by a real house.

## Layout

```
backend/    Django 5 + DRF. Apps under apps/: core, accounts,
            restaurants, menu, reservations, gallery, reviews, contact
frontend/   React 18 + TypeScript + Vite + Tailwind, React Router,
            TanStack Query, Axios, Framer Motion, React Hook Form + Zod
screenshots/  Captures from the verification walk (see BUILD-REPORT.md)
BUILD-REPORT.md  Phase-by-phase build and verification record
```

## Backend

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
cp .env.example .env            # defaults work locally as-is
.venv/bin/python manage.py migrate
.venv/bin/python manage.py seed_demo     # sample content + dev staff user
.venv/bin/python manage.py runserver 8000
.venv/bin/python -m pytest               # 31 tests
```

- API base: `http://127.0.0.1:8000/api/v1/` — schema at `/api/schema/`,
  Swagger UI at `/api/docs/`, admin at `/admin/`.
- Dev staff login (created by the seed, only while `DEBUG=True`):
  `manager` / `maison-admin-dev`. The staff API uses JWT:
  `POST /api/v1/auth/token/`.
- Database: `DATABASE_URL` decides. Local default is SQLite;
  production sets e.g. `DATABASE_URL=postgresql://user:pass@host/db`.
  The same migrations run on both.
- Email: reservation confirmations are a Celery task. Locally Celery
  runs eagerly (`CELERY_TASK_ALWAYS_EAGER=True`) and the email backend
  is the console backend, so messages print to the server log instead
  of being delivered. In production, set `EMAIL_BACKEND` to SMTP,
  `CELERY_TASK_ALWAYS_EAGER=False`, point `REDIS_URL` at Redis and run
  `celery -A config worker`.

### Reservations, briefly

Slots are generated from the opening-hours table (closed days produce
none; the last seating is closing time minus the 2-hour seating).
Creating a reservation runs in a transaction, locks the candidate
table rows (`select_for_update`), rejects any overlap with a pending
or confirmed booking, assigns the smallest table that fits, and only
then saves — the API cannot return a confirmation for a booking that
does not exist. Guests cancel with their confirmation code + email;
staff manage the night from `/api/v1/reservations/staff/` or the
Django admin (filters and search included).

## Frontend

```bash
cd frontend
npm install
cp .env.example .env            # VITE_API_BASE_URL, points at local Django
npm run dev                     # http://localhost:5173
npm run build                   # type-checks (strict) and builds
```

Pages: Home, Our Story (About, incl. The Experience and private
dining), The Menu (live categories, search, allergen and availability
information, print-friendly), Reservations (live availability,
confirmation codes, cancellation), Gallery (lightbox), Contact
(form, hours, OpenStreetMap embed), and a branded 404.

Design: deep charcoal `#101010` / rich black `#080808`, champagne gold
`#C6A76A`, warm ivory `#F5F0E8`, muted warm gray `#A6A098`; Cormorant
Garamond for display type, Inter for text. Motion uses Framer Motion
and respects `prefers-reduced-motion`.

The site also carries a concierge chatbot (bottom-right, "Maison
Concierge"). It is rule-based, not an LLM: it answers only from the
live API — opening hours and open/closed status, dishes with prices
and ingredients — and it takes real reservations inside the chat
(date, party size, live availability, guest details, then a POST to
the same reservations endpoint, returning the ME- confirmation code),
cancels them the same way, and routes parties over eight to a
private-dining enquiry. The presentation layer adds a first-visit
preloader, gold-curtain page transitions, Lenis inertial scrolling,
a custom cursor and magnetic buttons on fine pointers, a
cursor-following photo reveal on the menu, and a printable
confirmation card — all disabled or simplified on touch devices and
under `prefers-reduced-motion`.

## Photography

All photography is real and licence-clean (Unsplash License and
Pexels License — free to use, attribution not required, given anyway).
Files live in `frontend/public/images/` and are never hotlinked.

| File | Source |
|---|---|
| hero-interior.jpg | Unsplash photo-1517248135467-4c7edcad34c4 |
| interior-two.jpg | Unsplash photo-1552566626-52f8b828add9 |
| chef-plating.jpg | Unsplash photo-1577219491135-ce391730fb2c |
| dish-scallops.jpg | Pexels 1484513 — Valeria Boltneva |
| dish-ashak.jpg | Unsplash photo-1534422298391-e4f8c172dddb |
| dish-pulao.jpg | Unsplash photo-1589302168068-964664d93dc0 |
| dish-wagyu.jpg | Unsplash photo-1600891964092-4316c288032e |
| dish-lamb.jpg | Unsplash photo-1558030006-450675393462 |
| dish-service.jpg | Unsplash photo-1414235077428-338989a2e8c0 |
| dumpling-steamer.jpg | Unsplash photo-1563245372-f21724e3856d |
| dish-sea.jpg | Unsplash photo-1467003909585-2f8a72700288 |
| kitchen-fire.jpg | Unsplash photo-1600565193348-f74bd3c7ccdf |
| dessert-caramel.jpg | Unsplash photo-1551024506-0bccd828d307 |
| table-setting.jpg | Unsplash photo-1519690889869-e705e59f72e1 |
| cocktail-pour.jpg | Unsplash photo-1470337458703-46ad1756a187 |

## Deployment notes

- Backend: gunicorn + `config.wsgi`, `DEBUG=False`, a long random
  `DJANGO_SECRET_KEY`, PostgreSQL via `DATABASE_URL`, Redis + a Celery
  worker for email, `collectstatic`, HTTPS at the proxy (the settings
  enable HSTS/SSL redirects when `DEBUG=False`).
- Frontend: `npm run build`, serve `dist/` as static files with SPA
  fallback to `index.html`, and set `VITE_API_BASE_URL` to the public
  API origin before building.
- Verification helper: with both servers running locally,
  `node walk.mjs` (from `frontend/`) re-runs the headless-Chromium
  page walk and reservation flow and refreshes `../screenshots/`.
