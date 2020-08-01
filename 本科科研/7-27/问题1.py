"""
求1-2+3-4+5 ... 99的所有数的和
"""
sum = 0
state = 1
for i in range(1,100):
    sum = sum + state * i
    state = -1 * state
print(sum)