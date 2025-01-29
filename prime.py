# prime
def isprime(a):
    if a<=1:
       return False
    for i in range(2,a):
        if a%i==0:
           return False
    print(a)
i=0
num1=int(input('enter starting base:'))
num2=int(input('enter ending base:'))
for i in range(num1,num2):
   isprime(i)