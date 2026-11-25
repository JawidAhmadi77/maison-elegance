# Maison Élégance — Project Structure

The real on-disk layout of the project (generated files and dependency
folders — `node_modules`, `.venv`, `__pycache__`, `.pytest_cache`, `dist`, `.git` — are
left out). The backend and frontend are fully separate and talk over a
versioned REST API (`/api/v1/`).

```text
maison-elegance/
├── backend/
│   ├── apps/
│   │   ├── accounts/
│   │   │   ├── tests/
│   │   │   │   └── __init__.py
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── contact/
│   │   │   ├── migrations/
│   │   │   │   ├── 0001_initial.py
│   │   │   │   └── __init__.py
│   │   │   ├── tests/
│   │   │   │   ├── __init__.py
│   │   │   │   └── test_api.py
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── core/
│   │   │   ├── tests/
│   │   │   │   └── __init__.py
│   │   │   ├── __init__.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── pagination.py
│   │   │   └── permissions.py
│   │   ├── gallery/
│   │   │   ├── migrations/
│   │   │   │   ├── 0001_initial.py
│   │   │   │   └── __init__.py
│   │   │   ├── tests/
│   │   │   │   └── __init__.py
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── menu/
│   │   │   ├── migrations/
│   │   │   │   ├── 0001_initial.py
│   │   │   │   └── __init__.py
│   │   │   ├── tests/
│   │   │   │   ├── __init__.py
│   │   │   │   └── test_api.py
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── reservations/
│   │   │   ├── migrations/
│   │   │   │   ├── 0001_initial.py
│   │   │   │   └── __init__.py
│   │   │   ├── tests/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── test_api.py
│   │   │   │   └── test_services.py
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── services.py
│   │   │   ├── tasks.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── restaurants/
│   │   │   ├── management/
│   │   │   │   ├── commands/
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   └── seed_demo.py
│   │   │   │   └── __init__.py
│   │   │   ├── migrations/
│   │   │   │   ├── 0001_initial.py
│   │   │   │   └── __init__.py
│   │   │   ├── tests/
│   │   │   │   ├── __init__.py
│   │   │   │   └── test_api.py
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── reviews/
│   │   │   ├── migrations/
│   │   │   │   ├── 0001_initial.py
│   │   │   │   └── __init__.py
│   │   │   ├── tests/
│   │   │   │   ├── __init__.py
│   │   │   │   └── test_api.py
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   └── __init__.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── celery.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── media/
│   ├── static/
│   ├── .env.example
│   ├── db.sqlite3
│   ├── manage.py
│   ├── pytest.ini
│   └── requirements.txt
├── docs/
├── frontend/
│   ├── public/
│   │   ├── images/
│   │   │   ├── chef-plating.jpg
│   │   │   ├── cocktail-pour.jpg
│   │   │   ├── dessert-caramel.jpg
│   │   │   ├── dish-ashak.jpg
│   │   │   ├── dish-lamb.jpg
│   │   │   ├── dish-pulao.jpg
│   │   │   ├── dish-scallops.jpg
│   │   │   ├── dish-sea.jpg
│   │   │   ├── dish-service.jpg
│   │   │   ├── dish-wagyu.jpg
│   │   │   ├── dumpling-steamer.jpg
│   │   │   ├── hero-interior.jpg
│   │   │   ├── interior-two.jpg
│   │   │   ├── kitchen-fire.jpg
│   │   │   └── table-setting.jpg
│   │   ├── favicon.svg
│   │   ├── icons.svg
│   │   ├── og-image.jpg
│   │   ├── robots.txt
│   │   └── sitemap.xml
│   ├── src/
│   │   ├── api/
│   │   │   ├── client.ts
│   │   │   └── services.ts
│   │   ├── assets/
│   │   │   ├── hero.png
│   │   │   └── vite.svg
│   │   ├── components/
│   │   │   ├── common/
│   │   │   │   ├── ErrorBoundary.tsx
│   │   │   │   ├── Lightbox.tsx
│   │   │   │   ├── PageHeader.tsx
│   │   │   │   ├── Reveal.tsx
│   │   │   │   ├── SectionHeading.tsx
│   │   │   │   └── Skeleton.tsx
│   │   │   └── layout/
│   │   │       ├── Footer.tsx
│   │   │       └── Navbar.tsx
│   │   ├── hooks/
│   │   │   └── useApi.ts
│   │   ├── pages/
│   │   │   ├── About.tsx
│   │   │   ├── Contact.tsx
│   │   │   ├── Gallery.tsx
│   │   │   ├── Home.tsx
│   │   │   ├── Menu.tsx
│   │   │   ├── NotFound.tsx
│   │   │   └── Reservations.tsx
│   │   ├── types/
│   │   │   └── index.ts
│   │   ├── utils/
│   │   ├── App.tsx
│   │   ├── index.css
│   │   └── main.tsx
│   ├── .env
│   ├── .env.example
│   ├── .gitignore
│   ├── .oxlintrc.json
│   ├── index.html
│   ├── package-lock.json
│   ├── package.json
│   ├── postcss.config.js
│   ├── README.md
│   ├── tailwind.config.js
│   ├── tsconfig.app.json
│   ├── tsconfig.json
│   ├── tsconfig.node.json
│   ├── vite.config.ts
│   └── walk.mjs
├── preview/
├── screenshots/
│   ├── about-desktop.png
│   ├── contact-desktop.png
│   ├── gallery-desktop.png
│   ├── gallery-lightbox.png
│   ├── gallery-mobile.png
│   ├── home-desktop.png
│   ├── home-hero.png
│   ├── home-mobile.png
│   ├── menu-desktop.png
│   ├── menu-mobile.png
│   ├── notfound-desktop.png
│   ├── reservation-confirmation.png
│   ├── reservations-desktop.png
│   └── reservations-mobile.png
├── .gitignore
├── BUILD-REPORT.md
├── README.md
└── STRUCTURE.md
```

