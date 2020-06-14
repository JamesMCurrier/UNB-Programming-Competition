# Get threshold inputs
thresholds = [int(i) for i in input().split()]

# Number of times where the speed was really fast, on a really hot day 
cat1 = 0
# Number of times where the speed was really slow, on a really hot day
cat2 = 0
# Number of times where the speed was really fast, on a really cold day
cat3 = 0
# Number of times where the speed was really slow, on a really cold day
cat4 = 0


for _ in range(int(input())):
    line = input().split()
    temp = int(line[0])
    speed = int(line[1])

    # cat1
    if temp > thresholds[1] and speed > thresholds[3]:
        cat1 += 1

    # cat2
    if temp > thresholds[1] and speed < thresholds[2]:
        cat2 += 1

    # cat3
    if temp < thresholds[0] and speed > thresholds[3]:
        cat3 += 1

    # cat4
    if temp < thresholds[0] and speed < thresholds[2]:
        cat4 += 1


print(cat1)
print(cat2)
print(cat3)
print(cat4)
