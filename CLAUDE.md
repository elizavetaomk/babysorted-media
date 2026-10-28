# BabySorted social posts — how to prepare a post

This repo holds the content plan, slide templates and published post images for BabySorted
(babysorted.com, a UK baby-gear price comparison site). Images in `posts/` are served publicly
via raw.githubusercontent.com and passed to Metricool as media URLs.

## Rhythm
One post every day at 20:00 Europe/London. Posts are prepared in batches on Mon (Mon+Tue), Wed (Wed+Thu)
and Fri (Fri+Sat+Sun), approved by the owner, then scheduled in Metricool.

## Workflow for each post

1. **Pick the topic.** Open `plan/content_plan.xlsx`, take the first row whose Status is `Planned`.
   Skip a topic that repeats a post already published (mark it `Skipped (duplicate of …)`).
2. **Make it genuinely useful.** No obvious, generic advice. Every post needs non-obvious, practical
   points a parent would save. Verify every fact, number and safety claim against primary UK sources
   (Lullaby Trust, NHS, RoSPA, Which?, gov.uk). Never invent numbers. List sources for the owner.
   Never recommend supplements or vitamins ourselves (no doses, no "take/give X"): only tell people to ask
   their GP, midwife or health visitor. When a post gives a phone number, say which country it serves and
   whether the call is free or charged.
3. **Product photos come from the BabySorted catalog.** The site loads products from Supabase
   (`https://khhjsjiltmtrrrkaghif.supabase.co`, table `products`). Take the public anon key from
   `https://babysorted.com/catalog` (it is in the page HTML). Read only — never write to the database.
   Use `image_url` / `images`, pick clean white-background shots, in stock, different models from
   recent posts. Cut out backgrounds with `rembg` (isnet-general-use), fill holes if white parts go
   transparent, check every cut-out visually.
   Article links: `https://babysorted.com/article?slug=<slug>` (table `articles`).
4. **Design.** Templates in `templates/`. Brand: pink `#F1D3DF`, navy `#051F45`, deeper pink
   `#E6B6C9`, mint `#DDF5E3`, white; font Inter; Instagram 1080×1350, Pinterest 1000×1500.
   - Change layout AND background colour from the previous post (pink / navy / white / mint rotate).
   - Covers carry two tags: type (Tips, Buying guide, Comparison, Deals, Checklist) + category
     (Pushchairs, Car Seats, Kids Furniture, Nursing & Feeding).
   - Close-up product style is for covers only; inner slides show whole products at a normal size,
     centred in the free space above the text card.
   - Last slide: babysorted.com/links + navy "Link in bio ↑".
   - Instagram API takes max 10 images per carousel.
   - Pinterest: one 2:3 image with all points, no "swipe" pill, no slide dots.
5. **Captions.**
   - Instagram: expert tone + marketing hook, plain short English, no blank lines, don't retell the
     slides, ~3 functional emojis (👉 🔗 📌), no affiliate disclosure line, exactly 5 UK-targeted
     hashtags (e.g. #ukmums #pregnancyuk).
   - Pinterest: Title, strong Description, Link (relevant article), alt text. No hashtags.
   - Threads: one post under 500 characters, no emojis, ends with a question; link goes in a reply
     (Metricool `descendants`); attach the cover; suggest one topic tag.
6. **Send for approval.** Send the slides, pin and all captions to the owner in one message, then send
   a push notification that the post is ready. Do NOT schedule anything before the owner says "ok".
7. **After "ok": publish.** Convert to JPEG, commit to `posts/<YYYY-MM-DD>-<slug>/`, push, check the
   raw URLs return 200. Schedule in Metricool (brand id `7547984`) for **20:00 Europe/London** on the
   same day (next day if it is already past 20:00 UK): Instagram, Pinterest, Threads. Not Facebook.
   Pinterest boards (pass the exact name as boardId):
   Pushchairs → "Pram & Pushchair Tips" · Car Seats → "Car Seat Safety Tips" ·
   Kids Furniture → "Nursery & Safe Sleep Tips" · Nursing & Feeding → "Breastfeeding & Bottle Feeding Tips".
   Deals posts (any category) → "Baby Gear Deals UK". New board names should not all end in "Tips".
   If Metricool cannot find a board, tell the owner instead of picking another one.
   Then set the plan row Status to `Scheduled <date>` and commit the plan.

## Posts so far
- #1 5 pram mistakes · #2 5 car seat mistakes · #3 Crib vs cot vs cot bed · #4 Breast pump types
- #6 i-Size explained · #7 8 safe sleep checks most parents miss · #9 Pram vs pushchair vs travel system
- #10 Infant carrier vs extended rear-facing seat (22 Oct)
- #11 How to choose a cot mattress (23 Oct) · #13 Best lightweight pushchairs for city life (24 Oct)
- #14 Car seat fitting checklist (25 Oct) · #15 Best bedside cribs for the first 6 months (26 Oct)
- #16 Breastfeeding essentials checklist (27 Oct)
- #17 One-hand fold: why it matters (28 Oct) · #18 When to move to the next car seat (29 Oct)
