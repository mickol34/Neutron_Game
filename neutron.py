import random
import itertools

U = "up"
D = "down"
L = "left"
R = "right"
UL = "up_left"
UR = "up_right"
DL = "down_left"
DR = "down_right"
empty = "__"
neutron = "N0"
B1 = "B1"
B2 = "B2"
B3 = "B3"
B4 = "B4"
B5 = "B5"
W1 = "W1"
W2 = "W2"
W3 = "W3"
W4 = "W4"
W5 = "W5"
band = "XX"
winning_message = "Gratulacje, białe wygrywają!"
losing_message = "Niestety, białe przegrywają..."
Random = "Random"
Advanced = "Advanced"

board = [[band, band, band, band, band, band, band],[band, B1, B2, B3, B4, B5, band],[band, empty, empty, empty, empty, empty, band],[band, empty, empty, neutron, empty, empty, band],[band, empty, empty, empty, empty, empty, band],[band, W1, W2, W3, W4, W5, band],[band, band, band, band, band, band, band]]

def show(board = board):
    print()
    print(board[0])
    print(board[1])
    print(board[2])
    print(board[3])
    print(board[4])
    print(board[5])
    print(board[6])
    print()

def find_pawn_Y(pawn, board = board):
    for row in range(1,6):
        if pawn in board[row]:
            return row

def find_pawn_X(pawn, board = board):
    row = find_pawn_Y(pawn, board)
    for column in range(len(board[row])):
        if board[row][column] == pawn:
            return column

def find_pawn(pawn, board = board):
    coordinates = [find_pawn_X(pawn, board), find_pawn_Y(pawn, board)]
    return coordinates

def check_for_collision(pawn, dir, board = board):
    x = find_pawn(pawn)[0]
    y = find_pawn(pawn)[1]
    distance = 0
    squares = []
    if dir.lower() == U:
        for i in range(1,y):
            squares.append(board[y-i][x])
    elif dir.lower() == D:
        for i in range(1,7-y):
            squares.append(board[y+i][x])
    elif dir.lower() == R:
        for i in range(1,7-x):
            squares.append(board[y][x+i])
    elif dir.lower() == L:
        for i in range(1,x):
            squares.append(board[y][x-1])
    elif dir.lower() == UR:
        for i in range(1,min(7-x,y)):
            squares.append(board[y-i][x+i])
    elif dir.lower() == DR:
        for i in range(1,min(7-x,7-y)):
            squares.append(board[y+i][x+i])
    elif dir.lower() == UL:
        for i in range(1,min(x,y)):
            squares.append(board[y-i][x-i])
    elif dir.lower() == DL:
        for i in range(1,min(x,7-y)):
            squares.append(board[y+i][x-i])
    for block in squares:
        if block == empty:
            distance = distance+1
        else:
            break
    return distance

def move(pawn, dir, board = board):
    x = find_pawn(pawn)[0]
    y = find_pawn(pawn)[1]
    if board[y][x] in (B1,B2,B3,B4,B5,W1,W2,W3,W4,W5,neutron):
        pawn = board[y][x]
        CFC = check_for_collision(pawn, dir, board)
        if CFC != 0:
            try:
                if dir.lower() == U:
                    board[y-CFC][x] = pawn
                    board[y][x] = empty
                elif dir.lower() == D:
                    board[y+CFC][x] = pawn
                    board[y][x] = empty
                elif dir.lower() == R:
                    board[y][x+CFC] = pawn
                    board[y][x] = empty
                elif dir.lower() == L:
                    board[y][x-CFC] = pawn
                    board[y][x] = empty
                elif dir.lower() == UR:
                    board[y-CFC][x+CFC] = pawn
                    board[y][x] = empty
                elif dir.lower() == UL:
                    board[y-CFC][x-CFC] = pawn
                    board[y][x] = empty
                elif dir.lower() == DR:
                    board[y+CFC][x+CFC] = pawn
                    board[y][x] = empty
                elif dir.lower() == DL:
                    board[y+CFC][x-CFC] = pawn
                    board[y][x] = empty
            except:
                print("Niewłaściwy kierunek!")     
        return CFC

