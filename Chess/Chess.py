# Chess Game
# 21992919 Melike Nur Dulkadir
import sys
from string import ascii_lowercase, ascii_uppercase
f = open(sys.argv[1], "r")
commands= [line.split() for line in f.readlines()]
f.close()

board = [{"a8": "R1", "b8": "N1", "c8": "B1", "d8": "QU", "e8": "KI", "f8": "B2", "g8": "N2", "h8": "R2"},
         {"a7": "P1", "b7": "P2", "c7": "P3", "d7": "P4", "e7": "P5", "f7": "P6", "g7": "P7", "h7": "P8"},
         {"a6": "  ", "b6": "  ", "c6": "  ", "d6": "  ", "e6": "  ", "f6": "  ", "g6": "  ", "h6": "  "},
         {"a5": "  ", "b5": "  ", "c5": "  ", "d5": "  ", "e5": "  ", "f5": "  ", "g5": "  ", "h5": "  "},
         {"a4": "  ", "b4": "  ", "c4": "  ", "d4": "  ", "e4": "  ", "f4": "  ", "g4": "  ", "h4": "  "},
         {"a3": "  ", "b3": "  ", "c3": "  ", "d3": "  ", "e3": "  ", "f3": "  ", "g3": "  ", "h3": "  "},
         {"a2": "p1", "b2": "p2", "c2": "p3", "d2": "p4", "e2": "p5", "f2": "p6", "g2": "p7", "h2": "p8"},
         {"a1": "r1", "b1": "n1", "c1": "b1", "d1": "qu", "e1": "ki", "f1": "b2", "g1": "n2", "h1": "r2"}]


# Function that finds piece
def find_piece(piece):
    for ranks in board:
        for keys in ranks.keys():
            if board[board.index(ranks)][keys] == piece:
                return keys, board.index(ranks)


# Function that executes initialize command
def initialize():
    global board
    board_initialize = [{"a8": "R1", "b8": "N1", "c8": "B1", "d8": "QU", "e8": "KI", "f8": "B2", "g8": "N2", "h8": "R2"},{"a7": "P1", "b7": "P2", "c7": "P3", "d7": "P4", "e7": "P5", "f7": "P6", "g7": "P7", "h7": "P8"},{"a6": "  ", "b6": "  ", "c6": "  ", "d6": "  ", "e6": "  ", "f6": "  ", "g6": "  ", "h6": "  "},{"a5": "  ", "b5": "  ", "c5": "  ", "d5": "  ", "e5": "  ", "f5": "  ", "g5": "  ", "h5": "  "},{"a4": "  ", "b4": "  ", "c4": "  ", "d4": "  ", "e4": "  ", "f4": "  ", "g4": "  ", "h4": "  "},{"a3": "  ", "b3": "  ", "c3": "  ", "d3": "  ", "e3": "  ", "f3": "  ", "g3": "  ", "h3": "  "},{"a2": "p1", "b2": "p2", "c2": "p3", "d2": "p4", "e2": "p5", "f2": "p6", "g2": "p7", "h2": "p8"},{"a1": "r1", "b1": "n1", "c1": "b1", "d1": "qu", "e1": "ki", "f1": "b2", "g1": "n2", "h1": "r2"}]
    board = board_initialize.copy()
    board_list = [[i for i in ranks.values()] for ranks in board]
    for j in board_list:
        print(*j)



# Function that finds possible positions
def possible_positions(letter_index, number_index, rank_number, incr1, incr2, incr3, black_list, white_list):
    global board
    while (0 <= rank_number < 8) and (0 <= letter_index < 8) and (0 < number_index < 9):
        if board[rank_number][ascii_lowercase[letter_index] + str(number_index)] == "  ":  # if the square is empty
            black_list.append(ascii_lowercase[letter_index] + str(number_index))
            white_list.append(ascii_lowercase[letter_index] + str(number_index))
            letter_index += incr1
            number_index += incr2
            rank_number += incr3
        elif board[rank_number].get(ascii_lowercase[letter_index] + str(number_index))[0] in ascii_lowercase and board[rank_number].get(ascii_lowercase[letter_index] + str(number_index))[0] != 'k':
            black_list.append(ascii_lowercase[letter_index] + str(number_index))
            break
        elif board[rank_number].get(ascii_lowercase[letter_index] + str(number_index))[0] in ascii_uppercase and board[rank_number].get(ascii_lowercase[letter_index] + str(number_index))[0] != 'K':
            white_list.append(ascii_lowercase[letter_index] + str(number_index))
            break
        else:
            break


