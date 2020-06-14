def recommendations(past, present):
    """Return recommendations when buying present, after past transations"""
    
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    ans = ""
    for i in alph:
        if i == present:
            continue

        bought = 0

        for j in past:
            if i in j and present in j:
                bought += 1

        if bought >= 3:
            ans += i + " "
        
    return ans


# Get all previous purchases
purchases = []
for _ in range(int(input())):
    purchases.append(input().split())

# Get inputs
inputs = [input() for i in range(int(input()))]

# Calculate and print results
for i in inputs:
    print(f"{i}: {recommendations(purchases, i)}")
