import timeit
def is_valid_move(board, N, row, col):
    return (row >= 0 and row < N and col >= 0 and col < N and board[row][col] == -1)

def get_unvisited_neighbors(board, N, row, col):
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    neighbors = []

    for move in moves:
        next_row = row + move[0]
        next_col = col + move[1]
        if is_valid_move(board, N, next_row, next_col):
            count = 0
            for neighbor_move in moves:
                neighbor_row = next_row + neighbor_move[0]
                neighbor_col = next_col + neighbor_move[1]
                if is_valid_move(board, N, neighbor_row, neighbor_col):
                    count += 1
            neighbors.append((next_row, next_col, count))
    neighbors.sort(key=lambda x: x[2])
    return neighbors

def knights_tour_util(board, N, row, col, move_count):
    if move_count == N * N:
        return True

    neighbors = get_unvisited_neighbors(board, N, row, col)
    for neighbor in neighbors:
        next_row, next_col, _ = neighbor
        board[next_row][next_col] = move_count
        if knights_tour_util(board, N, next_row, next_col, move_count + 1):
            return True
        board[next_row][next_col] = -1

    return False

def knights_tour(N):
    board = [[-1 for _ in range(N)] for _ in range(N)]
    start_row = 0
    start_col = 0
    board[start_row][start_col] = 0

    if knights_tour_util(board, N, start_row, start_col, 1):
        print("Knight's Tour:")
        for i in range(N):
            for j in range(N):
                print(board[i][j], end="\t")
            print()
    else:
        print("No solution exists.")

# Example usage
# board_size = 5  # Adjust the board size as desired
# knights_tour(board_size)

# Iterating over different board sizes
board_sizes = [5, 6, 7, 8, 9, 10, 11, 12]
for size in board_sizes:
    print(f"Board Size: {size}")
    code = f"knights_tour({size})"
    time_taken = timeit.timeit(code, globals=globals(), number=1)
    print(f"Time Taken: {time_taken} seconds")
    print("-" * 30)