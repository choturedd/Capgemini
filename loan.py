# bank loan
name='indra'
age=int(input('enter your age:'))
salary=int(input('enter your salary:'))
credit_score=int(input('enter your credit score:'))
if age<21:
    print("you are under aged, we can't provide loan at this time")
elif salary<25000 and credit_score<690:
    print(f'you are not eligible for applying this loan as your age is:{age}, your salary is:{salary}, and your credit score is:{credit_score} are too low') 
else:
    print(f'you are eligible for applying this loan as your age is:{age}, your salary is:{salary}, and your credit score is:{credit_score} are meeting the requirements with our loan constrains, as per CIBIL SCORE CRITERIA') 