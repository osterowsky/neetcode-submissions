class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # Store already seen integers

        for num in nums:
            if num in seen: # Duplicate was already in the list
                return True
            seen.add(num)
        
        return False # No duplicates were to be found