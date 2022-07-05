import random
import itertools
from neutron import show, find_pawn, find_pawn_X, find_pawn_Y, check_for_collision, move, check_for_stalemate, check_for_win, check_for_lose, players_neutron_turn, players_pawn_turn, randomly_generated_move, randomly_generated_neutron_move, try_winning_neutron_move, try_not_losing_neutron_move, try_winning_pawn_move, priority_pawn_move, gameplay, main_menu

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

def test_find_pawn_Y():
    board = [[band, band, band, band, band, band, band],[band, B1, B2, B3, B4, B5, band],[band, empty, empty, empty, empty, empty, band],[band, empty, empty, neutron, empty, empty, band],[band, empty, empty, empty, empty, empty, band],[band, W1, W2, W3, W4, W5, band],[band, band, band, band, band, band, band]]
    Y = find_pawn_Y(B2, board)
    assert Y == 1

def test_find_pawn_X():
    board = [[band, band, band, band, band, band, band],[band, B1, B2, B3, B4, B5, band],[band, empty, empty, empty, empty, empty, band],[band, empty, empty, neutron, empty, empty, band],[band, empty, empty, empty, empty, empty, band],[band, W1, W2, W3, W4, W5, band],[band, band, band, band, band, band, band]]
    X = find_pawn_X(B2, board)
    assert X == 2

def test_find_pawn():
    board = [[band, band, band, band, band, band, band],[band, B1, B2, B3, B4, B5, band],[band, empty, empty, empty, empty, empty, band],[band, empty, empty, neutron, empty, empty, band],[band, empty, empty, empty, empty, empty, band],[band, W1, W2, W3, W4, W5, band],[band, band, band, band, band, band, band]]
    XY = find_pawn(B2, board)
    assert XY == [2,1]

def test_check_for_collision():
    board = [[band, band, band, band, band, band, band],[band, B1, B2, B3, B4, B5, band],[band, empty, empty, empty, empty, empty, band],[band, empty, empty, neutron, empty, empty, band],[band, empty, empty, empty, empty, empty, band],[band, W1, W2, W3, W4, W5, band],[band, band, band, band, band, band, band]]
    CFC1 = check_for_collision(B1, D, board)
    CFC2 = check_for_collision(B3, DL, board)
    CFC3 = check_for_collision(neutron, R, board)
    CFC4 = check_for_collision(W2, U, board)
    CFC5 = check_for_collision(W5, UR, board)
    assert CFC1 == 3
    assert CFC2 == 2
    assert CFC3 == 2
    assert CFC4 == 3
    assert CFC5 == 0

def test_move():
    board = [[band, band, band, band, band, band, band],[band, B1, B2, B3, B4, B5, band],[band, empty, empty, empty, empty, empty, band],[band, empty, empty, neutron, empty, empty, band],[band, empty, empty, empty, empty, empty, band],[band, W1, W2, W3, W4, W5, band],[band, band, band, band, band, band, band]]
    board2 = [[band, band, band, band, band, band, band],[band, B1, B2, B3, B4, B5, band],[band, empty, empty, empty, neutron, empty, band],[band, empty, empty, empty, empty, empty, band],[band, empty, empty, empty, empty, empty, band],[band, W1, W2, W3, W4, W5, band],[band, band, band, band, band, band, band]]
    move(neutron, UR, board)
    assert board == board2

def test_check_for_win():
    board = [[band, band, band, band, band, band, band],[band, B1, B2, B3, B4, B5, band],[band, empty, empty, empty, empty, empty, band],[band, empty, empty, W1, empty, empty, band],[band, empty, empty, empty, empty, empty, band],[band, neutron, W2, W3, W4, W5, band],[band, band, band, band, band, band, band]]
    board2 = [[band, band, band, band, band, band, band],[band, B1, B2, B3, B4, B5, band],[band, empty, empty, empty, neutron, empty, band],[band, empty, empty, empty, empty, empty, band],[band, empty, empty, empty, empty, empty, band],[band, W1, W2, W3, W4, W5, band],[band, band, band, band, band, band, band]]
    wynik = check_for_win(board)
    wynik2 = check_for_win(board2)
    assert wynik == True
    assert wynik2 == False

def test_check_for_lose():
    board = [[band, band, band, band, band, band, band],[band, B1, B2, B3, neutron, B5, band],[band, empty, empty, empty, empty, empty, band],[band, empty, empty, B4, empty, empty, band],[band, empty, empty, empty, empty, empty, band],[band, W1, W2, W3, W4, W5, band],[band, band, band, band, band, band, band]]
    board2 = [[band, band, band, band, band, band, band],[band, B1, B2, B3, B4, B5, band],[band, empty, empty, empty, neutron, empty, band],[band, empty, empty, empty, empty, empty, band],[band, empty, empty, empty, empty, empty, band],[band, W1, W2, W3, W4, W5, band],[band, band, band, band, band, band, band]]
    wynik = check_for_lose(board)
    wynik2 = check_for_lose(board2)
    assert wynik == True
    assert wynik2 == False

