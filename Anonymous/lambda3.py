#Program for accepting List of Values and Find Biggest among them

findmax=lambda ls:max(ls)

ls=[int(i) for i in input("Enter the number with space : ").split()]

print(findmax(ls))
