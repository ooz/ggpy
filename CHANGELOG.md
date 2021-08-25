---
title: Changelog
---

## ????-??-??: Version 3.0 (unreleased)

* Remove twitter meta tag support (opengraph is sufficient)
* Change ggconfig social link to arbitrary key-value-map (link label to link)

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
