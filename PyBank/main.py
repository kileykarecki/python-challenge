#import modules
import csv
import os

#import statistics module to assist with math
import statistics

#create path
csvpath = os.path.join(r"C:\Users\kiley\OneDrive\Desktop\Module Challenges\Module 3 Challenge\python-challenge\PyBank\Resources\budget_data.csv")

# variables
total_months = 0
total_volume = 0
previous_profit = 0
greatest_increase_profits = 0
best_month = ''
greatest_decrease_profits = 0
worst_month = ''

month_to_month = []

#open the file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #loop for rows
    for row in csvreader:
        total_months += 1
        current_profit = int(row[1])
        total_volume += current_profit

        if previous_profit is not None:
            monthly_change = current_profit - previous_profit
            month_to_month.append(monthly_change)

            if monthly_change > greatest_increase_profits:
                greatest_increase_profits = monthly_change
                best_month = row[0]

            if monthly_change < greatest_decrease_profits:
                greatest_decrease_profits = monthly_change
                worst_month = row[0]

        previous_profit = current_profit

averageChange = statistics.mean(month_to_month) if month_to_month else 0

# Print the analysis to the terminal
print("Financial Analysis")
print("___________________________________")
print("Total Months: " + str(total_months))
print("Average Change: $" + str(round(averageChange, 2)))
print("Total Volume: $" + str(total_volume))
print("Greatest Increase in Profits: " + str(best_month) + " ($" + str(greatest_increase_profits) + ")")
print("Greatest Decrease in Profits: " + str(worst_month) + " ($" + str(greatest_decrease_profits) + ")")

# Export the analysis to a text file
output_path = os.path.join(r"C:\Users\kiley\OneDrive\Desktop\Module Challenges\Module 3 Challenge\python-challenge\PyBank\analysis\analysis.txt")

with open(output_path, 'w') as txtfile:
    txtfile.write(
        "Financial Analysis\n"
        "___________________________________\n"
        "Total Months: " + str(total_months) + "\n"
        "Average Change: $" + str(round(averageChange, 2)) + "\n"
        "Total Volume: $" + str(total_volume) + "\n"
        "Greatest Increase in Profits: " + str(best_month) + " ($" + str(greatest_increase_profits) + ")\n"
        "Greatest Decrease in Profits: " + str(worst_month) + " ($" + str(greatest_decrease_profits) + ")\n"
    )