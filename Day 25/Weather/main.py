#Using csv library
import csv

#Using just file methods
# with open("./weather_data.csv") as weather:
#     data = csv.reader(weather)
#     temperature = []
#     for row in data:
#         # print(row)
#         temperature_value = row[1]
#         temperature.append(temperature_value)
#         print(temperature_value)

# with open("./weather_data.csv") as weather:
#     data = csv.reader(weather)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)  #[12, 14, 15, 14, 21, 22, 24]


# Using the pandas library
import pandas
data = pandas.read_csv("./weather_data.csv")
# print(data)  #Full data print
print(data["temp"])   #Only Temperature print
# print(data["condition"])  #Only condition print
# print(data["day"])  # only day part print

