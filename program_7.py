list1=[23,45,34,26]
list2=[11,12,13,14]
print("Elements in list one is:",list1)
print("Elements in list two:",list2)
if len(list1)==len(list2):
    print("Lists have same length")
else:
    print("Lists have different length")
s1=0
s2=0
for i in range(len(list1)):
    s1=s1+list1[i]
    print("The sum of list1 is:",s1)
for i in range(len(list2)):
        s2=s2+list2[i]
        print("The sum of list2 is:",s2)
if s1==s2:
            print("The sum of lists are same")
else:
        print("he sum of lists are diffrent")
        print("The common element in list is:")
for i in list1:
    for j in list2:
        if i==j:
            print(i)