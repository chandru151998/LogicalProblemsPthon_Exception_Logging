def fibonacci_sequence(nterms):
    '''
    fibonacci_sequence
    :param nterms:
    :return:
    '''
    n1 = 0
    n2 = 1
    count = 0
    nth = n1 + n2
    if nterms <= 0:
       print("Please enter a positive integer")
    elif nterms == 1:
       print("Fibonacci sequence upto ",nterms,":")
       print(n1)
    else:
       print("Fibonacci sequence : ")
       while count < nterms:
           print(n1)
           nth = n1 + n2
           n1 = n2
           n2 = nth
           count += 1

if __name__ == '__main__':
    nterms = int(input("How many terms : "))
    fibonacci_sequence(nterms)