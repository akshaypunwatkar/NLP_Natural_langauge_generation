import numpy as np
import nltk

class FileParser:
    def __init__(self, **kwargs):
        ## Either pass a file path or an nltk corpus
        if "corpus" in kwargs:
            self.default = True
            self.corpus = kwargs["corpus"]
        elif "path" in kwargs:
            self.default = False
            self.path = kwargs["path"]
        else:
            raise TypeError("Either path or corpus name required")

    def parse(self):
        """
        Responsible for file parsing, and data sanitization. Central method
        Return: Sanlitized sentences
        """
        if(self.default):
            self.__parse_corpus()
        else:
            self.__parse_file()
        self.__sanitize_data()
        self.__create_sentences()
        print(self.clean_sentences)
        return self.clean_sentences



    #### Private

    def __create_sentences(self):
        self.junk_sentences = self.data.split(".")
        self.clean_sentences = []
        for sentence in self.junk_sentences:
            words = self.__sanitize_sentence(sentence)
            self.clean_sentences.append(words)
        return self.clean_sentences

    def __sanitize_sentence(self, sentence):
        words = sentence.replace(',',' ').split(" ")
        words = list(filter(lambda word: word != '', words))
        return words


    def __sanitize_data(self):
        self.__replace_chars()
        self.__delete_unwanted_tokens()

    def __replace_chars(self):
        self.data = self.data.replace('\r',' ') \
                        .replace('\n',' ') \
                        .replace('?','.')  \
                        .replace('!','.')  \
                        .replace('“','.')  \
                        .replace('”','.')  \
                        .replace("\"",".") \
                        .replace('‘',' ')  \
                        .replace('-',' ')  \
                        .replace('’',' ')  \
                        .replace('\'',' ')

    def __delete_unwanted_tokens(self):
        self.data = self.data.replace('[', '') \
                        .replace(']', '') \
                        .replace('*', '') \
                        .replace('-', '') \
                        .replace(':', '') \
                        .replace(';', '')

    


    
    def __parse_corpus(self):
        self.data = nltk.corpus.gutenberg.raw(self.corpus).lower()
    


if __name__ == "__main__":
    fp = FileParser(corpus = "austen-sense.txt")
    fp.parse()

