def format_name(f_name, l_name):
    """The user input the first and
    last name
    then the first name store in format_f_name and
    last name store is format_l_name
    then next part is
    return the first name and last name complete name."""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


# formatted_name = format_name("AnGeLa", "YU")
#
# length = len(formatted_name)

def my_function(num):
    """Multiply a number itself"""
    return num*num
print(my_function(12))


