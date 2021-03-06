def main():
    player = next_player("")
    board = create_board()
    while not (there_are_winner(board) or is_a_draw(board)):
        show_board(board)
        choose_option(player, board)
        player = next_player(player)
    show_board(board)
    print("Thanks for playing!") 
print(f'\n-------------------------------------')
print(f'-------------------------------------')
print('Welcome to the Tic-tac-toe game!')
print(f'-------------------------------------')
print(f'-------------------------------------\n')
def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def show_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-----')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-----')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def is_a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 

def there_are_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])
    
def choose_option(player, board):
    square = int(input(f"{player}'s choose a number (1-9) to put {player}: "))
    board[square - 1] = player 

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"
    
if __name__ == "__main__":
    main()