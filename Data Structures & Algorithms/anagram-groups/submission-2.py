class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqMap = {}

        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord in freqMap:
                freqMap[sortedWord].append(word)
            else:
                freqMap[sortedWord] = [word]
        
        res = []
        for _, val in freqMap.items():
            res.append(val)
        
        return res