def check_for_win(board = board):
    if neutron in board[5]:
        return True
    else:
        return False

def check_for_lose(board = board):
    if neutron in board[1]:
        return True
    else :
        return False

def check_for_stalemate(board = board):
    stalemate_indicator = 0
    for dir in (U,D,L,R,UR,UL,DR,DL):
        stalemate_indicator = stalemate_indicator + check_for_collision(neutron, dir, board)
    if stalemate_indicator == 0:
        return True
    else:
        return False

def players_neutron_turn(board = board):
    loop = True
    while loop:
        try:
            direction = input("Wskaż ruch dla neutrona: ")
            if direction in (U,D,L,R,UR,UL,DR,DL):
                CFC = check_for_collision(neutron, direction, board)
                if CFC != 0:
                    move(neutron, direction, board)
                    loop = False
            else:
                print("Coś poszło nie tak")
        except:
            print("Coś poszło nie tak")
    
def players_pawn_turn(board = board):
    loop = True
    while loop:
        try:
            pawn, direction = input("Wskaż ruch dla wybranego pionka: ").split()
            if pawn in (W1,W2,W3,W4,W5) and direction in (U,D,L,R,UR,UL,DR,DL):
                CFC = check_for_collision(pawn, direction, board)
                if CFC != 0:
                    move(pawn, direction, board)
                    loop = False
            else:
                print("Coś poszło nie tak")
        except:
            print("Coś poszło nie tak")

def randomly_generated_move(board = board):
    loop = True
    while loop:
        pawns = [B1,B2,B3,B4,B5]
        directions = [U,D,L,R,UR,UL,DR,DL]
        chosen_pawn = random.choice(pawns)
        chosen_direction = random.choice(directions)
        check = check_for_collision(chosen_pawn, chosen_direction, board)
        if check != 0:
            move(chosen_pawn, chosen_direction, board)
            loop = False

def randomly_generated_neutron_move(board = board):
    loop = True
    while loop:
        directions = [U,D,L,R,UR,UL,DR,DL]
        chosen_direction = random.choice(directions)
        check = check_for_collision(neutron, chosen_direction, board)
        if check != 0:
            move(neutron, chosen_direction, board)
            loop = False

def try_winning_neutron_move(board = board):
    possible_directions = [U, R, L, D, UL, UR, DL, DR]
    winning_directions = []
    primal_position = find_pawn(neutron)
    for direction in possible_directions:
        CFC = check_for_collision(neutron, direction, board)
        if CFC != 0:
            move(neutron, direction, board)
            new_position = find_pawn(neutron) 
            if check_for_lose() == True:
                winning_directions.append(direction)
            board[new_position[1]][new_position[0]] = empty
            board[primal_position[1]][primal_position[0]] = neutron
    if len(winning_directions) != 0:
        move(neutron, random.choice(winning_directions), board)
        return True
    else:
        return False

def try_not_losing_neutron_move(board = board):
    possible_directions = [U, R, L, D, UL, UR, DL, DR]
    primal_position = find_pawn(neutron)
    for direction in possible_directions:
        CFC = check_for_collision(neutron, direction, board)
        if CFC != 0:
            move(neutron, direction, board)
            new_position = find_pawn(neutron) 
            if check_for_win() == True:
                possible_directions.remove(direction)
            board[new_position[1]][new_position[0]] = empty
            board[primal_position[1]][primal_position[0]] = neutron
    if len(possible_directions) != 0:
        move(neutron, random.choice(possible_directions), board)
        return True
    else:
        return False

def try_winning_pawn_move(board = board):
    pawns = [B1, B2, B3, B4, B5]
    directions = [U, R, L, D, UL, UR, DL, DR]
    possible_moves = list(itertools.product(pawns, directions))
    winning_moves = []
    for PM in possible_moves:
        primal_position = find_pawn(PM[0], board)
        CFC = check_for_collision(PM[0], PM[1], board)
        if CFC != 0:
            move(PM[0], PM[1], board)
            new_position = find_pawn(PM[0], board)
            if check_for_stalemate() == True:
                winning_moves.append(PM)
            board[new_position[1]][new_position[0]] = empty
            board[primal_position[1]][primal_position[0]] = PM[0]
    if len(winning_moves) != 0:
        move(winning_moves[0][0], winning_moves[0][1], board)
        return True
    else:
        return False

