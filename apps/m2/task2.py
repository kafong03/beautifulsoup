# Task 2: Print all the hyperlinks <a> tags

from bs4 import SoupStrainer, BeautifulSoup
import sys
import time

def task2():
    only_a_tags = SoupStrainer("a")

    with open(sys.argv[1], encoding='utf-8') as file:
        parser = "xml" if sys.argv[1][-3:].lower() == "xml" else "html.parser"
        soup = BeautifulSoup(file, parser, parse_only=only_a_tags)
        
        for a_tags in soup.contents:
            print(a_tags)


def main():
    start = time.time()
    task2()
    end = time.time()

    # Uncomment if you want the runtime
    # print("\nTotal runtime of program on " + sys.argv[1] + f" is {end - start} seconds")

if __name__ == "__main__":
    main()