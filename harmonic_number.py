def harmonic_number(n,a,d):
    '''
    harmonic_number
    :param n:
    :param a:
    :param d:
    :return:
    '''
    for i in range(1, n+1):
        v = a + (i - 1) * d

        if v == 1:
            print("1", end=" ")
        else:
            print(f'1/{v}', end=" ")

if __name__ == '__main__':
    n = int(input("Enter the value of n: "))
    a = int(input("Enter the value of a: "))
    d = int(input("Enter the value of d: "))
    harmonic_number(n, a, d)