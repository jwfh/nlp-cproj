from Edge import Edge
from Node import Node
import re

class Paragraph:
    
    def __init__(self, text):
        self.text = text
        self.nodes = list()
        self.edges = list()
        self.sentences = self.preProcess(text)
        self.initializeNodes(self.sentences)

        self.words = self.findWords()

        print("Words: ", self.words)
        print(self.edges)
        print(self.nodes)
        

        #for node in self.nodes:

    def findWords(self):
        words = dict()

        for node in self.nodes:
            print(node)
            words[node] = node.findWords()

        return words

    def preProcess(self, text):
        DATA = ['.', '!', '?']
        return re.split(r"[\.|!|\?]+", text)
        
    def initializeNodes(self, sentences):

        def addNode(sentences, previousNode):
            if sentences == "":
                return
            print(sentences)
            node1 = previousNode
            node2 = Node(sentences)
            
            edge = Edge(node1, node2)
            print("Edge: ", edge)

            node1.addEdge(edge)
            node2.addEdge(edge)

            #self.nodes.append(node1)
            self.nodes.append(node2)
            
            self.edges.append(edge)
        
        node1 = Node(sentences[0])
        self.nodes.append(node1)
        i = 1
        while i < len(sentences) - 1:

            addNode(sentences[i], self.nodes[-1])

            i += 1  