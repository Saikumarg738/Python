import csv # Step-1
def createcsvfile():
    colname=["SNO","SNAME","MARKS"] # Step-2
    records=[[100,"Rajesh",56.78],
            [200,"Raju",26.78],
            [300,"Ramesh",46.58],
            [400,"Rakesh",66.78]] # Step-3
    with open("C:\\Users\\GangupamuS\\PyCharmMiscProject\\Python\\CSV\\student.csv","w") as fp: # Step-4
        csvwr=csv.writer(fp) # here csvwr is an object of <class, csv.writer>
        #write col name to the csv file--we use writerow() present in csv.writer class object
        csvwr.writerow(colname) # Step-5
        # write the records to the csv file--we use writerows() present in csv.writer class object
        csvwr.writerows(records) #Step-6
        print("CSV File Created and Records Saved in csv file--verify")

#Main Program
createcsvfile()