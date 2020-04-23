"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

"""
def isValid(s):

    if not s:
        return True
    stack = []
    matched = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        tmp = matched.get(ch)

        if tmp:
            if not stack or tmp != stack.pop():
                return False
        else:
            stack.append(ch)

    return not stack
