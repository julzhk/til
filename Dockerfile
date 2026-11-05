# Static site served by nginx (https://fly.io/docs/languages-and-frameworks/static/).
# Build the site first: python scripts/build_site.py _site
FROM nginx:alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY _site /usr/share/nginx/html
