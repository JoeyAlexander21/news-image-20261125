#!/usr/bin/env python3
"""Build entry.png for make.fun news-image-20261125.

Draws a one-page newspaper front page (1024x1024) with PIL only.
Deterministic: same input -> same bytes (PIL PNG is deterministic for
identical drawing calls). Run: python3 build_image.py
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 243, 232)
INK = (17, 17, 17)
RED = (178, 34, 34)
NAVY = (27, 58, 92)
GREY = (90, 86, 78)
LIGHT = (255, 255, 255)
RULE = (200, 192, 172)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, lines, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 36  # margin

    # ---- top strip ----
    d.rectangle([0, 0, W, 10], fill=RED)
    d.text((M, 22), "WORLD NEWS  •  ONE DAY  •  ONE PAGE",
           font=font(SANS_B, 20), fill=INK)
    d.text((W - M - d.textlength("25 NOV 2026", font=font(SANS_B, 20)),
            22), "25 NOV 2026", font=font(SANS_B, 20), fill=INK)
    d.line([M, 52, W - M, 52], fill=INK, width=2)

    # ---- masthead ----
    title = "THE WORLD TODAY"
    tf = font(SERIF, 76)
    d.text(((W - d.textlength(title, font=tf)) / 2, 58), title,
           font=tf, fill=INK)
    d.line([M, 148, W - M, 148], fill=INK, width=3)

    # ---- date banner ----
    d.rectangle([M, 158, W - M, 216], fill=NAVY)
    date_txt = "WEDNESDAY, 25 NOVEMBER 2026"
    df = font(SANS_B, 40)
    d.text(((W - d.textlength(date_txt, font=df)) / 2, 168), date_txt,
           font=df, fill=LIGHT)
    stand = "Six stories that defined the day — from Riyadh to Sydney, Kyiv to Washington."
    sf = font(SERIF_R, 22)
    # use italic-ish serif regular; centre it
    d.text(((W - d.textlength(stand, font=sf)) / 2, 226), stand,
           font=sf, fill=GREY)

    # ---- lead story: Riyadh ----
    y0 = 262
    d.rectangle([M, y0, W - M, y0 + 210], outline=INK, width=2)
    d.rectangle([M, y0, W - M, y0 + 34], fill=RED)
    d.text((M + 14, y0 + 5), "LEAD STORY  •  MIDDLE EAST",
           font=font(SANS_B, 20), fill=LIGHT)
    lx, ly = M + 14, y0 + 44
    lw = 600
    hl = font(SERIF, 36)
    lines = wrap(d, "Houthi drone hits Riyadh's tallest tower",
                 hl, lw)
    ly = text_block(d, lx, ly, lines, hl, INK, 42)
    body = ("Second strike on the PIF tower in under a week. "
            "Saudi Civil Defence: 11 injured — 2 Saudis, "
            "2 Indians, 3 Nepalese, 4 Egyptians. Coalition "
            "vows a \"decisive\" response.")
    ly = text_block(d, lx, ly + 6, wrap(d, body, font(SANS, 19), lw),
                    font(SANS, 19), INK, 25)
    d.text((W - M - 14 - d.textlength("11 INJURED", font=font(SANS_B, 20)),
            y0 + 5), "11 INJURED", font=font(SANS_B, 20), fill=LIGHT)
    # ---- tower illustration (right of lead) ----
    ix0, iy0 = W - M - 300, y0 + 44
    ibox_h = 210 - 44 - 12
    d.rectangle([ix0, iy0, ix0 + 300, iy0 + ibox_h], fill=(232, 226, 208),
                outline=RULE, width=1)
    base = iy0 + ibox_h - 8
    # small skyline, bottom left
    d.rectangle([ix0 + 16, base - 42, ix0 + 56, base], fill=NAVY)
    d.rectangle([ix0 + 64, base - 58, ix0 + 100, base], fill=(70, 90, 120))
    d.rectangle([ix0 + 108, base - 34, ix0 + 140, base], fill=NAVY)
    # PIF tower: tapered polygon, centre-right
    tx = ix0 + 205
    d.polygon([(tx - 34, base), (tx + 34, base),
               (tx + 16, iy0 + 14), (tx - 16, iy0 + 14)], fill=INK)
    d.rectangle([tx - 6, iy0 + 4, tx + 6, iy0 + 14], fill=RED)
    for yy in range(iy0 + 34, base - 10, 22):
        wdt = 30 - (yy - iy0) // 12
        d.line([tx - wdt, yy, tx + wdt, yy], fill=(120, 118, 110), width=2)
    # impact burst on tower flank
    cx, cy = tx + 36, iy0 + 78
    for dx, dy in [(0, 0), (11, -7), (-10, 5), (7, 11), (-7, -10)]:
        d.ellipse([cx + dx - 6, cy + dy - 6, cx + dx + 6, cy + dy + 6],
                  fill=RED)
    # drone, top right
    d.ellipse([ix0 + 258, iy0 + 16, ix0 + 270, iy0 + 28], fill=INK)
    d.line([ix0 + 250, iy0 + 22, ix0 + 278, iy0 + 22], fill=INK, width=3)

    # ---- grid: 5 stories + ALSO box, 2 cols x 3 rows ----
    gy = y0 + 210 + 12
    cell_w = (W - 2 * M - 16) // 2
    cell_h = 150
    stories = [
        ("ECONOMY  •  AUSTRALIA", "Australia's inflation jumps to 4.9%",
         "CPI rose 4.9% in the year to October, up from 4.3% in "
         "September, the ABS said on 25 Nov. Electricity +25.2%.",
         "4.9%"),
        ("WAR IN UKRAINE  •  BALTIC SEA", "Zelenskyy: Ukraine hit Russian ship",
         "Kyiv says its drone struck the cargo ship Sparta II in "
         "the Gulf of Finland on 21 Nov. Norway urged caution.",
         "SPARTA II"),
        ("TECH  •  UNITED STATES", "Huawei guilty of stealing trade secrets",
         "A New York jury convicted Huawei on 10 of 12 counts, "
         "including trade-secret conspiracy and bank fraud. It will appeal.",
         "10 OF 12"),
        ("SECURITY  •  UNITED STATES", "CIA and ODNI hit by cyberattack",
         "An unclassified system was breached, sources say; no "
         "classified information was affected. The breach is resolved.",
         "UNCLASSIFIED"),
        ("POLITICS  •  WASHINGTON", "Trump gives Giuliani the Medal of Freedom",
         "The President awarded the nation's highest civilian honour "
         "to the former New York mayor in an Oval Office ceremony.",
         "MEDAL OF FREEDOM"),
    ]
    for i, (kick, head, body, chip) in enumerate(stories):
        cx0 = M + (i % 2) * (cell_w + 16)
        cy0 = gy + (i // 2) * (cell_h + 10)
        d.rectangle([cx0, cy0, cx0 + cell_w, cy0 + cell_h],
                    outline=INK, width=2)
        d.text((cx0 + 12, cy0 + 8), kick, font=font(SANS_B, 14), fill=RED)
        d.text((cx0 + cell_w - 12 - d.textlength(chip, font=font(SANS_B, 14)),
                cy0 + 8), chip, font=font(SANS_B, 14), fill=NAVY)
        hl = font(SERIF, 23)
        hlines = wrap(d, head, hl, cell_w - 24)
        hy = cy0 + 30
        hy = text_block(d, cx0 + 12, hy, hlines, hl, INK, 27)
        text_block(d, cx0 + 12, hy + 4,
                   wrap(d, body, font(SANS, 16), cell_w - 24),
                   font(SANS, 16), INK, 20)

    # ALSO box (6th cell)
    ax0 = M + cell_w + 16
    ay0 = gy + 2 * (cell_h + 10)
    d.rectangle([ax0, ay0, ax0 + cell_w, ay0 + cell_h], fill=NAVY)
    d.text((ax0 + 12, ay0 + 8), "ALSO TODAY  •  25 NOVEMBER",
           font=font(SANS_B, 15), fill=(255, 210, 120))
    also = [
        "Sarkozy corruption case ordered to trial in France.",
        "International Day for the Elimination of Violence against Women.",
        "Trump pardons Thanksgiving turkeys Freedom and Feathers.",
    ]
    yy = ay0 + 34
    for item in also:
        for ln in wrap(d, "\u2022  " + item, font(SANS, 17), cell_w - 24):
            d.text((ax0 + 12, yy), ln, font=font(SANS, 17), fill=LIGHT)
            yy += 22
        yy += 4

    # ---- footer ----
    fy = gy + 3 * cell_h + 2 * 10 + 10
    d.line([M, fy, W - M, fy], fill=INK, width=2)
    foot = ("Sources: Reuters, ABS, Bloomberg, AP, CNN, Saudi Civil Defence. "
            "Stories reported on 25 November 2026 in at least one time zone.")
    d.text((M, fy + 8), foot, font=font(SANS, 15), fill=GREY)
    d.text((M, fy + 28),
           "THE WORLD TODAY — one day's world news, on one page.",
           font=font(SERIF_R, 15), fill=GREY)

    img.save("entry.png", optimize=True)


if __name__ == "__main__":
    main()
