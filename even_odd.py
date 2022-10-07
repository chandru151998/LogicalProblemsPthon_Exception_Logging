def even_odd(num):
    '''
    even_odd
    :param num:
    :return:
    '''
    if (num % 2) == 0:
       print(f'{num} is Even')
    else:
       print(f'{num} is Odd')

if __name__ == '__main__':
    num = int(input("Enter a number: "))
    even_odd(num)