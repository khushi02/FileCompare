# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 15:55:35 2020

@author: k9wad
"""

"""
*can compare -> figure out if the two files are comparable
cleanup -> clean data
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

def canCompare(file1, file2):
    return file1.columns.equals(file2.columns)

#update w cleaned data
def total(file1):
    len(file1)

def firstMean(file1):
    np.mean(file1, axis=0)
    
def secondMean(file2):
    np.mean(file2, axis=0)
    
def diffMean(file1, file2):
    # should I create variables?
    np.subtract(np.mean(file1, axis=0), np.mean(file2, axis=0))
    
def firstSTD(file1):
    np.std(file1, axis=0)
    
def secondSTD(file2):
    np.std(file2, axis=0)
    
def diffSTD(file1):
    # should I create variables?
    np.subtract(np.std(file1, axis=0), np.std(file2, axis=0))
 
    
file1 = pd.read_csv(r'C:\Users\k9wad\Downloads\LI Base.csv')
file1 = file1.select_dtypes([np.number])
file2 = pd.read_csv(r'C:\Users\k9wad\Downloads\LI Test.csv')
file2 = file2.select_dtypes([np.number])
diff = pd.DataFrame()

print(canCompare(file1, file2))
print(np.subtract(np.std(file1, axis=0), np.std(file2, axis=0)))

#print(len(file1))
#print(file1.shape)
#print(file1.head())
#file1.info()
#print(file1.columns)
#print(file2.columns)
#print("time_ms" in file1.keys())
#print(file1.describe())
#print(file1["time_ms"].max())
#print(file1.loc["seq"].std())

