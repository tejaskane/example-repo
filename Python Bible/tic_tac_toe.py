board=['  ' for x in range(0,9)]
def print_board():
    row1=' {} | {} | {} '.format(board[0],board[1],board[2])
    des1=' --------'
    row2=' {} | {} | {} '.format(board[3],board[4],board[5])
    des2=' --------'
    row3=' {} | {} | {} '.format(board[6],board[7],board[8])
    print()
    print(row1)
    print(des1)
    print(row2)
    print(des2)
    print(row3)

def player_move(icon):
    if icon=='X':
        n=1
    if icon=='O':
        n=2
    print("Your turn player {}".format(n))
    choice=int(input("enter your move 1-9 : ").strip())
    if board[choice-1]=='  ':
        board[choice-1]=icon
    else:
        print()
        print("please seclect another position")
        player_move(icon)
def won(icon):
    if (board[0] ==icon and board[1]==icon and board[2]==icon
        ) or (board[3] ==icon and board[4]==icon and board[5]==icon
              )or (board[6] ==icon and board[7]==icon and board[8]==icon
                   ) or(board[0] ==icon and board[3]==icon and board[6]==icon
                        ) or(board[1] ==icon and board[4]==icon and board[7]==icon
                             ) or (board[2] == icon and board[5]==icon and board[8]==icon
                                   )or(board[0] ==icon and board[4]== icon and board[8]==icon
                                       ) or (board[2] ==icon and board[4]==icon and board[6]==icon):
        return True
    else:
        return False
def draw():
    if '  ' not in board:
        return True
    else:
        return False
while True:
    print_board()
    player_move('X')
    print_board()
    if won('X'):
        print("player 1 won")
        break
    elif draw():
        print("Its a draw")
        break
    player_move('O')
    if won('O'):
        print("player 2 won")
        break
    elif draw():
        print("Its a draw")
        break


    
