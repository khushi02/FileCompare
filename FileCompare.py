# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 15:55:35 2020
@author: k9wad
"""

"""
*can compare -> figure out if the two files are comparable
*cleanup -> clean data
*total -> return len
num diff -> return num differences
percent diff -> return percent different
num higher -> return num higher values
percent higher -> return percent higher values
num lower -> return num lower values
percent lower -> return percent lower values
*first mean -> return mean of first file
*second mean -> return mean of second file
*diff mean -> return diff in 2 means
*first std -> return standard deviation of first file
*second std -> return standard deviation of second file
*diff std -> return diff in 2 stds
optional: min, max, 25%, 50%, 75%
"""

import pandas as pd
import numpy as np
import itertools as it

# Check if the files can be compared
def canCompare(file1, file2):
    return file1.columns.equals(file2.columns)

# Output the total number of rows, num/percent differences, num/percent higher, num/percent lower
def compare(file1, file2):
    diff['total'] = len(file1)
    dct1 = file1.to_dict('list')
    dct2 = file2.to_dict('list')
    
    numDiff = np.array([])
    numSame = np.array([])
    numHigh = np.array([])
    numLow = np.array([])
    for i in dct1:
        higher = 0
        lower = 0 
        change = 0
        same = 0
        for (j, k) in it.zip_longest(dct1[i], dct2[i]):
            if (k > j):
                higher += 1
                change += 1
            elif (k < j):
                lower += 1
                change += 1
            else:
                same += 1
        numDiff = np.append(numDiff, change)
        numSame = np.append(numSame, same)
        numHigh = np.append(numHigh, higher)
        numLow = np.append(numLow, lower)
        
    
    diff['num diff'] = numDiff
    diff['pct diff'] = (numDiff/len(file1))*100
    diff['num same'] = numSame
    diff['pct same'] = (numSame/len(file1))*100
    diff['num higher'] = numHigh
    diff['pct higher'] = (numHigh/len(file1))*100
    diff['num lower'] = numLow
    diff['pct lower'] = (numLow/len(file1))*100
        
# Output the mean of each column and the difference in both files
def mean(file1, file2):
    diff['mean f1'] = np.mean(file1, axis=0)
    diff['mean f2'] = np.mean(file2, axis=0)
    diff['mean diff'] = np.subtract(np.mean(file1, axis=0), np.mean(file2, axis=0))

# Output the standard deviation of each column and the difference in both files
def std(file1, file2):
    diff['std f1'] = np.std(file1, axis=0)
    diff['std f2'] = np.std(file2, axis=0)
    diff['std diff'] = np.subtract(np.std(file1, axis=0), np.std(file2, axis=0))

# Execute the script in the correct order
def start(file1, file2):
    if (canCompare(file1, file2)):
        compare(file1, file2)
        mean(file1, file2)
        std(file1, file2)
        diff.to_csv(r'C:/Users/k9wad/OneDrive/Documents/GitHub/FileCompare/Diff.csv')
    else:
        print("Files are not compatable")
    
# Import files
file1 = pd.read_csv(r'C:/Users/k9wad/Downloads/LI Base full.csv')
file2 = pd.read_csv(r'C:/Users/k9wad/Downloads/LI Test full.csv')

# Cleanup data
file1 = file1.select_dtypes(exclude=['object'])
file2 = file2.select_dtypes(exclude=['object'])

# Setup output
diff = pd.DataFrame(data=file1.columns, columns=['attributes'])
diff = diff.set_index('attributes')

# Execute script
start(file1, file2)
print(diff)