# Function that controls knight's L moves and king's moves
def knight_king_move(letter_index, number_index, rank_number, black_knight_list, white_knight_list):
    global board
    if 0 <= rank_number < 8 and 0 <= letter_index < 8 and 0 < number_index < 9:
        if board[rank_number][ascii_lowercase[letter_index] + str(number_index)] == "  ":   # if the square is empty
            black_knight_list.append(ascii_lowercase[letter_index] + str(number_index))
            white_knight_list.append(ascii_lowercase[letter_index] + str(number_index))
        elif board[rank_number].get(ascii_lowercase[letter_index] + str(number_index))[0] in ascii_lowercase and board[rank_number].get(ascii_lowercase[letter_index] + str(number_index))[0] != 'k':
            black_knight_list.append(ascii_lowercase[letter_index] + str(number_index))
        elif board[rank_number].get(ascii_lowercase[letter_index] + str(number_index))[0] in ascii_uppercase and board[rank_number].get(ascii_lowercase[letter_index] + str(number_index))[0] != 'K':
            white_knight_list.append(ascii_lowercase[letter_index] + str(number_index))

# Function that controls knight's diagonal moves
def knight_dia(letter_index, number_index, rank_number, black_knight_list, white_knight_list):
    global board
    if 0 <= rank_number < 8 and 0 <= letter_index < 8 and 0 < number_index < 9:
        if board[rank_number][ascii_lowercase[letter_index] + str(number_index)] == "  ":
            black_knight_list.append(ascii_lowercase[letter_index] + str(number_index))
            white_knight_list.append(ascii_lowercase[letter_index] + str(number_index))

# Move commands for pieces
def moving_command(arg, piece):
    for ranks in board:
        for i in ranks:
            if i == arg:
                board[board.index(ranks)][arg] = piece

# Function that operates commands according to given input
def show_moves(list_name, rank, key_name, piece, *argv):
    if argv[0] == "showmoves":
        print("FAILED") if list_name == [] else print(*sorted(list_name))
    elif argv[0] == "move":
        if argv[1] in list_name:
            moving_command(argv[1], piece)
            board[rank][key_name] = "  "
            print("OK")
        else:
            print("FAILED")


def pawn(piece, *argv):
    global board
    black_pawn_list, white_pawn_list = [], []
    key_name, rank = find_piece(piece)
    if piece[0] == 'P' and rank < 7:                # if the piece is black
        if board[rank+1][key_name[0]+(str(int(key_name[1])-1))] == "  " or (board[rank+1].get(key_name[0]+(str(int(key_name[1])-1)))[0] in ascii_lowercase and board[rank+1].get(key_name[0]+(str(int(key_name[1])-1)))[0] != 'k'):
            black_pawn_list.append(key_name[0]+(str(int(key_name[1])-1)))
        if argv[0] == "move":
            if argv[1] in black_pawn_list:
                board[rank+1][key_name[0]+(str(int(key_name[1])-1))] = piece
                board[rank][key_name] = "  "
                print("OK")
            else:
                print("FAILED")
        elif argv[0] == "showmoves":
            print("FAILED") if white_pawn_list == [] else print(*black_pawn_list)
    elif piece[0] == 'p' and rank > 1:          # if the piece is white
        if board[rank-1][key_name[0]+(str(int(key_name[1])+1))] == "  " or (board[rank-1].get(key_name[0]+(str(int(key_name[1])+1)))[0] in ascii_uppercase and board[rank-1].get(key_name[0]+(str(int(key_name[1])+1)))[0] != 'K'):
            white_pawn_list.append(key_name[0]+(str(int(key_name[1])+1)))
        if argv[0] == "move":
            if argv[1] in white_pawn_list:
                board[rank-1][key_name[0]+(str(int(key_name[1])+1))] = piece
                board[rank][key_name] = "  "
                print("OK")
            else:
                print("FAILED")
        elif argv[0] == "showmoves":
            print("FAILED") if white_pawn_list == [] else print(*white_pawn_list)


