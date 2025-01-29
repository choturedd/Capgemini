#word counter
sentence=input('enter a sentence:')
sentence=sentence.lower()
words=sentence.split()
count={}
for i in words:
    if i in count:
        count[i]+=1

    else:
        count[i]=1
for i in range(len(sentence)):
    print(f"'{words}':{count}")
    break