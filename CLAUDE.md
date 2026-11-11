# BabySorted social posts — how to prepare a post

This repo holds the content plan, slide templates and published post images for BabySorted
(babysorted.com, a UK baby-gear price comparison site). Images in `posts/` are served publicly
via raw.githubusercontent.com and passed to Metricool as media URLs.

## Rhythm
Two posts every day: 09:00 and 20:00 Europe/London. Posts are prepared in batches on Mon, Wed and Fri, approved
by the owner, then scheduled in Metricool. Runs happen after 09:00 UK, so each batch starts with that day's 20:00 slot
and ends with the 09:00 slot on the day of the next run: Mon = Mon 20:00 to Wed 09:00 (4 posts),
Wed = Wed 20:00 to Fri 09:00 (4 posts), Fri = Fri 20:00 to Mon 09:00 (6 posts).

Lunchtime extras (owner's request, Nov 2026): every day at 13:00 Europe/London, one short Threads post and one fresh Pinterest pin. Not an Instagram post,
and no Instagram Stories. Batches cover the 13:00 slots from the next day up to and including the day of the next run: Mon = Tue, Wed; Wed = Thu, Fri;
Fri = Sat, Sun, Mon. Threads extra: a useful tip or question from a published topic, same Threads rules, no image needed, no link reply needed.
Pinterest extra: a new 2:3 design on an already published topic, never a repeat of an existing pin image, with its own title, description, link, alt text and board.
They don't use a Planned topic or change its Status. Facts still get checked, and they go to the owner for approval with the batch. Don't list them in "Posts so far".

Parenting Tips posts (owner's request, Nov 2026): about 1 carousel in 5, plus lunchtime Threads posts. Pick topics close to something in the catalog or a published article.
Sources: NHS, Best Start in Life, Lullaby Trust. No medical advice or diagnosis: send worries to the GP or health visitor. No judging parents. Avoid contested topics
(breast vs formula, co-sleeping, sleep training). Pinterest board for these: "Baby Care & Development Ideas".

## Workflow for each post

1. **Pick the topic.** Open `plan/content_plan.xlsx`, take the first row whose Status is `Planned`.
   Skip a topic that repeats a post already published (mark it `Skipped (duplicate of …)`).
2. **Make it genuinely useful.** No obvious, generic advice. Every post needs non-obvious, practical
   points a parent would save. Verify every fact, number and safety claim against primary UK sources
   (Lullaby Trust, NHS, RoSPA, Which?, gov.uk). Never invent numbers. List sources for the owner.
   Never recommend supplements or vitamins ourselves (no doses, no "take/give X"): only tell people to ask
   their GP, midwife or health visitor. When a post gives a phone number, say which country it serves and
   whether the call is free or charged.
   Sources (owner's request, Nov 2026): show a `Source:` label only on medical and health advice, safety recommendations, certificates,
   standards and legal rules, and only from NHS, Best Start in Life, Lullaby Trust, RoSPA or gov.uk (e.g. `Source: NHS`). Never a bare name or
   a date on its own. On slides, pins and Pinterest descriptions explain lesser-known names: `Source: RoSPA, the UK accident prevention charity`,
   `Source: The Lullaby Trust, the UK safer baby sleep charity`. NHS stays short. In Threads use the short name only. No label on ordinary buying advice. Which? and other sites that publish SEO articles are for our own fact checks only:
   never name or quote them in posts, and don't use their surveys or test figures as our headline facts. Still list all sources for the owner.
   Brands (owner's request, Nov 2026): never give advice in a brand's name or quote a brand as the authority, and never use one
   brand's limit or figure as general advice. Use independent UK sources. If only makers say something, write "Pushchair makers say"
   with no brand name. Product names belong only to catalog products shown as products.
   Prices (owner's request, Nov 2026): every price on a slide or pin carries `Price on BabySorted, <d Mon YYYY>` (`Prices on ...` for
   several), the date the price was read from our aggregator. Only use prices from our aggregator.
   No prices in captions. Check a price range against the whole catalog, including the most expensive models, not a few examples.
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
   - Colour harmony (owner's request): background, panels, pills and accents must suit the product's own colour.
     Pick the product colour variant (from the catalog) and the brand background together: e.g. green/sage products on
     pink or white, wood/beige on pink or mint, navy/black products on pink or white, white products on navy or deeper pink.
     Avoid putting a product on a panel of nearly the same colour, and avoid more than 2 brand colours plus the product per slide.
     Before sending, view the slides side by side and adjust any slide where colours clash.
   - Covers carry two tags: type (Tips, Buying guide, Comparison, Deals, Checklist, Parenting Tips) + category
     (Pushchairs, Car Seats, Kids Furniture, Nursing & Feeding, or another site catalog category such as Play & Development).
   - Close-up product style is for covers only; inner slides show whole products at a normal size,
     centred in the free space above the text card.
   - Last slide: babysorted.com/links + navy "Link in bio ↑".
   - Deals posts look different from normal posts (owner's request, 11 Nov 2026): navy coupon style from `templates/deals_coupon_navy.py`:
     white tear-off coupons with side notches and a dashed tear line, deeper-pink starburst SAVE badges, a tilted deeper-pink event ribbon
     (e.g. "11.11 DEALS", "BLACK FRIDAY"), the dearer shop's price struck through. Covers and pins stay photo-led. Compare the same product
     and colour across shops in our catalog rather than trusting shop "was" prices (bundle was-prices are often the sum of parts).
   - Instagram API takes max 10 images per carousel.
   - Pinterest: one 2:3 image with all points, no "swipe" pill, no slide dots. Every pin, lunchtime pins too, is photo-led (owner's request, 9 Nov 2026):
     a big baby photo full width across the top (about 45%), then a short title and short one-line points, product small beside the list
     (`pin_hero` in templates/extras.py). Avoid walls of text.
   - Baby photos (owner's request, Nov 2026): add a real baby to covers and last slides so the niche reads at a glance; inner slides stay
     product-led. Make them big (owner's request, 9 Nov 2026): covers and last slides are photo-led, with the photo full width across the top
     (about 60% of the slide) and the product inside the text card, not on the photo; pins carry a large photo too. Library: private artifact https://claude.ai/artifact/SCWMb7rm46mY1QULyosL4X (read files with the Artifact tool, `photos/baby_NN.jpg`).
     The page lists which photos may run. Never put these source files in this public repo. Don't imply the child endorses a product.
     Photos 05, 08 and 14 run only as tight crops that hide the sleep setting, and never in sleep, cot or crib posts. Never show anything else that contradicts safe sleep or car seat advice. Recognisable faces are fine (owner approved these stock photos).
     Photos 16–35 (added 6 Nov 2026) do not run until the owner confirms their source and licence.
5. **Captions.**
   - Instagram: expert tone + marketing hook, plain short English, no blank lines, don't retell the
     slides, ~3 functional emojis (👉 🔗 📌), no affiliate disclosure line, exactly 5 UK-targeted
     hashtags (e.g. #ukmums #pregnancyuk).
   - Pinterest: Title, strong Description, Link (relevant article), alt text. No hashtags.
   - Calls to action (owner's request, Nov 2026): our main selling point is comparing prices, then features. Every call to action on
     slides, pins and captions says compare prices, e.g. "Compare car seat prices at babysorted.com", never "Compare car seats".
   - Threads: one post under 500 characters, no emojis, ends with a question; link goes in a reply
     (Metricool `descendants`); attach the cover; suggest one topic tag.
6. **Send for approval.** Send the slides, pin and all captions to the owner in one message, then send
   a push notification that the post is ready. Do NOT schedule anything before the owner says "ok".
7. **After "ok": publish.** Convert to JPEG, commit to `posts/<YYYY-MM-DD>-<slug>/`, push, check the
   raw URLs return 200. Schedule in Metricool (brand id `7547984`) for the post's planned slot, **09:00 or 20:00
   Europe/London** (next free slot if that time has already passed): Instagram, Pinterest, Threads. Not Facebook.
   Each network is a separate Metricool post, because the captions and images differ.
   Pinterest boards (pass the exact name as boardId):
   Pushchairs → "Pram & Pushchair Tips" · Car Seats → "Car Seat Safety Tips" ·
   Kids Furniture → "Nursery & Safe Sleep Tips" · Nursing & Feeding → "Breastfeeding & Bottle Feeding Tips".
   Deals posts (any category) → "Baby Gear Deals UK". Parenting Tips → "Baby Care & Development Ideas". New board names should not all end in "Tips".
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
- #19 7 nursery mistakes to avoid (30 Oct) · #22 How to choose baby bottles (31 Oct)
- #23 Bugaboo Fox 5 Renew vs Butterfly 2 (1 Nov)
- #24 ISOFIX vs seat belt fitting (3 Nov) · #25 Best high chairs that grow with your child (3 Nov, 20:30)
- #26 Nursery furniture deals before Christmas (4 Nov, 21:05)
- #27 Best bottle sterilisers: steam vs UV (5 Nov, 09:00) · #28 Best compact strollers for travel and flights (5 Nov)
- #29 Best rotating car seats for easy lifting (6 Nov, 09:00)
- #30 Wooden vs plastic high chair (6 Nov) · #31 Bottle feeding starter kit (7 Nov, 09:00) · #32 When to switch from carrycot to seat unit (7 Nov)
- Parenting Tips: Baby hates tummy time? (8 Nov, 09:00) · #33 Why you should never buy a used car seat (8 Nov)
- #35 Nursery furniture you really need (9 Nov, 09:00)
- #36 5 feeding gear mistakes new parents make (9 Nov) · #37 Pram accessories you need and ones you don't (10 Nov, 09:00)
- #38 Best car seats for small cars (10 Nov) · Parenting Tips: #55 Bath time safety in the first year (11 Nov, 09:00)
- Black Friday deals topics #20 and #21 are kept for the week of 20–27 Nov (Black Friday is 27 Nov 2026).
- Boxing Day deals topic #34 is kept for just before 26 Dec.
