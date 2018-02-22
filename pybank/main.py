#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 16:07:22 2018

@author: sivenpatel
"""

import csv
import os

csvFile = ["budget_data_2.csv"]

for file in csvFile:
    csvPath = os.path.join("raw_data",file)
    previousChange = [1]
    date = []
    revenue = []

    with open (csvPath, newline="") as cfile:
        csv_reader = csv.reader(cfile, delimiter=',')
        next (csv_reader)
    
        for row in csv_reader:
            date.append(row[0])
            #print(date)
            revenue.append(int(row[1]))
            #print(revenue)
    
    
        for i in range(1,len(revenue)):
            previousChange.append(revenue[i]-revenue[i-1])
            #print (previousChange)
            avgRevChange = round(sum(previousChange)/len(previousChange))
            #print (avgRevChange)
            maxRevChange = max(previousChange)
            #print (maxRevChange)
            minRevChange = min(previousChange)
            #print (minRevChange)
            
            maxRevChangeDate = str(date[previousChange.index(maxRevChange)])
    
            
            minRevChangeDate = str(date[previousChange.index(minRevChange)])


    with open ("Results.txt", "w") as output:
        print()
        print()
        print("The results are for " + str(csvFile[0]))
        print()
        print("Financial Analysis")
        print("-------------------")
        print("Total Months: ", len(date))
        print("Total Revenue: $",sum(revenue))
        print("Average Revenue Change: $",avgRevChange)
        print("Greatest Increase in Revenue: "+ 
              str(maxRevChangeDate) + "($" + str(maxRevChange) +")")
        print("Greatest Decrease in Revenue: "+ 
              str(minRevChangeDate) + "($" + str(minRevChange) +")")
        output.write('\n')
        output.write('\n')
        output.write('The results are for ' + str(csvFile[0]) + '\n')
        output.write('\n')
        output.write('Financial Analysis\n')
        output.write('-------------------\n')
        output.write('Total Months: ' + str(len(date)) + '\n')
        output.write('Total Revenue: $' + str(sum(revenue)) + '\n')
        output.write('Average Revenue Change: $' + str(avgRevChange) + '\n')
        output.write('Greatest Increase in Revenue: ' + 
                     str(maxRevChangeDate) + '($' + str(maxRevChange) + ')\n')
        output.write('Greatest Decrease in Revenue: ' + 
                     str(minRevChangeDate) + '($' + str(minRevChange) + ')\n')

    

