student = {
    "name" : "Khushi Jindal",
    "subjects" : {
        "phy" : 97,
        "chem" : 86,
        "math" : 89,
    }
}
#nested dictionary
print(student["subjects"]["chem"])
print(student.keys())
print(list(student.keys()))
print(len(student))
print(len(list(student.keys())))
#methods
print(student.values())
print(list(student.values()))
print((student.items()))
pairs = list(student.items())
print(pairs[0])
print(student["name"])
print(student.get["name"])
new_dict = {"city" : "delhi"}
student.update(new_dict)