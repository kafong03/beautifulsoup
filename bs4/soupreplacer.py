from __future__ import annotations

from typing import (
    Callable,
    Optional,
    TYPE_CHECKING,
)

from bs4.element import Tag

if TYPE_CHECKING:
    from bs4._typing import _RawOrProcessedAttributeValues


class SoupReplacer():
    """

    A 'SoupReplacer' encapsulates the logic necessary to match and replace
    Tag objects during file parsing.

    :param og_tag: optional string name of the Tag that will be replaced

    :param alt_tag: optional string name of the Tag that will replace og_tag in the document

    :param name_xformer: optional function that takes a Tag object and returns a replacement for its name

    :param attrs_xformer: optional function that takes a Tag object and returns a replacement for its attributes

    :param xformer: optional function that can transform a Tag object and does not return anything
    """
    og_tag: Optional[str]
    alt_tag: Optional[str]
    name_xformer: Optional[Callable[[Tag], str]]
    attrs_xformer: Optional[Callable[[Tag], Optional[_RawOrProcessedAttributeValues]]] # not sure what this should return yet -> tag.attrs value?
    xformer: Optional[Callable[[Tag], None]]

    def __init__(
        self,
        og_tag: Optional[str] = None,
        alt_tag: Optional[str] = None,
        name_xformer: Optional[Callable[[Tag], str]] = None, 
        attrs_xformer: Optional[Callable[[Tag], Optional[_RawOrProcessedAttributeValues]]] = None, 
        xformer: Optional[Callable[[Tag], None]]= None
    ):
        self.og_tag = og_tag
        self.alt_tag = alt_tag
        self.name_xformer = name_xformer
        self.attrs_xformer = attrs_xformer
        self.xformer = xformer

        if (og_tag is not None and alt_tag is not None):
            self.name_xformer = lambda tag : self.alt_tag if tag.name == self.og_tag else tag.name
            if (name_xformer is not None):
                raise ValueError("name_xformer cannot be given if og_tag and alt_tag have values")
        elif ((og_tag is None and alt_tag is not None) or (og_tag is not None and alt_tag is None)):
            raise ValueError("Both og_tag and alt_tag must be given a value or have no value.") 
