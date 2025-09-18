current_year=int(input("enter the current year"))
final_year=int(input("enter the final year"))
for x in range(current_year,final_year+1):
    if(x % 4==0 and x%100!=0)or(x%400==0):
        print(x)