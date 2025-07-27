# class User:
#     print("Hello Class.")
#     pass

# class User:
#     def __init__(self):
#         print("New user beging.")
#     # print("Hello Class.")
#
# user_1 = User()
# user_1.id = "001"
# user_1.username = "Arjun."
# print(f"user id : {user_1.id} , user name : {user_1.username}.")
#
# user_2 = User()
# user_2.id = "002"
# user_2.username = "Jaga."
# print(f"user id : {user_2.id} , user name : {user_2.username}.")

# class User:
#     def __init__(self,user_id,username):
#         print("New user beging.")
#         self.id = user_id
#         self.username = username
#         self.followrs = 5
#     # print("Hello Class.")
#
# user_1 = User("001","Arjun")
# print(user_1.id)
# print(user_1.username)
# print(user_1.followrs)

class User:
    def __init__(self,user_id,username):
        print("New user beging.")
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0
    # print("Hello Class.")
    def follow(self,user):
        user.follower += 1
        self.following += 1

user_1 = User("001","Arjun")
user_2 = User("002","jaga.")

user_1.follow(user_2)
print(user_1.follower)
print(user_1.following)
print(user_1.follower)
print(user_1.following)
