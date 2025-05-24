# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
# greet_with_name("Jack Bauer")

#PAUSE 1
# def greet(name, age):
#     print(f"My name is {name} ")
#     print(f"and My age is {age}")
#
# greet("Arjun Murmu",21)
def greet_with(name,location):
    print(f"My name is {name}")
    print(f"I am from {location}")

# greet_with("Arjun Murmu","Balasore")
# greet_with("Chum","Mmr")
greet_with(location="Balasore",name="Arjun murmu")
# This is a positional argument
# def my_function(a,b,c):
#     print(a)
#     print(b)
#     print(c)
# my_function(3,4,5)
#

#Simple Function
def greet():
  print("Hello Angela")
  print("How do you do Jack Bauer?")
  print("Isn't the weather nice today?")
greet()

#Function that allows for input
#'name' is the parameter.
#'Jack Bauer' is the argument.
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")
greet_with_name("Jack Bauer")

#Functions with more than 1 input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

#Calling greet_with() with Positional Arguments
greet_with("Jack Bauer", "Nowhere")
#vs.
greet_with("Nowhere", "Jack Bauer")


#Calling greet_with() with Keyword Arguments
greet_with(location="London", name="Angela")
