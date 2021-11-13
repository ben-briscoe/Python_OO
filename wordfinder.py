"""Word Finder: finds random words from a dictionary."""

from random import randint
from typing import NewType


class WordFinder:
    ...
    
    def __init__(self,path):
        #initializes class instance saving words found in file
        self.path = path
        self.read_and_save()
        self.words_read()

    def read_and_save(self):
        #reads the file, puts words in list and save the list as well as its length
        file = open(self.path,'r')
        self.words = list()
        for line in file:
            line = line[:len(line)-3]
            self.words.append(line)
        file.close()
        self.num_words = len(self.words)

    def words_read(self):
        #prints number of words found in file
        print(f'{self.num_words} words read')

    def random(self):
        #returns a random word from our list
        return self.words[randint(0,self.num_words)]


class SpecialWordFinder(WordFinder):

    def __init__(self,path):
        '''initializes instance utilizing super initialization and then removing extraneous words'''
        super().__init__(path)
        self.toss_junk()

    def toss_junk(self):
        '''omits special cases from the words'''
        new_words = list()
        for word in self.words:
            if len(word)>0 and word[0]!='#':
                new_words.append(word)

        self.words = new_words
        print(f'{self.num_words - len(new_words)} chucked out. {len(new_words)} legit words read')
        self.num_words = len(new_words)