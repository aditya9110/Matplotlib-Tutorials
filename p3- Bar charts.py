from matplotlib import pyplot as plt
import numpy as np

#print(plt.style.available)
plt.style.use('ggplot')

width = 0.25

year = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
indices = np.arange(len(year))

population_china = [1.359, 1.397, 1.403, 1.409, 1.415, 1.42, 1.424, 1.428, 1.431, 1.434]

population_india = [1.23, 1.309, 1.324, 1.339, 1.354, 1.368, 1.383, 1.397, 1.411, 1.445]


plt.bar(indices - width/2, population_india, width = width, label = 'India', color = 'blue')
plt.bar(indices + width/2, population_china, width = width, label = 'China', color = 'red')

plt.title('BarChart on Population')
plt.xlabel('Years')
plt.ylabel('Population in Billions')
plt.legend()

plt.xticks(ticks = indices, labels = year)

plt.grid(True)
plt.tight_layout()  #padding
plt.show()

