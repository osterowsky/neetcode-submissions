class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while l < r:
            mid = l + (r - l) // 2
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid

        left, right = l - 1, l
        res = []

        while len(res) < k:
            a = arr[left] if left >= 0 else float('inf')
            b = arr[right] if right < len(arr) else float('inf')

            if abs(a - x) <= abs(b - x):
                res.append(a)
                left -= 1
            else:
                res.append(b)
                right += 1
        
        return sorted(res)