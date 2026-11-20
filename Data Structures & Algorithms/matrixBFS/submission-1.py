class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1

        visit = set()
        q = deque([(0,0)])
        visit.add((0,0))

        length = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    if (min(r + dr, c + dc) < 0) or (r + dr) >= ROWS or (c + dc) >= COLS or (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1:
                        continue

                    visit.add((r + dr, c+ dc))
                    q.append((r + dr, c + dc))

            length += 1

        return -1

