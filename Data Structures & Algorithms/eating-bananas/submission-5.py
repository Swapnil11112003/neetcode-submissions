class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        i = 1
        j = max(piles)
        res = max(piles)
        while i <= j:
            sum = 0
            k = (i+j)//2

            for pile in piles:
                sum += math.ceil(float(pile) / k)
            if sum <= h:
                res = k
                j = k - 1
            else:
                i = k + 1
            
        return res

        