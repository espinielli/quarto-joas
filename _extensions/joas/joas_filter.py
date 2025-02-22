#!/usr/bin/env python

"""
Pandoc filter for JOAS papers
"""

from pandocfilters import toJSONFilter, Str


def caps(key, value, format, meta):
    if key == "MetaInlines":
        return value.append({"t": "Str", "c": "; "})


if __name__ == "__main__":
    toJSONFilter(caps)
