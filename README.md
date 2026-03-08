# Good Generator`.py`

[![GitHub Actions](https://img.shields.io/github/actions/workflow/status/ooz/ggpy/test-and-deploy.yml?label=build)](https://github.com/ooz/ggpy/actions/workflows/test-and-deploy.yml)
[![GNU AGPLv3 Badge](https://img.shields.io/badge/license-AGPLv3-blue.svg)](LICENSE.txt)
[![MIT License Badge](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.txt)
[![Changelog](https://img.shields.io/badge/-CHANGELOG-blueviolet.svg)](CHANGELOG.html)

----

Yet another static site generator. Written in Python.
[Why?](https://oliz.io/blog/2018/why-i-wrote-yet-another-static-site-gen.html)

It powers [its website](https://oliz.io/ggpy), which is its [README.md](https://github.com/ooz/ggpy) rendered via [CircleCI](https://circleci.com/gh/ooz/ggpy).
An infinite incepted loop!
It also powers [my website](https://oliz.io) and [blog](https://oliz.io/blog/).

## Features

* Static site generator supporting [Markdown with various extensions](https://oliz.io/ggpy/test/features/)
  and [Markdown meta header format](https://oliz.io/ggpy/test/features/meta.html)
* Renders all `*.md` to `*.html` files in the passed directories and recursively in their sub-directories
* Files named `README.md` are converted to `index.html`. Thus, it is fully compatible with GitHub Pages
* It may render a time-stamped index of all generated HTML files, suitable for blogs. Documents may also be inlined into the index, suitable for micro-blogs
* Built-in responsive style with light mode and dark mode
* Open Graph and schema.org support
* Generates `sitemap.xml` with `lastmod` timestamps taken from git history
* Generates `rss.xml` RSS feed
* Requires `python3`, `brew`, and optionally `git` (for more accurate, CI-friendly timestamps) and `make` if you want to use the provided Makefile. Thus, it [runs in Termux on Android](https://oliz.io/blog/2018/code-and-deploy-using-termux.html)
* The provided [GitHub Actions configuration](https://github.com/ooz/ggpy/blob/master/.github/workflows/ci.yml) may serve as a blueprint to let GitHub build your page on every commit

## Usage

* Copy `gg.py`, `ggconfig.py` and `Makefile` to the root of your website/blog
* Adjust `ggconfig.py` to your preferences. Since it is an imported Python file, you can use it for preprocessing hooks, too!
* Place markdown files everywhere
* Install dependencies (requires Homebrew)
```
make install_uv
```
* Generate your site
```
make
```
* To update your `gg.py` "installation", run (your configuration will not be touched)
```
make update
```
* See all make targets with short documentation
```
make help
```

## Tests

* Install dependencies (if you have not yet)
```
make install_uv
```
* Run tests with coverage
```
make test
```

## License

This software is dual-licensed under GNU AGPLv3 or MIT License,
see [LICENSE.txt](https://oliz.io/ggpy/LICENSE.txt) file for details.
