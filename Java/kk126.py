with open("practise.txt","r") as f:
    data = f.read()
new_data = data.replace("java", "python")
print(new_data)