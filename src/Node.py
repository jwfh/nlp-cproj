from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('wordnet')

class Node:

    def __init__(self, sentence, num):
        self.sentence = sentence
        self.words = self.parse(self.sentence)
        self.edges = dict()
        self.sentenceNum = num

    def sentence(self):
        return self.sentence

    def parse(self, sentence):
        words = sentence.split()
        wordnet_lemmatizer = WordNetLemmatizer()

        for index in range(len(words)):
            print(words[index])
            words[index] = wordnet_lemmatizer.lemmatize(words[index], pos='v').encode("utf-8")

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