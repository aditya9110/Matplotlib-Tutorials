import matplotlib.pyplot as plt
import numpy as np

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

width = 0.35
x = np.arange(len(labels))

plt.bar(x - width / 2, men_means, label='Men', color='b', width=width)
plt.bar(x + width / 2, women_means, label='Women', color='pink', width=width)

plt.xticks(ticks=x, labels=labels)
plt.ylabel('Scores')
plt.title('Men vs Women')
plt.legend()

plt.tight_layout()
plt.grid()
plt.show()
