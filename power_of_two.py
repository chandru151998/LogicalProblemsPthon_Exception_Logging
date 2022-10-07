import math

def power_of_two(num):
    '''
    power_of_two
    :param num:
    :return:
    '''
    print("2 to the power of ",num," is ",math.pow(2,num))
    print("printing all til the power value ",num)
    if(num > 0 and num <= 31):
        for i in range(1, num):
            print("2 to the power of ",i," is : ",math.pow(2, i))

if __name__ == '__main__':
    num = int(input("Enter a number: "))
    power_of_two(num)