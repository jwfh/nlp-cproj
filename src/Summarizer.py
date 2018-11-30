#!/usr/bin/env python
from Text import Text
import os

def main():
    print "Test files:"
    tests = [x for x in os.listdir('./texts/') if x.lower().endswith('.txt')]
    for i in range(len(tests)):
        print "\t" + str(i) + ": " + tests[i]

    fileid = int(raw_input("Please specify a test file number:\n"))
    filename = './texts/' + tests[fileid]

    with open(filename, 'r') as textfile:
        text = Text(textfile.read())

        for val in text.summary:
            print "\n-", val[0].sentence.strip()

if __name__ == "__main__":
    main()
