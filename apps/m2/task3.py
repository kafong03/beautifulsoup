# Task 3: Print out all the tags in the document

from bs4 import SoupStrainer, BeautifulSoup, Tag
import sys 
import time

def task3():
    get_tag_objects = SoupStrainer(name=True)

    with open(sys.argv[1], encoding='utf-8') as file:
        parser = "xml" if sys.argv[1][-3:].lower() == "xml" else "html.parser"
        soup = BeautifulSoup(file, parser, parse_only=get_tag_objects)

        for tag in soup.find_all(name=True):
            print(tag.name)


def main():
    start = time.time()
    task3()
    end = time.time()

    # Uncomment if you want the runtime
    # print("\nTotal runtime of program on " + sys.argv[1] + f" is {end - start} seconds")

if __name__ == "__main__":
    main()