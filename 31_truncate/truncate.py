def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """
    new_phrase = ''
    if n >= 3 and n <= len(phrase):
        new_phrase = phrase[0:n-3]
        return new_phrase + "..."
    elif n > len(phrase):
        return phrase
    else:
        return "Truncation must be at least 3 characters."
    # new_phrase = ''
    # if n >= 3 and n < len(phrase):
    #     for letter in range(0, len(phrase)-(n+2), 1):
    #         new_phrase += phrase[letter]
    #         print(new_phrase + "...")
    # else:
    #     return "Truncation must be at least 3 characters."
    # return new_phrase + "..."
        
truncate("Hello World", 6)
truncate("Woah", 4)