// News-image entry for make.fun bounty news-image-20261125.
// "The World Today" — one page, six stories, Wednesday 25 November 2026.
// The image is entry.png beside this file: a one-page newspaper
// front page summing up Wednesday 25 November 2026, drawn with
// build_image.py (PIL) and checked visually before shipping.
// The program only copies that image to /output/entry.png:
// no network, no randomness, same bytes on every run.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in
// for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
copyFileSync(new URL('./entry.png', import.meta.url), join(outDir, 'entry.png'));
