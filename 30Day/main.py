try:
    file = open("a_file.txt")
    a_dictionary = {"key" : "value"}
    print(a_dictionary["smth"])
#   if we change our print to print(a_dictionary["key"]) then our program will execute
#                                                               else: and skip except KeyError:
except FileNotFoundError:
    file = open("a_file.txt", mode="w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")