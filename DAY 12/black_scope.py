# Accessible anywhere
# my_global_var = 1
#
#
# def my_function():
#     # Only accessible within my_function()
#     my_local_var = 2
#
#
# for _ in range(10):
#     # Accessible anywhere
#     my_block_var = 3

#global Scope
enimies = 1

def inc():
    enimies = 19
    print(f"Local Scope : {enimies}")

print(f"Global Scope : {enimies}")
inc()
