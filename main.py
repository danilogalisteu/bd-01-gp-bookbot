

def get_file_text(path):
    file_contents = ""
    with open(path, 'r') as f:
        file_contents = f.read()
    return file_contents


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_file_text(book_path)
    print(book_text)


main()
