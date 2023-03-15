# import library
import os
import csv

# join path
budget_data = os.path.join("Resources", "budget_data.csv")

# open and read csv
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csv.reader(csvfile, delimter=',')
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")
                           
    " find net amount of profit and loss
    P = []
    months = []
                           
    # read each row of data after header
