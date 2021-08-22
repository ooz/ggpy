---
title: Markdown Meta Data
description: Meta data format and supported options
date: 2021-04-04T18:59:03Z
tags: documentation
---

`ggpy` supports Markdown meta headers at the beginning of each file, e.g. for this document:

```
---
title: Markdown Meta Data
description: Meta data format and supported options
date: 2021-04-04T18:59:03Z
tags: documentation
---

`ggpy` supports Markdown meta headers [...]
```

Tags may be separated by commas or with a separate key, spaces are ignored, e.g.:

```
---
tags: topic, other
tags: __draft__
---
```

...produces three tags `topic`, `other` and `__draft__`

## Meta Keys

All keys are optional:

| Key | Description |
|-----|-------------|
| `title` | Document title |
| `description` | Short description or summary of the document |
| `date` | Creation date of the document |
| `tags` | List of tags. Some tags may have special effects (see below). This key may be used multiple times (see example above). |

## Special Tags

Special tags may be used to configure `ggpy`'s behavior. Such tags always start and end with double underscore (`__`, also called "dunder" in the Python world):

| Tag | Description/Effect |
|-----|--------------------|
| `__draft__` | Marks a document as "draft". Drafts are not included in the generated sitemap or index |
| `__index__` | Document should be an index of all documents. Other markdown content of the file is then ignored, not rendered |
| `__inline__` | Inline document in the index generated with `__index__`. Absolute links for images are advised, to not break rendering in the index and as a separate document. |
| `__no_meta__` | Don't render machine-readable meta data for social media etc. |
| `__no_header__` | Omit the page header with site icon, title headline, author and date |
| `__no_footer__` | [Omit the page footer with navigation, theme control and social links](no-footer/) |
