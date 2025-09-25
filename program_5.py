text=input("Enter the integers")
x=text.split(",")
x_int=[]
for item in x:
    item=int(item)
    if item>100:
        x_int.append('over')
    else:
        x_int.append(item)
print(x_int)