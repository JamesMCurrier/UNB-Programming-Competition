def find_UNBSJ(board: list) -> tuple:
    """Finds UNBSJ in a board"""

    # Check left to right
    for i in range(len(board)):
        result = board[i].find("UNBSJ")
        if result != -1:
            return (i+1, result+1)

    # Transpose the board to check top to bottom
    transposed = []
    for i in range(len(board[0])):
        s = ""
        for j in range(len(board)):
            s += board[j][i]

        transposed.append(s)
    
    for i in range(len(transposed)):
        result = transposed[i].find("UNBSJ")
        if result != -1:
            return (result+1, i+1)

# Get inputs
num = int(input().split()[0])
my_board = [input() for i in range(num)]

# Calculates and print outputs
output = find_UNBSJ(my_board)
print(f"{output[0]} {output[1]}")
