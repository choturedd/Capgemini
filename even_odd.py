#odd even sepertor
i=0
even=[]
odd=[]
num=list(map(int,input().split()))
for i in range(len(num)):
    if num[i]%2==0:
        even+=[num[i]]
    else:
        odd+=[num[i]]
print(even)
print(odd)