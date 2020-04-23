"""
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  
It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  
The answer is in lowercase. 

Example:

Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"

"""
import string
def mostCommonWord(self, paragraph, banned):

    all_words = {}
    # cleaning
    for ch in string.punctuation:
        paragraph = paragraph.replace(ch, ' ')

    # counting occurance of words
    for word in paragraph.lower().split():
        all_words[word] = all_words.get(word, 0) + 1

    # remove banned words from the dictionary
    for word in banned:
        if all_words.get(word):
            del all_words[word]        

    most_common, target = 0, ''
    for word, cnt in all_words.items():
        if cnt > most_common:
            most_common = cnt
            target = word

    return target
