def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    new_string = ''
    for letter in phrase[::-1]:
        new_string += letter
    return new_string