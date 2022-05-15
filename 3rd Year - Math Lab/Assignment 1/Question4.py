# Question 4
# Question Statement: Print all numbers between 1 and 50 that are divisible by 2,3,5 or 7 and print
# 5 numbers in each line, and then show the remaining numbers in a seperate line(if any).

def main():
    numbers = []
    for number in range(2,50):
        if ((number%2 == 0) or (number%3 == 0) or (number%5 == 0) or (number%7 == 0)):
            numbers.append(number)
    
    full = len(numbers)//5

    print("The required numbers printed 5 in each line:")
    
    for i in range(0,full*5,5):
        
        print(' '.join(str(x) for x in numbers[i:i+5]))

    print("The numbers left after printing 5 in each line are:")
    print(' '.join(str(x) for x in numbers[5*full:]))

if __name__ == "__main__":
    main()