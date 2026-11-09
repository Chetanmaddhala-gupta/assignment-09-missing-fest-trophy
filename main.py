def find_missing_trophy(total, found_numbers):
    expected = set(range(1, total + 1))
    found = set(found_numbers)
    if len(found_numbers) != len(found):
        raise ValueError("Trophy numbers must not contain duplicates.")
    if not found <= expected:
        raise ValueError(f"Numbers must be between 1 and {total}.")
    missing = expected - found
    if len(missing) != 1:
        raise ValueError("There must be exactly one missing trophy number.")
    return missing.pop()


def main():
    try:
        total = int(input("How many trophies should there be? "))
        if total < 1:
            raise ValueError("Total must be at least 1.")
        raw = input("Enter the numbers that were found, separated by spaces: ")
        numbers = [int(part) for part in raw.split()] if raw.strip() else []
        print("The missing trophy is number", find_missing_trophy(total, numbers))
    except ValueError as error:
        print("Input error:", error)


if __name__ == "__main__":
    main()
