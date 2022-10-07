def reverse_number(num):
    '''
    reverse_number
    :param num:
    :return:
    '''
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    print("Reversed Number: " + str(reversed_num))

if __name__ == '__main__':
    num = int(input("Enter any number: "))
    reverse_number(num)