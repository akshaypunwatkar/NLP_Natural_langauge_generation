from collections import defaultdict
import random
import operator
class MarkovCain:
    def __init__(self, sentences):
        self.sentences = sentences
        self.bigrams = {}
        self.trigrams = {}

    def predict(self):
        self.run_predictor()
        f = open("./synth_data_pred.txt", "w")
        blob = self.parse_sentences(self.predicted_sentences)
        f.write(blob)
        f.close()


    def get_synthetic_data(self):
        # self.create_bigram_trigram()
        self.sentences = self.generate_synthetic_data()
        blob = self.parse_sentences(self.sentences)
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

    def run_predictor(self):
        ## We will use the same text generated to find predicted text
        ## We have sentences, we will assume the first two words remain constant
        self.predicted_sentences = []
        for words in self.sentences:
            pred_sent = [words[0], words[1]]
            for ind in range(2, len(words)):
                temp = pred_sent[ind - 2] + " " + pred_sent[ind - 1]
                if temp in self.trigrams:
                    pred_sent.append(self.find_max_trigram(temp))
                elif(pred_sent[ind - 1] in self.bigrams):
                    pred_sent.append(self.find_max_bigram(pred_sent[ind - 1]))
                else:
                    break
            self.predicted_sentences.append(pred_sent)


    def find_max_bigram(self):
        return max(self.bigrams[token].items(), key = operator.itemgetter(1))[0]

    def find_max_trigram(self, token):
        return max(self.trigrams[token].items(), key = operator.itemgetter(1))[0]



    def generate_synthetic_data(self):
        ### https://yurichev.com/blog/markov/
        text = random.choice([["this", "is"], ["it", "is"], ["you", "are"], ["that", "is"]])
        text = ["it", "is"]
        tlen = len(text)
        sentences = []
        for j in range(100000):
            l_ind = tlen - 1
            temp = text[l_ind - 2] + " " + text[l_ind - 1]
            if temp in self.trigrams:
                new_word = self.__generate_random_trigram(temp)
                text.append(new_word)
            elif text[l_ind - 1] in self.bigrams:
                new_word = self.__generate_random_bigram(text[l_ind - 1])
                text.append(new_word)
                if(j%10 == 0):
                    sentences.append(text)
                    text = random.choice([["this", "is"], ["it", "is"], ["you", "are"], ["that", "is"]])
                    tlen = len(text) 
            else:
                sentences.append(text)
                text = random.choice([["this", "is"], ["it", "is"], ["you", "are"], ["that", "is"]])
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
                    self.__update_ngram(2, words[idx - 2] + " " + words[idx - 1], word)
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
        return random.choices(list(self.bigrams[token].keys()), weights = list(self.bigrams[token].values()))[0]


    def __generate_random_trigram(self, token):
        return random.choices(list(self.trigrams[token].keys()), weights = list(self.trigrams[token].values()))[0]