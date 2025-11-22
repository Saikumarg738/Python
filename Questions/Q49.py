"""Write a Python program to convert list to list of dictionaries.
Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
"""
ls1=["Black", "Red", "Maroon", "Yellow"]
ls2=["#000000", "#FF0000", "#800000", "#FFFF00"]

"""newls=[]
for i in range(len(ls1)):
    set1={}
    set1['color_name']=ls1[i]
    set1['color_code']=ls2[i]
    newls.append(set1)

print(newls)"""

newls=[{'color_name':name,'color_code':code} for name,code in zip(ls1,ls2)]

print(newls)
