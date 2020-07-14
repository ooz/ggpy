# Good Generator`.py`

[![CircleCI](https://circleci.com/gh/ooz/ggpy.svg?style=shield)](https://circleci.com/gh/ooz/ggpy)
[![MIT License Badge](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/ooz/ggpy)

----

Yet another static site generator. Written in Python.
[Why?](https://ooz.github.io/blog/2018/why-i-wrote-yet-another-static-site-gen.html)

It powers its [website](https://ooz.github.io/ggpy), which is its [README.md](https://github.com/ooz/ggpy) rendered via [circleci](https://circleci.com/gh/ooz/ggpy). An infinite incepted loop!

It also powers [my website](https://ooz.github.io).

## Usage

* Copy `gg.py`, `ggconfig.py` and `Makefile` to the root of your website/blog
* Adjust `ggconfig.py` to your preferences. Since it is an imported Python file, you can use it for preprocessing hooks, too!
* Place markdown files everywhere
* Install dependencies
```
make install_pipenv
make init
```
* Generate your site
```
make
```
* To update your `gg.py` "installation", run (your configuration will not be touched)
```
make update
```

## Tests

* Install dependencies (if you have not yet)
```
make install_pipenv
make init
```
* Run tests with coverage
```
make test
```

## Features

* Static site generator supporting [Markdown with various extensions](https://ooz.github.io/ggpy/test/features/)
* Renders all `*.md` to `*.html` files in the passed directories and recursively in their sub-directories
* Files named `README.md` are converted to `index.html`. Thus, it is fully compatible with GitHub Pages
* Built-in responsive style
* Twitter Card, Open Graph and schema.org support
* Generates `sitemap.xml` with `lastmod` timestamps taken from git history
* Requires `python3`, `pip`, `git` and optionally `make` if you want to use the provided Makefile. Thus, it [runs on Android in Termux](https://oliz.io/blog/2018/code-and-deploy-using-termux.html)
* The provided CircleCI configuration may serve as a blueprint to let CircleCI build your page on every commit

## License

```
MIT License

Copyright (c) 2018-2020 Oliver Z.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
