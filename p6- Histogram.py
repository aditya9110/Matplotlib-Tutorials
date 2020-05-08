import matplotlib.pyplot as plt

blood_sugar = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
#bins = 3   #bins are vertical columns in histogram and 3 is no of bins
bins = [80, 100, 125, 150]  #here bins are the points on x axis 80-100, 100-125, 125-150

plt.hist(blood_sugar, bins = bins, edgecolor = 'yellow', color = 'red', rwidth = 0.95, histtype = 'step')
#rwidth is width between two bins
#histtype provide only outline and in forms of steps
plt.show()
