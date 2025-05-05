from itertools import permutations

def solve_cryptarithmetic(word1, word2, result):
    unique_letters = set(word1 + word2 + result)
    if len(unique_letters) > 10:
        print("Too many unique letters (max 10).")
        return

    letters = list(unique_letters)
    digits = range(10)

    for perm in permutations(digits, len(letters)):
        letter_to_digit = dict(zip(letters, perm))

        # Leading letter check
        if any(letter_to_digit[word[0]] == 0 for word in [word1, word2, result]):
            continue

        def word_to_num(word):
            return int(''.join(str(letter_to_digit[char]) for char in word))

        num1 = word_to_num(word1)
        num2 = word_to_num(word2)
        num_result = word_to_num(result)

        if num1 + num2 == num_result:
            print(f"{word1}: {num1}, {word2}: {num2}, {result}: {num_result}")
            print("Mapping:", letter_to_digit)
            return

    print("No solution found.")

# Get user input
w1 = input("Enter first word: ").upper()
w2 = input("Enter second word: ").upper()
res = input("Enter result word: ").upper()

solve_cryptarithmetic(w1, w2, res)
