def main():
    s = str(input("Input a string: "))
    k = int(input(f"Input a negative integer k such that {-len(s)} <= k < 0: "))

    print(f"The kth index value of the string is {s[k]}")

    j = len(s) + k

    print(f"The positive index equivalent to k is {j}")
    print(f"The jth index value of the string is {s[j]}")



if __name__ == "__main__":
    main()