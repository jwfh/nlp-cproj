#!/usr/bin/env python
from Text import Text

def main():
    print("SUMMARIZING")

    with open('sample-data/shoelaces.txt', 'r') as textfile:
        text = Text(textfile.read())

if __name__ == "__main__":
    main() 