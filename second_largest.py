#2nd largest
ll=list(map(int,input().split()))
n=len(ll)
max=0
ll.sort()
print(ll[n-2])