---
title: Markdown Feature Test without "quotes bug"
date: 1996-06-06T13:37:42Z
---

## Headline 2

Paragraph
with
non-empty
lines.

## Lists

1. **Ordered list item, bold**
2. *Ordered list item, italic*

----

* Normal unordered list item
* ~~Unordered list item, DELETED!~~
* `Unordered list item, inline coded`

----

- [ ] unchecked
- [x] checked

## Code

```
# Code blocks work
```

```python
def python_code_blocks():
    return "work, too!"
```

Let there be...

    another
    code
    block

## Tables

Tables | work | just | fine
---|---|---:|---
for | real | yep | yeah.

## Quotes

> "So smart"

> "So smart" - me, sometimes

## Image

![Good Generator Logo](https://oliz.io/ggpy/static/gg.png)

Horizontal rule...

----

## Other Markdown Extensions

### Definition Lists and Footnotes

Definition List
:   is defined here[^1].

Other List
:   is defined here[^here].

### Abbreviations

HTML

*[HTML]: Hyper Text Markup Language

## Leftovers

Yep, now the footnotes are arriving!

[^1]: Numbered footnote
[^here]: Labeled footnote