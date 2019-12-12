[![CircleCI](https://circleci.com/gh/NMarkgraf/include_exclude.py.svg?style=svg)](https://circleci.com/gh/NMarkgraf/include_exclude.py)
[![StyleCI](https://github.styleci.io/repos/163188282/shield?branch=master)](https://github.styleci.io/repos/163188282)
[![BCH compliance](https://bettercodehub.com/edge/badge/NMarkgraf/include_exclude.py?branch=master)](https://bettercodehub.com/)
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
[![Minimal Python needed: 3.5+](https://img.shields.io/badge/Python-3.5%2B-brightgreen.svg)](https://www.python.org)
[![CodeFactor](https://www.codefactor.io/repository/github/nmarkgraf/include_exclude.py/badge)](https://www.codefactor.io/repository/github/nmarkgraf/include_exclude.py)
[![ORCiD](https://img.shields.io/badge/ORCiD-0000--0003--2007--9695-green.svg)](https://orcid.org/0000-0003-2007-9695)

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

## Using include-/exclude liste with care and without spaces!

```

## A slide {exclude=*, include=tagname1,tagname2,tagname3}

This slide will never be displayed, unless in `tagname1`, `tagname2` or `tagname3` mode!

## A slide {exclude=*, include=tagname1, tagname2,tagname3}

This will cause an unexpected result, as the list ist broken by a fatal *space*! Don't do this, please!

```

