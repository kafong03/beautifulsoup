# Milestone-2

# Part 2 - Locating the files/lines of the API functions used in Milestone 1 and Part 1 [before file changes]
BeautifulSoup() - File: "bs4/__init__.py" Lines: 133-1143 ~ object constructor/initializer at 209-490
prettify() - File: "bs4/element.py" Lines: 2601-2617
find_all() - File: "bs4/filter.py" Lines: 137-156
Tag.get() - File: "bs4/element.py" Lines: 2160-2171
find_parent() - File: "bs4/element.py" Lines: 992-1018
get_text() - File: "bs4/element.py" Lines: 524-547

SoupStrainer() - File: "bs4/filter.py" Lines: 313-682 ~ object constructor/initializer at 345-396

# Part 3
I implemented the SoupReplacer Class in bs4/soupreplacer.py. It is successfully implemented in the application program apps/m2/task6.py.

In my additions to the BeautifulSoup code in bs4/__init__.py, SoupStrainer parses first / filters out unwanted tags, so if a tag that matches SoupReplacer.og_tag is nested in a tag that is ignored, that tag will not be changed or visible.

Furthermore, the tag name is changed before a tag is created and pushed to or popped from the tag_stack during BeautifulSoup's parsing process if a SoupReplacer object exists and matches a tag (see changes in handle_starttag and handle_endtag)

At this time, like the original implementation of task6 in Milestone-1, tags that are typically single tags (like span or br) that are alt_tags of tags that have a start and end (like b, p, etc.) will have both a start and end tag.