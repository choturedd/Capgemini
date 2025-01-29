#string analysis tool
i=0
j=0
k=0
sent=input('enter a string:')
n=len(sent)
vowels=['a','e','i','o','u']
spl_char=['!','@','#','$']
conso=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','u','v','w','x','y','z']
for ii in range(len(sent)):
    for jj in range(len(vowels)):
      if sent[ii]==vowels[jj]:
        i+=1
for ii in range(len(sent)):
    for kk in range(len(spl_char)):
      if sent[ii]==spl_char[kk]:
        j+=1
for ii in range(len(sent)):
    for ll in range(len(conso)):
      if sent[ii]==conso[ll]:
        k+=1
print('vowels:',i,'special characters:',j,'consonants:',k)
ans=str()
iii=0
print(sent[::-1])