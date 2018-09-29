# Good Generator`.py`

[![Build Status](https://travis-ci.org/ooz/ggpy.svg?branch=master)](https://travis-ci.org/ooz/ggpy)
[![MIT License Badge](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/ooz/ggpy)

----

Yet another static site generator. Written in Python.
[Why?](https://ooz.github.io/blog/2018/why-i-wrote-yet-another-static-site-gen.html)

It powers its [website](https://ooz.github.io/ggpy), which is its rendered [README.md](https://github.com/ooz/ggpy). Inception!

It also powers my [website](https://ooz.github.io).

## Usage

* Copy `gg.py`, `ggconfig.py`, `Makefile` and `newpost.sh` to the root of your website/blog
* Adjust `ggconfig.py` to your preferences. Since it is an imported Python file, you can use it for preprocessing hooks, too!
* Place markdown files everywhere
* Install dependencies
```
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

* Clone the whole repository
```
git clone https://github.com/ooz/ggpy.git
cd ggpy
```
* Install dependencies (if you have not yet)
```
make init
```
* Test
```
make test
```

## Features

* [Markdown support with various extensions](https://ooz.github.io/ggpy/test/features/)

## License

```
MIT License

Copyright (c) 2018 Oliver Zeit

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