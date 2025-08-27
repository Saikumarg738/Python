#program for Finding Number of Occurences of Values in in List

ls=[10,20,30,10,20,30,45,29,29]

sample=set(ls)

for i in sample:
    print("The number of occurences of {} is {}".format(i,ls.count(i)))