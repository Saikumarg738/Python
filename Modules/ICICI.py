bankname="ICICI"
add="Hitech City"

def calintrest():
    prin=float(input("Enter principle amount : "))
    int=float(input("Enter intrest amount : "))
    time=float(input("Enter time : "))
    intamt=(prin*int*time)/100
    totamt=intamt+prin
    print("="*30)
    print(f"Your principle amount is : {prin:<10.2f}")
    print(f"Your Intrest amount is   : {int:<8.2f}%")
    print(f"Your time amount is      : {time:<8.2f}")
    print("=" * 30)
    print(f"Your total amount is     : {totamt:<10.2f}")