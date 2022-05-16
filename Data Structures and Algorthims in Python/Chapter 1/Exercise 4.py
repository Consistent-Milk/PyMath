def main():

    n = int(input("Enter a positive integer: "))

    print(f"The sum of squares of all positive numbers less than n is: {squareSum(n)}")


def squareSum(n: int) -> int:
    
    s = 0
    for val in range(n):
        s = s + val**2

    return s


if __name__ == "__main__":
    main()