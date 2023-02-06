def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    new_phrase = phrase.lower().split()
    result = ''
    for word in new_phrase:
        result += ''.join(word.capitalize()) + ' '
    return result.strip()

    # return ' '.join(word.capitalize() for word in phrase.lower().split(' '))

titleize('oNLy cAPITALIZe fIRSt')