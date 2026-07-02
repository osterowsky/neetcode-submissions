class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for item in s:
            if item in brackets.values():
                if not stack or brackets[stack[-1]] != item:
                    return False
                stack.pop()
            else:
                stack.append(item)
        
        return True if not stack else False