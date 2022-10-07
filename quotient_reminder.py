def find(n, m):
    '''
    find
    :param n:
    :param m:
    :return:
    '''
    # for quotient
    q = n // m
    print("Quotient: ", q)

    # for remainder
    r = n % m
    print("Remainder", r)

if __name__ == '__main__':
    n = int(input("Devidend"))
    m = int(input("Divisor"))
    find(n, m)