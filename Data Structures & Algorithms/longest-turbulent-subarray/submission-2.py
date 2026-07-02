class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        inc = dec = res = 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                inc, dec = dec + 1, 1
            elif arr[i] < arr[i - 1]:
                dec, inc = inc + 1, 1
            else:
                inc = dec = 1
            res = max(res, inc, dec)
        return res