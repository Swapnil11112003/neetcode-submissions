class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lengths = defaultdict(int)
        greatest = 0

        for num in nums:
            if lengths[num] == 0:
                lengths[num] = lengths[num-1] + 1 + lengths[num+1]

                lengths[num - lengths[num-1]] = lengths[num]
                lengths[num + lengths[num+1]] = lengths[num]

                greatest = max(greatest, lengths[num])

        return greatest