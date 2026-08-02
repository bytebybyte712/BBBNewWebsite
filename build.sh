#!/usr/bin/env bash
set -euo pipefail

rm -rf dist
mkdir -p dist/client/assets dist/server

cp index.html about.html podcast.html publications.html peter-aiken.html Romain-Lheritier.html styles.css script.js dist/client/
cp -R assets/. dist/client/assets/
cp worker.js dist/server/index.js
