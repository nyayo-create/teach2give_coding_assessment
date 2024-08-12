def reverseString(s):
    reversed_string = ''
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string


def main():
     print(reverseString("hello"))


if __name__ == "__main__":
    main()