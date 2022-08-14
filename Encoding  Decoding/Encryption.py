# Encryption
# 21992919 Melike Nur Dulkadir

import sys
import os
from string import ascii_uppercase,ascii_lowercase

class UndefinedParameterError(Exception):
    pass

class ParameterNumberError(Exception):
    pass

class CouldNotBeReadError(Exception):
    pass

class FileEmptyError(Exception):
    pass

class InvalidCharError(Exception):
    pass

class KeyFileCouldNotBeReadError(Exception):
    pass

class KeyFileEmptyError(Exception):
    pass

class InvalidCharInKeyError(Exception):
    pass

try:
    operation = sys.argv[1]
    if operation == "dec" or operation == "enc":                                    # Operation type parameter should be enc or dec.
        pass
    else:
        raise UndefinedParameterError
    if not len(sys.argv) == 5:                                                      # The program should has 4 parameters.
        raise ParameterNumberError

    try:
        key_file = open(sys.argv[2], "r")
    except FileNotFoundError:
        print("Key file not found error")
        quit()

    if not sys.argv[2].endswith('.txt'):                                            # Key file should be in txt format.
        raise KeyFileCouldNotBeReadError

    try:
        key_file_nums = []
        for i in key_file.readlines():
            if " " in i:
                raise ValueError
            else:
                key_file_nums.append([int(j) for j in i.strip("\n").split(",")])

        if not key_file_nums:
            raise KeyFileEmptyError                                                 # Occurs if key file is empty.
    except ValueError:
        print("Invalid character in key file error")
        quit()

    try:
        input_file = open(sys.argv[3],"r")
    except FileNotFoundError:
        print("Input file not found error")
        quit()

    if not sys.argv[3].endswith('.txt'):                                            # Input file should be in txt format.
        raise CouldNotBeReadError

    input_file_char = input_file.readline()
    if not input_file_char:
        raise FileEmptyError                                                        # Occurs if input file is empty.

    # Encoding
    if os.path.basename(sys.argv[3]) == "plain_input.txt":
        letters = [i for i in input_file_char]
        for j in letters:
            if j in ascii_uppercase or j in ascii_lowercase or j == " ":
                pass
            else:
                raise InvalidCharError

        def encoding(group_matrix):                                                 # Function multiplies key matrix and group matrix for encoding.
            global key_file_nums
            matrix1 = key_file_nums
            matrix2 = [[i] for i in group_matrix]
            result = [[0] for i in range(len(matrix2))]
            for i in range(len(matrix1)):
                for j in range(len(matrix2[0])):
                    for k in range(len(matrix2)):
                        result[i][j] += matrix1[i][k] * matrix2[k][j]
            return result

        n = len(key_file_nums)
        if len(letters) % n != 0:                                                   # Spaces should be added for make groups fully formed.
            letters.extend([" " for i in range(len(letters) % n + 1)])
        enc_list = [letters[i:i + n] for i in range(0, len(letters), n)]            # The letters of the message divided into groups.
        for i in range(len(enc_list)):
            for j in enc_list[i]:
                if j in ascii_uppercase:
                    enc_list[i][enc_list[i].index(j)] = ascii_uppercase.index(j)+1
                elif j in ascii_lowercase:
                    enc_list[i][enc_list[i].index(j)] = ascii_lowercase.index(j)+1
                elif j == ' ':
                    enc_list[i][enc_list[i].index(j)] = 27

        result = map(encoding,enc_list)                                             # Map function returns a list of the results of encoding function.

        with open(sys.argv[4],"w") as output_file:
            output_file.write(",".join(repr(*j) for i in list(result) for j in i))

    # Decoding
    elif os.path.basename(sys.argv[3]) == "ciphertext.txt":
        numbers = [i for i in input_file_char]
        n = len(key_file_nums)
        dec_list = [int(i) for i in input_file_char.split(",")]
        dec_list = [dec_list[i:i+n] for i in range(0, len(dec_list), n)]            # Numbers of the encoding message divided into groups.

        for j in numbers:
            if j.isdigit() or j == ",":
                pass
            else: raise InvalidCharError


        def reverse(matrix_list):                                                   # This function reverse the matrix for decoding.
            def find_determinant(matrix_list):                                      # This function finds the determinant of matrix.
                if len(matrix_list) == 2:
                    det_min = matrix_list[0][0] * matrix_list[1][1] - matrix_list[0][1] * matrix_list[1][0]
                    return det_min
                else:
                    det_min = 0
                    for i in range(len(matrix_list)):
                        sign = 1 if i % 2 == 0 else -1
                        minor_of_matrix = []
                        for line in (matrix_list[1:]):
                            minor_of_matrix.append(line[:i] + line[i + 1:])
                        det_min += sign * matrix_list[0][i] * find_determinant(minor_of_matrix)
                    return det_min

            det_min = find_determinant(matrix_list)
            if len(matrix_list) == 2:
                inverse_matrix = [[matrix_list[1][1] / det_min, -1 * matrix_list[0][1] / det_min],[-1 * matrix_list[1][0] / det_min, matrix_list[0][0] / det_min]]
                return inverse_matrix
            else:
                n = len(matrix_list)
                inverse_matrix = [[0 for j in range(n)] for i in range(n)]            # It makes a matrix of key matrix size.
                for i in range(len(matrix_list)):
                    for j in range(len(matrix_list)):
                        sign = -1 if (i + j) % 2 == 0 else 1
                        minor_list = []
                        for line in (matrix_list[:i] + matrix_list[i + 1:]):
                            minor_list.append(line[:j] + line[j + 1:])
                        inverse_matrix[j][i] = (sign) * find_determinant(minor_list)  # It determines the elements of inverse matrix
                        if det_min > 0:                                               # with using determinants of minor lists.
                            inverse_matrix[j][i] = -inverse_matrix[j][i]
                return inverse_matrix

        def decoding(pair_matrix):                                                    # Function multiplies key matrix and group matrix for decoding.
            matrix1 = reverse(key_file_nums)
            matrix2 = [[i] for i in pair_matrix]
            result = [[0] for i in range(len(matrix2))]
            for i in range(len(matrix1)):
                for j in range(len(matrix2[0])):
                    for k in range(len(matrix2)):
                        result[i][j] += (matrix1[i][k] * matrix2[k][j])
            return result

        result = map(decoding, dec_list)                                                # Map function returns a list of the results of decoding function.
        result = [int(k) for i in list(result) for j in i for k in j]

        with open(sys.argv[4], "w") as output_file:
            for i in result:
                if i == 27:
                    output_file.write(" ")
                else:
                    output_file.write(ascii_uppercase[i-1])


except KeyFileCouldNotBeReadError:
    print("Key file could not be read error")
except KeyFileEmptyError:
    print("Key file is empty error")
except ParameterNumberError:
    print("Parameter number error")
except UndefinedParameterError:
    print("Undefined parameter error")
except CouldNotBeReadError:
    print("Input file could not be read error")
except FileEmptyError:
    print("Input file is empty error")
except InvalidCharError:
    print("Invalid character in input file error")
except InvalidCharInKeyError:
    print("Invalid character in key file error")

