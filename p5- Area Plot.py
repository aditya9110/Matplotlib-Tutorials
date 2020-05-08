from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

days = [1,2,3,4,5]

eat =   [1, 3, 4, 3, 2]
study = [8, 5, 6, 8, 10]
code =  [6, 8, 7, 4, 2]
sleep = [9, 8, 7, 9, 11]

labels = ['eat','study','code','sleep']

colors = ['#C70039', '#70B2FF', '#FFC300', '#DAF7A6']

plt.stackplot(days,eat,study,code,sleep, labels = labels, colors = colors)

plt.legend(loc = (0.7,0.7))
plt.title('Stack Plot')
plt.grid('True')
plt.tight_layout()
plt.show()
