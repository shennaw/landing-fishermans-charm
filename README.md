# Fisherman's Charm: landing page

A static, dependency-free page for Fisherman's Charm: `index.html` (inline CSS and a few lines of JS) and
`img/`. Open `index.html` in a browser, or serve the folder (`python3 -m http.server`).

## Before it goes live

- **Store link:** the two "coming soon" buttons are placeholders (`aria-disabled`). Point them at the App Store
  page once there is one, and change the headings from "Coming soon".
- **Email sign-up:** set `SIGNUP_URL` at the bottom of `index.html` to a form endpoint (Formspree, Buttondown,
  Mailchimp...). While it is empty the sign-up form stays hidden.
- **Link previews:** make `og:image` an absolute URL (`https://your-domain/img/og.jpg`).
- **Claims:** the page says *$3.99*, *no ads* and *no timers*. Change them if the plan changes.
- **Hosting:** any static host works (GitHub Pages from the repository root, Netlify, Cloudflare Pages). The page only carries screenshots and the key art, never the licensed art packs from the game repository.

## The images

`img/shot-*.webp` are real in-game screenshots at 810x1440, captured with the debug flags:

```bash
godot --path . --resolution 810x1440 -- --setup=mid --dog --scene=island --spawn=bar --shot=island.png --frames=100
godot --path . --resolution 810x1440 -- --setup=mid --dog --scene=fishing --island=0 --autoreel --frames=104 --shot=reel.png
```

(`--scene=map|bar|home|encyclopedia|charms` for the others; the pup shot comes from `tools/ui_test_tutorial.tscn`.)
`key-art.webp` and `og.jpg` come from `assets/art/key_art.png`; `icon.png` is the app icon.
