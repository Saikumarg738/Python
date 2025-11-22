"""
Write a Python program to sort a list of nested dictionaries.
		my_collection = {
						'KEY1':{'name':'foo','data':1351,'completed':100},
						'KEY2':{'name':'bar','data':1541,'completed':12},
						 'KEY3':{'name':'baz','data':58413,'completed':18}
					    }
"""
my_collection = {
						'KEY1':{'name':'foo','data':1351,'completed':100},
						'KEY2':{'name':'bar','data':1541,'completed':12},
						 'KEY3':{'name':'baz','data':58413,'completed':18}
					    }
newcoll=sorted(my_collection.items(),key=lambda a:a[1]['data'])

print(newcoll)