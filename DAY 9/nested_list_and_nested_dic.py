capital = {
    "France" : "Paris",
    "Germany" : "Berlin",
}

#Nested List Dictionaries

travel_log = {
    "France" : ["Paris","Lille","Dijon"],
    "Germany": ["Stuttgart","Berlin"],
}
#Print out of lille
#
# print(travel_log["France"][1])
# print(travel_log["France"][2])
#print(travel_log["France"][3]) #IndexError

# print(travel_log["France"][-1]) #Dijon
#
# print(len(travel_log)+1)

nested_list = ["A","B",["C","D"]]

# print(nested_list[2][1]) #D
# print(nested_list[1]) #B
# print(nested_list[0]) #A
# print(nested_list[2][0]) #C
# travel_log = {
#     "France" : {
#         "cities_visited" : ["Paris","Lille","Dijon"],
#         "num_times_visited": 12,
#     },
#     "Germany": {
#         "cities_visited" : ["Stuttgart","Berlin"],
#         "total_visited" : 5
#     },
# }

# print(travel_log)
# print(travel_log["France"])
# print(travel_log["France"]["cities_visited"]) #['Paris', 'Lille', 'Dijon']
# print(travel_log["France"]["cities_visited"][2]) #Dijon
#
# print(travel_log["Germany"]["cities_visited"]) #['Stuttgart', 'Berlin']
# print(travel_log["Germany"]["cities_visited"][0]) #Stuttgart

#Length Check

# print(len(travel_log)) #2
# print(type(travel_log)) #<class 'dict'>

starting_dictionary = {
    "a" : 9,
    "b" : 8,
}

final_dictionary = {
    "a" : 9,
    "b" : 8,
    "c" : 7,
}

# starting_dictionary["c"]=7
# print(starting_dictionary)
# final_dictionary = starting_dictionary
# print(final_dictionary)
dict = {
    "a" : 1,
    "b" : 2,
    "c" : 3,
}
# # dict["c"] = [1,2,3]
# print(dict[1])
# dict[1] = 4
# for key in dict:dict[key] += 1
