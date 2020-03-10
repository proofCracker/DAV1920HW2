import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = np.genfromtxt('data_2a.csv', delimiter=',')
labels = ['China', 'India', 'United States', 'Russian Federation', 'Japan']

def plot(population, labels, year):
    # build the plot
    fig, ax = plt.subplots()
    print(year)


    index = np.arange(len(labels))
    index_y = np.arange(8)*200000000
    labels_y = []
    for i in range(len(index_y)):
        labels_y.append(np.round((i)*0.2,1))

    plt.text(4.2, 1300000000.0, str(year), size=50,
             ha="right", va="top",
             bbox=dict(boxstyle="square",
                       ec=(1., 0.5, 0.5),
                       fc=(1., 0.8, 0.8),
                       )
             )

    plt.bar(index, population)
    plt.ylabel('Population [billion]')
    plt.xticks(index, labels, rotation=45)
    plt.title('Evolution of the populations of the most populous countries in 1960')
    plt.yticks(index_y, labels_y)
    plt.ylim(0, 1500000000)
    plt.tight_layout()
    plt.savefig('2a/' + str(year)  + '.png')
    plt.close(fig)


population = []
for i in range(59):
    for j in range(5):
        population.append(data[j][i])
    plot(population, labels, i+1960)
    population = []