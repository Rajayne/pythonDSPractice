def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    sum = 0
    start = 0
    end = 3
    for i in range(0, len(nums)-2):
        for num in nums[i:end]:
            sum += num
        if sum % 2 == 0:
            sum = 0
            start += 1
            end += 1
        else:
            sum = 0
            start += 1
            end += 1
            return True
    return False
        
three_odd_numbers([1, 2, 3, 3, 2])
