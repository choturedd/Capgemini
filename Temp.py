#Temperature conversion

def cel_to_kel(celsius):
    k=celsius+273.15
    return k
def cel_to_fahren(celsius):
    f=(9/5)*celsius+32
    return f
def fahren_to_cel(fahren):
    c=(5/9)*(fahren-32)
    return c
def fahren_to_kel(fahren):
    k=(5/9)*(fahren+459.67)
    return k
def kel_to_fahren(kelvin):
    f=(kelvin-273.15)*(9/5)+32
    return f
def kel_to_cel(kelvin):
    c=kelvin-273.154
user_choice_temp=int(input('enter the respective temperature:'))
choice=int(input('enter the below options:\n1.celsius to kelvin\n2.celsius to fahrenheit\n3.fahrenheit to celsius\n4.fahrenheit to kelvin\n5.kelvin to celsius\n6.kelvin to fahrenheit\n'))
if choice==1:
    print(cel_to_kel(user_choice_temp))
elif choice==2:
    print(cel_to_fahren(user_choice_temp))
elif choice==3:
    print(fahren_to_cel(user_choice_temp))
elif choice==4:
    print(fahren_to_kel(user_choice_temp))
elif choice==5:
    print(kel_to_cel(user_choice_temp))
elif choice==6:
    print(kel_to_fahren(user_choice_temp))
else:
    print("You've choosen wrong option select again!")
    user_choice_temp=int(input())
