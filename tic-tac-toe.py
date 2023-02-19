def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    print(draw_move(board))

    while victory_for(board, "x") == False:
        enter_move(board)
        print(draw_move(board))


def enter_move(board):
    # The function accepts the board current status, asks the user about their move,
    # checks the input and updates the board according to the user's decision.

    free_fields = make_list_of_free_fields(board)
    count_free_fields = 0;

    for i in free_fields:
        count_free_fields += 1;

    if count_free_fields % 2 == 0:

        jogador = "O"
        sign = int(input(" Enter your move : "))

    else:

        jogador = "X"
        sign = computer()

    lista = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    move = False

    while move == False:

        for free in free_fields:

            if free == lista[sign - 1]:
                board[lista[sign - 1][0]][lista[sign - 1][1]] = jogador
                move = True
                return board

        else:

            if jogador == "o":

                sign = int(input(" Enter your move : "))

            else:

                sign = computer()

            move = False


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

    free_fields = []
    l = 0;
    c = 0;

    for line in board:
        for field in line:
            if field != 'X' and field != 'O':
                free_fields.append((l, c))

                if c < 2:
                    c += 1
                else:
                    c = 0;
            else:
                if c < 2:
                    c += 1
                else:
                    c = 0;
        if l < 2:
            l += 1;
        else:
            l = 0;

    return free_fields;


def victory_for(board, sign):
    # The function analyzes the board status in order to check if
    # the player using 'O's or 'X's has won the game

    # checking the horizontal
    for l in range(3):

        if board[l][0] == board[l][1] and board[l][0] == board[l][2]:
            print("The computer won!")
            return True

    else:
        # checking the vertical
        for c in range(3):
            if board[0][c] == board[1][c] and board[0][c] == board[2][c]:

                if board[1][c] == "X":

                    print("The computer won!")

                else:

                    print("You won !")

                return True
        else:
            # checking primary diagonal
            if board[0][0] == board[1][1] and board[0][0] == board[2][2]:

                if board[0][0] == "X":

                    print("The computer won!")

                else:

                    print("You won !")

                return True
            # checking secundary diagonal
            elif board[0][2] == board[1][1] and board[0][2] == board[2][0]:

                if board[0][2] == "X":

                    print("The computer won!")

                else:

                    print("You won !")

                return True

            # Checking all fields
            else:

                count = 0
                for line in board:
                    for field in line:
                        if field == 'X' or field == 'O':
                            count += 1

                if count == 9:
                    print("A tie !");
                    return True

    return False


def draw_move(board):
    # The function draws the computer's move and updates the board.

    gui = """
    +-------+-------+-------+
    |       |       |       |
    |   """ + board[0][0] + """   |   """ + board[0][1] + """   |   """ + board[0][2] + """   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   """ + board[1][0] + """   |   """ + board[1][1] + """   |   """ + board[1][2] + """   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   """ + board[2][0] + """   |   """ + board[2][1] + """   |   """ + board[2][2] + """   |
    |       |       |       |
    +-------+-------+-------+
                        """

    return gui


def computer():
    # Function responsible for generating random number
    from random import randrange

    for i in range(10):
        return randrange(8)


board = [
    ['1', '2', '3'],
    ['4', 'X', '6'],
    ['7', '8', '9']
]

display_board(board)

