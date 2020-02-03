from random import randint

premio = []

for i in range(6):
    premio.append(randint(1,49))
for j in range(6):
    if premio[i]==premio[j]:
        premio[i] = (randint(1,49))
print(premio)
