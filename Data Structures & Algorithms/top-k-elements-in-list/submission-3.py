class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1

        arr = []

        for num, cnt in freq_dict.items():
            arr.append([cnt, num])

        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res