def bishop(piece, *argv):
    global board
    black_bishop_list, white_bishop_list = [], []
    key_name, rank = find_piece(piece)
    x, y = ascii_lowercase.index(key_name[0]), int(key_name[1])
    if piece[0] == 'B':                         # if the piece is black
        possible_positions(x - 1, y - 1, rank + 1, -1, -1, 1, black_bishop_list, white_bishop_list), possible_positions(x + 1, y - 1, rank + 1, 1, -1, 1, black_bishop_list, white_bishop_list)
        if argv[0] == "showmoves":
            show_moves(black_bishop_list, rank, key_name, piece, argv[0])
        elif argv[0] == "move":
            show_moves(black_bishop_list, rank, key_name, piece, argv[0], argv[1])
    elif piece[0] == 'b':                       # if the piece is white
        possible_positions(x - 1, y + 1, rank - 1, -1, 1, -1, black_bishop_list, white_bishop_list), possible_positions(x + 1, y + 1, rank - 1, 1, 1, -1, black_bishop_list, white_bishop_list)
        if argv[0] == "showmoves":
            show_moves(white_bishop_list, rank, key_name, piece, argv[0])
        elif argv[0] == "move":
            show_moves(white_bishop_list, rank, key_name, piece, argv[0], argv[1])


def rook(piece, *argv):
    global board
    black_rook_list, white_rook_list = [], []
    key_name,rank = find_piece(piece)
    x, y = ascii_lowercase.index(key_name[0]), int(key_name[1])
    possible_positions(x, y - 1, rank + 1, 0, -1, 1, black_rook_list, white_rook_list), possible_positions(x, y + 1, rank - 1, 0, 1, -1, black_rook_list, white_rook_list)
    possible_positions(x + 1, y, rank, 1, 0, 0, black_rook_list, white_rook_list), possible_positions(x - 1, y, rank, -1, 0, 0, black_rook_list, white_rook_list)
    if piece[0] == 'R':                             # if the piece is black
        if argv[0] == "showmoves":
            show_moves(black_rook_list, rank, key_name, piece, argv[0])
        elif argv[0] == "move":
            show_moves(black_rook_list, rank, key_name, piece, argv[0], argv[1])
    if piece[0] == 'r':                             # if the piece is white
        if argv[0] == "showmoves":
            show_moves(white_rook_list, rank, key_name, piece, argv[0])
        elif argv[0] == "move":
            show_moves(white_rook_list, rank, key_name, piece, argv[0], argv[1])


def queen(piece, *argv):
    global board
    black_queen_list, white_queen_list = [], []
    key_name, rank = find_piece(piece)
    x, y = ascii_lowercase.index(key_name[0]), int(key_name[1])
    possible_positions(x, y - 1, rank + 1, 0, -1, 1, black_queen_list, white_queen_list), possible_positions(x, y + 1, rank - 1, 0, 1, -1, black_queen_list, white_queen_list)
    possible_positions(x + 1, y, rank, 1, 0, 0, black_queen_list, white_queen_list), possible_positions(x - 1, y, rank, -1, 0, 0, black_queen_list, white_queen_list)
    possible_positions(x - 1, y - 1, rank + 1, -1, -1, 1, black_queen_list, white_queen_list), possible_positions(x + 1, y - 1, rank + 1, 1, -1, 1, black_queen_list, white_queen_list)
    possible_positions(x - 1, y + 1, rank - 1, -1, 1, -1, black_queen_list, white_queen_list), possible_positions(x + 1, y + 1, rank - 1, 1, 1, -1, black_queen_list, white_queen_list)
    if piece[0] == 'Q':                         # if the piece is black
        if argv[0] == "showmoves":
            show_moves(black_queen_list, rank, key_name, piece, argv[0])
        elif argv[0] == "move":
            show_moves(black_queen_list, rank, key_name, piece, argv[0], argv[1])
    if piece[0] == 'q':                         # if the piece is white
        if argv[0] == "showmoves":
            show_moves(white_queen_list, rank, key_name, piece, argv[0])
        elif argv[0] == "move":
            show_moves(white_queen_list, rank, key_name, piece, argv[0], argv[1])


