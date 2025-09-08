from Encapsulation4 import Account

a=Account()

print(getattr(a,"_Account__accno"))
setattr(a,"_Account__accno",5678)
print(getattr(a,"_Account__accno"))