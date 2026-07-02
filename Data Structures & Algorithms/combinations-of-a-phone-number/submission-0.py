class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        digit_to_char = {"2": "abc", "3": "def",
        "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []

        def backtrack(idx: int, sol: List[str]):
            if len(sol) == len(digits):
                res.append("".join(sol))
                return
            
            for c in digit_to_char[digits[idx]]:
                sol.append(c)
                backtrack(idx + 1, sol)
                sol.pop()
        

        backtrack(0, [])
        return res