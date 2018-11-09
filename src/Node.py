

class Node:

    def __init__(self, sentence):
        self.sentence = sentence
        self.words = self.parse(self.sentence)
        self.edges = []

    def parse(self, sentence):
        words = sentence.split()
        print(words)
        return words

    def returnWords(self)
        return self.words

    def addEdge(self, node):
        self.edges.append(node)

    def returnEdgeNum(self)
        return len(edges)

    def returnEdges(self)
        return edges