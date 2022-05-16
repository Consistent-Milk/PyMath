def main():
    sequence = list(range(1,11))
    products = oddProduct(sequence)

    print("The distinct pair of numbers in the sequence that has an odd product are:")
    for val1, val2 in products:
        print(f"{val1} with a product of {val2}")


def oddProduct(sequence: list) -> list:
    products = [[(x,y),x*y] for x in sequence for y in sequence if x*y%2 !=0 and x != y and x < y]

    return products


if __name__ == "__main__":
    main()