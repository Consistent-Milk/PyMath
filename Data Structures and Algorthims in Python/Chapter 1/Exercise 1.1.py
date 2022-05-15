def main():
    n = int(input("Enput a positive integer: "))
    m = int(input("Enput a positive integer: "))

    if is_multiple(n,m):
        print(f"{n} is a multiple of {m}")
    else:
        print(f"{n} is not a multiple of {m}")


def is_multiple(n: int, m: int) -> bool:
    if (n%m == 0):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
