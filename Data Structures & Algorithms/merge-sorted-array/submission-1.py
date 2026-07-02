class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = 0
        while idx < n:
            nums1[m + idx] = nums2[idx]
            # Bubble swap of newly added value
            for i in range(m + idx, 0, -1):
                if nums1[i] < nums1[i - 1]:
                    nums1[i], nums1[i - 1] = nums1[i - 1], nums1[i]
                else:
                    break
            idx += 1
