#!/usr/bin/env python
# -*- encoding: utf-8
"""
Convert a Markdown file into HTML suitable for use on Dreamwidth.

Installation:

1.  Copy the script
2.  $ pip install markdown2

Usage:

    $ python markdownify.py <PATH>

Notes:

-   You can use @name in the Markdown file to get a <user> link.

"""

import re
import sys

import markdown2


# Username restrictions (https://www.dreamwidth.org/support/faqbrowse?faqid=64):
#
#     25 or fewer characters with letters, numbers, and hyphens (-) only, with the
#     first and last characters of the username being letters and numbers only
#
# Experimenting with "Rename Journal" suggests that single-char usernames
# are reserved.
#
# The regex doesn't check first/last characters because it's my own fault if
# I put that in a tag.
#
USER_TAG = re.compile(r"@(?P<name>[A-Za-z0-9-_]{1,25})")


def md_to_dreamwidth_html(md_src):
    # Convert the Markdown to HTML
    html = markdown2.markdown(md_src, extras=["smarty-pants"])

    # The HTML includes linebreaks, which the Dreamwidth editor interprets as
    # "add a linebreak to the post".  Ditch those by compressing all the newlines.
    # Because I use semantic linebreaks, add a space between lines --
    # just not a newline.
    no_newlines_html = " ".join(html.splitlines())

    # Close up opening/closing <p> tags
    compact_html = no_newlines_html.replace("</p>  <p>", "</p><p>")

    # Render any "@name" as <user> tags
    with_name_tags_html = USER_TAG.sub(r'<user name="\g<name>">', compact_html)

    return with_name_tags_html


if __name__ == "__main__":
    try:
        path = sys.argv[1]
    except IndexError:
        sys.exit("Usage: %s <PATH>" % __file__)

    md_src = open(path).read()
    print(md_to_dreamwidth_html(md_src))
