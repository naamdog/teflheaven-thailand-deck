"""Build image-prompts.csv — one row per image placeholder in the deck.

Prompts follow OpenAI's gpt-image-2 best practices:
- Photo prompts: photography language (35mm film, real grain, real texture),
  consistent style anchor across all images for series cohesion
- Illustration prompts: explicit "flat, editorial, no photorealism" cues
- Text-bearing images: literal text in quotes, "EXACT TEXT" markers
- Structure: subject → environment → lighting → lens → mood → constraints
"""
import csv
import os
from textwrap import dedent

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   'image-prompts.csv')

# Universal style anchor — appended to every PHOTO prompt
PHOTO_ANCHOR = (
    'Shot on 35mm film, real grain, warm color grading, deep navy '
    'shadows (#1a1a2e), accents of amber gold (#e8a020). Documentary '
    'editorial photography aesthetic, Cereal Magazine / Monocle / '
    'Kinfolk reference. No stock-photo polish, no posed smiles, '
    'no fake bokeh. Natural light only. Real authentic textures and '
    'imperfections. Photorealistic.'
)

PORTRAIT_ANCHOR = (
    'Shot on 35mm film, 50mm lens, shallow depth of field, real grain, '
    'real skin texture (pores, light wrinkles, faint freckles), warm '
    'natural daylight. Editorial documentary portrait, candid not '
    'staged. No glossy retouching, no laser-white teeth, no studio '
    'polish. Photorealistic.'
)


def p(body, anchor=PHOTO_ANCHOR, aspect='16:9'):
    return dedent(body).strip() + '\n\n' + anchor + f' Aspect ratio {aspect}.'


