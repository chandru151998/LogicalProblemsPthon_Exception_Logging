import random

def flip_coin_percentage(flip_coin):
    '''
    flip_coin_percentage
    :param flip_coin:
    :return:
    '''
    heads = 0
    tails = 0
    headspercent = 0
    tailspercent = 0
    if(flip_coin > 0):
        for i in range (0, flip_coin):
            coin = random.randint(1, 2)
            if coin == 1:
                heads += 1
            else:
                tails += 1
        headspercent = heads * 100 // flip_coin
        tailspercent = tails * 100 // flip_coin
        print("Heads percent: " + str(headspercent))
        print("Tails percent: " + str(tailspercent))
    else:
        print("Enter positive number")

if __name__ == '__main__':
    flip_coin = int(input("Enter any number: "))
    flip_coin_percentage(flip_coin)