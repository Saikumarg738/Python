#DateEx6.py
from datetime import datetime
td=datetime.now()
print("Weekday, short version=",td.strftime("%a"))
print("Weekday, Full version=",td.strftime("%A"))
print("Weekday as a number 0-6=",td.strftime("%w"))
print("Day of month 01-31=",td.strftime("%d"))
print("Month name, short version=",td.strftime("%b"))
print("Month name, full version	=",td.strftime("%B"))
print("Month Number=",td.strftime("%m"))
print("Year, short version, without centuryr=",td.strftime("%y"))
print("Year, short version, without centuryr=",td.strftime("%Y"))