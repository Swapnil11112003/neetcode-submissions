class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1

        sort_dict = dict(sorted(freq_dict.items(), key=lambda item: item[1], reverse=True))

        res = []
        for key, val in sort_dict.items():
            res.append(key)
        
        return res[:k]
