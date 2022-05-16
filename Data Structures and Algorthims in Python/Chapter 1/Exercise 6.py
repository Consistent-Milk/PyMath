def main():
    
    n = int(input("Enter a positive integer: "))
    result = squareOddSum(n)
    print(f"The sum is: {result}")


def squareOddSum(n: int) -> int:
    
    s = 0
    for val in range(n):
        if val%2 != 0:
            s = s + val**2

    return s

if __name__ == "__main__":
    main()