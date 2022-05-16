# Question 3
# Question Statement: Find the sum and product of two given sequences upto N. 

import math

def main():
    n = int(input('Enter the upper limit of summation and product:'))
    s = 0
    p = 1
    for i in range(1,n+1):
        s = s + f1(i)
        p = p * f2(i)
    
    print(f"The summation is: {s:.2f}")
    print(f"The product is: {p:.2f}")

def f1(x: float) -> float:
    y = math.sqrt(x)/(x**2 +1)
    return y

def f2(x: float) -> float:
    y = ((x-1)**2)/math.sqrt(x)
    return y

if __name__ == "__main__":
    main()