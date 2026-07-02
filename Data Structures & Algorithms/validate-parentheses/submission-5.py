class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for item in s:
            if item in brackets:
                stack.append(item)
            else:
                if not stack or brackets[stack[-1]] != item:
                    return False
                stack.pop()

        return not stack