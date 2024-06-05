SEAT_NUM = int(input('Please input a number: '))
SMALL_CAP = 5
MEDIUM_CAP = 10
LARGE_CAP = 15

SMALL_COST = 5000
MEDIUM_COST = 8000
LARGE_COST = 12000

# Function Here

def HOW_MANY_CAR(x, CAR_CAPACITY):
    count = 1
    while (CAR_CAPACITY*count) < x:
        count += 1
    return count

SMALL_FINAL = HOW_MANY_CAR(SEAT_NUM, 5) * SMALL_COST
MEDIUM_FINAL = HOW_MANY_CAR(SEAT_NUM, 10) * MEDIUM_COST
LARGE_FINAL = HOW_MANY_CAR(SEAT_NUM, 15) * LARGE_COST

F_COST = [SMALL_FINAL, MEDIUM_FINAL, LARGE_FINAL]
print(F_COST[0])
print(F_COST[1])
print(F_COST[2])

if F_COST.index(min(F_COST)) == 0:
    print('S x ' + str(HOW_MANY_CAR(SEAT_NUM, 5)))
elif F_COST.index(min(F_COST)) == 1:
    print('M x ' + str(HOW_MANY_CAR(SEAT_NUM, 10)))
elif F_COST.index(min(F_COST)) == 2:
    print('L x ' + str(HOW_MANY_CAR(SEAT_NUM, 15)))

print('TOTAL COST: ' + str(min(F_COST)))
