"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
"""

def addBinary(self, a, b):

    #return bin(int(a,2) + int(b,2))[2:]
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    carry = 0
    result = ''
    for i in range(max_len - 1, -1, -1):
        tmp = carry
        if a[i] == '1':
            tmp += 1
        if b[i] == '1':
            tmp += 1

        result += str(tmp%2)
        carry = tmp//2
    if carry != 0:
        result += str(carry)
    return result[::-1]
