class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        k = len(s1)
        freq_s1 = {}
        for c in s1:
            freq_s1[c] = freq_s1.get(c, 0) + 1

        window = {}
        for high in range(len(s2)):
            c = s2[high]
            window[c] = window.get(c, 0) + 1

            # once the window would exceed size k, drop the leftmost char
            if high >= k:
                left_c = s2[high - k]
                window[left_c] -= 1
                if window[left_c] == 0:
                    del window[left_c]

            # window is exactly size k once high >= k - 1
            if high >= k - 1 and window == freq_s1:
                return True

        return False