def priority_pawn_move(board = board):
    not_moved_pawns = []
    for square in board[1]:
        if square in (B1, B2, B3, B4, B5):
            not_moved_pawns.append(square)
    loop = True
    while loop:
        if len(not_moved_pawns) != 0:
            directions = [U,D,L,R,UR,UL,DR,DL]
            chosen_pawn = random.choice(not_moved_pawns)
            chosen_direction = random.choice(directions)
            CFC = check_for_collision(chosen_pawn, chosen_direction, board)
            if CFC !=0:
                move(chosen_pawn, chosen_direction, board)
                loop = False
                return True
        else:
            loop = False
            return False

def gameplay():
    print()
    print("Wybierz przeciwnika spośród 'Random', 'Advanced': ")
    print()
    opponents_loop = True
    while opponents_loop:
        opponent = input()
        if opponent in (Random, Advanced):
            opponents_loop = False
        else:
            print("Coś poszło nie tak")
    number_of_turns = 0
    show()
    loop = True
    while loop:
        if number_of_turns == 0:
            players_pawn_turn()
            show()
            number_of_turns = number_of_turns + 1
        if number_of_turns % 2 == 0 and number_of_turns > 0:
            players_neutron_turn()
            show()
            if check_for_win() == True:
                print(winning_message)
                loop = False
            elif check_for_lose() == True:
                print(losing_message)
                loop = False
            else:
                players_pawn_turn()
                show()
                if check_for_stalemate() == True:
                    print(winning_message)
                    loop = False
                else:
                    number_of_turns = number_of_turns + 1
        if number_of_turns % 2 == 1:
            if opponent == Random:
                randomly_generated_neutron_move()
                show()
                if check_for_win() == True:
                    print(winning_message)
                    loop = False
                elif check_for_lose() == True:
                    print(losing_message)
                    loop = False
                else:
                    randomly_generated_move()
                    show()
                    if check_for_stalemate() == True:
                        print(losing_message)
                        loop = False
                    else:
                        number_of_turns = number_of_turns + 1
            if opponent == Advanced:
                if try_winning_neutron_move() == True:
                    show()
                    print(losing_message)
                    loop = False
                elif try_not_losing_neutron_move() == False:
                    move(neutron, D, board)
                    show()
                    print(winning_message)
                    loop = False
                elif try_winning_neutron_move() == False and try_not_losing_neutron_move() == True:
                    show()
                    if try_winning_pawn_move() == True:
                        show()
                        print(losing_message)
                        loop = False
                    else:
                        if priority_pawn_move() == True:
                            show()
                            number_of_turns = number_of_turns + 1
                        else:
                            randomly_generated_move()
                            show()
                            number_of_turns = number_of_turns + 1

