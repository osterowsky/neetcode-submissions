class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for token in tokens:
            if token == '+':
                first, second = res.pop(), res.pop()
                res.append(second + first)
            elif token == '-':
                first, second = res.pop(), res.pop()
                res.append(second - first)
            elif token == '*':
                first, second = res.pop(), res.pop()
                res.append(second * first)
            elif token == '/':
                first, second = res.pop(), res.pop()
                res.append(int(second / first))
            else:
                res.append(int(token))
        
        return res.pop()