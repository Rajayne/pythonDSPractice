def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """
    # Hint: you may find the ord() function useful here
    # Created dictionary of alphabet values to reference
    dic = dict.fromkeys('abcdefghijklmnopqrstuvwxyz')
    value = 1
    for letter in dic:
        dic[letter] = value
        value += 1

    sum = 0
    for char in word:
        sum += dic[char.lower()]

    if sum % 2 == 0:
        return False
    return True

is_odd_string('amazing')