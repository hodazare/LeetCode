"""
Given two strings s and t, determine if they are both one edit distance apart.

Note: 

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t

"""
def isOneEditDistance(self, s, t):
        
        if len(t) > len(s):
            s, t = t, s
        ns = len(s)
        nt = len(t)
        if abs(ns - nt) > 1 or s == t:
            return False
    
        for i in range(nt):
            if s[i] != t[i]:
                # s, t have the same length
                if ns == nt:
                    return s[i+1:] == t[i+1:]
                # with different length
                else:
                    return s[i+1:] == t[i:]
        
        # if s has one more character
        return True
# use two pointers
def isOneEditDistance(self, s, t):
        
        if len(t) > len(s):
            s, t = t, s
        ns = len(s)
        nt = len(t)
        if abs(ns - nt) > 1 or s == t:
            return False
        
        i = j = 0
        flag = False
        while i < ns and j < nt:
            if s[i] != t[j]:
                if flag:
                    return False
                flag = True
                if ns == nt:
                    j += 1
            else:
                j += 1
            i += 1
        return True
