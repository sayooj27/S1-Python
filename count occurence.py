text=input("Enter a word:")
word=text.split()
word_count={}
for i in word:
    if i in word_count:
        word_count[i]+=1
    else:
        word_count[i]=1
print(word_count)





