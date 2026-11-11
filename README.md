# MensaWeb ICT website

This is a static multi-page website for MensaWeb ICT.

## Preview locally

Requirements: Python 3.

```bash
python3 build.py
python3 -m http.server 8000
```

Open `http://localhost:8000`.

The default build uses relative links and embeds the CSS and JavaScript in each page, making it easy to preview locally or deploy to static hosting.

## Production clean URLs

For a domain-root deployment with clean URLs:

```bash
python3 build.py --clean
```

This mode uses root-relative paths and shared files in `assets/`. Configure the host to serve directory `index.html` files and use `404.html` as the not-found page.

## Main files

- `build.py` — source of truth for page content, shared templates, metadata and page generation.
- `assets/style.css` — responsive styling and design tokens.
- `assets/site.js` — navigation and contact-form behaviour.
- `assets/favicon.svg` — site favicon.
- `assets/og-image.png` — social-sharing preview image.
- `sitemap.xml` and `robots.txt` — search-engine discovery.

## Before launch

Verify the brand spelling, domain, public email address and phone number in `build.py`. The contact form uses the Formbold endpoint configured in `assets/site.js`; make a real test submission after the domain is live and authorised with the provider. Review the site in current desktop and mobile browsers before launch.
