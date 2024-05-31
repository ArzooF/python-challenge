import csv 
import os

inputFile = ("./Resources/budget_data.csv")
outputFile = ("analysis.txt")

total_months = 0
month_of_change = []
net_change_list = []
greatest_inc = ["",0]
greatest_dec = ["", 9999999999]
total_net = 0


with open(inputFile, "r") as file:
    reader = csv.reader(file)
    header = next(reader)

    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:
        total_months+=1
        total_net += int(row[1])

        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]

        if net_change > greatest_inc[1]:
            greatest_inc[1] = net_change
            greatest_inc[0] = row[0]
        if net_change < greatest_dec[1]:
            greatest_dec[1] = net_change
            greatest_dec[0] = row[0]

net_monthly_avg = round(sum(net_change_list) / len(net_change_list),2)

output = (
    f"Financial Analysis\n"
    f"---------------------\n"
    f"Total Month: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: {net_monthly_avg}\n"
    f"Greatest Inc: {greatest_inc[0]}  (${greatest_inc[1]})\n"
    f"Greatest dec: {greatest_dec[0]} (${greatest_dec[1]})"


)

print(output)

with open(outputFile,"w") as analysis:
    analysis.write(output)