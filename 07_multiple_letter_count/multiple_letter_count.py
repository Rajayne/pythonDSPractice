def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    dic = {}
    for char in phrase:
        if char in dic:
            c = int(dic[char])
            c += 1
            dic.update({char:c})
        else:
            dic.update({char: 1})
    return dic