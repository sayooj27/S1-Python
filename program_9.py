a=str(input("Enter a string:"))
b=a[0]
c=a[-1]
x=c
for i in a[1:-1]:
    x+=i
x+=b
print(x)