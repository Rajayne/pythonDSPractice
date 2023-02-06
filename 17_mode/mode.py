def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    frequency = {}
    for num in nums:
        frequency.setdefault(num, 0)
        frequency[num] += 1
    most_frequent = max(frequency.values())
    # most_list = []
    for num, freq in frequency.items():
        if freq == most_frequent:
            # most_list.append(num)
            return num
    # return most_list
mode([1, 2, 1])
mode([2, 2, 3, 3, 2])