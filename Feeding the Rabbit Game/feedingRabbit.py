# Assignment 2 - Feeding the rabbit game
# Melike Nur Dulkadir 21992919

import ast

feeding_map = input("Please enter feeding map as a list: \n")
feeding_map = str(feeding_map)
matrix = ast.literal_eval(feeding_map)                 # Converting string feeding map to an array
movements_lists = input("Please enter direction of movements as a list: \n")
movements_lists = str(movements_lists)
directions = movements_lists.strip('][').split(', ')    # Converting string movements lists to a list type
counter = 0                                             # This counter keep the score
print("Your board is: ")
for list in matrix:
    print(*list)


def score_table(list_index, element_index):             # This function arrange the scoring status
    global matrix
    global counter
    if matrix[list_index][element_index] == 'M':        # Rabbit eats meats
        matrix[list_index][element_index] = '*'         # Rabbit moves to the desired direction
        counter -= 5
    elif matrix[list_index][element_index] == 'C':      # Rabbit eats carrot
        matrix[list_index][element_index] = '*'         # Rabbit moves to the desired direction
        counter += 10
    elif matrix[list_index][element_index] == 'A':      # Rabbit eats apple
        matrix[list_index][element_index] = '*'         # Rabbit moves to the desired direction
        counter += 5
    else:
        matrix[list_index][element_index] = '*'         # Rabbit moves to the desired direction


def printing_matrix():
    global counter
    global matrix
    print("Your output should be like this:")
    for list in matrix:
        print(*list)
    print("Your score is:", counter)


def right(string, element_index, list_index):               # Funtion for right direction
    global matrix
    if string == matrix[list_index][-1] or matrix[list_index][element_index + 1] == 'W':
        pass
    elif matrix[list_index][element_index + 1] == 'P':      # Rabbit eats poison
        matrix[list_index][element_index + 1] = '*'         # Rabbit moves to the desired direction
        matrix[list_index][element_index] = 'X'
        printing_matrix()
        quit()                                              # Rabbit dies
    else:
        score_table(list_index, element_index + 1)
        matrix[list_index][element_index] = 'X'


def left(string, element_index, list_index):                # Function for left direction
    global matrix
    if string == matrix[list_index][0] or matrix[list_index][element_index - 1] == 'W':
        pass
    elif matrix[list_index][element_index - 1] == 'P':      # Rabbit eats poison
        matrix[list_index][element_index - 1] = '*'         # Rabbit moves to the desired direction
        matrix[list_index][element_index] = 'X'
        print("Your output should be like this:")
        printing_matrix()
        quit()                                              # Rabbit dies
    else:
        score_table(list_index, element_index - 1)
        matrix[list_index][element_index] = 'X'


def upward(list_index, element_index):                      # Function for up direction
    global matrix
    global list
    if list_index == 0 or matrix[list_index - 1][element_index] == 'W':
        list = matrix[list_index]
    elif matrix[list_index - 1][element_index] == 'P':      # Rabbit eats poison
        matrix[list_index - 1][element_index] = '*'         # Rabbit moves to the desired direction
        matrix[list_index][element_index] = 'X'
        printing_matrix()
        quit()                                              # Rabbit dies
    else:
        score_table(list_index - 1, element_index)
        matrix[list_index][element_index] = 'X'
        list = matrix[list_index - 1]


def downward(list_index, element_index):                    # Function for down direction
    global matrix
    global list
    if list_index == matrix.index(matrix[-1]) or matrix[list_index + 1][element_index] == 'W':
        list = matrix[list_index]
    elif matrix[list_index + 1][element_index] == 'P':      # Rabbit eats poison
        matrix[list_index + 1][element_index] = '*'         # Rabbit moves to the desired direction
        matrix[list_index][element_index] = 'X'
        printing_matrix()
        quit()                                              # Rabbit dies
    else:
        score_table(list_index + 1, element_index)
        matrix[list_index][element_index] = 'X'
        list = matrix[list_index + 1]


for list in matrix:
    for j in list:
        if j == '*':                                        # Finding the place of rabbit
            sizeCounter = len(directions)                   # Number of commands
            step = 1
            for direction in directions:
                if direction == "'R'":
                    right(j, list.index(j), matrix.index(list))
                elif direction == "'L'":
                    left(j, list.index(j), matrix.index(list))
                elif direction == "'U'":
                    upward(matrix.index(list), list.index(j))
                elif direction == "'D'":
                    downward(matrix.index(list), list.index(j))
                if step == sizeCounter:                     # If step counter reaches to number of commands,
                    printing_matrix()                       # program prints result and terminates.
                    exit()
                step += 1
