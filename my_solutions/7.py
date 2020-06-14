import itertools

size = int(input())
containers = [int(i) for i in input().split()]

smallest_ans = float("inf")

# find best solution of all possibilities
for i in itertools.permutations(containers):

    diff = abs(sum(i[:3]) - sum(i[3:]))

    if diff < smallest_ans:
        smallest_ans = diff


print(smallest_ans)