ROWS = [
    # =========== SLIDE 1 — COVER ==============
    dict(
        slide=1, slide_title='Cover',
        filename='01-cover-bangkok-wat-arun.jpg',
        aspect='16:9', resolution='2560x1440', quality='high',
        purpose='Full-bleed hero behind cover headline',
        prompt=p('''
            Photorealistic cinematic wide shot of Bangkok at golden
            hour, viewed across the Chao Phraya river. Wat Arun
            temple silhouetted in warm amber dusk light, the river
            reflecting the burning sky. A single wooden long-tail
            boat drifts in the middle distance. The skyline in the
            background fading to soft purple. 35mm lens, side-light
            from the setting sun, shallow depth of field on the
            boat. No people in the foreground. Mood: monumental,
            wistful, the quiet moment before a story begins.
        '''),
    ),

    # =========== SLIDE 3 — FOUNDER ==============
    dict(
        slide=3, slide_title='A Note from Mike',
        filename='03-mike-portrait.jpg',
        aspect='3:4', resolution='1600x2133', quality='high',
        purpose='Left-half portrait of founder Mike Maitland',
        prompt=p('''
            Photorealistic portrait of a Western man in his late
            40s with short greying hair, a light beard, and warm
            blue eyes. Casual blue button-up shirt, sleeves rolled.
            He sits in a sunlit Thai cafe, soft window light from
            his right side. Looking slightly off-camera, a
            contemplative half-smile, the way someone looks when
            they're about to tell you a true story. Real skin
            texture, faint laugh-lines around the eyes, not posed.
            A cup of Thai iced tea on the table, slightly blurred
            in foreground. Background blurred warmly.
        ''', anchor=PORTRAIT_ANCHOR, aspect='3:4'),
    ),

    # =========== SLIDE 5 — WHY THAILAND ==============
    dict(
        slide=5, slide_title='Why Thailand',
        filename='05-night-market.jpg',
        aspect='3:2', resolution='2400x1600', quality='high',
        purpose='Right-side hero behind reasons panel',
        prompt=p('''
            Photorealistic candid wide shot of a Thai street night
            market in full swing. Strings of warm paper lanterns
            overhead glowing amber, a wok of pad thai mid-toss with
            steam rising and orange flames briefly licking up.
            Locals and travellers walking between stalls in soft
            motion blur, a cyclist passing through frame. Deep navy
            night sky above. A sliver of a temple roof in the far
            distance. 35mm lens, low angle from chest height,
            shallow depth of field on the stall in foreground.
            Mood: alive, sensory, the smell of chilli and lime
            almost visible.
        ''', aspect='3:2'),
    ),

    # =========== SLIDE 6 — DAY IN LIFE COLLAGE ==============
    dict(
        slide=6, slide_title='A Day in Your Life — tuk-tuk',
        filename='06a-tuktuk.jpg',
        aspect='16:9', resolution='1920x1080', quality='high',
        purpose='Top of collage, larger frame',
        prompt=p('''
            Photorealistic candid photograph of a brightly painted
            three-wheeled Bangkok tuk-tuk parked on a side-street at
            golden hour. The driver leans against the seat,
            mid-laugh, talking to someone off-frame. Background
            full of motorbikes, street vendors, signs in Thai
            script in soft motion blur. Warm side-light from the
            late sun. 35mm lens, shallow depth of field on the
            tuk-tuk paintwork showing scratches and metallic wear.
            Mood: kinetic, generous, ordinary-magical.
        '''),
    ),
    dict(
        slide=6, slide_title='A Day in Your Life — beach',
        filename='06b-beach.jpg',
        aspect='1:1', resolution='1200x1200', quality='high',
        purpose='Bottom-left of collage',
        prompt=p('''
            Photorealistic candid wide shot of two friends walking
            barefoot along a tropical Thai beach at sunset, seen
            from behind. Coconut palms framing the right side.
            Calm sea reflecting amber and rose sky. Long shadows in
            soft sand with visible footprint texture. Unposed,
            walking away from camera. 35mm lens, real lens flare
            from the low sun. Mood: easy, end-of-day, the kind of
            friendship made in a single intake week.
        ''', aspect='1:1'),
    ),
    dict(
        slide=6, slide_title='A Day in Your Life — rooftop',
        filename='06c-rooftop.jpg',
        aspect='1:1', resolution='1200x1200', quality='high',
        purpose='Bottom-right of collage',
        prompt=p('''
            Photorealistic candid shot of a small group of friends
            (mixed nationalities, late 20s) gathered on a Bangkok
            rooftop bar at dusk. The city skyline glowing in the
            background. String lights overhead, sweating cocktail
            glasses, easy laughter mid-conversation, no one looking
            at the camera. 50mm lens, shallow depth of field on a
            speaker mid-gesture, others in soft focus. Real skin
            texture, real fabric wear on a denim jacket. Mood:
            belonging, the cohort that became friends.
        ''', aspect='1:1'),
    ),

    # =========== SLIDE 9 — ORIENTATION WEEK ==============
    dict(
        slide=9, slide_title='Orientation Week',
        filename='09-orientation-temple.jpg',
        aspect='4:5', resolution='1600x2000', quality='high',
        purpose='Left-half image of cohort at a Thai temple',
        prompt=p('''
            Photorealistic candid photograph of a small group
            (15–20 people, late 20s, mixed nationalities, sitting
            in a row with shoes off) at a Thai temple during
            cohort orientation week. They are listening to a Thai
            monk seated in front, soft amber afternoon light
            filtering through temple columns. Stone floor with
            visible texture. Some in casual cotton shirts, one
            woman in a respectful shawl over her shoulders. Eyes
            on the monk, not the camera. 35mm lens, soft golden
            backlight. Mood: humbled, attentive, the second day
            of the rest of their life.
        ''', aspect='4:5'),
    ),

    # =========== SLIDE 10 — TESOL CLASSROOM ==============
    dict(
        slide=10, slide_title='TESOL Course',
        filename='10-tesol-classroom.jpg',
        aspect='4:5', resolution='1600x2000', quality='high',
        purpose='Right-half image of TESOL course in session',
        prompt=p('''
            Photorealistic candid photograph of a TESOL training
            classroom in Hua Hin. A young Western trainee teacher
            (late 20s, casual smart attire) stands at a whiteboard
            mid-lesson, pointing at a grammar chart, laughing at
            something a peer just said. The other 8–12 trainees
            sit at desks watching, a few with laptops, real focus
            on their faces. The trainer (an older British woman in
            her 50s, glasses, warm presence) sits to the side
            with a clipboard. Bright Thai afternoon light through
            open windows. Real wear on the whiteboard, marker
            stains. 35mm lens, slight side angle, real grain.
            Mood: real classroom, real learning, real cohort.
        ''', aspect='4:5'),
    ),

    # =========== SLIDE 11 — ACCREDITATION LOGOS ==============
    dict(
        slide=11, slide_title='Accreditation — TQUK',
        filename='11a-tquk.png',
        aspect='1:1', resolution='600x600', quality='medium',
        purpose='Official TQUK logo on light background',
        prompt='''Use the official TQUK (Training Qualifications UK) logo
        — download from the awarding body. DO NOT generate. This is a
        registered trademark. Place on a clean white #ffffff or pale
        grey #f5f5f5 background, centered, with ~20% margin around the
        logo. Output as transparent PNG.'''.strip(),
    ),
    dict(
        slide=11, slide_title='Accreditation — Trinity',
        filename='11b-trinity.png',
        aspect='1:1', resolution='600x600', quality='medium',
        purpose='Trinity College London-tier badge',
        prompt='''Use the official Trinity College London logo (if your
        TESOL is Trinity-accredited) OR a custom-designed editorial
        "Trinity-tier course design" badge: a circular mark, navy
        outline #1a1a2e on white background, inside the circle the
        text "TRINITY-TIER" in DM Mono uppercase amber, plus a small
        academic-style emblem. Transparent PNG.'''.strip(),
    ),
    dict(
        slide=11, slide_title='Accreditation — Ofqual',
        filename='11c-ofqual.png',
        aspect='1:1', resolution='600x600', quality='medium',
        purpose='Ofqual-regulated badge',
        prompt='''Use the official Ofqual logo OR design a small badge
        marker: text "Ofqual-Regulated" in navy #1a1a2e DM Sans on
        white #ffffff, with a small crown / accent in amber #e8a020.
        Transparent PNG.'''.strip(),
    ),

    # =========== SLIDE 17 — MAP ILLUSTRATION ==============
    dict(
        slide=17, slide_title='Map of Thailand',
        filename='17-map-illustration.png',
        aspect='4:3', resolution='1600x1200', quality='high',
        purpose='Left-half hand-drawn map illustration',
        prompt=dedent('''
            Editorial hand-drawn line-art map illustration of
            Thailand, on a soft cream background (#f5f5f5).
            Country outline in deep navy ink #1a1a2e, single-weight
            0.8pt clean line, hand-drawn warmth — NOT vector-flat.
            Eight small filled amber circles (#e8a020, ~8mm
            diameter) marking placement cities, each labelled
            beside the dot in small Playfair Display serif dark
            navy: "Bangkok", "Hua Hin", "Chiang Mai", "Phuket",
            "Korat", "Udon Thani", "Pattaya", "Sukhothai".
            Subtle compass rose in the bottom-right corner.
            Tiny DM Mono coordinate labels in the corners
            ("13°45′N", "100°30′E").
            Small caption bottom-center: "FIG. 02 — KINGDOM OF
            THAILAND" in DM Mono uppercase tracked.
            Style: minimalist editorial cartography, magazine-
            quality line-art, hand-drawn feel — NO photorealism,
            NO shading, NO gradients, NO 3D, NO topography.
            Output as transparent PNG.
        ''').strip(),
    ),

    # =========== SLIDE 18 — SCHOOL TYPES ==============
    dict(
        slide=18, slide_title='Schools — government',
        filename='18a-school-government.jpg',
        aspect='16:10', resolution='1920x1200', quality='high',
        purpose='Top of card 1 — government school classroom',
        prompt=p('''
            Photorealistic candid photograph inside a Thai
            government primary classroom. A young Western English
            teacher (late 20s, smart-casual button-up shirt — no
            tie) standing among rows of uniformed Thai children
            aged 8–10. The children are mid-laugh at something the
            teacher said; some have hands raised. Bright natural
            daylight from large barred windows on the right. Worn
            wooden desks with carved initials, chalkboard with
            English alphabet and a half-erased sentence. Real
            fabric wear on the uniforms. 35mm lens, slightly low
            angle from the back of the room. Mood: warm, alive,
            real teaching, no performance.
        ''', aspect='16:10'),
    ),
    dict(
        slide=18, slide_title='Schools — private',
        filename='18b-school-private.jpg',
        aspect='16:10', resolution='1920x1200', quality='high',
        purpose='Top of card 2 — private/language school',
        prompt=p('''
            Photorealistic photograph of a modern Thai private
            language-school classroom. A small group of Thai
            teenagers (4–6 students, ages 13–16, in neat polo
            uniforms) gathered around a circular table working on
            English worksheets. A young Western teacher pointing
            at a whiteboard mid-sentence. Modern bright space —
            wooden floors, white walls, large floor-to-ceiling
            windows with diffused afternoon light. 35mm lens,
            shallow depth of field on the worksheet in the
            foreground, students in soft focus. Mood: focused,
            warm, well-resourced.
        ''', aspect='16:10'),
    ),

    # =========== SLIDE 20 — ACCOMMODATION ==============
    dict(
        slide=20, slide_title='Accommodation — Hua Hin',
        filename='20a-huahin-accom.jpg',
        aspect='16:10', resolution='1920x1200', quality='high',
        purpose='Top of card 1 — orientation accommodation',
        prompt=p('''
            Photorealistic interior photograph of a simple, clean
            Thai apartment bedroom in Hua Hin used as TESOL course
            accommodation. A neatly made bed with crisp white
            linen, bamboo blinds filtering soft afternoon light,
            a small writing desk with a laptop and a coffee mug,
            an open packing rucksack on the floor. Tile floors,
            white walls. 35mm lens, natural color, soft
            directional light from the right. Mood: arrived,
            settled, the first week of the rest of your life.
        ''', aspect='16:10'),
    ),
    dict(
        slide=20, slide_title='Accommodation — Bangkok apartment',
        filename='20b-bangkok-apt.jpg',
        aspect='16:10', resolution='1920x1200', quality='high',
        purpose='Top of card 2 — placement apartment',
        prompt=p('''
            Photorealistic interior of a modern, mid-range Bangkok
            one-bed apartment living area. Tile floors, an open
            balcony door overlooking a low-rise neighbourhood with
            palm trees and distant skyscrapers. A small kitchenette
            to one side. Late afternoon sunlight streaming through
            the doorway, casting long warm shadows across the
            floor. A potted monstera in the corner, a guitar
            leaning against the wall. No people. 35mm lens,
            natural light, real scuffs on the wall. Mood:
            settled-in, lived-in.
        ''', aspect='16:10'),
    ),

    # =========== SLIDE 30 — THE TEAM ==============
    dict(
        slide=30, slide_title='Team — Mike (founder)',
        filename='30a-mike.jpg',
        aspect='1:1', resolution='1024x1024', quality='high',
        purpose='Circular team portrait — founder Mike',
        prompt=p('''
            Photorealistic square portrait of the same Western man
            from slide 3 (Mike Maitland) — late 40s, short greying
            hair, light beard, warm blue eyes. Casual blue
            button-up shirt. Soft daylight from the left. Looking
            directly at the camera with a genuine, easy half-smile.
            Real skin texture, faint laugh-lines. Plain warm cream
            background (#f5f0e8). Square framing — head and
            shoulders centered for circular crop.
        ''', anchor=PORTRAIT_ANCHOR, aspect='1:1'),
    ),
    dict(
        slide=30, slide_title='Team — Placement Lead',
        filename='30b-team-2.jpg',
        aspect='1:1', resolution='1024x1024', quality='high',
        purpose='Circular team portrait — placement lead',
        prompt=p('''
            Photorealistic square portrait of a Western woman in
            her early 40s with shoulder-length brown hair, a warm
            wide smile, a few subtle laugh lines. Wearing a soft
            green cardigan. Soft daylight from the right. Plain
            warm cream background (#f5f0e8). Looking directly at
            camera, calm professional energy. Square framing —
            head and shoulders centered for circular crop.
        ''', anchor=PORTRAIT_ANCHOR, aspect='1:1'),
    ),
    dict(
        slide=30, slide_title='Team — In-country Hua Hin',
        filename='30c-team-3.jpg',
        aspect='1:1', resolution='1024x1024', quality='high',
        purpose='Circular team portrait — in-country coordinator',
        prompt=p('''
            Photorealistic square portrait of a Thai woman in her
            mid-30s, warm smile, hair tied back. Wearing a simple
            white linen shirt. Bright Thai daylight from the left.
            Plain warm cream background (#f5f0e8). Confident,
            welcoming presence. Square framing — head and
            shoulders centered for circular crop.
        ''', anchor=PORTRAIT_ANCHOR, aspect='1:1'),
    ),
    dict(
        slide=30, slide_title='Team — Marketing & Earn-Back',
        filename='30d-team-4.jpg',
        aspect='1:1', resolution='1024x1024', quality='high',
        purpose='Circular team portrait — marketing lead',
        prompt=p('''
            Photorealistic square portrait of a Western man, late
            20s, slightly tousled hair, a small visible tattoo on
            the side of his neck, a relaxed grin showing he's the
            creative on the team. Plain T-shirt under a denim
            shirt. Soft daylight from the right. Plain warm cream
            background (#f5f0e8). Square framing for circular crop.
        ''', anchor=PORTRAIT_ANCHOR, aspect='1:1'),
    ),

    # =========== SLIDE 31 — TESTIMONIAL PORTRAITS ==============
    dict(
        slide=31, slide_title='Testimonial A',
        filename='31a-teacher-A.jpg',
        aspect='1:1', resolution='1024x1024', quality='high',
        purpose='Circular testimonial portrait',
        prompt=p('''
            Photorealistic candid square portrait of a young
            Western woman in her late 20s, smiling warmly at the
            camera, in a bright Thai classroom. Wearing a simple
            light cotton blouse, hair tucked behind one ear. Real
            skin texture, faint freckles, natural unstyled hair,
            no make-up beyond the basics. Side-light through
            windows on her left, warm tones. Plain blurred
            classroom in the background. Square framing —
            head and shoulders centered for circular crop.
        ''', anchor=PORTRAIT_ANCHOR, aspect='1:1'),
    ),
    dict(
        slide=31, slide_title='Testimonial B',
        filename='31b-teacher-B.jpg',
        aspect='1:1', resolution='1024x1024', quality='high',
        purpose='Circular testimonial portrait',
        prompt=p('''
            Photorealistic candid square portrait of a young
            Western man, late 20s, with tousled hair and a small
            tattoo visible on his upper arm. Standing on a Thai
            beach at golden hour, in a faded cotton t-shirt,
            gentle half-smile, eyes slightly squinting in the low
            sun. Sand grains visible on his collarbone. The
            blurred sea behind. Real skin texture, subtle sunburn
            on his nose. Square framing for circular crop.
        ''', anchor=PORTRAIT_ANCHOR, aspect='1:1'),
    ),
    dict(
        slide=31, slide_title='Testimonial C',
        filename='31c-teacher-C.jpg',
        aspect='1:1', resolution='1024x1024', quality='high',
        purpose='Circular testimonial portrait',
        prompt=p('''
            Photorealistic candid square portrait of a young
            woman of South Asian descent, mid-20s, sitting at an
            outdoor Bangkok cafe table with a glass of iced Thai
            tea in her hand, looking just past the camera with a
            quiet smile. Soft afternoon window light, real skin
            texture. Background: blurred cafe greenery and
            warm-toned brick wall. Square framing for circular
            crop.
        ''', anchor=PORTRAIT_ANCHOR, aspect='1:1'),
    ),

    # =========== SLIDE 43 — APPLY CTA HERO ==============
    dict(
        slide=43, slide_title='Apply hero',
        filename='43-island-sunset.jpg',
        aspect='16:9', resolution='2560x1440', quality='high',
        purpose='Full-bleed CTA hero — tropical sunset',
        prompt=p('''
            Photorealistic cinematic wide shot of a tropical Thai
            beach at sunset on Koh Samui. The sea calm and
            reflective, soft pink and amber sky, coconut palms
            framing the foreground from the right side, fronds
            slightly silhouetted. Two distant figures walking
            barefoot along the shoreline, small in the frame,
            facing away. Real wet-sand reflections of the sky.
            35mm lens, very low angle near the wet sand for
            reflection. Real grain, real lens flare from the low
            sun. Mood: the door at the end of the corridor —
            open it.
        '''),
    ),

    # =========== SLIDE 43 — QR CODE ==============
    dict(
        slide=43, slide_title='Apply QR code',
        filename='43-qr.png',
        aspect='1:1', resolution='600x600', quality='medium',
        purpose='Real QR code linking to apply page',
        prompt='''DO NOT generate with gpt-image-2. Use a real QR generator
        (qr-code-generator.com, qrtiger.com, or any library like
        python-qrcode). Encode the URL: https://teflheaven.com/apply
        (or your actual apply form URL — likely
        https://teflheaven.wufoo.com/forms/wfey5l00uk6yk3/).
        Style: pure black #1a1a2e modules on white #ffffff
        background. No logo embedded. Save as PNG. 600x600px
        minimum.'''.strip(),
    ),
]


fieldnames = [
    'slide_num', 'slide_title', 'image_purpose', 'filename',
    'aspect_ratio', 'resolution', 'quality', 'prompt'
]

with open(OUT, 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    w.writeheader()
    for r in ROWS:
        w.writerow({
            'slide_num':    r['slide'],
            'slide_title':  r['slide_title'],
            'image_purpose': r['purpose'],
            'filename':     r['filename'],
            'aspect_ratio': r['aspect'],
            'resolution':   r['resolution'],
            'quality':      r['quality'],
            'prompt':       r['prompt'],
        })

print(f'Wrote {len(ROWS)} image prompts to:')
print(f'  {OUT}')
