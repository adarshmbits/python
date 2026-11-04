startyear=int(input("Enter the start year:"))
print("Enter the Last year")
endyear=int(input("Enter the end year"))
print("list of loop years:")
 #loop through between the start and end year for year in range (start year,end year):
for year in range(startyear,endyear):#check if the yaer is a leap year
      if((year%4==0) and(year%100!=0))or (year % 400==0):
            print(year) 
