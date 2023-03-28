# import library
import os
import csv

# Reference variables
total_months = 0
total_profit = 0
month_change = 0
previous_month = 0
total_month_change = 0
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""
average_month_change = 0

# join path for the CSV file
budget_data = os.path.join('Resources', 'budget_data.csv')
print(os.path.abspath(budget_data))

C:\Users\rjean\Downloads\Resources\budget_data.csv

with open(budget_data,newline="", encoding="utf") as budget_data:
    csvreader = csv.reader(budget_data,delimiter=",")
    csv_header = next(csvreader)
    
    total_profit = []
    total_months = []
    
    for rows in csvreader:
        P.append(int(rows[1]))
        months.append(rows[0])
        
# find revenue change, iterate through the profits
    revenue_change =[]
    for x in range(1, len(P)):
        revenue_change.append((int(P[x]) - int(P[x-1])))

# Calculate average revenue change
revenue_average_change = sum(revenue_change) / len(revenue_change)
revenue_average = round(revenue_average_change, 2)

# Calculate total length of months
total_months = len(months)

# greatest increase in revenue
greatest_increase = max(revenue_change)

# greatest decrease in revenue
greatest_decrease = min(revenue_change)

# Print statements
print ("Financial Analysis")

print(".........................................")

print ("Total Months:" + str(total_months))

print("Total:" + "$" + str(sum(P)))

print ("Average Change:" + "$" + str(revenue_average))

print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "($" + str(greatest_increase) + ")")

print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "($" + str(greatest_decrease) + ")")

Financial Analysis
.........................................
Total Months:432
Total:$114998956
Average Change:$-1639.08
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)

#// Write a text file with analysis
budget_data = os.path.join("Resources", "Financial_Analysis.txt")
with open(budget_data, "w") as file:
    file.write("Financial Analysis" + "\n")

    file.write("......................................." + "\n")

    file.write("total months: " + str(total_months) + "\n")

    file.write("Total: " + "$" + str(sum(P)) + "\n")

    file.write("Average change: " + "$" + str(revenue_average) + "\n")

    file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "($" + str(greatest_increase) + ")\n")

    file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "($" + str(greatest_decrease) + ")\n")

    file.close()
