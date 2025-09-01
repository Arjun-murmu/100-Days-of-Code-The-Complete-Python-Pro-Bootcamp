import pandas
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

word_dict = pandas.read_csv("./nato_phonetic_alphabet.csv")
# print(word_dict)
# print(word_dict.to_dict())

phonetic_dictionary = {row.letter:row.code for (key, row) in word_dict.iterrows()}
# print(phonetic_dictionary)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter Your name : ").upper()
name_dict = [letter for letter in name]
output_list = [phonetic_dictionary[word] for word in name]
# print(name_dict)
# print(output_list)
# print(f"{name_dict} : {output_list}")

# Print the output in the desired format
for letter, code in zip(name, output_list): # Using zip to iterate through name (letters) and output_list (codes) simultaneously
    print(f"{letter} : {code}")