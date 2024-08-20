#import modules
import csv
import statistics
import os

csvpath = os.path.join(r"C:\Users\kiley\OneDrive\Desktop\Module Challenges\Module 3 Challenge\python-challenge\PyBank\Resources\budget_data.csv")

# variables
total_months = 0
total_volume = 0
previous_profit = None
greatest_increase_profits = 0
best_month = ''
greatest_decrease_profits = 0
worst_month = ''
monthToMonthChange = []

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
            monthlyChange = current_profit - previous_profit
            monthToMonthChange.append(monthlyChange)

            if monthlyChange > greatest_increase_profits:
                greatest_increase_profits = monthlyChange
                best_month = row[0]

            if monthlyChange < greatest_decrease_profits:
                greatest_decrease_profits = monthlyChange
                worst_month = row[0]

        previous_profit = current_profit

averageChange = statistics.mean(monthToMonthChange) if monthToMonthChange else 0

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