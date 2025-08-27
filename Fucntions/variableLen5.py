
def disp(name,name2,**gar):
    print(name)
    print(name2)
    for i in gar.keys():
        print("Key is {}".format(i))

def hel(*var,**gar):
    print(var)
    disp(*var,**gar)  # This is taking as disp("Sai","Kumar)

hel("Sai","Kumar",hesaru="Meghna",age="28",job="SE")