#Program for Demonstrating the Need of Generators
#GenEx4.py
def kvrrange(Beg,End=1,Step=1):
	if(Beg>End):
		End=Beg
		Beg=1
	while(Beg<=End):
		yield Beg
		Beg=Beg+Step

#Main Program
go1=kvrrange(10)
for val in go1:
	print(val)
print("--------------------------------------------------")
go3=kvrrange(10,21,2)
for val in go3:
	print(val)