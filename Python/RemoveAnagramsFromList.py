""" Fun with Anagrams
Two strings are anagrams if they are permutations of each other. For example, “aaagmnrs” is an anagram of “anagrams”.
Given an array of strings, remove each string that is an anagram of an earlier string, then return the remaining array in sorted order.
For example, given the strings s = ['code', 'doce', 'ecod', 'framer', 'frame'], the strings 'doce' and 'ecod' are both anagrams of 'code' so they are removed from the list.
The words 'frame' and 'framer' are not anagrams due to the extra 'r' in 'framer', so they remain. The final list of strings in alphabetical order is ['code', 'frame', 'framer'].

  Function Description
  Complete the function funWithAnagrams in the editor below. It must return a list of strings in alphabetical order, ascending.

  funWithAnagrams has the following parameters:

  s[s[0],...s[n-1]]: an array of strings
  Constraints
  1 ≤ n ≤ 1000
  1 ≤ |s[i]| ≤ 1000
  Each string s[i] is made up of characters in the range ascii[a-z]
"""

# check if two words are anagram using "Counter"
from collections import Counter


def isAnagram(word1, word2):
    return Counter(word1) == Counter(word2) 


# check if two words are anagram comparing the number of their characters
def isAnagramCh(word1, word2):
    char_count = {}
    for ch in word1:
        char_count[ch] = char_count.get(ch, 0) + 1
    for ch in word2:
        char_count[ch] = char_count.get(ch, 0) - 1
    for key in char_count.keys():
        char_count[key] = abs(char_count[key])
    return sum(char_count.values()) == 0


def funWithAnagrams(s):
    dict_a = {}
    for i in range(0, len(s)-1):
        for j in range(i+1, len(s)):
            if(s[j] not in dict_a and isAnagramCh(s[i], s[j])):
                dict_a[s[j]] = 1

    for key in dict_a:
        s.remove(key)
    s.sort()
    return s


# Test
s = ['code', 'aaagmnrs', 'anagrams', 'doce']
funWithAnagrams(s)
