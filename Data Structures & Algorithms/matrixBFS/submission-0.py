class Solution:
    directions = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0]
    ]

    def shortestPath(self, grid: List[List[int]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        if grid[0][0] == 1 or grid[self.rows-1][self.cols-1] == 1:
            return -1
        
        queue = collections.deque([(0, 0, 0)])
        visited = {(0, 0)}
        
        while queue:
            r, c, dist = queue.popleft()
            if r == self.rows - 1 and c == self.cols - 1:
                return dist
            
            for dr, dc in self.directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in visited:
                    if 0 <= nr < self.rows and 0 <= nc < self.cols and grid[nr][nc] == 0:
                        visited.add((nr, nc))
                        queue.append((nr, nc, dist + 1))
        return -1