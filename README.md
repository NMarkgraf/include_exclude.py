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

