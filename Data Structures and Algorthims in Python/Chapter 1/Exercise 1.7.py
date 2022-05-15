def main():
    n = int(input("Enter a positive integer: "))
    result = sum([x**2 for x in range(n) if x%2 != 0])
    print(f"The sum is {result}")


if __name__ == "__main__":
    main()