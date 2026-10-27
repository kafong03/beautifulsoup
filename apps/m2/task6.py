# Task 6: Change all b tags to blockquotes using SoupReplacer

from bs4 import SoupReplacer, BeautifulSoup
import sys 
import time

def task6():
    b_to_blockquote = SoupReplacer("b", "span")
    
    with open(sys.argv[1], encoding='utf-8') as file:
        parser = "xml" if sys.argv[1][-3:].lower() == "xml" else "html.parser"
        soup = BeautifulSoup(file, parser, replacer=b_to_blockquote)

        print(soup.prettify())


def main():
    start = time.time()
    task6()
    end = time.time()

    # Uncomment if you want the runtime
    # print("\nTotal runtime of program on " + sys.argv[1] + f" is {end - start} seconds")

if __name__ == "__main__":
    main()