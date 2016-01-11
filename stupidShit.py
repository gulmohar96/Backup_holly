import random
acc = []
for i in range(0,10):
    prob = random.random()
    acc.append(prob)

print(len(acc))
b = sum(acc)
print(b)