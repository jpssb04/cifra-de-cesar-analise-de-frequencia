import unicodedata
import time
from collections import Counter


def remove_accents(text):
    # remove accents from letters
    return ''.join(
        c for c in unicodedata.normalize("NFD", text)
        if unicodedata.category(c) != "Mn"
    )


def decipher_text(text, alphabet, shift_value):
    # create number->letter mapping
    alphabet_reversed = {v: k for k, v in alphabet.items()}
    deciphered_text = ""

    for letter in text:
        if letter.isalpha():
            num = alphabet[letter.lower()]
            # reverse Caesar shift with wrap-around
            num = (num - shift_value - 1) % 26 + 1
            deciphered_text += alphabet_reversed[num]
        else:
            deciphered_text += letter

    return deciphered_text


def prepare_text(text):
    # lowercase, remove accents, keep only letters
    temp_text = text.lower()
    temp_text = remove_accents(temp_text)
    return "".join(c for c in temp_text if c.isalpha())


def get_top_letters(text, n=3):
    # return n most common letters
    count = Counter(text)
    most_common_letters = count.most_common(n)
    first = most_common_letters[0][0]
    second = most_common_letters[1][0]
    third = most_common_letters[2][0]
    return first, second, third


def calculate_shift(first, second, third, alphabet, common_en_letters):
    # compute probable Caesar shift
    first_shift_value = abs(alphabet[first] - alphabet[common_en_letters[0]])
    second_shift_value = abs(alphabet[second] - alphabet[common_en_letters[1]])
    third_shift_value = abs(alphabet[third] - alphabet[common_en_letters[2]])

    # if 2nd and 3rd shifts match, use it; else use first
    if second_shift_value == third_shift_value:
        return second_shift_value
    return first_shift_value


def output_deciphered_text(final_text):
    # choose to print or save the deciphered text
    print("Choose an option:")
    print("1 - Print the deciphered text")
    print("2 - Create a file named deciphered_text.txt")

    choice = input("Enter 1 or 2: ").strip()
    if choice == "1":
        print("\nDeciphered text:\n")
        print(final_text)
    elif choice == "2":
        with open("deciphered_text.txt", "w", encoding="utf-8") as f:
            f.write(final_text)
        print("File 'deciphered_text.txt' created successfully!")
    else:
        print("Invalid option. Nothing was done.")


def main():
    alphabet = {
        "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9,
        "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17,
        "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25,
        "z": 26,
    }

    common_en_letters = ["e", "t", "o"]

    start_time = time.time()

    with open("text.txt", "r", encoding="utf-8") as f:
        text = f.read()

    temp_text = prepare_text(text)

    first, second, third = get_top_letters(temp_text)
    print(first, second, third)

    shift_value = calculate_shift(first, second, third, alphabet, common_en_letters)

    final_text = decipher_text(text, alphabet, shift_value)

    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.6f} seconds")
    print(f"Most common letter: {first.upper()}")
    print(f"Predicted shift: {shift_value}")

    output_deciphered_text(final_text)


if __name__ == "__main__":
    main()