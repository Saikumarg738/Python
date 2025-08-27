import csv
import os
print(os.path.exists("C:\\Users\\GangupamuS\\PyCharmMiscProject\\Python\\CSV\\country_full.csv"))

try:
    with open("C:\\Users\\GangupamuS\\PyCharmMiscProject\\Python\\CSV\\country_full.csv","r") as fp:
        record=csv.reader(fp) # Store result in iterable object of class _csv.reader
        for val in record:  # The elements of _csv.reader are lists
            for i in val:
                print("%-40s"%i,end="")
            print()
        print(type(record))
except FileNotFoundError:
    print("File not found")