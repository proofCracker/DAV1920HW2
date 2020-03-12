import matplotlib.pyplot as plt
import numpy as np

# import data
# randomly generated year for Poland: 1971
data = np.genfromtxt('data/data_C.csv', delimiter=',')
# countries closest to Poland in 1971
# ascending order in terms of population
labels = ['Poland', 'Korea, Rep.', 'Spain', 'Egypt, Arab Rep.', 'Turkey']

def plot(population, labels, year, colors):
    # build the plot
    fig, ax = plt.subplots()

    index = np.arange(len(labels))
    index_y = np.arange(11)*10000000
    labels_y = []
    for i in range(len(index_y)):
        labels_y.append(np.round((i)*10,1))

    plt.text(0.75, 93000000.0, str(year), size=30,
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
              'similar population-wise to Poland in 1971')
    plt.yticks(index_y, labels_y)
    plt.ylim(0, 105000000)
    plt.tight_layout()
    plt.savefig('C/' + str(year)  + '.png')
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
