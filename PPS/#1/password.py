pwd = "1234"
user_input = ""
while user_input != pwd:
    user_input = input("enter password")
    if user_input == pwd:
        print("access")
    else:
        user_input = input("enter password")

n = int(input(""))
for i in range(1, n + 1):
    spaces = ' ' * (n - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)