def main_menu():
    loop = True
    while loop:
        print()
        print("Witaj w 'Neutron: The Game'! Co chcesz zrobić? 1 - Rozpocznij grę! 2 - Instrukcja i pomoc 3 - Objaśnienie sterowania Z - Zakończ program")
        print()
        option = input()
        if option not in ("1","2","3","Z"):
            print()
            print("Hej! Już na wstępie masz problemy z obsługą terminala? Nie cwaniakuj, jeśli próbujesz sztuczek! :<")
            print("Jeśli naprawdę nie wiesz, jak obsłużyć menu, powiem ci, że musisz wybrać jedną z trzech opcji,")
            print("wpisując wyłącznie numer opcji (1, 2, 3 lub Z) i zatwierdzić enterem :>")
            print()
        if option == "1":
            gameplay()
            loop = False
        if option == "2":
            print()
            print("Witaj w 'Neutron: The Game'! Pozwól, że objaśnię ci, na czym polega ta rozgrywka:")
            print("Przed tobą znajdzie się plansza o wymiarach 5x5, a na niej 11 pionków. 5 należy do ciebie (te oznaczone W - white)")
            print("i są umieszczone wzdłuż dolnego boku, a 5 do twojego przeciwnika (B - black).")
            print("Dodatkowo, na środku planszy umieszczony jest pionek neutralny, tzw. neutron i to wokół niego będzie kręcić się cała rozgrywka!")
            print("Zadaniem gracza jest przesunięcie neutrona na swój brzeg planszy, czyli na jedno z tych pól, które pierwotnie zajmują jego pionki.")
            print("Jak to zrobić? Otóż zasady są całkiem proste:")
            print("1) W każdym ruchu, oprócz pierwszego, gracz porusza się dwa razy, neutronem i pionkiem swojego koloru, w tej kolejności.")
            print("2) Grę rozpoczynają białe, ruszając się tylko raz, pionkiem swojego koloru.")
            print("3) Pionki, zarówno kolorowe i neutron, podczas swojego ruchu muszą się poruszyć o maksymalną możliwą ilość pól w wybranym kierunku.")
            print("4) W grze nie ma zbijania pionków ani ich przeskakiwania, ruch można wykonywać w 8 stron tylko po pustych polach.")
            print("5) Wygrywa gracz, po którego stronie planszy neutron wyląduje (pierwsza lub piąta ranka), niezależnie od tego, kto przesunął tam neutrona.")
            print("6) Dodatkowo, wygrywa gracz, który uniemożliwi przeciwnikowi poruszenie się neutronem ('pat')")
            print("Wszystko zrozumiałe? Zatem powodzenia w grze!")
            print()
        if option == "3":
            print()
            print("Sterowanie:")
            print("Wybór przeciwnika:")
            print("		Random - gra z komputerem generującym ruchy losowe,")
            print("		Advanced - gra z komputerem generującym ruchy nielosowe")
            print("Poruszanie pionkiem:")
            print("		Aby poruszyć pionkiem należy wpisać dwuczłonową komendę oddzieloną spacją i niczym więcej (!),")
            print("		składającą się z nazwy pionka oraz kierunku, w którym chcemy go przesunąć z pierwszeństwem ruchu pionowego.")
            print("		Np.: 'B3 down_right' spowoduje przesunięcie pionka B3 na ukos w prawo i w dół.")
            print("		Uwaga: 'B3 right_down' nie zadziała, ponieważ pierwszy wpisano ruch w prawo!")
            print("		Osiem kierunków ruchu: up, down, left, right, up_right, up_left, down_right, down_left")
            print()
        if option == "Z":
            loop = False

board2 = [[band, band, band, band, band, band, band],[band, B1, B2, empty, B4, B5, band],[band, empty, empty, empty, empty, empty, band],[band, empty, empty, neutron, empty, empty, band],[band, empty, empty, empty, empty, empty, band],[band, W1, W2, W3, W4, W5, band],[band, band, band, band, band, band, band]]
board3 = [[band, band, band, band, band, band, band],[band, B1, B2, B3, B4, B5, band],[band, empty, band, band, band, empty, band],[band, empty, band, neutron, band, empty, band],[band, empty, empty, empty, empty, empty, band],[band, empty, W2, empty, W4, empty, band],[band, band, band, band, band, band, band]]
board4 = [[band, band, band, band, band, band, band],[band, B1, B2, B3, B4, B5, band],[band, empty, empty, band, band, empty, band],[band, empty, band, neutron, band, empty, band],[band, empty, band, band, band, empty, band],[band, W1, W2, W3, W4, W5, band],[band, band, band, band, band, band, band]]
board5 = [[band, band, band, band, band, band, band],[band, empty, empty, empty, empty, empty, band],[band, B1, B2, B3, B4, B5, band],[band, empty, empty, neutron, empty, empty, band],[band, empty, empty, empty, empty, empty, band],[band, W1, W2, W3, W4, W5, band],[band, band, band, band, band, band, band]]
    
show(board2)
show(board3)
show(board4)
show(board5)