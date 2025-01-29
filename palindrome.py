#palindrome Checker
rev=0
i=0
while True:
    print('choose to enter a string or int to check whether it is palindrome or not:\n1.string \n2.number')
    choose=int(input())
    if choose==1:
        print("you've choosen string!")
        string=input('enter a string:').split()
        n=string[::-1]
        if string==n:
           print('is palidrome')
        else:
           print('is not palindrome')
    elif choose==2:
        print("You've choosen number!")
        number=int(input('enter a number:').split())
        while number>0:
          n=number%10
          number/=number
          rev=rev*10+n
          number//=number
          if number==rev:
                  print('is palindrome')
    else:
        print("you've choosen wrong option!!!")
        choose=int(input("choose again from options 1 & 2 only!!"))