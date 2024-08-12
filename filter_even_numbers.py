def filterEvenNumbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


def main():
     print(filterEvenNumbers([1, 2, 3, 4, 5]))


if __name__ == "__main__":
    main()
   