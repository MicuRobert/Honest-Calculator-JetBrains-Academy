user_input = "_________"
l = list(user_input)

board = [
    [l[0], l[1], l[2]],
    [l[3], l[4], l[5]],
    [l[6], l[7], l[8]]
]


def grid():
    print("---------")
    print(f"| {board[0][0]} {board[0][1]} {board[0][2]} |")
    print(f"| {board[1][0]} {board[1][1]} {board[1][2]} |")
    print(f"| {board[2][0]} {board[2][1]} {board[2][2]} |")
    print("---------")


grid()
last = 'O'

while True:
    coor = input("Enter the coordinates: ")
    n = [x for x in coor.split() if x.isalpha()]
    if len(n) > 0:
        print("You should enter numbers!")
    else:
        row, col = coor.split()
        row, col = int(row), int(col)
        if row > 3 or col > 3:
            print("Coordinates should be from 1 to 3!")
        elif board[row - 1][col - 1] == "_":
            if last == 'X':
                board[row - 1][col - 1] = "O"
                last = 'O'
            elif last == 'O':
                board[row - 1][col - 1] = "X"
                last = 'X'
            grid()
            user_input = sum(board, [])
            print(user_input)
            ls = ["".join(user_input[0:3]), "".join(user_input[3:6]), ''.join(user_input[6:9]), user_input[0] + user_input[3] + user_input[6], user_input[1] + user_input[4] + user_input[7], user_input[2] + user_input[5] + user_input[8], user_input[0] + user_input[4] + user_input[8], user_input[6] + user_input[4] + user_input[2]]
            print(ls)
            if "_" not in user_input and "XXX" not in ls and "OOO" not in ls:
                print("Draw")
                break
            elif "XXX" in ls:
                print("X wins")
                break
            elif "OOO" in ls:
                print("O wins") 
                break
        else:
            print("This cell is occupied! Choose another one!")
