

def get_file_text(path):
    file_contents = ""
    with open(path, 'r') as f:
        file_contents = f.read()
    return file_contents


def get_word_count(text):
    return len(text.split())


def get_letter_dict(text):
    letter_dict = {}
    for letter in text.lower():
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict


def main():
    book_path = "books/frankenstein.txt"

    book_text = get_file_text(book_path)
    print(f"{get_word_count(book_text)} words")

    letter_dict = get_letter_dict(book_text)
    print(letter_dict)


main()
