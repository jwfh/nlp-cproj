# !usr/bin/env python

from PreProcessing import PreProcessor
from Paragraph import Paragraph

def main():
    print("SUMMARIZING")

    with open('test.txt', 'r') as text:
        paragraph = Paragraph(text.read())

if __name__ == "__main__":
    main() 