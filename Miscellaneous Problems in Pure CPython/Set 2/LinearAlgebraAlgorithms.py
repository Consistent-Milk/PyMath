# Pure CPython implementations of various basic Linear Algebra operations

def zeros_matrix(rows: int, cols: int) -> list:
    """
    Creates a matrix filled with zeros.
        :param rows: the number of rows the matrix should have
        :param cols: the number of columns the matrix should have
        :return: list of lists that form the matrix
    """
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)

    return M


def identity_matrix(n: int) -> list:
    """
    Creates and returns an identity matrix.
        :param n: the square size of the matrix
        :return: a square identity matrix
    """
    IdM = zeros_matrix(n, n)
    for i in range(n):
        IdM[i][i] = 1.0

    return IdM


def copy_matrix(M: list) -> list:
    """
    Creates and returns a copy of a matrix.
        :param M: The matrix to be copied
        :return: A copy of the given matrix
    """
    # Section 1: Get matrix dimensions
    rows = len(M)
    cols = len(M[0])

    # Section 2: Create a new matrix of zeros
    MC = zeros_matrix(rows, cols)

    # Section 3: Copy values of M into the copy
    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j]

    return MC


def print_matrix(M: list, decimals=3):
    """
    Print a matrix one row at a time
        :param M: The matrix to be printed
    """
    for row in M:
        print([round(x, decimals)+0 for x in row])


def transpose(M: list) -> list:
    """
    Returns a transpose of a matrix.
        :param M: The matrix to be transposed
        :return: The transpose of the given matrix
    """
    # Section 1: if a 1D array, convert to a 2D array = matrix
    if not isinstance(M[0], list):
        M = [M]

    # Section 2: Get dimensions
    rows = len(M)
    cols = len(M[0])

    # Section 3: MT is zeros matrix with transposed dimensions
    MT = zeros_matrix(cols, rows)

    # Section 4: Copy values from M to it's transpose MT
    for i in range(rows):
        for j in range(cols):
            MT[j][i] = M[i][j]

    return MT


def matrix_addition(A: list, B: list) -> list:
    """
    Adds two matrices and returns the sum
        :param A: The first matrix
        :param B: The second matrix
        :return: Matrix sum
    """
    # Section 1: Ensure dimensions are valid for matrix addition
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if rowsA != rowsB or colsA != colsB:
        raise ArithmeticError('Matrices are NOT the same size.')

    # Section 2: Create a new matrix for the matrix sum
    C = zeros_matrix(rowsA, colsB)

    # Section 3: Perform element by element sum
    for i in range(rowsA):
        for j in range(colsB):
            C[i][j] = A[i][j] + B[i][j]

    return C


def matrix_subtraction(A: list, B: list) -> list:
    """
    Subtracts matrix B from matrix A and returns difference
        :param A: The first matrix
        :param B: The second matrix
        :return: Matrix difference
    """
    # Section 1: Ensure dimensions are valid for matrix subtraction
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if rowsA != rowsB or colsA != colsB:
        raise ArithmeticError('Matrices are NOT the same size.')

    # Section 2: Create a new matrix for the matrix difference
    C = zeros_matrix(rowsA, colsB)

    # Section 3: Perform element by element subtraction
    for i in range(rowsA):
        for j in range(colsB):
            C[i][j] = A[i][j] - B[i][j]

    return C


def matrix_multiply(A: list, B: list) -> list:
    """
    Returns the product of the matrix A * B
        :param A: The first matrix - ORDER MATTERS!
        :param B: The second matrix
        :return: The product of the two matrices
    """
    # Section 1: Ensure A & B dimensions are correct for multiplication
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if colsA != rowsB:
        raise ArithmeticError(
            'Number of A columns must equal number of B rows.')

    # Section 2: Store matrix multiplication in a new matrix
    C = zeros_matrix(rowsA, colsB)
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C
