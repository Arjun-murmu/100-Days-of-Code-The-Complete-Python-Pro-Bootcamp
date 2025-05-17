import random
from math import radians

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#Radom name print in the list

#Option no 1
#print(random.choice(friends))

#option no 2
# choice_friends = random.choice(friends)
# print(choice_friends)

#option no 3
radom_index = random.randint(0,4)
print(friends[radom_index])