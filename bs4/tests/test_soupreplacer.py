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
from bs4.element import Tag
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

        test_tag = Tag(name="b")

        assert soup_replacer.name_xformer(test_tag) == "blockquote"


    def test_change_tag_name_no_match(self):
        # SoupReplacer should return original name when tag name does not match og_tag
        og_tag = "b"
        alt_tag = "blockquote"
        soup_replacer = SoupReplacer(og_tag, alt_tag)

        test_tag = Tag(name="p")

        assert soup_replacer.name_xformer(test_tag) == "p"


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


    # Milestone 3 Tests
    def test_soupreplacer_with_only_og_tag(self):
        # ValueError is thrown if SoupReplacer is only given an og_tag argument
        og_tag = "b"
        with pytest.raises(ValueError, match="Both og_tag and alt_tag must be given a value or have no value."):
            soup_replacer = SoupReplacer(og_tag=og_tag)


    def test_soupreplacer_with_only_alt_tag(self):
        # ValueError is thrown if SoupReplacer is only given an og_tag argument  
        alt_tag = "blockquote"
        with pytest.raises(ValueError, match="Both og_tag and alt_tag must be given a value or have no value."):
            soup_replacer = SoupReplacer(alt_tag=alt_tag) 


    def test_soupreplacer_with_name_xformer(self):
        # A SoupReplacer should apply given name_xformer function to the applicable tags
        def name_xformer(tag : Tag):
            if (tag.name == "b"):
                return "blockquote"
            return tag.name
        
        soup_replacer = SoupReplacer(name_xformer=name_xformer)

        data = "<b>I want to be a blockquote!</b>"
        changed_data = "<blockquote>I want to be a blockquote!</blockquote>"
        soup = self.soup(data, replacer=soup_replacer)

        assert soup.decode() == changed_data

    
    def test_soupreplacer_with_tag_names_and_name_xformer(self):
        # A SoupReplacer throws ValueError if og_tag and alt_tag are also given with name_xformer
        og_tag = "b"
        alt_tag = "blockquote"
        def name_xformer(tag : Tag):
            if (tag.name == "b"):
                return "blockquote"
            return tag.name
        
        with pytest.raises(ValueError, match="name_xformer cannot be given if og_tag and alt_tag have values"):
            soup_replacer = SoupReplacer(og_tag, alt_tag, name_xformer=name_xformer)


    def test_soupreplacer_with_attrs_xformer(self):
        # A SoupReplacer should apply given attrs_xformer function to the applicable tags
        def attrs_xformer(tag):
            if tag.name == "p":
                if 'class' not in tag.attrs.keys():
                    tag['class'] = ["test"]
                else:
                    tag['class'].append('test')
            return tag.attrs

        soup_replacer = SoupReplacer(attrs_xformer=attrs_xformer)

        data = "<p>I want to be a blockquote!</p>"
        changed_data = "<p class=\"test\">I want to be a blockquote!</p>"

        soup = self.soup(data, replacer=soup_replacer)

        assert soup.decode() == changed_data


    def test_soupreplacer_with_xformer(self):
        # A SoupReplacer with xformer allows for tag modifications without returning a value
        def xformer(tag):
            # combines name_xformer and attrs_xformer
            if (tag.name == "b"):
                tag.name = "blockquote"
            if tag.name == "p":
                if 'class' not in tag.attrs.keys():
                    tag['class'] = ["test"]
                else:
                    tag['class'].append('test')

        soup_replacer = SoupReplacer(xformer=xformer)

        data = "<p>I want to be a <b>blockquote!</b></p>"
        changed_data = "<p class=\"test\">I want to be a <blockquote>blockquote!</blockquote></p>"

        soup = self.soup(data, replacer=soup_replacer)

        assert soup.decode() == changed_data


    def test_soupreplacer_with_all_xformer_args(self):
        # A SoupReplacer with all xformer function args operates in the proper order [name_xformer, attrs_xformer, xformer]
        def name_xformer(tag : Tag):
            if (tag.name == "b"):
                return "p"
            return tag.name

        def attrs_xformer(tag):
            if tag.name == "p":
                if 'class' not in tag.attrs.keys():
                    tag['class'] = ["test"]
                else:
                    tag['class'].append('test')
            return tag.attrs

        def xformer(tag):
            if tag.name == "p":
                if 'class' in tag.attrs.keys():
                    if "test" in tag['class']:
                        tag['class'].append('xformer')

        soup_replacer = SoupReplacer(name_xformer=name_xformer, attrs_xformer=attrs_xformer, xformer=xformer)

        data = "<p>I want to be a <b>paragraph!</b></p>"
        changed_data = "<p class=\"test xformer\">I want to be a <p class=\"test xformer\">paragraph!</p></p>"

        soup = self.soup(data, replacer=soup_replacer)

        assert soup.decode() == changed_data


    def test_soupreplacer_with_no_args(self):
        # A SoupReplacer that is given no arguments should leave the file unchanged
        soup_replacer = SoupReplacer()

        data = "<p>I want to be a blockquote!</p>"
        unchanged_data = "<p>I want to be a blockquote!</p>"

        soup = self.soup(data, replacer=soup_replacer)

        assert soup.decode() == unchanged_data
