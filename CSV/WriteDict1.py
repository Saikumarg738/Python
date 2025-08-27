import csv

header=["Name","Age"]
data=[{"Name":"Sai","Age":26},{"Name":"Kumar","Age":27}]

with open("C:\\Users\\GangupamuS\\PyCharmMiscProject\\Python\\CSV\\WriteData.csv","w+",newline="") as fp:
    wrobj=csv.DictWriter(fp,fieldnames=header)
    wrobj.writeheader()
    wrobj.writerows(data)
    fp.seek(0)
    rdobj=csv.DictReader(fp)
    for i in rdobj:
        for a,b in i.items():
            print("%-8s %-8s"%(a,b))



