STARTING_PAIR = 1
LITTER_SIZE = 3
MONTHS = 1

class RabbitPair():
    def __init__(self, age):
        self.age = age


allRabbits = []

while STARTING_PAIR != 0:
    allRabbits.append(RabbitPair(0))
    STARTING_PAIR -= 1

months = 0

while MONTHS != months:
    counter = 0
    for i in allRabbits:
        if i.age == 0:
            i.age = 1
        else:
            counter += LITTER_SIZE
    add = 0
    while add != counter:
        allRabbits.append(RabbitPair(0))
        add += 1
    months += 1

print(len(allRabbits))
