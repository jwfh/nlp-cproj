#!/usr/bin/env python
from PreProcessing import PreProcessor
from Paragraph import Paragraph
import os

def main():
    print "Test files:"
    tests = [x for x in os.listdir('./texts/') if x.lower().endswith('.txt')]
    for i in range(len(tests)):
        print "\t" + str(i) + ": " + tests[i]

    fileid = int(raw_input("Please specify a test file number:\n"))
    filename = './texts/' + tests[fileid]

    sumLength = int(raw_input("How many sentences would you like to include in the summary?\n")) 

    with open(filename, 'r') as text:
        paragraph = Paragraph(text.read(), sumLength)
        
        for val in paragraph.summary:
            print "\t-", val[0].sentence.strip()

if __name__ == "__main__":
    main() 