def get_animal(year: int) -> str:
    """Gets the animal associated with the given year"""

    animals = {0: "Dog",
               1: "Pig",
               2: "Rat",
               3: "Ox",
               4: "Tiger",
               5: "Rabbit",
               6: "Dragon",
               7: "Snake",
               8: "Horse",
               9: "Goat",
               10: "Monkey",
               11: "Rooster"}

    return animals[(year-1982) % 12]


def are_compatible(year1: int, year2: int) -> bool:
    """Returns the compatibility of two years"""
    
    steps_diff = abs(year1 - year2) % 12

    if steps_diff == 4:
        return "compatible"
    
    elif steps_diff == 6:
        return "not compatible"

    else:
        return "not determined"


# Get all inputs
inputs = [input() for _ in range(4)]

# Clean the inputs
cleaned_inputs = []
for i in inputs:
    a,b = i.split()
    cleaned_inputs.append((int(a),int(b)))
    
# Calculate and print results
for i in cleaned_inputs:
    animal1 = get_animal(i[0])
    animal2 = get_animal(i[1])

    print(f"{animal1} {animal2}")
    print(are_compatible(i[0], i[1]))
