
try:
    with open("C:\\Users\\GangupamuS\\PyCharmMiscProject\\Python\\CSV\\country_full.csv","r",encoding="utf-8") as fp:
        record=fp.read()
        print(record)
        print(type(record))
except FileNotFoundError:
    print("File not found")