#leap year
year=list(map(int,input().split()))
for i in range(len(year)):
    if year[i]%4==0 and year[i]%100!=0:
        print('the inputed year is a leap year')
    else:
        print('the inputed year is not a leap year')