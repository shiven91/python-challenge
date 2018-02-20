#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 16:07:22 2018

@author: sivenpatel
"""

import csv
import os

csvFiles = ["budget_data_1.csv"]

for file in csvFiles:
    csvPath = os.path.join("raw_data",file)
    previousChange = []
    date = []
    revenue = []

    with open (csvPath, newline='') as cfile:
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
            avgRevChange = sum(previousChange)/len(previousChange)
            #print (avgRevChange)
            maxRevChange = max(previousChange)
            #print (maxRevChange)
            maxRevChangeDate = str(date[previousChange.index(maxRevChange)])
    
            minRevChange = min(previousChange)
            minRevChangeDate = str(date[previousChange.index(minRevChange)])

        
print ()
print ()
print ("Financial Analysis")
print ("-------------------")
print ()
print ("Total Months: ", len(date))
print ("Total Revenue: $",sum(revenue))
print ("Average Revenue Change: $",avgRevChange)
print ("Greatest Increase in Revenue: "+ 
       str(maxRevChangeDate) + "($" + str(maxRevChange) +")")
print ("Greatest Decrease in Revenue: "+ 
       str(minRevChangeDate) + "($" + str(minRevChange) +")")

