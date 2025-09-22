from datetime import datetime

date_str1="2025-09-01"
date_str2="2025/09/20"

date1=datetime.strptime(date_str1,"%Y-%m-%d")
date2=datetime.strptime(date_str2,"%Y/%m/%d")

print(date1,type(date1))
print(date2,type(date2))

print("date different is",date2-date1)
print(type(date2-date1))