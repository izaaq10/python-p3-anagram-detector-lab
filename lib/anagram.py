# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
        
    def match(self, word_list)  :
        anagram_list = []
        for candidate in word_list:
            if sorted(candidate.lower()) == sorted(self.word) and candidate.lower() != self.word:
             anagram_list.append(candidate)
        return anagram_list
        
anagram = Anagram("listen")
words = ["enlist", "google", "inlets", "banana"]
print(anagram.match(words))  