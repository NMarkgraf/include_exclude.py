[![CircleCI](https://circleci.com/gh/NMarkgraf/include_exclude.py.svg?style=svg)](https://circleci.com/gh/NMarkgraf/include_exclude.py)
[![StyleCI](https://github.styleci.io/repos/163188282/shield?branch=master)](https://github.styleci.io/repos/163188282)
[![BCH compliance](https://bettercodehub.com/edge/badge/NMarkgraf/include_exclude.py?branch=master)](https://bettercodehub.com/)
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
[![Minimal Python needed: 3.5+](https://img.shields.io/badge/Python-3.5%2B-brightgreen.svg)](https://www.python.org)


# include_exclude.py

A Pandoc filter, based on panflute, to include or exclude tagged slides.


## A short example of the usage

```

## A slide {include=* exclcude=tagname}

This slide will allways be displayed, but not in `tagname` mode!

```

## An other example

```

## A slide {include=tagname exclude=*}

This slide will never be displayed, but not in `tagname` mode!

```

