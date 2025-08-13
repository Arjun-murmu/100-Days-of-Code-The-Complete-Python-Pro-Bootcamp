import pandas
from numpy.ma.extras import average
from pandas.core.interchange.dataframe_protocol import DataFrame

data = pandas.read_csv("./weather_data.csv")
# print(data)
# print(type(data))  #<class 'pandas.core.frame.DataFrame'>
# print(type(data["day"]))  #<class 'pandas.core.series.Series'>

data_dict = data.to_dict()
# print(data_dict)
# print(len(data_dict))

data_list = data["temp"].to_list()
# print(data_list)
# print(len(data_list))
# total_list = sum(data_list)
# print(total_list)
# average_temp = total_list/len(data_list)
# print(average_temp)

# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].min())
#
# print(data.condition)
# print(data.day)

# print(data[data.day == "Monday"])
# print(data.temp.max())
# print(data[data.temp == data.temp.max()])
# print(data[data.temp == data.temp.min()])

monday = data[data.day == "Monday"]
# print(monday.condition)

# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

data_dict = {
    "student" : ["arjun","uttam","nabin"],
    "mark" : [73,72,77]
}
# print(data_dict)
data_student = pandas.DataFrame(data_dict)
# print(data_student)

data_student.to_csv("student_data.csv")

