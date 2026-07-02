class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ']':
                # Processing logic
                seq = []
                while len(stack) > 0 and stack[-1] != '[':
                    seq.append(stack.pop())
                stack.pop()
                multiplier = []
                while len(stack) > 0 and stack[-1].isdigit():
                    multiplier.append(stack.pop())
                multiplier = reversed(multiplier)
                multiplier = int("".join(multiplier))
                seq = reversed(seq)
                stack.append("".join(seq) * multiplier)
            else:
                stack.append(c)
        
        return "".join(stack)