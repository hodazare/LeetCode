"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

from collections import defaultdict, deque
class Solution(object):
        
    def findLadders(self, beginWord, endWord, wordList):
        
        if not beginWord or not endWord or endWord not in wordList:
            return []
        
        neighbors = defaultdict(list)
        output = []
        lenght = len(beginWord)
        
        # create list of adjacent words
        for word in wordList:
            for i in range(lenght):
                neighbors[word[:i] + '*' + word[i+1:]].append(word)  
                
        # keep the trace of visited words
        visited = {beginWord:1}
        q = deque([(beginWord, [beginWord])])
        
        # quit the loop if the found path is more than minPath
        minPath = float('inf')
        while q:
            word, path = q.popleft()
            i = 0
            #for i in range(lenght):
            while i < lenght and len(path) < minPath:
                words = neighbors[word[:i] + '*' + word[i+1:]]
                for w in words:
                    if w == endWord:
                        path.append(w) 
                        if path not in output and beginWord in path:
                            output.append(path)
                            minPath = len(path)
                        
                        # if endWord is found ignore the rest neighbors  
                        i = lenght        
                    elif not visited.get(w) or visited.get(w) > len(path):
                        visited[w] = len(path) + 1
                        path.append(w)
                        q.append((w, path))
                        path = path[:-1]
                i += 1
        return output
        
