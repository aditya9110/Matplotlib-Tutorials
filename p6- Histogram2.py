import matplotlib.pyplot as plt

blood_sugar_men = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
blood_sugar_women = [67, 98, 89, 120, 133, 150, 84, 69, 89, 79, 120, 112, 100]

bins = [80, 100, 125, 150]

type = [blood_sugar_men, blood_sugar_women]
color = ['b','pink']
labels = ['men', 'women']

plt.hist(type, color = color, label = labels, bins = bins, rwidth = 0.95,
         orientation = 'horizontal')

plt.ylabel('No of people')
plt.xlabel('Blood Sugar Range')
plt.legend()
plt.title('Blood Sugar Level Chart')
plt.show()
