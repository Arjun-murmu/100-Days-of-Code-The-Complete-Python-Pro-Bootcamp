from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_images[dice_num])

# randint(1, 6) returns a random number from 1 to 6 (inclusive).
# But dice_images is a list with indices 0 to 5.
# So if dice_num == 6, then dice_images[6] will raise an IndexError because index 6 is out of range.



# from random import randint
# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 5)
# print(dice_images[dice_num])
# randint(1, 5) gives numbers from 1 to 5 only (excluding 6), so you're missing the 6th side of the die.
# Also, like the first one, dice_images[dice_num] will access index 1 to 5 — skipping the image at index 0.


# from random import randint
# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_images[dice_num-1])

# 1. List indices in Python start at 0.
# 2. randint(1, 6) returns a value from 1 to 6.
# 3. Accessing dice_images[dice_num] is wrong because index 6 doesn't exist (list index out of range).
# 4. Fix: use dice_images[dice_num - 1] to match dice faces correctly.


from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_images[dice_num])
