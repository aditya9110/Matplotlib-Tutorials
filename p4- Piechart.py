from matplotlib import pyplot as plt
#print(plt.style.available)
plt.style.use('ggplot')

slices = [1433783686, 1366417754, 329064917, 270625568, 216565318]
labels = ['China', 'India', 'United States', 'Indonesia', 'Pakistan']
explode = [0,0.1,0,0.2,0]
colors = ['#C70039', '#70B2FF', '#FFC300', '#DAF7A6', '#FF5733']

plt.pie(slices, labels = labels, explode = explode, colors = colors,
        startangle = 90,autopct = '%1.1f%%',
        wedgeprops = {'edgecolor':'black','linewidth':1})

plt.title('Population Pie Chart')
plt.grid(True)
plt.tight_layout()
plt.show()
