def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    count_left = 0
    count_right = 0

    if parens[0] == '(':
        for par in parens:
            if par == ')':
                count_left += 1
            if par == '(':
                count_right += 1
        if count_left == count_right:
            return True
        else:
            return False
    else:
        return False