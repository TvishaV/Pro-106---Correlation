import csv
import numpy as np 

marks_percentage = []
days_present = []

with open(r"marks_vs_Presenty.csv") as df:
    data_reader = csv.DictReader(df)
    
    for row in data_reader:
         marks_percentage.append(float(row["Marks In Percentage"]))
         days_present.append(float(row["Days Present"]))

correlation = np.corrcoef(marks_percentage,days_present)
print(correlation[0,1])
