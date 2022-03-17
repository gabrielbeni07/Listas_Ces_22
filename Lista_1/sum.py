def sum_to(n):
    """Function that returns the sum of all integer numbers up to and including n."""

    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

