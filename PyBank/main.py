import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
	reader = csv.reader(csvfile, delimiter = ',')
	header = next(reader)

	total_month = 0
	total = 0
	changes = []
	pre = 1
	inc = 0
	dec = 0

	for row in reader:
		total_month +=1
		pro_los = int(row[1])
		total += pro_los
		change = pro_los - pre
		pre = pro_los
		changes.append(change)
		if change > inc:
			inc = change
			inc_d = row[0]
		elif change < dec:
			dec = change
			dec_d = row[0]

	average_change = sum(changes[1:])/(total_month-1)
	print("Financial Analysis\n----------------------------")
	print(f"Total Months: {total_month}")
	print(f"Total: ${total}")
	print(f"Average Change: ${round(average_change,2)}")
	print(f"Greatest Increase in Profits: {inc_d} (${inc})")
	print(f"Greatest Decrease in Profits: {dec_d} (${dec})")

filepath = os.path.join('analysis', 'analysis.txt')
with open(filepath, 'w') as analysis:
    analysis.write("Financial Analysis\n----------------------------\n")
    analysis.write(f"Total Months: {total_month}\n")
    analysis.write(f"Total: ${total}\n")
    analysis.write(f"Average Change: ${round(average_change,2)}\n")
    analysis.write(f"Greatest Increase in Profits: {inc_d} (${inc})\n")
    analysis.write(f"Greatest Decrease in Profits: {dec_d} (${dec})")
