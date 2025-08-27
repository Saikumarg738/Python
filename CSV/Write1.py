import csv

col=["Name","Age","Role"]
data=[["Sai",28,"SE"],["Kumar",30,"RE"],["Gangu",25,"GW"]]

with open("C:\\Users\\GangupamuS\\PyCharmMiscProject\\Python\\CSV\\WriteData.csv","w+",newline="") as fp:
    record=csv.writer(fp)
    record.writerow(col)
    record.writerows(data)
    fp.seek(0)
    rd=csv.reader(fp)
    for data in rd:
        print(data)
