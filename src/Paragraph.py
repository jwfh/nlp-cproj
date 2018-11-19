from edge import Edge
from node import Node

class Paragraph:
    
    def __init__(self, text):
        self.text = text
        self.sentences = self.preProcess(text)
        self.initializeNodes(self.sentences)

        for node in self.nodes:


    def preProcess(self, text):
        return text.split('.')
        
    def initializeNodes(self, sentences):

        def addNode(sentences):
            print(sentences)
            node1 = Node(sentences[0])
            node2 = Node(sentences[1])
            
            node1.addEdge(node2)
            node2.addEdge(node1)

            self.nodes.append(node1)
            self.nodes.append(node2)
            
            self.edges.append(Edge(node1, node2))
        
        i = 0
        while i < len(sentences) - 1:

            addNode(sentences[i:i+2])

            i += 1  