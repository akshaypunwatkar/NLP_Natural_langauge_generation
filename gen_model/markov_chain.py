class MarkovCain:
    def __init__(self, sentences):
        self.sentences = sentences
        self.bigrams = {}
        self.trigrams = {}

    

    def create_bigram_trigram(self):


    def __update_ngram(self, sequence, word, dictionary):
        if sequence not in dictionary:
            dictionary[sequence] = defaultdict(int)
        dictionary[sequence][word] = dictionary[sequence][word] + 1