# Task 7: Find all <p> tags and add (or replace) a class attribute class="test"

from bs4 import SoupReplacer, BeautifulSoup
import sys 
import time

def add_class_to_p_tag_html(tag):
    if tag.name == "p":
        if 'class' not in tag.attrs.keys():
            tag['class'] = ["test"]
        else:
            tag['class'].append('test')
    return tag.attrs

def add_class_to_p_tag_xml(tag):
    if tag.name == "p":
        if 'class' not in tag.attrs.keys():
            tag['class'] = "test"
        else:
            tag['class'] += " test"
    return tag.attrs

def task7():
    add_class_test_to_p_tags = None
    
    with open(sys.argv[1], encoding='utf-8') as file:
        parser = "xml" if sys.argv[1][-3:].lower() == "xml" else "html.parser"
        # parser = "html.parser"
        if (parser == "xml"):
            add_class_test_to_p_tags = SoupReplacer(attrs_xformer=add_class_to_p_tag_xml)
        else:
            add_class_test_to_p_tags = SoupReplacer(attrs_xformer=add_class_to_p_tag_html)

        soup = BeautifulSoup(file, parser, replacer=add_class_test_to_p_tags)

        file_output_name = "./test_output/task7_output."
        file_output_name += "xml" if sys.argv[1][-3:].lower() == "xml" else "html"
        with open(file_output_name, 'w', encoding='utf-8') as f:                    
            f.write(soup.prettify())


def main():
    start = time.time()
    task7()
    end = time.time()

    # Uncomment if you want the runtime
    # print("\nTotal runtime of program on " + sys.argv[1] + f" is {end - start} seconds")

if __name__ == "__main__":
    main()