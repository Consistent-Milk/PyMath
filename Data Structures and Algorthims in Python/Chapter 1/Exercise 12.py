import random

def main():
    ref_list = [1, 5, 8, 2, -2, 6, 0, 2]
    rand_index = random.randrange(0,len(ref_list))

    print(f"The random index chosen is: {rand_index}")
    print(f"The random element from the given sequence is: {ref_list[rand_index]}")

if __name__ == "__main__":
    main()