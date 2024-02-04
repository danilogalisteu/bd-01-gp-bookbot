

def get_file_text(path):
    file_contents = ""
    with open(path, 'r') as f:
        file_contents = f.read()
    return file_contents


def get_word_count(text):
    return len(text.split())


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_file_text(book_path)
    print(f"{get_word_count(book_text)} words")


main()
