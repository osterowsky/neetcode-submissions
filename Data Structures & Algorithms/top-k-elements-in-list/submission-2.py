class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)

        for num in nums:
            freqMap[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for key, value in freqMap.items():
            buckets[value].append(key)

        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for item in buckets[i]:
                res.append(item)
                if len(res) == k:
                    return res