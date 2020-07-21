# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import string
import csv
import array as my_array

#definig the input and output file paths. 
#due to runtime error, I had to use absoulte addressing than the prefferred relative one
file_to_load = "c:/Users/elija/Desktop/Class_Room/Python-challenge/Python-challenge/PyBank/Resources/budget_data.csv"
file_to_output = os.path.join("c:/Users/elija/Desktop/Class_Room/Python-challenge/Python-challenge/PyBank/Analysis", "Analysis_result.txt")

number_of_month=0
Total_profit_loss=0
greatest_increase=0
greatest_decrease=0
greatest_increase_month=0
greatest_decrease_month=0
Total_change_profit=0
average_change_profit=0
profit_by_month=[]
profit_date=[]
profit=0
dates_profit=0
profit1=0
change_in_profit=[]
change=0
counter_i=0
counter_j=0
ary_len=0

#section to load and read the input data from the CSV file
with open (file_to_load) as budget_data:
    reader=csv.reader(budget_data)
    next(reader) #code to skip the header
    
    for row in reader:
        #counting the number of months
        number_of_month=number_of_month + 1 
        #Summing up Total Profit
        Total_profit_loss= Total_profit_loss + (int(row[1]))
        #section to populate a list with the monthly profit and a second list to hold the corresponding month
        profit=int(row[1])
        dates_profit=(row[0])
        
        profit_by_month.append(profit)
        profit_date.append(dates_profit)

ary_len=len(profit_by_month)
j=1
#populating a list with the profit change from month to month
for i in range(0,ary_len-1): 
    change=(profit_by_month[j] - profit_by_month[i])
    change_in_profit.append(change)
    if j<ary_len:
       j= j+1

#section to analyse the numbers

array_len2=len(change_in_profit)
greatest_increase=change_in_profit[0]
greatest_decrease=change_in_profit[0]
index_increase=0
index_decrease=0

#loop to find the greatest increase, greatest decrease and to calculate profit
for i in range(0,array_len2):
    if change_in_profit[i]>greatest_increase:
        greatest_increase=change_in_profit[i]
        index_increase=i
    if change_in_profit[i]<greatest_decrease:
        greatest_decrease=change_in_profit[i]  
        index_decrease=i

    Total_change_profit=Total_change_profit+change_in_profit[i]  

average_change_profit= round(Total_change_profit/array_len2,2)
greatest_increase_month=profit_date[index_increase+1]
greatest_decrease_month=profit_date[index_decrease+1]

print("Financial Analysis")
print("............................................")
print(f"Total Months: {str(number_of_month)}")
print(f"Total: {str(Total_profit_loss)}")
print(f"Average Change: {str(average_change_profit)}")
print (f"Greatest Increase in Profits:{greatest_increase_month} (${str(greatest_increase)})")
print (f"Greatest decrease in Profits:{greatest_decrease_month} (${str(greatest_decrease)})")

#section to write the result analysis to a text file
with open(file_to_output, "w") as pyfile:
    pyfile.write("Financial Analysis\n")
    pyfile.write("....................................\n")
    pyfile.write(f"Total Months: {str(number_of_month)}\n")
    pyfile.write(f"Total: {str(Total_profit_loss)}\n")
    pyfile.write(f"Average Change: {str(average_change_profit)}\n")
    pyfile.write (f"Greatest Increase in Profits:{greatest_increase_month} (${str(greatest_increase)})\n")
    pyfile.write (f"Greatest decrease in Profits:{greatest_decrease_month} (${str(greatest_decrease)})\n")