#!/usr/bin/env bash
set -euo pipefail

rm -rf dist
mkdir -p dist/client/assets dist/server

cp index.html podcast.html publications.html peter-aiken.html Romain-Lheritier.html riad-hasan.html featured-guests.html press-media.html recognition-awards.html speaking.html impact.html press-releases.html styles.css script.js dist/client/
cp -R assets/. dist/client/assets/
rm -f dist/client/assets/Vihaan_Publication.jpg \
  dist/client/assets/vihaan-tsa-awards.jpeg \
  dist/client/assets/vihaan-state-conference-awards.jpeg \
  dist/client/assets/vihaan-technosphere-2024.jpeg \
  dist/client/assets/vihaan-tsa-speaking.jpeg
cp worker.js dist/server/index.js
