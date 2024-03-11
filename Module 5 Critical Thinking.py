# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:20:11 2024

@author: dennis.lindberg
"""
##We'll keep constants at the top
total_rain = 0.0
months_in_year = 12

total_years = int(input("Enter the number of years we want to consider: "))

##Someone might try to slip some nonsensical number into this calculation.
while total_years <=0:
    total_years = int(input("Let's just use whole, positive, non-zero years, shall we? Try again: "))
    

for year in range(0, total_years):
    print(f"\n Year {year+1}: ") 
    
    for month in range(months_in_year):
       monthly_rainfall = float(input(f"Enter the rainfall for month {month +1} (inches): ")) 
       total_rain = monthly_rainfall + total_rain
       
months_required = months_in_year * total_years

if months_required > 0:
    ave_rain = total_rain/months_required
else:
    ave_rain = 0.0
    
print(f"\nWe collected data over a period of {months_required} months.")
print(f"\nWe accumulated {total_rain} inches of rain over those {months_required} months.")
print(f"\nThat means the average rainfall per month is {ave_rain} inches per month.")
       
       
     
     
     
     