

class Node:

    def __init__(self, sentence):
        self.sentence = sentence
        self.words = self.parse(self.sentence)
        self.edges = dict()

    def sentence(self):
        return self.sentence

    def parse(self, sentence):
        words = sentence.split()
        print(words)
        return words

    def findWords(self):
        return self.words

    #
    # Adds an edge object to the node
    #
    def addEdge(self, edge):
        if edge.node[0] == self:
            self.edges[edge.node[1]] = edge
        else:
            self.edges[edge.node[0]] = edge

    def returnEdgeNum(self):
        return len(self.edges)

    def returnEdges(self):
        return edges