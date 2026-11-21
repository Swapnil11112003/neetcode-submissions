class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if not grid or grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1

        visit = set()
        q = deque([(0, 0)])
        visit.add((0,0))

        count = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return count

                dir = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
                for dr, dc in dir:

                    if (r + dr) < 0 or (c + dc) < 0 or (r + dr) >= ROWS or (c + dc) >= COLS or grid[r][c] == 1 or (r + dr, c + dc) in visit:
                        continue

                    visit.add((r + dr, c + dc))
                    q.append((r + dr, c + dc))

            count += 1

        return -1

            

        