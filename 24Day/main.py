file = open("../../../../phone_files/my_file.txt")
contents = file.read()
print(contents)
file.close()

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt", mode="w") as file:
    file.write("Hello Guys")

with open("my_file.txt", mode="a") as f:
    f.write("\nhihihihihi")

with open("new_file.txt", mode="w") as f:
    f.write("Hello it is a new file")
