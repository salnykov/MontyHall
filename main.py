import random
import matplotlib.pyplot as plt

def doors():
    result = ['goat', 'goat', 'goat']
    result[random.randint(0, 2)]='car'
    return result

def choice():
    return random.randint(0, 2)

def nochange():
    if doors()[choice()] == 'car':
        return 'win'
    else:
        return 'loose'

def change():
    if doors()[choice()] == 'goat':
        return 'win'
    else:
        return 'loose'

def simulation (iterations, strategy):
    wincount = 0
    for _ in range(iterations-1):
        if strategy() == 'win':
            wincount += 1
    return wincount/iterations

change_outcomes = []
nochange_outcomes = []

for _ in range(5000):
    change_outcomes.append(simulation(100, change))
    nochange_outcomes.append(simulation(100, nochange))


plt.subplot(1, 2, 2)
plt.hist(change_outcomes, bins=10)
plt.title("Win chance if CHANGE")
plt.xlabel('Probability')
plt.ylabel('Frequency')


plt.subplot(1, 2, 1)
plt.hist(nochange_outcomes, bins=10)
plt.title("Win chance if NO CHANGE")
plt.xlabel('Probability')
plt.ylabel('Frequency')

plt.show()