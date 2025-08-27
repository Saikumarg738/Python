#Program for Demonstrating the Need of Generators
#GenEx3.py
def kvrrange(BVal,EVal):
	while(BVal<=EVal):
		yield BVal
		BVal=BVal+1

#Main Program
r=kvrrange(10,20) # Function Call--gives the values only on demand
print(next(r))
print(next(r))
for val in r:
	print(val)