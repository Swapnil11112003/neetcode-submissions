class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        cur_color = image[sr][sc]

        def dfs(image, r, c, visit):
            ROWS, COLS = len(image), len(image[0])
            if r < 0 or c < 0 or r == ROWS or c == COLS or image[r][c] != cur_color or (r, c) in visit:
                return
            
            if image[r][c] == cur_color:
                image[r][c] = color

            visit.add((r, c))

            dfs(image, r+1, c, visit)
            dfs(image, r-1, c, visit)
            dfs(image, r, c+1, visit)
            dfs(image, r, c-1, visit)

            visit.remove((r, c))
            return image
            
        return dfs(image, sr, sc, set())

        