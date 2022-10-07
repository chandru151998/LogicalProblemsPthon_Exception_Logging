def character(ch):
    '''
    character
    :param ch:
    :return:
    '''
    if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I' or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
        print(ch, "is a Vowel")
    else:
        print(ch, "is a Consonant")

if __name__ == '__main__':
    ch = input("Enter a character: ")
    character(ch)