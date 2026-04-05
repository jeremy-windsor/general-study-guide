// General Class Ham Radio Study PWA - Service Worker
const CACHE_PREFIX = 'hamradio-general-study-app';
const CACHE_VERSION = '2026-04-05a';
const CACHE_NAME = `${CACHE_PREFIX}-${CACHE_VERSION}`;
const ASSETS = [
  './',
  './index.html',
  './app.js',
  './manifest.json',
  './icon-192.png',
  './icon-512.png',
  '../../pools/2023-2027/questions.json',
  '../../figures/G7-1-schematic-symbols.svg'
];
const APP_BASE_URL = new URL('./', self.location.href);
const PRECACHE_URLS = ASSETS.map(path => new URL(path, APP_BASE_URL).href);
const PRECACHE_URL_SET = new Set(PRECACHE_URLS);
const OFFLINE_URL = new URL('./index.html', APP_BASE_URL).href;

self.addEventListener('install', event => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE_NAME);
    const requests = PRECACHE_URLS.map(url => new Request(url, { cache: 'reload' }));
    await cache.addAll(requests);
  })());
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    const staleKeys = keys.filter(key => key.startsWith(`${CACHE_PREFIX}-`) && key !== CACHE_NAME);

    await Promise.all(staleKeys.map(key => caches.delete(key)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;

  const requestUrl = new URL(event.request.url);
  if (requestUrl.origin !== self.location.origin) return;

  if (event.request.mode === 'navigate') {
    event.respondWith(
      fetch(event.request).catch(() => caches.match(OFFLINE_URL))
    );
    return;
  }

  if (!PRECACHE_URL_SET.has(requestUrl.href)) return;

  event.respondWith(
    caches.match(requestUrl.href).then(cached => {
      if (cached) return cached;
      return fetch(event.request).then(response => {
        if (!response || response.status !== 200 || response.type !== 'basic') return response;
        const clone = response.clone();
        event.waitUntil(
          caches.open(CACHE_NAME).then(cache => cache.put(requestUrl.href, clone))
        );
        return response;
      }).catch(() => caches.match(requestUrl.href));
    })
  );
});
