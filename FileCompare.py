# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 15:55:35 2020
@author: Khushi Wadhwa
"""

import pandas as pd
import numpy as np
import itertools as it
from tkinter import *
from tkinter import filedialog as fd


# Check if the files can be compared
def canCompare(file1, file2):
    return file1.columns.equals(file2.columns)


# Output the total number of rows, num/percent differences, num/percent same, num/percent higher, num/percent lower
def compare(file1, file2, diff):
    diff['total'] = len(file1)
    dct1 = file1.to_dict('list')
    dct2 = file2.to_dict('list')
    
    # Calculate changes
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
        
    # Add to csv output file
    diff['num diff'] = numDiff
    diff['pct diff'] = (numDiff/len(file1))*100
    diff['num same'] = numSame
    diff['pct same'] = (numSame/len(file1))*100
    diff['num higher'] = numHigh
    diff['pct higher'] = (numHigh/len(file1))*100
    diff['num lower'] = numLow
    diff['pct lower'] = (numLow/len(file1))*100
        
    
# Output the mean of each column and the difference in both files
def mean(file1, file2, diff):
    diff['mean f1'] = np.mean(file1, axis=0)
    diff['mean f2'] = np.mean(file2, axis=0)
    diff['mean diff'] = np.subtract(np.mean(file1, axis=0), np.mean(file2, axis=0))


# Output the standard deviation of each column and the difference in both files
def std(file1, file2, diff):
    diff['std f1'] = np.std(file1, axis=0)
    diff['std f2'] = np.std(file2, axis=0)
    diff['std diff'] = np.subtract(np.std(file1, axis=0), np.std(file2, axis=0))


# Execute the script in the correct order
def start(file1, file2, diff):
    if (canCompare(file1, file2)):
        compare(file1, file2, diff)
        mean(file1, file2, diff)
        std(file1, file2, diff)
        diff.to_csv(r'C:/Users/k9wad/OneDrive/Documents/GitHub/FileCompare/Diff.csv')
        print(diff)
    else:
        print("Files are not compatable")


# Find the files
def get_file_name(file_entry):
    file_name = fd.askopenfilename(title = "Select file",filetypes = (("CSV Files","*.csv"),))
    file_entry.delete(0,END)
    file_entry.insert(0,file_name)


# Run the comparison code
def run_and_close(event=None):
    
    # Read the csv files
    file1 = pd.read_csv(inputCSV.get())
    file2 = pd.read_csv(inputCSV2.get())
    
    # Cleanup the data (remove strings)
    file1 = file1.select_dtypes(exclude=['object'])
    file2 = file2.select_dtypes(exclude=['object'])
    
    # Setup the output
    diff = pd.DataFrame(data=file1.columns, columns=['attributes'])
    diff = diff.set_index('attributes')
    
    start(file1, file2, diff)
    close()


# Cancel the process
def close(event=None):
    master.withdraw()
    sys.exit()


# Setup the GUI
master = Tk()
master.title("File Compare")

# First file search
inputCSV=Entry(master, text="", width=50)
inputCSV.grid(row=0, column=1, sticky=W, padx=5)
Label(master, text="Input CSV Base").grid(row=0, column=0 ,sticky=W)
Button(master, text="Browse...", width=10, command=lambda:get_file_name(inputCSV)).grid(row=0, column=2, sticky=W)

# Second file search
inputCSV2=Entry(master, text="", width=50)
inputCSV2.grid(row=1, column=1, sticky=W, padx=5)
Label(master, text="Input CSV Test").grid(row=1, column=0 ,sticky=W)
Button(master, text="Browse...", width=10, command=lambda:get_file_name(inputCSV2)).grid(row=1, column=2, sticky=W)

# Run process and cancel process
Button(master, text="Ok",     command=run_and_close, width=10).grid(row=3, column=1, sticky=E, padx=5)
Button(master, text="Cancel", command=close, width=10).grid(row=3, column=2, sticky=W)
master.bind('<Return>', run_and_close)
master.bind('<Escape>', close)

mainloop()