def test_check_for_stalemate():
    board = [[band, band, band, band, band, band, band],[band, empty, empty, empty, empty, B5, band],[band, empty, W2, W3, W4, empty, band],[band, empty, B4, neutron, W1, empty, band],[band, empty, B1, B2, B3, empty, band],[band, empty, empty, empty, empty, W5, band],[band, band, band, band, band, band, band]]
    board2 = [[band, band, band, band, band, band, band],[band, B1, B2, B3, B4, B5, band],[band, empty, empty, empty, neutron, empty, band],[band, empty, empty, empty, empty, empty, band],[band, empty, empty, empty, empty, empty, band],[band, W1, W2, W3, W4, W5, band],[band, band, band, band, band, band, band]]
    wynik = check_for_stalemate(board)
    wynik2 = check_for_stalemate(board2)
    assert wynik == True
    assert wynik2 == False

def test_try_winning_neutron_move():
    board = [[band, band, band, band, band, band, band],[band, B1, B2, B3, B4, B5, band],[band, empty, empty, empty, empty, empty, band],[band, empty, empty, neutron, empty, empty, band],[band, empty, empty, empty, empty, empty, band],[band, W1, W2, W3, W4, W5, band],[band, band, band, band, band, band, band]]
    board2 = [[band, band, band, band, band, band, band],[band, B1, B2, empty, B4, B5, band],[band, empty, empty, empty, empty, empty, band],[band, empty, empty, neutron, empty, empty, band],[band, empty, empty, empty, empty, empty, band],[band, W1, W2, W3, W4, W5, band],[band, band, band, band, band, band, band]]
    try_winning_neutron_move(board)
    try_winning_neutron_move(board2)
    wynik = check_for_win(board)
    wynik2 = check_for_win(board2)
    assert wynik == False
    assert wynik2 == True

def test_try_not_losing_neutron_move():
    board = [[band, band, band, band, band, band, band],[band, B1, B2, B3, B4, B5, band],[band, empty, empty, empty, empty, empty, band],[band, empty, empty, neutron, empty, empty, band],[band, empty, empty, empty, empty, empty, band],[band, W1, W2, W3, W4, W5, band],[band, band, band, band, band, band, band]]
    board2 = [[band, band, band, band, band, band, band],[band, B1, B2, B3, B4, B5, band],[band, empty, band, band, band, empty, band],[band, empty, band, neutron, band, empty, band],[band, empty, empty, empty, empty, empty, band],[band, empty, W2, empty, W4, empty, band],[band, band, band, band, band, band, band]]
    try_not_losing_neutron_move(board)
    try_not_losing_neutron_move(board2)
    wynik = check_for_lose(board)
    wynik2 = check_for_lose(board2)
    assert wynik == True
    assert wynik2 == False

def test_try_winning_pawn_move():
    board = [[band, band, band, band, band, band, band],[band, B1, B2, B3, B4, B5, band],[band, empty, empty, empty, empty, empty, band],[band, empty, empty, neutron, empty, empty, band],[band, empty, empty, empty, empty, empty, band],[band, W1, W2, W3, W4, W5, band],[band, band, band, band, band, band, band]]
    board2 = [[band, band, band, band, band, band, band],[band, B1, B2, B3, B4, B5, band],[band, empty, empty, band, band, empty, band],[band, empty, band, neutron, band, empty, band],[band, empty, band, band, band, empty, band],[band, W1, W2, W3, W4, W5, band],[band, band, band, band, band, band, band]]
    try_winning_pawn_move(board)
    try_winning_pawn_move(board2)
    wynik = check_for_stalemate(board)
    wynik2 = check_for_stalemate(board2)
    assert wynik == False
    assert wynik2 == True

def test_priority_pawn_move():
    board = [[band, band, band, band, band, band, band],[band, B1, B2, B3, B4, B5, band],[band, empty, empty, empty, empty, empty, band],[band, empty, empty, neutron, empty, empty, band],[band, empty, empty, empty, empty, empty, band],[band, W1, W2, W3, W4, W5, band],[band, band, band, band, band, band, band]]
    board2 = [[band, band, band, band, band, band, band],[band, empty, empty, empty, empty, empty, band],[band, B1, B2, B3, B4, B5, band],[band, empty, empty, neutron, empty, empty, band],[band, empty, empty, empty, empty, empty, band],[band, W1, W2, W3, W4, W5, band],[band, band, band, band, band, band, band]]
    wynik = priority_pawn_move(board)
    wynik2 = priority_pawn_move(board2)
    assert wynik == True
    assert wynik2 == False