# Question 5
# Question Statement: Reverse a given number and print it, write a function to check if the given number is
# palindromic or not. 

def main():
    n = int(input("Input an integer number: "))
    print(f"The number reversed is : {reverse(n)}")
    if palindrome(n):
        print(f"The given number is palindromic.")
    else:
        print(f"The given number is not palindromic.")

def reverse(number: int) -> int:
    digits = list(str(number))
    reversed = digits[::-1]
    reversed_number = ''.join(x for x in reversed)
    return int(reversed_number)

def palindrome(number: int) -> bool:
    digits = list(str(number))
    reversed = digits[::-1]
    if digits == reversed:
        return True
    else:
        return False

if __name__ == "__main__":
    main()