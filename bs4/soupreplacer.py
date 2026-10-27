class SoupReplacer():
    """

    A 'SoupReplacer' encapsulates the logic necessary to match and replace
    Tag objects during file parsing.

    :param og_tag: the name of the Tag that will be replaced

    :param alt_tag: the name of the Tag that will replace og_tag in the document
    """
    og_tag: str
    alt_tag: str

    def __init__(
        self,
        og_tag: str,
        alt_tag: str
    ):
        self.og_tag = og_tag
        self.alt_tag = alt_tag

    def change_tag_name(self, name: str) -> str:
        # if the tag's name matches og_tag return alt_tag
        if (name == self.og_tag):
            return self.alt_tag
        return name

    # think about what to do with a tag that has no end tag
    # or vise versa? (maybe have a start tag and end tag function)