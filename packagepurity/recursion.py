def sum_array(array):
    theSum = 0
    for i in array:
        theSum += i
    return theSum


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num


def reverse(word):
    word_string = ''
    start = len(word)
    while start:
        start -= 1
        word_string += word[start]
    return word_string
