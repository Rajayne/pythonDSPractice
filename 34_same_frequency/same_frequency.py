def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1 = str(num1)
    count = dict.fromkeys(num1, 0)

    num2 = str(num2)
    count2 = dict.fromkeys(num2, 0)

    for num in num1:
        if num in count:
            c = count[num]
            c += 1
            count.update({num: c})
    for num in num2:
        if num in count2:
            c = count2[num]
            c += 1
            count2.update({num: c})
    if count == count2:
        print(True)
    else:
        print(False)

same_frequency(551122, 221515)