def knight(piece, *argv):
    black_knight_list, white_knight_list = [], []
    key_name, rank = find_piece(piece)
    x, y = ascii_lowercase.index(key_name[0]), int(key_name[1])
    knight_king_move(x - 1, y + 2, rank - 2, black_knight_list, white_knight_list), knight_king_move(x + 1, y + 2, rank - 2, black_knight_list, white_knight_list)
    knight_king_move(x - 2, y + 1, rank - 1, black_knight_list, white_knight_list), knight_king_move(x + 2, y + 1, rank - 1, black_knight_list, white_knight_list)
    knight_king_move(x - 1, y - 2, rank + 2, black_knight_list, white_knight_list), knight_king_move(x + 1, y - 2, rank + 2, black_knight_list, white_knight_list)
    knight_king_move(x - 2, y - 1, rank + 1, black_knight_list, white_knight_list), knight_king_move(x + 2, y - 1, rank + 1, black_knight_list, white_knight_list)
    knight_dia(x - 1, y + 1, rank - 1, black_knight_list, white_knight_list), knight_dia(x + 1, y + 1, rank - 1, black_knight_list, white_knight_list)
    knight_dia(x - 1, y - 1, rank + 1, black_knight_list, white_knight_list), knight_dia(x + 1, y - 1, rank + 1, black_knight_list, white_knight_list)
    if piece[0] == 'N':                         # if the piece is black
        if argv[0] == "showmoves":
            show_moves(black_knight_list, rank, key_name, piece, argv[0])
        elif argv[0] == "move":
            show_moves(black_knight_list, rank, key_name, piece, argv[0], argv[1])
    elif piece[0] == 'n':                       # if the piece is white
        if argv[0] == "showmoves":
            show_moves(white_knight_list, rank, key_name, piece, argv[0])
        elif argv[0] == "move":
            show_moves(white_knight_list, rank, key_name, piece, argv[0], argv[1])


def king(piece, *argv):
    black_king_list, white_king_list = [], []
    key_name, rank = find_piece(piece)
    x, y = ascii_lowercase.index(key_name[0]), int(key_name[1])
    knight_king_move(x - 1, y + 1, rank - 1, black_king_list, white_king_list), knight_king_move(x + 1, y + 1, rank - 1, black_king_list, white_king_list)
    knight_king_move(x, y + 1, rank - 1, black_king_list, white_king_list), knight_king_move(x, y - 1, rank + 1, black_king_list, white_king_list)
    knight_king_move(x - 1, y - 1, rank + 1, black_king_list, white_king_list), knight_king_move(x + 1, y - 1, rank + 1, black_king_list, white_king_list)
    knight_king_move(x - 1, y, rank, black_king_list, white_king_list), knight_king_move(x + 1, y, rank, black_king_list, white_king_list)
    if piece[0] == 'K':                     # if the piece is black
        if argv[0] == "showmoves":
            show_moves(black_king_list, rank, key_name, piece, argv[0])
        elif argv[0] == "move":
            show_moves(black_king_list, rank, key_name, piece, argv[0], argv[1])
    elif piece[0] == 'k':                   # if the piece is white
        if argv[0] == "showmoves":
            show_moves(white_king_list, rank, key_name, piece, argv[0])
        elif argv[0] == "move":
            show_moves(white_king_list, rank, key_name, piece, argv[0], argv[1])


for word in commands:
    if word[0] == "print":
        print(">", *word)
        print("-------------------------")
        board_list = [[i for i in ranks.values()] for ranks in board]
        for j in board_list:
            print(*j)
        print("-------------------------")
    elif word[0] == "initialize":
        print(">", *word)
        print("OK")
        print("-------------------------")
        initialize()
        print("-------------------------")
    elif word[0] == "exit":
        print(">", *word)
        exit()
    elif word[0] == "showmoves":
        print(">", *word)
        if word[1][0] == 'p' or word[1][0]=='P':
            pawn(word[1],word[0])
        elif word[1][0] == 'b' or word[1][0]=='B':
            bishop(word[1],word[0])
        elif word[1][0] == 'r' or word[1][0]=='R':
            rook(word[1],word[0])
        elif word[1][0] == 'q' or word[1][0]=='Q':
            queen(word[1],word[0])
        elif word[1][0] == 'n' or word[1][0]=='N':
            knight(word[1],word[0])
        elif word[1][0] == 'k' or word[1][0]=='K':
            king(word[1],word[0])
    elif word[0] == "move":
        print(">", *word)
        if word[1][0] == 'p' or word[1][0] == 'P':
            pawn(word[1], word[0],word[2])
        elif word[1][0] == 'b' or word[1][0] == 'B':
            bishop(word[1],word[0],word[2])
        elif word[1][0] == 'r' or word[1][0] == 'R':
            rook(word[1],word[0],word[2])
        elif word[1][0] == 'q' or word[1][0] == 'Q':
            queen(word[1],word[0],word[2])
        elif word[1][0] == 'n' or word[1][0] == 'N':
            knight(word[1],word[0],word[2])
        elif word[1][0] == 'k' or word[1][0] == 'K':
            king(word[1], word[0], word[2])
    else:
        pass

