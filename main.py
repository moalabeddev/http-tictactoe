import httpx

EMPTY_STRING = ""
WINNING_POSITIONS = [
    [0,1,2], [3,4,5],[6,7,8], #rows
    [0,3,6], [1,4,7],[2,5,8], #columns
    [0,4,8], [2,4,6]] #diagonals

class MoveError(Exception):pass

def switch_players(current_player):
    return "X" if current_player == "O" else "O"

def print_board(board):
    print(
    f"|{board[0]}|{board[1]}|{board[2]}|""\n"
    f"|{board[3]}|{board[4]}|{board[5]}|""\n"
    f"|{board[6]}|{board[7]}|{board[8]}|""\n"
    )

def move_handler(current_player, board):
    move = int(input("Make your move: Enter a number between 1 and 9:")) -1
    if board[move] != EMPTY_STRING:
        print("Position already occupied try different move")

    board[move] = current_player


def check_winner(current_player, board):
    for position in WINNING_POSITIONS:
        if board[position[0]] and  board[position[0]] == board[position[1]] == board[position[2]] == current_player:
            print_board(board)
            print(f"{current_player} has won the game")
            return current_player
    
def check_full_board(board):
    return  EMPTY_STRING not in board

def main():
    board = [""] * 9
    current_player = "X"

    while True:
        print_board(board)
        if check_full_board(board):
            print ("TIE")
            break

        move_handler(current_player, board)

        if check_winner(current_player, board):
            break

        current_player = switch_players(current_player)

def network():
    import httpx

    for port in range (2000,50000):
        try:
            res = httpx.get(f"http://localhost:{port}")
        except httpx.ConnectError as e:
            print (e, f"to {port}")
            continue
    print (res.status_code)

if __name__ == "__main__":
    network()