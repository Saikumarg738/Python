list1=[1,"sai",7.8,2+3j,True,59,"Kumar"]

print(list1,id(list1))

############# Append(value)

list1.append("Teja")

print(list1,id(list1))

############# insert(index,value)

list1.insert(4,85)

print(list1,id(list1))

############# Remove(Value)

list1.remove('Teja')

print(list1,id(list1))

############# pop(index)

list1.pop(2)

############# pop() - If we don't specify value, last object is removed.

list1.pop()

print(list1,id(list1))

############# clear()

#list1.clear()

#print(list1,id(list1))

############# del() - del will delete list and elements inside

############# index()

print(list1.index(85))

print(list1[2])

############# enumerate