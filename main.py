from kmeans import Kmeans
from kmeanspp import KmeansPP
import matplotlib.pyplot as plt

def plot_fig(x,y,file):
    plt.plot(x, y)
    plt.ylabel('J')
    plt.xlabel('k values')
    plt.savefig(file)
    plt.close()
if __name__ =='__main__':
    kmeans_val = []
    for i in range(2, 11):
        k = Kmeans('./data/kmeans_data.csv', i)
        kmeans_val.append(k.clusterify())
    plot_fig(range(2,11),kmeans_val,'./captures/kmeans.png')

    kmeans_pp = []
    for i in range(2, 11):
        k = Kmeans('./data/kmeans_data.csv', i)
        kmeans_pp.append(k.clusterify())
    plot_fig(range(2,11),kmeans_pp,'./captures/kmeanspp.png')



