"""
SoupReplacer Tests:

Testing SoupReplacer Class and Methods

Testing for proper implementation in BeautifulSoup Class

Kele Fong kelef

"""
import pytest
import re
import warnings

from . import (
    SoupTest,
)
from bs4.filter import SoupStrainer
from bs4.soupreplacer import(
    SoupReplacer
)

class TestSoupReplacer(SoupTest):
    def test_constructor(self):
        # A new SoupReplacer object should save the proper tag names to the proper variables
        og_tag = "b"
        alt_tag = "blockquote"
        soup_replacer = SoupReplacer(og_tag, alt_tag)

        assert og_tag == soup_replacer.og_tag
        assert alt_tag == soup_replacer.alt_tag


    def test_change_tag_name_changes_match(self):
        # SoupReplacer should return alt_tag when the og_tag matches the given tag name
        og_tag = "b"
        alt_tag = "blockquote"
        soup_replacer = SoupReplacer(og_tag, alt_tag)

        assert soup_replacer.change_tag_name("b") == "blockquote"


    def test_change_tag_name_no_match(self):
        # SoupReplacer should return original name when tag name does not match og_tag
        og_tag = "b"
        alt_tag = "blockquote"
        soup_replacer = SoupReplacer(og_tag, alt_tag)

        assert soup_replacer.change_tag_name("p") == "p"


    def test_beautifulsoup_tag_change(self):
        # data should change upon SoupReplacer tag match
        og_tag = "b"
        alt_tag = "blockquote"
        soup_replacer = SoupReplacer(og_tag, alt_tag)

        data = "<b>I want to be a blockquote!</b>"
        changed_data = "<blockquote>I want to be a blockquote!</blockquote>"
        soup = self.soup(data, replacer=soup_replacer)

        assert soup.decode() == changed_data


        
    def test_beautifulsoup_no_tag_change(self):
        # data should remain unchanged upon SoupReplacer tag match
        og_tag = "b"
        alt_tag = "blockquote"
        soup_replacer = SoupReplacer(og_tag, alt_tag)

        data = "<p>I want to be a blockquote!</p>"
        unchanged_data = "<p>I want to be a blockquote!</p>"
        soup = self.soup(data, replacer=soup_replacer)

        assert soup.decode() == unchanged_data

    
    def test_default_behavior(self):
        # An unconfigured SoupReplacer should not change the parsed file
        og_tag = "b"
        alt_tag = "blockquote"
        soup_replacer = SoupReplacer(og_tag, alt_tag)

        data = "<p>I want to be a blockquote!</p>"
        unchanged_data = "<p>I want to be a blockquote!</p>"
        soup = self.soup(data)

        assert soup.decode() == unchanged_data


    def test_soupstrainer_with_soupreplacer(self):
        # Matching tags within tags that are skipped by SoupStrainer are removed from soup
        og_tag = "b"
        alt_tag = "blockquote"
        soup_replacer = SoupReplacer(og_tag, alt_tag)

        soup_strainer = SoupStrainer(name="p")

        data = """<p>I want to be a <b>blockquote!</b></p><b>I want to be a blockquote too!</b>"""
        changed_data = "<p>I want to be a <blockquote>blockquote!</blockquote></p>"
        soup = self.soup(data, parse_only=soup_strainer, replacer=soup_replacer)

        assert soup.decode() == changed_data
