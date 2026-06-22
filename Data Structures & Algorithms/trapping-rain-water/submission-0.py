class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        max_left = []
        max_right = []
        
        max_l = height[l]
        for i in range(len(height)):
            max_left.append(max_l)
            if height[i] > max_l:
                max_l = height[i]
        print(max_left)
        max_r = height[r]
        for i in range(len(height) - 1, -1, -1):
            max_right.append(max_r)
            if height[i] > max_r:
                max_r = height[i]

        max_right_rev = max_right[::-1]

        trapped_water = 0
        for i in range(len(height)):
            trap = min(max_left[i], max_right_rev[i]) - height[i]
            if trap <= 0:
                trapped_water += 0
            else:
                trapped_water += trap

        return trapped_water

        


        

        