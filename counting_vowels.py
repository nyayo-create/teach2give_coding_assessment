def count_vowels(word):
     vowels = ['a', 'e', 'i', 'o', 'u']
     vowel_count = 0
     for _ in word:
          if _ in vowels:
               vowel_count = vowel_count + 1
     return vowel_count


def main():
     word = "the quick brown fox"
     print(count_vowels(word.lower()))


if __name__ == "__main__":
     main()
