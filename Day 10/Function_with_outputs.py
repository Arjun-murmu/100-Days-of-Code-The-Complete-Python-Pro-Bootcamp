# def my_fun():
#     result = 3*2
#     return result
# output = my_fun()
# print(output)

# def my_fun():
#     return 3*2
# output = my_fun()
# print(output)

# def format_name(f_name ,l_name):
#     print(f_name.title())
#     print(l_name.title())
# format_name(f_name="Arjun",l_name="Murmu")

# def format_name(f_name ,l_name):
#     format_f_name = f_name.title()
#     format_l_name = l_name.title()
#     # print(f"{format_f_name} {format_l_name}")
#     return f"{format_f_name} {format_l_name}"
#
# format_name(f_name="Arjun",l_name="Murmu")
# format_string = format_name(f_name="UTTAM",l_name="MURMU") #Uttam Murmu
# print(format_string)
#
# output = len("Arjun")
# print(output)

def function_1(text):
    return text +" "+ text

def function_2(text):
    return text.title()

# output = function_1("Sonali")
# print(output)
# output = function_2("Sonali")
# print(output)
output = function_2(function_1("GOOD MORINING "))
print(output)
