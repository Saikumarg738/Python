#Write a Python program to find a tuple, the smallest second index value from a list of tuples.



def findtuple(ls):
    #return list(sorted(ls,key=lambda x:x[1]))[0]
    return min(ls,key=lambda x:x[1])

print(findtuple([(2,3),(9,8),(5,6),(9,1)]))

