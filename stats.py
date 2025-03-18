def get_num_words(text):
    return len(text.split())


def get_letter_dict(text):
    letter_dict = {}
    for letter in text.lower():
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict


def sort_letter_dict(letter_dict):
    letter_list = [{'name':k, 'num':letter_dict[k]} for k in letter_dict]
    sort_on = lambda d: d['num']
    letter_list.sort(key=sort_on, reverse=True)
    return letter_list
