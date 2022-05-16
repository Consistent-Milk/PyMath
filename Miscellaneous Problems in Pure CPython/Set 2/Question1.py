from LinearAlgebraAlgorithms import print_matrix, matrix_multiply, transpose, matrix_addition


def main():
    M = [[1, 5, -3], [2, -9, 5], [-1, 1, -6]]
    G = [[3, -1, 2], [-2, 6, 3], [0, -4, 5]]
    T = [[4, -3, -3], [3, -2, -3], [-1, 1, 2]]

    print("The given matrices are:\n")
    for matrix in [M, G, T]:
        print_matrix(matrix)
        print('')

    GT = matrix_multiply(G, T)
    add_result = matrix_addition(transpose(M), transpose(T))

    print("The result of matrix multiplication is GT is:\n")
    print_matrix(GT)
    print("\nThe result of adding transposes of M and T is:\n")
    print_matrix(add_result)


if __name__ == "__main__":
    main()