## What each top-level area is

- **backend/** — Django 5 + DRF API. Project config in `config/`
  (settings, root URLs, Celery, WSGI/ASGI); the domain lives in
  modular apps under `apps/`:
  - `core/` — shared base model, pagination and permissions used by
    every other app.
  - `accounts/` — staff users and the JWT token endpoints
    (`/api/v1/auth/token/`).
  - `restaurants/` — the restaurant profile, opening hours and social
    links; also holds the `seed_demo` management command that loads
    the sample content and the dev staff user.
  - `menu/` — menu categories and items (ingredients, allergens,
    featured/available flags), public read API plus staff editing.
  - `reservations/` — tables, availability slots and bookings. The
    booking rules live in `services.py` (transaction + row locks,
    overlap rejection); confirmation emails are a Celery task in
    `tasks.py`.
  - `gallery/` — gallery images with categories and display order.
  - `reviews/` — customer reviews, public only once approved.
  - `contact/` — contact-form messages and the newsletter signup.
  Each app carries its own models, serializers, views, urls, admin
  and tests; `pytest.ini` + the per-app `tests/` folders hold the
  31-test backend suite. `db.sqlite3` is the local dev database
  (production uses PostgreSQL via `DATABASE_URL`).
- **frontend/** — React 18 + TypeScript + Vite + Tailwind SPA.
  `src/api/` is the Axios client and service layer, `src/types/` the
  shared API types, `src/hooks/` the TanStack Query hooks,
  `src/components/` the layout (Navbar, Footer) and common pieces
  (Reveal, Lightbox, Skeleton, ErrorBoundary, PageHeader), and
  `src/pages/` one component per route (Home, About, Menu,
  Reservations, Gallery, Contact, NotFound). `public/` holds the
  favicon, the licence-clean photography in `images/`, the OG image,
  `robots.txt` and `sitemap.xml`. `walk.mjs` is the headless-Chromium
  verification script that produced the screenshots.
- **screenshots/** — desktop and mobile captures from the
  verification walk (see BUILD-REPORT.md).
- **docs/** — reserved for project documentation (currently empty).
- **preview/** — local-only previews (GitHub/portfolio mock-ups);
  not part of the product.
- **README.md** — overview, setup for both tiers, the reservations
  rules, photography credits and deployment notes.
- **BUILD-REPORT.md** — the phase-by-phase build and verification
  record, including the test results and honest caveats.
- **.gitignore** — ignores env files, databases, dependency folders
  and build output.
