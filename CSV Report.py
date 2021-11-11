# Rodrigo Alcover
# 7/11/2021
# CIS-216-12292 
# Python Programming

from collections import Counter
from typing import List

def read_csv():
    header = True  
    year_data = {}
    print("Year |  Min |  Max |  Avg") #header 
    print("==== | ==== | ==== | ====")
    with open('MIGRNDRA.csv', 'r') as my_file:# Open file for reading with open(path)
         for line in my_file.readlines():#search for lines 
            line = line.strip() #   
            if not line: 
                continue
            if header:#search for header
                header = False#ignore the header
                continue
            values = line.split(',')#How to read the values separated by a coma
            month = int(values[0])#read and store values
            day = int(values[1])
            year = int(values[2])
            temp = float(values[3])
            if year not in year_data:#load year 
                year_data[year] = []# add year to the collection
            year_data[year].append(temp) #append the dictionary    
                
    for year, temps in year_data.items():#read year and temps
         
        average = sum (temps) / len(temps)#calculate average
        minimun = min (temps) #calulate minimun
        maximun = max (temps)#calculate max
        
                
        print("{} | {:=4} | {:>.1f} | {:>.1f}".format (year, minimun, maximun, average))#Print the results
        
        
read_csv()#run the program

#Write one sentence that explains why the average for 2020 is much lower than the other years

# The average temperature for 2020 is because a success called la niña . 
# La Niña is an oceanic and atmospheric phenomenon that is the colder counterpart of El Niño, 
# as part of the broader El Niño–Southern Oscillation climate pattern.

#The total development time is 15 hs.


#This program reads the data from a list of temperature data (in Fahrenheit) for Grand Rapids, MI from 1995 until 2020. 
#The program will organize, calculate and print the average, min, max temperature by year.
#Run the program executing the comand "read_csv()"





#How to read the values

#if month != userInput:  

#     continue        