"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

class Solution(object):
    
    # sorting words    
    def groupAnagrams(self, strs):
        
        result = collections.defaultdict(list)
        for word in strs:
            result[tuple(sorted(word))].append(word)
        return result.values()
    
    #count characters of words
    def groupAnagramsNK(self, strs):
        
        result = collections.defaultdict(list)
        for word in strs:
            count_char = [0]* 26
            for char in word:
                count_char[ord(char) - ord('a')] += 1
            result[tuple(count_char)].append(word)
        return result.values()
