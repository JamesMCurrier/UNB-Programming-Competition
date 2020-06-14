def convert_time(x: int) -> str:
    """Converts Time from 24-hr to 12-hr"""
    
    if x == 0:
        return "12am"

    elif x == 12:
        return "12pm"

    elif x < 12:
        return f"{x}am"

    else:
        return f"{x-12}pm"


# Get all three inputs
inputs = [input() for _ in range(3)]

# Convert times and print results
for i in inputs:
    print(convert_time(int(i)))
