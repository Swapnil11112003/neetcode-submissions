class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1

        sorted_dict_by_value = dict(sorted(freq_dict.items(), key=lambda item:item[1], reverse=True))

        list = []
        for key, value in sorted_dict_by_value.items():
            list.append(key)

        return list[:k]
        