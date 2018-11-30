from Edge import Edge
from Node import Node
from nltk.stem import WordNetLemmatizer
import re


class Paragraph:

    def __init__(self, text):
        self.exclude = ['the']
        self.text = text
        self.nodes = list()
        self.edges = list()

        # Creates a node for every sentence in the text
        self.sentences = self.preProcess(text)
        self.initializeNodes(self.sentences)
        self.words = self.findWords()
        
        self.matchWords()
        if len(self.sentences) > 9:
            recommended = len(self.sentences) / 3
        else:
            recommended = len(self.sentences) / 2

        sumLength = int(raw_input("How many sentences would you like to include in the summary? (Recommended is " + str(recommended) + ")\n"))

        self.summary = self.retSummary(sumLength)

        self.summary.sort(key=lambda summary: summary[0].sentenceNum)


    #
    #   retSummary(sumLength)
    #
    #       sumLength: The number of sentences to include in the final summary.
    #
    #   This function will use all the nodes and edges in the graph to determine which sentences have the most relations.
    #   It does this by first looping through all the nodes in the Text object, and by calling the returnEdgeNum() method
    #   to determine how many relations each sentence has.
    #   The program will then sort the nodes in descending order, and will return the sentences with the most relations.
    #   The number of sentences returned, and therefore the length of the summary is determined by the sumLength variable.
    #
    def retSummary(self, sumLength):
        summary = list()
        final_sum = []
        for node in self.nodes:

            size = node.returnEdgeNum()
            #print("Size: ", [node, size])
            if len(final_sum) < sumLength:
                final_sum.append([node, size])
                final_sum.sort()
                final_sum.sort(key=lambda final_sum: final_sum[1])
            elif len(final_sum) >= sumLength:
                found = -1
                for i in range(len(final_sum)):
                    #print(final_sum[i])
                    if size >= final_sum[i][1]:
                        found = i


                if found != -1:
                    first = final_sum[1:found + 1]
                    second = [[node, size]]
                    third = final_sum[found + 1:]
                    final_sum = first + second + third

            summary = final_sum
        return summary


        print("Summary: ", summary)

    def matchWords(self):

        for word in self.words:
            if word not in self.exclude and len(word) > 2:
                for node1 in self.words[word]:
                    for node2 in self.words[word]:
                        if node1 != node2:
                            edge = Edge(node1, node2)
                            if edge not in self.edges:
                                node1.addEdge(edge)
                                node2.addEdge(edge)
                                self.edges.append(edge)

    def findWords(self):
        words = dict()

        for node in self.nodes:
            #print(node)
            for word in node.findWords():
                safeword = re.sub(r'^["(]|[")]$', '', word.lower())
                if safeword in words:
                    words[safeword].append(node)
                else:
                    words[safeword] = [node]

        return words

    def preProcess(self, text):
        DATA = ['.', '!', '?']
        text = text.decode('utf-8')
        text = text.replace('\r\n', ' ').replace('\n', ' ')
        processed = re.split(r"(?:[\.!\?]\s)+", text)
        processed = [x.encode('ascii', 'ignore') for x in processed]
        #print "Processed: ", processed

        return processed

    def initializeNodes(self, sentences):

        def addNode(sentences, previousNode, num):
            if sentences == "":
                return
            #print(sentences)
            node1 = previousNode
            node2 = Node(sentences, num)

            edge = Edge(node1, node2)
            #print("Edge: ", edge)

            node1.addEdge(edge)
            node2.addEdge(edge)

            #self.nodes.append(node1)
            self.nodes.append(node2)

            self.edges.append(edge)

        node1 = Node(sentences[0], 0)
        self.nodes.append(node1)
        i = 1
        while i < len(sentences) - 1:

            addNode(sentences[i], self.nodes[-1], i)

            i += 1
