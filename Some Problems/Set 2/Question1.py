from LinearAlgebraAlgorithms import print_matrix

def main():
    M = [[1, 5, -3], [2, -9, 5], [-1, 1, -6]]
    G = [[3, -1, 2], [-2, 6, 3], [0, -4, 5]]
    T = [[4, -3, -3], [3, -2, -3], [-1, 1, 2]]

    print("The given matrices are:\n")
    for matrix in [M, G, T]:
        print_matrix(matrix)
        print('')

if __name__ == "__main__":
    main()
