#TODO: Create a letter using starting_letter.txt

# f = open("C:/Users/murmu/PycharmProjects/100 Days of Code - The Complete Python Pro Bootcamp/DayN 24/Mail+Merge+Project+Start/__MACOSX/Mail Merge Project Start/Input/Letters/._starting_letter.txt", "r")
# print(f.readlines(20))

#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as names_list:
    names = names_list.readlines()
    # print(names)
with open("./Input/Letters/starting_letter.txt") as letter:
    write_content = letter.read()
    for name in names:
        name_striped = name.strip()
        new_letter = write_content.replace(PLACEHOLDER, name_striped)
        # print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{name_striped}.docx", mode="w") as complete:
            complete_letter = complete.write(new_letter)
            # print(complete_letter)