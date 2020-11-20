from collections import defaultdict
import random
class MarkovCain:
    def __init__(self, sentences):
        self.sentences = sentences
        self.bigrams = {}
        self.trigrams = {}

    def get_synthetic_data(self):
        sentences = self.generate_synthetic_data()
        blob = self.parse_sentences(sentences)
        f = open("./synth_data.txt", "w")
        f.write(blob)
        f.close()

    def parse_sentences(self, sentences):
        new_sentences = ""
        for sentence in sentences:
            s1 = " ".join(sentence)
            s1 += "."
            new_sentences += s1
        return new_sentences


    def generate_synthetic_data(self):
        ### https://yurichev.com/blog/markov/
        text = random.choice([["this", "is"], ["it", "is"], ["you", "are"], ["that", "is"]])
        tlen = len(text)
        sentences = []
        for j in range(100000):
            l_ind = tlen - 1
            temp = text[l_ind - 2] + " " + text[l_ind - 1]
            if temp in self.trigrams:
                new_word = self.__generate_random_trigram(temp)
                text.append(new_word)
            elif temp in self.bigrams:
                new_word = self.__generate_random_bigram(text[l_ind - 1])
                text.append(new_word)
            else:
                # print("coming hehre")
                sentences.append(text)
                text = random.choice([["this", "is"], ["it", "is"], ["you", "are"],["that", "is"]])
                tlen = len(text) 
        return sentences
    

    def create_bigram_trigram(self):
        for words in self.sentences:
            if len(words) == 0:
                continue
            for idx, word in enumerate(words):
                if idx >= 1:
                    self.__update_ngram(1, words[idx - 1], word)
                if idx >= 2:
                    self.__update_ngram(2, words[idx - 1] + " " + words[idx - 2], word)
        # print(self.bigrams)




    def __update_ngram(self, gram, sequence, word):
        if gram == 1:
            if sequence not in self.bigrams:
                self.bigrams[sequence] = defaultdict(int)
            self.bigrams[sequence][word] = self.bigrams[sequence][word] + 1
        else:
            if sequence not in self.trigrams:
                self.trigrams[sequence] = defaultdict(int)
            self.trigrams[sequence][word] = self.trigrams[sequence][word] + 1

    def __generate_random_bigram(self, token):
        return random.choices(list(self.bigrams[token].keys()), weights=list(self.bigrams[token].values()))[0]


    def __generate_random_trigram(self, token):
        return random.choices(list(self.trigrams[token].keys()), weights = list(self.trigrams[token].values()))[0]