def main():

    sequence = [1, 2, 3, 5]

    if (matcher(sequence)):
        print("The elements in the sequence are distinct.")
    else:
        print("The elements in the sequence are not distinct.")


def matcher(sequence: list) -> bool:
    duplicate_drop = list(set(sequence))

    if len(sequence) == len(duplicate_drop):
        return True
    else:
        return False


if __name__ == "__main__":
    main()