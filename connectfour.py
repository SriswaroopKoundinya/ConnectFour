import numpy as np
_user = np.resize([['_'] for x in range(1,43)], (6,7))
def checkBoard(board):
    BOOL = False;
    for rows in range(0, 6):
        for ITER in range(0, 4):
            p1 = board[rows, ITER];
            p2 = board[rows, ITER+1];
            p3 = board[rows, ITER + 2];
            p4 = board[rows, ITER+3];
            if p1 == p2 and p2 == p3 and p3 == p4 and p1 != '_':
                return p1;
    for rows in range(0, 3):
        for ITER in range(0, 7):
            p1 = board[rows, ITER];
            p2 = board[rows+1, ITER];
            p3 = board[rows+2, ITER];
            p4 = board[rows+3, ITER];
            if p1 == p2 and p2 == p3 and p3 == p4 and p1 != '_':
                return p1;
    for rows in range(0, 3):
        _ROW = board[rows];
        for ITER in range(0, 4):
            p1 = board[rows, ITER];
            p2 = board[rows + 1, ITER + 1];
            p3 = board[rows+2, ITER + 2];
            p4 = board[rows + 3, ITER+3];
            if p1 == p2 and p2 == p3 and p3 == p4 and p1 != '_':
                BOOL = True;
                return p1;
    for rows in range(3, 6):
        Row = board[rows];
        for ITER in range(0, 4):
            p1 = board[rows, ITER];
            p2 = board[rows - 1, ITER + 1];
            p3 = board[rows-2, ITER + 2];
            p4 = board[rows - 3, ITER+3];
            if p1 == p2 and p2 == p3 and p3 == p4 and p1 != '_':
                BOOL = True;
                return p1;
    return None;
def master():
    _user = np.resize([['_'] for x in range(1,43)], (6,7))
    print('_______________________')
    print('Welcome to Connect Four!');
    print('Player1 will play first. Player1 is represented by O, while Player2 is represented by T.')
    name1 = input("Enter Player1 Name: ");
    name2 = input("Enter Player2 Name: ");
    circles = 21;
    def gameplay():
        move1 = int(input(name1 + ", which column will your token go into?"))-1;
        column = [];
        for _row in _user:
            column.append(_row[move1])
        num = 0;
        for _item in column:
            if _item != '_':
                break;
            num += 1;
        _user[num-1, move1] = 'O';
        res = checkBoard(_user);
        print(_user);
        if res != None:
            if res == 'O':
                print("Congrats, " + name1 + "!"+ " You have won the game!")
                master()
            else:
                print("Congrats, " + name2 + "!"+ " You have won the game!")
                master();
        move2 = int(input(name2 + ", which column will your token go into?"))-1;
        column = [];
        for _row in _user:
            column.append(_row[move2])
        num = 0;
        for _item in column:
            if _item != '_':
                break;
            num += 1;
        _user[num-1, move2] = 'T';
        res = checkBoard(_user);
        print(_user)
        if res != None:
            if res == 'O':
                print("Congrats, " + name1 + "!"+ " You have won the game!")
                master()
            else:
                print("Congrats, " + name2 + "!"+ " You have won the game!")
                master();
        gameplay();
    gameplay();
master()
