# Milestone 4 application code
from bs4 import BeautifulSoup
import sys
import time

def soup_app():
    # Application program that prints the nodes of a BeautifulSoup object
    with open(sys.argv[1], encoding='utf-8') as file:
        parser = "xml" if sys.argv[1][-3:].lower() == "xml" else "html.parser"
        soup = BeautifulSoup(file, parser)

        for node in soup:
            print(node)
            
            

def main():
    start = time.time()
    soup_app()
    end = time.time()

    # Uncomment if you want the runtime
    # print("\nTotal runtime of program on " + sys.argv[1] + f" is {end - start} seconds")

if __name__ == "__main__":
    main()