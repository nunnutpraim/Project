size_type = input().split()
size = size_type[0]  
type_ = size_type[1]  

topping_input = input().split()
topping_type = topping_input[0]  
topping_count = 0 if topping_type == 'N' else int(topping_input[1])
topping_count = 0
if topping_type != 'N':
    topping_count = int(topping_input[1])

price = 0
if size == 'S':
    if type_ == 'R':
        price = 60
    elif type_ == 'T':
        price = 80
elif size == 'M':
    if type_ == 'R':
        price = 80
    elif type_ == 'T':
        price = 100
elif size == 'L':
    if type_ == 'R':
        price = 100
    elif type_ == 'T':
        price = 120

if topping_type == 'P': 
    price += topping_count * 15
elif topping_type == 'E': 
    price += topping_count * 10

print(price)
