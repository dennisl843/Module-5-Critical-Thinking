# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:20:11 2024

@author: dennis.lindberg
"""
##This portion of the program deals with Part 1 of Module 5
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
print(f"\nThat means the average rainfall per month is {ave_rain:.2f} inches per month.")
       
#%%

#This program deals with Part 2 of Module 5 
#The idea for this portion is to create a dictionary using "books_purchased" as a key value.
#I have modified the program to make it more fair.  For example, if we didn't have any way of 
#dealing with the values not originally defined in the dictionary, the purchaser would get nothing.
#I am making the assumption that this is a one-time evaluation of the number of books purchased, in
#other words, the points are awarded based on a single evaluation of the number of purchases.  It 
#seems unfair to evaluate the number of books a single time, and if the purchaser had, say, 5 books,
#they would still get the number of points defined for the next lowest entry in the dictionary rather than
#returning 0, as 5 was not previously defined.  So that's why you see the dictionary different than what
#was originally provided in the problem statement.

points_per_book = {0:0, 1:0, 2:5, 3:5, 4:15, 5:15, 6:30, 7:30} 
books_purchased = int(input('Enter the number of purchased books: '))

if books_purchased >= 8:
    points = 60
else: points = points_per_book.get(books_purchased, 0)


print(f"Books purchased: {books_purchased}")
print(f"Points awarded: {points}")

     
     
     
     