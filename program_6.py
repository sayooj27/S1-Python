names=["alice","bobby","arjun","sarah"]
a_count=0
for i in names:
    for j in i:
        if 'a' in j.lower():
            a_count=a_count+1
print("occurrence of 'a':",a_count)