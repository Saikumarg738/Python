
def disp(*dish,**details):
    print("Order list is:")
    for i in dish:
        print(f" - {i}")
    print("Order details are:")
    for i,j in details.items():
        print(" %-7s : %7s"%(i,j))

disp("Appolo Fish","Biriyani","Coke", Name="Sai",table="6",time="4 PM")