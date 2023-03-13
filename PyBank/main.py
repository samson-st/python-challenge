# Create a Python script that analyzes the records to calculatethe following:
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes and average in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

#import modules
import os
import csv

#input file for data analysis
budget_data = os.path.join("Resources/", "budget_data.csv")
#output file
text_path = os.path.join("analysis", "results.txt")


# declare variables

months = []
profit_change_list = []

month_total = 0
net_profit_loss = 0
change_profit_loss = 0
avg_change_profit_loss = 0
prev_profit = 0
current_profit = 0

#open csv
with open(budget_data, newline="") as csvfile:

   csv_reader = csv.reader(csvfile, delimiter=",")

   csv_header = next(csvfile)
   
   #read through rows
   for row in csv_reader:

      #monthly count 
      month_total +=1

      #net profit/losses
      current_profit = int(row[1])
      net_profit_loss += current_profit

      if (month_total == 1):
         prev_profit = current_profit
         continue

      else:

         #find change in profits
         change_profit_loss = current_profit - prev_profit
         
         months.append(row[0])

         profit_change_list.append(change_profit_loss)

         prev_profit = current_profit

   #calculate changes in profits/losses (sum and average)
   sum_profit_loss = sum(profit_change_list)
   avg_change_profit_loss = round(sum_profit_loss/(month_total - 1), 2)

   #find highest and lowest values
   greatest_increase = max(profit_change_list)
   greatest_decrease = min(profit_change_list)

   #create indexes
   highest_month_change = profit_change_list.index(greatest_increase)
   lowest_month_change = profit_change_list.index(greatest_decrease)

   #find best and worst month
   best_month = months[highest_month_change]
   worst_month = months[lowest_month_change]



#export to terminal
print(f"CSV Path: {budget_data}")
print(f"Analysis Path; {text_path}")
print(f" ")
print(f"Financial Analysis")
print(f"--------------------------------")
print(f"Total Months: {month_total}")
print(f"Net Profit/Loss: ${net_profit_loss}")
print(f"Average Profit/Loss: ${avg_change_profit_loss}")
print(f"Greatest Increase Profit/Loss: {best_month} (${greatest_increase})")
print(f"Greatest Decrease Profit/Loss: {worst_month} (${greatest_decrease})")

#export to text file
with open(text_path, "w", newline="") as csvfile:
   
   text_output = csv.writer(csvfile, delimiter=" ", quotechar=" ", quoting=csv.QUOTE_MINIMAL)
   #https://docs.python.org/3/library/csv.html

   print (text_output)
   text_output.writerow(['Financial Analysis'])
   text_output.writerow(['---------------------------------'])
   text_output.writerow(['Total Months:', month_total])
   text_output.writerow([f'Net Profit/Loss: ${net_profit_loss}'])
   text_output.writerow([f'Average Profit/Loss: ${avg_change_profit_loss}'])
   text_output.writerow([f'Greatest Increase Profit/Loss: {best_month} ({greatest_increase})'])
   text_output.writerow([f'Greatest Decrease Profit/Loss: {worst_month} ({greatest_decrease})'])




             