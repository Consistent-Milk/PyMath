def main():
    n = int(input("Input a positive integer: "))

    if isEven(n):
        print(f"{n} is even")
    else:
        print(f"{n} is odd")


def isEven(k: int) -> bool:
    digits = list(str(k))

    even = ['0','2','4','6','8']

    if digits[-1] in even:
        return True
    else:
        return False


if __name__ == "__main__":
    main()