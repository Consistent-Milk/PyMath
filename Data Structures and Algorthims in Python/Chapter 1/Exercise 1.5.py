def main():
    n = int(input("Enter a positive integer n: "))
    
    result = sum([x**2 for x in range(n)])
    print(f"The sum is: {result}")


if __name__ == "__main__":
    main()