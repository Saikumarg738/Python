#Program for Accepting a Line of Text and Find the length of each word and display in the form of dict
import random
line=input("Enter the input: ")

ls=line.split(" ")
dic={}
for i in ls:
    dic[i]=len(i)
    print("The lemght of {} is {}".format(i,len(i)))

random.shuffle(dic)


