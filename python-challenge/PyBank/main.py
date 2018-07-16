# dependencies
import os
import csv

#files
budget_data_load = os.path.join("..", "PyBank","budget_data.csv")
budget_data_save = os.path.join("..", "PyBank", "budget_data.txt")


prevRevenue = 0
totalNumMonths = 0
totalRevenue = 0
MonthofGreatestIncrease = ""
greatestIncrease = 0
MonthofGreatestDecrease = ""
greatestDecrease = 0

with open(budget_data_load) as budget_data:
    budget_data_read = csv.reader(budget_data)
    next(budget_data_read)

    for row in budget_data_read:
        totalNumMonths+=1

        thisMonth = row[0]
        thisRevenue = int(row[1])

        RevenueChange= thisRevenue - prevRevenue

        if RevenueChange > greatestIncrease:
            MonthofGreatestIncrease = thisMonth
            GreatestIncrease = RevenueChange

        if RevenueChange < greatestDecrease:
            MontofGreatestDecrease = thisMonth
            GreatestDecrease = RevenueChange

        prevRevenue = thisRevenue

        totalRevenue += thisRevenue

    AverageRevenue = totalRevenue/totalNumMonths
    AvgRev2= round(AverageRevenue,2)
    #print(AvgRev2)
print("Financial Analysis")
print("-----------------------------------------------")
print(f"Total Number of Months: {totalNumMonths} months")
print(f"Total Revenue: ${totalRevenue}")
print(f"Average Change: ${AvgRev2}")
print(f"Greatest Increase in Revenue: {MonthofGreatestIncrease} ${GreatestIncrease}")
print(f"Greatest Decrease in Revenue: {MontofGreatestDecrease} ${GreatestDecrease}")
print("------------------------------------------------")

output = (
 
    f"\nFinancial Analysis\n"
    f"\n-----------------------------------------------\n"
    f"\nTotal Number of Months: {totalNumMonths} months\n"
    f"\nTotal Revenue: ${totalRevenue}\n"
    f"\nAverage Change: ${AvgRev2}\n"
    f"\nGreatest Increase in Revenue: {MonthofGreatestIncrease} ${GreatestIncrease}\n"
    f"\nGreatest Decrease in Revenue: {MontofGreatestDecrease} ${GreatestDecrease}\n"
    f"\n------------------------------------------------\n")
#print(output)
with open(budget_data_save, "w") as txt_file:
    txt_file.write(output)

