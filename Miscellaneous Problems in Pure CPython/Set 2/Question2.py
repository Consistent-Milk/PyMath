# Test whether M is invertible, if invertible find its inverse and verify result.

from LinearAlgebraAlgorithms import determinant_fast


def main():
    M = [[1, 5, -3], [2, -9, 5], [-1, 1, -6]]

    det = determinant_fast(M)

    if det == 0:
        print("M is not invertible.")
    else:
        print(f"M is invertible and the determinant of M is = {det:.2f}")


if __name__ == "__main__":
    main()
