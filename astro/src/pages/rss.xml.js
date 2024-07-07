import rss, { pagesGlobToRssItems } from '@astrojs/rss';
import { config } from '../consts.js';
export const SITE_TITLE = config.SITE_TITLE;
export const SITE_DESCRIPTION = config.SITE_DESCRIPTION;

import {SITE_URL } from '../consts.js';

export async function get() {
  let items = await pagesGlobToRssItems(import.meta.glob('./**/*.md'));

  return rss({
    title: SITE_TITLE,
    description: SITE_DESCRIPTION,
    site: SITE_URL,
    items: items.sort((a, b) => Date.parse(b.pubDate) - Date.parse(a.pubDate)),
    customData: `<language>zh-cn</language>`,
  });
}
