# ATM 
def check_bal():
    return balance
def withdraw_money():
    num=int(input('enter the amount to be withdrawed:'))
    balance=200000
    if num<balance:
        balance-=num
        print(f"sucessfully withdrawed:{num}")
        print(f"current balance:{balance}")
    else:
        print('Insufficent balance,\nexited by wrong entry!')
def deposit_money():
    balance=200000
    num=int(input('enter the amount to be deposited:'))
    balance+=num
    print(f"current balance:{balance}")
    print("successfully deposited money, thank you for visiting!")
def ee():
    exit()
balance=200000
x=1
print('Welcome to the xxx ATM \nPlease insert your card')
pin=input('enter your pin,within three tries:')
if pin=='12345678':
  print("select the following services \n 1.check balance\n 2.Withdraw money \n 3.Deposit money \n 4.exit")
  choose=int(input('choose the any of the above option\n'))
  if choose==1:
    print(f'your current balance is:{check_bal()}')
  elif choose==2:
    withdraw_money()
  elif choose==3:
    deposit_money()
  elif choose==4:
    ee()
else:
    print('entered wrong pin, try again!!')
    pin=int(input('re-enter your pin:'))
    if pin!='12345678':
       while x<2:
          pin=int(input(f're-enter within {x}-try:'))
          x+=1
