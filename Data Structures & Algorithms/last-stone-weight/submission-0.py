class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            if stones[0] > stones[1]:
                first = heapq.heappop_max(stones)
                second = heapq.heappop_max(stones)
                heapq.heappush_max(stones, first - second)
            else:
                heapq.heappop_max(stones)
                heapq.heappop_max(stones)

        return stones[0] if stones else 0



        