---
title: Changelog
---

## 2022-04-05: Version 3.1.1

* Fix error if used without a git repo

## 2022-03-27: Version 3.1

* Change default style: no shadows, greater max. logo size
* Drop IE ("X-UA-Compatible" meta tag) support
* Render post tags next to author and date

## 2022-01-16: Version 3.0.1

* Improve determinism of RSS feed sort order (higher last_modified precision)

## 2022-01-02: Version 3.0

* Remove twitter meta tag support (opengraph is sufficient)
* Change ggconfig social link to arbitrary key-value-map (link label to link)
* Remove the 'back' navigation link from posts in the footer.
  If you want to link to your post index, use the new ggconfig social link mechanism.
* Support RSS feed generation. It's limited to the 10 latest posts (by last_modified date)
* Cut-off sitemap after 50000 entries, see https://www.sitemaps.org/faq.html

## 2021-08-22: Version 2.0.1

* Fix filtering single special tag
* Make regular links to blog posts bold

## 2021-08-22: Version 2.0

* Remove `__index_inline_posts__` tag support.
  To inline posts in the index, use `__inline__` tag on the respective post.
* Filter special tags controlling ggpy behavior from the meta `keywords` list

## 2021-07-17: Version 1.3

* Add micro-blog support via new `__index_inline_posts__` tag
* For this, update included CSS
* Improve layout of the regular blog-style post index

## 2021-06-10: Version 1.2

* Update included style:
    - smaller default font-size and line-spacing
    - increase inline code font-size
    - use relative unit for body max-width
    - add footer control for bigger font-size

## 2021-06-06: Version 1.1

* Make `gitpython` dependency optional, degrading last-modified functionality e.g. for sitemap

## 2021-06-06: Version 1.0
