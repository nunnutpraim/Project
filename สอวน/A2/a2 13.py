mocca_type, mocca_quantity = input().split()
mocca_quantity = int(mocca_quantity)

tea_type, sweetness_level, tea_quantity = input().split()
sweetness_level = int(sweetness_level)
tea_quantity = int(tea_quantity)

mocca_energy = {
    'H': 5,  
    'O': 3,  
    'J': 2   
}

tea_energy = {
    'R': {1: 12, 2: 18, 3: 25},  
    'T': {1: 15, 2: 20, 3: 30},  
    'M': {1: 10, 2: 15, 3: 20}   
}

mocca_total_energy = mocca_energy[mocca_type] * mocca_quantity

tea_total_energy = tea_energy[tea_type][sweetness_level] * tea_quantity

total_energy = mocca_total_energy + tea_total_energy

print(total_energy)