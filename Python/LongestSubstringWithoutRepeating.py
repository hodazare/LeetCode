# Given a string, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(s):
  
  start = max_length = 0
  dic_char = {}
  
  for i, ch in enumerate(s):
    if dic_char.get(ch):
      start = max(dic_ch[ch], start)
    
    max_length = max(i - start + 1, max_length)
    dic_char[ch] = i + 1
  return max_length    
