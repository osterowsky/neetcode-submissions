class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:    
        people.sort() # [1, 2, 2, 3, 3]
        l, r = 0, len(people) - 1 # 0, 4
        boats = 0

        while l <= r:
            if l == r:
                boats += 1
                l, r = l + 1, r - 1
                continue
            
            heavy = people[r]
            light = people[l]
            boats += 1
            r -= 1
            
            if heavy + light <= limit:
                l += 1
        
        return boats