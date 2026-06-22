class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqElementDict = defaultdict(int)
        for num in nums:
            freqElementDict[num] += 1

        sortedFreq = sorted(freqElementDict.items(), key=lambda x: x[1])
        
        return [x for (x, y) in sortedFreq[-k:]]