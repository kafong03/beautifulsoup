# Task 4: Print out all the tags that have an id attribute

from bs4 import SoupStrainer, BeautifulSoup
import sys 
import time

def task4():
    only_tags_with_ids = SoupStrainer(id=True)
    
    with open(sys.argv[1], encoding='utf-8') as file:
        parser = "xml" if sys.argv[1][-3:].lower() == "xml" else "html.parser"
        soup = BeautifulSoup(file, parser, parse_only=only_tags_with_ids)

        for tag in soup.find_all(id=True):
            print(tag.name)


def main():
    start = time.time()
    task4()
    end = time.time()

    # Uncomment if you want the runtime
    # print("\nTotal runtime of program on " + sys.argv[1] + f" is {end - start} seconds")

if __name__ == "__main__":
    main()