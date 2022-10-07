def swap_numbers(x,y):
    '''
    swap_numbers
    :param x:
    :param y:
    :return:
    '''
    temp = x
    x = y
    y = temp

    print(f'The value of x after swapping: {x}')
    print(f'The value of y after swapping: {y}')

if __name__ == '__main__':
    x = input('Enter value of x: ')
    y = input('Enter value of y: ')
    swap_numbers(x, y)