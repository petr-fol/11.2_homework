def str_upper_word(word):
    """
    :param word:
    :return строка в верхнем регистре:
    """
    return word.upper()


def is_letter(symbol):
    if symbol not in "'\"!@#$%^&*()_+=-.,;:?/0123456789":
        return True
    else:
        return False


def str_upper_letter(str_):
    """
    :param str_:
    :return: строку, в которой у каждого слова первая буква заглавная
    """
    word_list = str_.split(' ')
    new_list_words = []

    for word in word_list:
        new_word = ''
        for i, char in enumerate(word):
            if i == 0 and is_letter(char):
                new_word += char.upper()
            else:
                new_word += char
        new_list_words.append(new_word)

    new_str_words = ' '.join(new_list_words)
    return new_str_words
