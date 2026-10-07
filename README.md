# Fisherman's Charm: landing page

A static, dependency-free page for Fisherman's Charm: `index.html` (inline CSS and a few lines of JS) and
`img/`. Open `index.html` in a browser, or serve the folder (`python3 -m http.server`).

## Before it goes live

- **Store link:** the two "coming soon" buttons are placeholders (`aria-disabled`). Point them at the App Store
  page once there is one, and change the headings from "Coming soon".
- **Email sign-up:** set `SIGNUP_URL` at the bottom of `index.html` to a form endpoint (Formspree, Buttondown,
  Mailchimp...). While it is empty the sign-up form stays hidden.
- **Link previews:** make `og:image` an absolute URL (`https://your-domain/img/og.jpg`).
- **Claims:** the page says *no ads* and *no timers*, and shows no price yet. Change them if the plan changes.
- **Hosting:** any static host works (GitHub Pages from the repository root, Netlify, Cloudflare Pages). The page only carries screenshots and the key art, never the licensed art packs from the game repository.

## The images

`img/shot-*.webp` are real in-game screenshots: the game's 405x720 window doubled to 810x1440 with
nearest-neighbour scaling, saved as lossless WebP (the sea chart, all parchment texture, as lossy). They
come from a staged save well into the game (the game's `Debug._setup("rich")` plus the dog named Biscuit,
every giant beaten, charms worn and an aquarium at home), captured scene by scene with the game's
screenshot helper (`tools/art_shots.gd`'s `_visit`):

- `shot-reel`: a reel at Coral Lagoon, the fish Darting and Heavy, in its driftwood frame
- `shot-dog`: the tutorial, Marlow spotting the fisherman's charm on the pup's bandana (`tools/ui_test_tutorial.tscn`, two lines on)
- `shot-island`: walking up to Pip on the home island, "Talk to Pip" showing, the pup alongside
- `shot-prep`: Prepare at Coral Lagoon, rain at dusk, with the recommendations
- `shot-map`, `shot-journal`, `shot-charms`, `shot-home`, `shot-bar`: those screens on the same save
- `shot-catch`: a legendary Blue Lobster landed at Abyssal Reef at night

`hero.webp` (1672 wide) and `hero-960.webp` (for phones) are the hero picture, pixel art of the boy and his
pup on the pier at sunset, shown full width with a slow parallax drift (off under reduced motion).

`og.jpg` and `icon.png` are built from the game repository (expected next to this one, at `../fisherman-charm`) by:

```bash
python3 tools/build_images.py            # or: python3 tools/build_images.py path/to/fisherman-charm
```

- `og.jpg`: the 1200x630 link preview: the pixel key art's sunset sky and sea run the full width, the fisher,
  the pup and the pier on the right, the game's logo on the left.

`logo.webp` (1200 wide) and `logo-720.webp` are the game's logo (`assets/art/logo.png`), the hero's title.
- `icon.png`: the app icon (`icon.png`).
