"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.

Note that you do not need to return anything.
"""

def gameOfLife(board):
    """
    Do not return anything, modify board in-place instead.
    """
    if not board or not board[0]:
        return
    
    m, n = len(board), len(board[0])
    # Create a copy of the original board
    original = [row[:] for row in board]
    
    # Directions for the eight possible neighbors
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    
    for i in range(m):
        for j in range(n):
            """For each cell (i, j), the code iterates through all eight possible neighbors using the directions list.
The neighbor's coordinates (ni, nj) are calculated as:
ni = i + di
nj = j + dj"""
            live_neighbors = 0
            for di, dj in directions:
                ni, nj = i + di, j + dj
                """The conditions 0 <= ni < m and 0 <= nj < n ensure that the neighbor is within the bounds of the board.
If the neighbor is a live cell (original[ni][nj] == 1), the live_neighbors counter is incremented."""
                if 0 <= ni < m and 0 <= nj < n and original[ni][nj] == 1:
                    live_neighbors += 1
            
            # Apply the rules to determine the next state
            if original[i][j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    board[i][j] = 0
            else:
                if live_neighbors == 3:
                    board[i][j] = 1
