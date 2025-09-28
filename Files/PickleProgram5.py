import pickle

userdata = {
    "name":"Sai",
    "Age":27,
    "Company":"Broadridge",
    "Tech Stack": ["Python","AWS","Devops","SQL"]
}

try:
    with open("PP5","wb") as fp:
        pickle.dump(userdata,fp)
except IOError:
    print("Error writing to file")
else:
    print("Data written sucesfully")

