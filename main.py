import sys

from stats import get_num_words, get_letter_dict, sort_letter_dict


def get_book_text(path):
    file_contents = ""
    with open(path, 'r') as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    book_text = get_book_text(book_path)
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")

    print("--------- Character Count -------")
    letter_dict = get_letter_dict(book_text)
    letter_list = sort_letter_dict(letter_dict)
    for letter in letter_list:
        if letter['name'].isalpha():
            print(f"{letter['name']}: {letter['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
