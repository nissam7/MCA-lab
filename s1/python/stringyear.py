print("print a leap year between two given years")
print("enter the start year")
startyear=int(input())
print("enter the last year")
endyear=int(input())
print("list of leap year")
for year in range(startyear,endyear):
	if(0==year%4) and (0!=year%100) or (0==year % 400):
	 print(year)
