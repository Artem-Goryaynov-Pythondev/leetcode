def reverseNumber(number):
    a = str(number)[::-1]
    a = int(a)
    return a


def addTwoNumbers(l1, l2):
    int1 = int(''.join(map(str, l1)))
    int2 = int(''.join(map(str, l2)))
    reversed1 = reverseNumber(int1)
    reversed2 = reverseNumber(int2)

    exitInt = reversed1 + reversed2

    exitIntReversed = reverseNumber(exitInt)

    lst = [int(i) for i in str(exitIntReversed)]
    return lst


assert addTwoNumbers([2,4,3], [5,6,4]) == [7,0,8]
assert addTwoNumbers([0], [0]) == [0]
assert addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9]) == [8,9,9,9,0,0,0,1]
