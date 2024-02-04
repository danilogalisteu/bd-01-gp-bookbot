

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
    print(f"--- Begin report of {book_path} ---")

    book_text = get_file_text(book_path)
    print(f"{get_word_count(book_text)} words found in the document\n")

    letter_dict = get_letter_dict(book_text)

    letter_list = [{'name':k, 'num':letter_dict[k]} for k in letter_dict]

    sort_on = lambda d: d['num']
    letter_list.sort(key=sort_on, reverse=True)

    for letter in letter_list:
        if letter['name'].isalpha():
            print(f"The '{letter['name']}' character was found {letter['num']} times")


main()
