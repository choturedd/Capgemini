#BMI
wt=int(input('enter your weight:'))
ht=float(input('enter your height:'))
BMI=wt/(ht*ht)
print(BMI)
if BMI<18.5:
    print('underweight')
elif BMI>18.5 and BMI<24.5:
    print('normal or healthy')
elif BMI>25 and BMI<29.9:
    print('overweight')
else:
    print('obese')