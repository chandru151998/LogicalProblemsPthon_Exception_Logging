def prime_number(num):
    '''
    prime_number
    :param num:
    :return:
    '''
    flag = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")

if __name__ == '__main__':
    num = int(input("Enter any number: "))
    prime_number(num)