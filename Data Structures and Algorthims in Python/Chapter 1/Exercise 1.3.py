import random

def main():
    data = [random.randint(1,100) for x in range(10)] 

    print(f"The sequence of numbers is: {data}")
    print(f"The tuple of minimum and maximum numbers is: {minMax(data)}")


def minMax(data: list) -> tuple:

    sorted_list = sorted(data)

    return (sorted_list[0], sorted_list[-1])


if __name__ == "__main__":
    main()