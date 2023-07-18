import pygame

def is_valid_move(board, N, row, col):
    # Check if the move is within the bounds of the board and the square is unvisited
    return (row >= 0 and row < N and col >= 0 and col < N and board[row][col] == -1)

def print_solution(board, N):
    # Print the Knight's Tour path
    for i in range(N):
        for j in range(N):
            print(board[i][j], end="\t")
        print()

def knights_tour_util(board, N, row, col, move_count, screen, background_image, knight_image):
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

            # Update the screen with the current move
            draw_board(board, N, screen, background_image, knight_image)
            pygame.time.wait(100)  # Adjust the delay between moves

            # Recursive call to explore the next move
            if knights_tour_util(board, N, next_row, next_col, move_count + 1, screen, background_image, knight_image):
                return True

            # Backtrack and unmark the square if a valid tour is not found
            board[next_row][next_col] = -1

            # Update the screen after backtracking
            draw_board(board, N, screen, background_image, knight_image)
            pygame.time.wait(100)  # Adjust the delay between moves

    return False

def knights_tour(N):
    # Initialize Pygame
    pygame.init()

    # Set up the screen
    screen_size = 32 * N
    screen = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption("Knight's Tour")
    clock = pygame.time.Clock()

    # Load the background image and scale it to fit the screen
    background_image = pygame.image.load("chess.png").convert()
    background_image = pygame.transform.scale(background_image, (screen_size, screen_size))

    # Load the knight image and scale it to the desired size
    knight_image = pygame.image.load("knight.png").convert_alpha()
    knight_image_size = screen_size // N
    knight_image = pygame.transform.scale(knight_image, (knight_image_size, knight_image_size))

    # Create the chessboard
    board = [[-1 for _ in range(N)] for _ in range(N)]

    # Starting position
    start_row = 0
    start_col = 0

    # Mark the starting square as visited
    board[start_row][start_col] = 0

    # Update the screen with the initial move
    draw_board(board, N, screen, background_image, knight_image)
    pygame.time.wait(100)  # Adjust the delay between moves

    # Try to find a Knight's Tour starting from the given position
    if not knights_tour_util(board, N, start_row, start_col, 1, screen, background_image, knight_image):
        print("No solution exists")

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(60)  # Adjust the frame rate if needed

    pygame.quit()

def draw_board(board, N, screen, background_image, knight_image):
    screen.blit(background_image, (0, 0))  # Draw the background image

    square_size = screen.get_width() // N

    # Draw the knight on each visited square
    for i in range(N):
        for j in range(N):
            if board[i][j] != -1:
                knight_x = j * square_size + square_size // 2 - knight_image.get_width() // 2
                knight_y = i * square_size + square_size // 2 - knight_image.get_height() // 2
                screen.blit(knight_image, (knight_x, knight_y))

    pygame.display.update()

