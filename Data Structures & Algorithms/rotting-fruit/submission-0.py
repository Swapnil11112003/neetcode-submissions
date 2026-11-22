class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        time = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in dir:
                    if (r + dr) < 0 or (c + dc) < 0 or (r + dr) >= ROWS or (c + dc) >= COLS or grid[r+dr][c+dc] == 0 or grid[r+dr][c+dc] == 2:
                        continue

                    grid[r+dr][c+dc] = 2
                    fresh -= 1
                    q.append((r + dr, c + dc))

            time += 1

        return time if fresh == 0 else -1

        