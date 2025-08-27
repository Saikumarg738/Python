import csv

try:
    with open("C:\\Users\\GangupamuS\\PyCharmMiscProject\\Python\\CSV\\country_full.csv") as fp:
        record=csv.DictReader(fp)
        print(type(record))
        for value in record:
            print(value)
except FileNotFoundError:
    print("File no found")
