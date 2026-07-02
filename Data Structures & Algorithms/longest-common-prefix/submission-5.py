class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]
        m = len(lcp)

        for i in range(1, len(strs)):
            s, m = strs[i], min(m, len(strs[i]))
            for j in range(m):
                if s[j] != lcp[j]:
                    m = j
                    break

        return lcp[:m]