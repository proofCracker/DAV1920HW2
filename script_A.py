import matplotlib.pyplot as plt
import numpy as np

# import data
data = np.genfromtxt('data/data_A.csv', delimiter=',')
# most populous countries in 1960
# ascending order in terms of population
labels = ['China', 'India', 'United States', 'Russian Federation', 'Japan']

def plot(population, labels, year, colors):
    # build the plot
    fig, ax = plt.subplots()

    index = np.arange(len(labels))
    index_y = np.arange(8)*200000000
    labels_y = []
    for i in range(len(index_y)):
        labels_y.append(np.round((i)*0.2,1))

    plt.text(0.75, 1350000000.0, str(year), size=30,
             ha="right", va="top",
             bbox=dict(boxstyle="square",
                       ec=(1., 0.5, 0.5),
                       fc=(1., 0.8, 0.8),
                       )
             )

    plt.bar(index, population, color=colors)
    plt.ylabel('Population [billion]')
    plt.xticks(index, labels, rotation=45)
    plt.title('Evolution of the populations of the most populous countries in 1960')
    plt.yticks(index_y, labels_y)
    plt.ylim(0, 1500000000)
    plt.tight_layout()
    plt.savefig('A/' + str(year)  + '.png')
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