def main():
    plist = []
    begin = int(input('Enter first number: '))
    end = int(input('Enter second number: '))
    for num in range(begin, end +1 , 1):
         if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                plist.append(num)
    print('Output:  ')
    print(plist)
    ##################################################
    # Comlete your code here
    ##################################################

    return plist


if __name__ == '__main__':
    main()
