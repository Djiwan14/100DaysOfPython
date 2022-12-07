#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Save the letters in the folder "ReadyToSend".
    
with open("Input/Names/invited_names.txt", "r") as f:
    names = f.readlines()
with open("Input/Letters/starting_letter.txt") as letter_contents:
    content = letter_contents.read()
for name in names:
    stripped_name = name.strip()
    new_letter = content.replace("[name]", f"{stripped_name}")
    with open(f"Output/ReadyToSend/letter_for{stripped_name}.txt", "w") as file:
        file.write(new_letter)
