#student grading system
ttl_score=0
student=input('enter your name as per school register:')
print('enter your marks:') 
marks=list(map(int,input().split()))
for i in range(len(marks)):
    ttl_score+=marks[i]
print(f'total score:{ttl_score}')
if ttl_score<90:
    print("you've failed in examination")
elif ttl_score<150:
    print("you've secured C grade, imporve in next semister!")
elif ttl_score<200:
    print("you've secured B grade, you can do better")
else:
    print("you've secured A grade, congratulations!!")