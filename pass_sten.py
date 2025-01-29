#pass Stren Check
spl_char=['!','@','#','$']
password=input('enter your password:')
if len(password)>=8:
  if password.capitalize():
    for i in range(len(password)):
      for j in range(len(spl_char)):
        if password[i]==spl_char[j]:
           print('your password is strong!')
           break
else:
  print("you've choosen very weak password try again!!")
  password=input('re-enter a strong password greater than 8 characters:')