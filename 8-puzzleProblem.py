from collections import deque

# Goal state (solved puzzle)
goal_state = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 0]  # 0 represents the empty tile
]

# Possible moves in (row, column) notation: Up, Down, Left, Right
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_empty(matrix):
    """Find the position of the empty tile (0)."""
    for row in range(3):
        for col in range(3):
            if matrix[row][col] == 0:
                return row, col
    return None

def is_valid(x, y):
    """Check if a move is within the 3x3 grid."""
    return 0 <= x < 3 and 0 <= y < 3

def swap(matrix, x1, y1, x2, y2):
    """Swap two tiles in the puzzle (creates a new matrix)."""
    new_matrix = [row[:] for row in matrix]  # Deep copy
    new_matrix[x1][y1], new_matrix[x2][y2] = new_matrix[x2][y2], new_matrix[x1][y1]
    return new_matrix

def bfs_solver(initial_state):
    """Solves the 8-puzzle problem using BFS with matrix notation."""
    queue = deque([(initial_state, [])])  # Stores (current state, moves taken)
    visited = set()
    
    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path  # Return the sequence of moves leading to the goal
        
        # Convert state to tuple (immutable) for tracking visited states
        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        
        # Find empty tile (0) position
        empty_x, empty_y = find_empty(state)

        # Try all possible moves
        for dx, dy in moves:
            new_x, new_y = empty_x + dx, empty_y + dy
            if is_valid(new_x, new_y):
                new_state = swap(state, empty_x, empty_y, new_x, new_y)
                queue.append((new_state, path + [(empty_x, empty_y, new_x, new_y)]))  # Store move sequence
    
    return None  # No solution found

# Example initial state (shuffled)
initial_state = [
    [4, 1, 3], 
    [7, 2, 5], 
    [0, 8, 6]
]

# Solve the 8-puzzle
solution_moves = bfs_solver(initial_state)

# Print solution
if solution_moves:
    print("Solution found in", len(solution_moves), "moves:")
    for move in solution_moves:
        print(f"Move empty tile from {move[:2]} to {move[2:]}")
else:
    print("No solution found.")