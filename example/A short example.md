---
title: "A short Example"
author: "NM"
date: "26.12.2018"
output: pdf_document
tag:
- tag1
- tag3
---

## A short Example

This is a short example of the `include_exclude.py` pandoc filter.


## This slide will not be displayed {exclude=all}

As we have the attribute `exclude=all`, this slide will not be displayed ever!


## This slide will not be displayed but in tag2 mode! {exclude=all include=tag2}

As we have the attribute `exclude=all`, this slide will not be displayed ever, except if we are in `tag2`-mode, because of the attribute `include=tag2`!

## This slide will not be displayed but in tag1 or tag2 mode! {exclude=all include=tag1,tag2}

As we have the attribute `exclude=all`, this slide will not be displayed ever, except if we are in `tag1`- or `tag2`-mode, because of the attribute `include=tag1,tag2`!

Remember **not** to add ** space** after a list element! So please try:

```
## ... {exclude=all include=tag1,tag2}
```

instead of 

```
## .. {exclude=all include=tag1, tag2}
```
because the later won't work as expected!


## This slide will not be displayed but in tag1 or tag2 mode! {exclude=all include=tag1, tag2}

As we have the attribute `exclude=all`, this slide will not be displayed ever, except if we are in `tag1`- or `tag2`-mode, because of the attribute `include=tag1,tag2`!



## This slide will not be displayed but in tag1 mode! {exclude=all include=tag1}

As we have the attribute `exclude=all`, this slide will not be displayed ever, except if we are in `tag1`-mode, because of the attribute `include=tag1`!


## This will not be displayed in `tag1`-mode {exclude=tag1}

As we have the attribute `exclude=tag1`, this slide will not be displayed in `tag1`-mode!


## This will not be displayed in `tag2`-mode {exclude=tag2}

As we have the attribute `exclude=tag2`, this slide will not be displayed in `tag2`-mode!


## This will not be displayed in `tag3`-mode {exclude=tag3}

As we have the attribute `exclude=tag3`, this slide will not be displayed in `tag3`-mode!

\[x^2\]

## This is the End!

At least of this short example.
