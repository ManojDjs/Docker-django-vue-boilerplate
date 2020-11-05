#!/bin/sh
cd src/
npm cache clean --force
npm install
npm run serve
## yarn install
## yarn serve --host 0.0.0.0
#yarn build --watch --mode=production