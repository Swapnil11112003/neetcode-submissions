class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        count = 0
        for num in hash_set:
            if (num - 1) not in hash_set:
                cur_count = 1
                while num + 1 in hash_set:
                    cur_count += 1
                    num += 1
                
                count = max(count, cur_count)

        return count
                
    



        