#!/usr/bin/env bash

cat >> draft-to-move.md <<EOF
---
date: $(date --utc +%FT%TZ)
title: New Post
description: New post by me
tags: new
---

## My Post
EOF