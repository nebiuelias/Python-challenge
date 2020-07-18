# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import string
import csv
import array as my_array

file_to_load = "c:/Users/elija/Desktop/Class_Room/Python-challenge/Python-challenge/PyBank/Resources/budget_data.csv"
#file_to_output = os.path.join("analysis", "employee_data_reformatted.csv")
number_of_month=0
Total_profit_loss=0
greatest_increase=0
greatest_decrease=0
profit_by_month=[]
profit_by_month2=[]
profit=0
change_in_profit=[]
change=0
counter_i=0
counter_j=0
with open (file_to_load) as budget_data:
    reader=csv.reader(budget_data)
    next(reader) #code to skip the header
    
    for row in reader:
        #counting the number of months
        number_of_month=number_of_month + 1 
        #Summing up Total Profit
        Total_profit_loss= Total_profit_loss + (int(row[1]))
        #section to populate array with the monthly profit_change
        profit=int(row[1])
        
        profit_by_month.append([profit])
        profit_by_month2.append([profit])
        change=((profit_by_month[counter_i]) - (profit_by_month2[counter_j]))
        change_in_profit.append(change)
        counter_i=counter_i + 1
        counter_j=counter_i - 1
print(change_in_profit)
print(number_of_month)
print(Total_profit_loss)
