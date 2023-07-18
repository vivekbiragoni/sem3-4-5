def is_valid_move(board, N, row, col):
    # Check if the move is within the bounds of the board and the square is unvisited
    return (row >= 0 and row < N and col >= 0 and col < N and board[row][col] == -1)


def print_solution(board, N):
    # Print the Knight's Tour path
    for i in range(N):
        for j in range(N):
            print(board[i][j], end="\t")
        print()


def knights_tour_util(board, N, row, col, move_count):
    # All squares have been visited, Knight's Tour is complete
    if move_count == N * N:
        print_solution(board, N)
        return True

    # Possible moves for the knight
    row_moves = [2, 1, -1, -2, -2, -1, 1, 2]
    col_moves = [1, 2, 2, 1, -1, -2, -2, -1]

    # Try all possible moves
    for i in range(8):
        next_row = row + row_moves[i]
        next_col = col + col_moves[i]

        if is_valid_move(board, N, next_row, next_col):
            # Mark the square as visited
            board[next_row][next_col] = move_count

            # Recursive call to explore the next move
            if knights_tour_util(board, N, next_row, next_col, move_count + 1):
                return True

            # Backtrack and unmark the square if a valid tour is not found
            board[next_row][next_col] = -1

    return False


def knights_tour(N):
    # Create the chessboard
    board = [[-1 for _ in range(N)] for _ in range(N)]

    # Starting position
    start_row = 0
    start_col = 0

    # Mark the starting square as visited
    board[start_row][start_col] = 0

    # Try to find a Knight's Tour starting from the given position
    if not knights_tour_util(board, N, start_row, start_col, 1):
        print("No solution exists")


# Example usage
board_size = 8  # Adjust the board size as desired
knights_tour(board_size)
