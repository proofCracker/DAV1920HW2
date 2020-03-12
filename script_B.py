import matplotlib.pyplot as plt
import numpy as np

# import data
# randomly generated country and year: Hong Kong, 1985
data = np.genfromtxt('data/data_B.csv', delimiter=',')
# countries closest to Hong Kong
# ascending order in terms of population
labels = ['South Sudan', 'Denmark', 'Slovak Republic', 'Guinea', 'Hong Kong']

def plot(population, labels, year, colors):
    # build the plot
    fig, ax = plt.subplots()
    print(year)

    index = np.arange(len(labels))
    index_y = np.arange(10)*1500000
    labels_y = []
    for i in range(len(index_y)):
        labels_y.append(np.round((i)*1.5,1))

    plt.text(0.75, 12500000.0, str(year), size=30,
             ha="right", va="top",
             bbox=dict(boxstyle="square",
                       ec=(1., 0.5, 0.5),
                       fc=(1., 0.8, 0.8),
                       )
             )

    plt.bar(index, population, color=colors)
    plt.ylabel('Population [million]')
    plt.xticks(index, labels, rotation=45)
    plt.title('Evolution of the populations of countries that were the most \n' +
              'similar population-wise to Hong Kong in 1984')
    plt.yticks(index_y, labels_y)
    plt.ylim(0, 14000000)
    plt.tight_layout()
    plt.savefig('B/' + str(year)  + '.png')
    plt.close(fig)

# lists for sorting plot bars in ascending order
colors = ['dodgerblue', 'orchid', 'green', 'darkorange', 'brown']
population = []
indices = []
sorted_pop = []
sorted_lab = []
sorted_col = []

for i in range(59):
    for j in range(5):
        population.append(data[j][i])

    indices = np.argsort(population)
    for k in range(len(indices)):
        sorted_pop.append(population[indices[k]])
        sorted_lab.append(labels[indices[k]])
        sorted_col.append(colors[indices[k]])

    plot(sorted_pop, sorted_lab, i+1960, sorted_col)

    population = []
    sorted_pop = []
    sorted_lab = []
    sorted_col = []