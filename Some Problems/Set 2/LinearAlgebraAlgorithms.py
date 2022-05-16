def zeros_matrix(rows,cols):
    # Creates a matrix of dimension (rows x cols) filled with zeros

    M = []

    while len(M) < rows:
        # Append an empty list if M doesn't have the required number of rows
        M.append([])  
        while len(M[-1]) < cols:
            # Append 0.0 to the last row of M as long as it doesn't have the required number of cols
            M[-1].append(0.0)
    
    return M


def copy_matrix(M):
    
    # Get matrix dimensions
    rows = len(M)
    cols = len(M[0])

    # Create a new matrix of zeros 
    MC = zeros_matrix(rows, cols)

    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j]

    return MC

def print_matrix(M, decimals=3):
    """
    Print a matrix one row at a time
        :param M: The matrix to be printed
    """
    for row in M:
        print([round(x, decimals)+0 for x in row])