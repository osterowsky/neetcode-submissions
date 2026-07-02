class KthLargest:

    def __init__(self, k: int, nums: List[int]):
            self.stream = sorted(nums)
            self.k = k

    def add(self, val: int) -> int:
        self.stream.append(val)
        for i in range(len(self.stream) - 2, -1, -1):
            if self.stream[i] > self.stream[i + 1]:
                self.stream[i], self.stream[i + 1] = self.stream[i + 1], self.stream[i]
            else:
                break

        return self.stream[-self.k]
    
