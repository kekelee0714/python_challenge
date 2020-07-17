<<<<<<< HEAD
#load csv
import os
import csv

#Path to collect data 
budget_data_csv ="C:/Users/Keke/git/python_challenge/PyBank/Resources/budget_data.csv"

#define variables
totalmonths=0
#set total as integer
nettotalamount=0

#calculate changes of each date
netmonthlychange=[]

#set first value as 0 from previous row
original = 0

averagechange=0
a=0
#set variables as list with "" reps date and numbers as the only value in the list
Gincrease= ["", 0]
Gdecrease= ["", 999999999999]

#read csv file
with open(budget_data_csv) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")

    #skip header line to start from row 2
    csv_header=next(csvfile)

    #title of hw
    print(f"Financial Analysis")

    #print a new line \n
    print("\n-------------------------------------")


    #loop the numbers
    for row in csv.reader(csvfile):

        #date=row[0]
        #profitloss=row[1]
        #next row value is value in previous row add next row value
        totalmonths = totalmonths+1
     
        #sum incremental values 
        nettotalamount = nettotalamount + int(row[1])
        #nettotalamount+= int(totalmonths

        #calculate average change, if there is no value before first row or value is 0
        if original == 0:
            #no original value exists
            #netmonthlychange.append(0) starts from 0 is added to the column in the file
            #original which is 0 equals to the new row value
            original = int(row[1])
        else:
            #original value exists, the new row value subtract previous row value is the difference
            a = int(row[1]) - original
            
            #append the net monthly change as a column
            netmonthlychange.append(a)
            original =  int(row[1])
            
        #if the value in net monthly change is greater the the only value, then column [0] is date column, column 2 [1] with greatest increase is value a from net monthly change
        if a > Gincrease[1]:        
            Gincrease[0] = row[0]
            Gincrease[1] = a
       
        if a < Gdecrease[1]:
            Gdecrease[0] = row[0]
            Gdecrease[1] = a
 


    #calculate the average of changes in total row   
    averagechange = sum(netmonthlychange)/len(netmonthlychange)

    
    

    print(f"Total Months:{totalmonths}")
    print(f"Total:${nettotalamount}")

    #print(netmonthlychange)
    #format average change to 2 decimal
    print(f"Average Change:${averagechange:,.2f}".format(averagechange))

    # [0] is date value, [1] is max or min value in the list
    print(f"Greatest Increase in Profits:{Gincrease[0]}:(${Gincrease[1]})")
    print(f"Greatest Decrease in Profits:{Gdecrease[0]}:(${Gdecrease[1]})")

   # Generate Output Summary
text =(
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {totalmonths}\n"
    f"Total: ${nettotalamount}\n"
    f"Average  Change: ${averagechange:.2f}\n"
    f"Greatest Increase in Profits: {Gincrease[0]} (${Gincrease[1]})\n"
    f"Greatest Decrease in Profits: {Gdecrease[0]} (${Gdecrease[1]})\n")

# Export the results to text file
saveFile= open('C:/Users/Keke/git/python_challenge/PyBank/analysis/saveFile.txt', 'w')
saveFile.write(text)
=======
#load csv
import os
import csv

#Path to collect data 
budget_data_csv ="C:/Users/Keke/git/python_challenge/PyBank/Resources/budget_data.csv"

#define variables
totalmonths=0
#set total as integer
nettotalamount=0

#calculate changes of each date
netmonthlychange=[]

#set first value as 0 from previous row
original = 0

averagechange=0
a=0
#set variables as list with "" reps date and numbers as the only value in the list
Gincrease= ["", 0]
Gdecrease= ["", 999999999999]

#read csv file
with open(budget_data_csv) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")

    #skip header line to start from row 2
    csv_header=next(csvfile)

    #title of hw
    print(f"Financial Analysis")

    #print a new line \n
    print("\n-------------------------------------")


    #loop the numbers
    for row in csv.reader(csvfile):

        #date=row[0]
        #profitloss=row[1]
        #next row value is value in previous row add next row value
        totalmonths = totalmonths+1
     
        #sum incremental values 
        nettotalamount = nettotalamount + int(row[1])
        #nettotalamount+= int(totalmonths

        #calculate average change, if there is no value before first row or value is 0
        if original == 0:
            #no original value exists
            #netmonthlychange.append(0) starts from 0 is added to the column in the file
            #original which is 0 equals to the new row value
            original = int(row[1])
        else:
            #original value exists, the new row value subtract previous row value is the difference
            a = int(row[1]) - original
            
            #append the net monthly change as a column
            netmonthlychange.append(a)
            original =  int(row[1])
            
        #if the value in net monthly change is greater the the only value, then column [0] is date column, column 2 [1] with greatest increase is value a from net monthly change
        if a > Gincrease[1]:        
            Gincrease[0] = row[0]
            Gincrease[1] = a
       
        if a < Gdecrease[1]:
            Gdecrease[0] = row[0]
            Gdecrease[1] = a
 


    #calculate the average of changes in total row   
    averagechange = sum(netmonthlychange)/len(netmonthlychange)

    
    

    print(f"Total Months:{totalmonths}")
    print(f"Total:${nettotalamount}")

    #print(netmonthlychange)
    #format average change to 2 decimal
    print(f"Average Change:${averagechange:,.2f}".format(averagechange))

    # [0] is date value, [1] is max or min value in the list
    print(f"Greatest Increase in Profits:{Gincrease[0]}:(${Gincrease[1]})")
    print(f"Greatest Decrease in Profits:{Gdecrease[0]}:(${Gdecrease[1]})")

   # Generate Output Summary
text =(
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {totalmonths}\n"
    f"Total: ${nettotalamount}\n"
    f"Average  Change: ${averagechange:.2f}\n"
    f"Greatest Increase in Profits: {Gincrease[0]} (${Gincrease[1]})\n"
    f"Greatest Decrease in Profits: {Gdecrease[0]} (${Gdecrease[1]})\n")

# Export the results to text file
saveFile= open('C:/Users/Keke/git/python_challenge/PyBank/analysis/saveFile.txt', 'w')
saveFile.write(text)
>>>>>>> 97012a5334b31988da5776f6a60bc53f1646e686
saveFile.close()