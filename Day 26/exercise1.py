with open("./file1.txt") as file:
    numbers1 = [int(line.strip()) for line in file]
# print(numbers1)

with open("./file2.txt") as sec_file:
    numbers2 = [int(line.strip()) for line in sec_file]
# print(numbers2)

result = [num for num in numbers1 if num in numbers2]

print(result)