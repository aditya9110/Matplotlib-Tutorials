from matplotlib import pyplot as plt

#print(plt.style.available)
plt.style.use('ggplot')

year = [1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2016, 2017, 2018,
        2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]

population_china = [0.55, 0.61, 0.65, 0.72, 0.82, 0.92, 0.99, 1.07, 1.172, 1.239, 1.283, 1.321, 1.359, 1.397,
                    1.403, 1.409, 1.415, 1.42, 1.424, 1.428, 1.431, 1.434, 1.436, 1.438, 1.44,
                    1.441, 1.441, 1.441, 1.441]

population_india = [0.376, 0.409, 0.449, 0.497, 0.553, 0.621, 0.696, 0.781, 0.87, 0.96, 1.053, 1.144, 1.23,
                    1.309, 1.324, 1.339, 1.354, 1.368, 1.383, 1.397, 1.411, 1.425, 1.438, 1.451, 1.464,
                    1.477, 1.489, 1.501, 1.512]


plt.subplot(1,2,1)
plt.plot(year, population_china, color = 'red', label = 'China')
plt.title('Subplot 1')
plt.xlabel('year')
plt.ylabel('Population in Billions')
plt.legend()

plt.subplot(1,2,2)
plt.plot(year, population_india, color = 'blue', label = 'India')
plt.title('Subplot 2')
plt.xlabel('year')
plt.ylabel('Population in Billions')
plt.legend()

plt.grid(True)
plt.tight_layout()  #padding
plt.show()
