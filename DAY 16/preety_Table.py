from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Name",["Arjun","Uttam","Abinash"])
table.add_column("Class",["B.Tech","Diploma","Graduation"])
table.align = "l"     #This is for the left alignment
# print(table)

pokeman_table = PrettyTable()

# pokeman_table.add_column("Pockeman Name ",["Pikachu","Squirtle","Charmander"])
# pokeman_table.add_column("Type ",["Electric","Water","Fire"])

pokeman_table.add_column("Pockeman Name ",["Pikachu","Squirtle","Charmander"])
pokeman_table.add_column("Type ",["Electric","Water","Fire"])

# pokeman_table.align = "r"    #This is for the right alignment

pokeman_table.align["Pockeman Name "] = "l"  #Same table this is left alignment
pokeman_table.align["Type "] = "r"    #Same table this is right alignment


print(pokeman_table)
