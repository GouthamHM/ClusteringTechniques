import numpy as np
import random
import math
import operator
import copy
import matplotlib.pyplot as plt

class Kmeans(object):
    #Initialize Class variables
    def __init__(self,file_name,no_of_cluster):
        self.file_name = file_name
        self.k = no_of_cluster
        self.x = np.genfromtxt(self.file_name,delimiter=',')

    #Getter for Data Points
    def get_x_array(self):
        return self.x

    #Initialize first center
    def get_random_center(self):
        centers = np.zeros(shape = (self.k,self.x.shape[1]))
        print centers.shape
        for k in range(self.k):
            centers[k] =(self.x[random.randint(0,len(self.x)-1)])
        self.centers = centers
        return centers

    #Helperto find the euclidian distance between two points
    def _euclidian_distance(self,instance1, instance2):
        return math.sqrt(np.sum(np.square(instance1 - instance2)))

    #helper to find squared distance between 2 points
    def _square_distance(self,instance1, instance2):
        return np.sum(np.square(instance1 - instance2))

    # Assign clusters to each datapoint/instance
    def assign_clusters(self):
        clusters = {}
        for i in range(self.k):
            clusters[i]=[]
        for index, data_point in enumerate(self.x):
            center,value = min(enumerate(
                          [self._euclidian_distance(data_point,self.centers[i])
                           for i in range(self.k)]),key = operator.itemgetter(1))
            clusters[center].append(index)
        self.clusters = clusters

    # Finding the new center based on updated clusters
    def find_new_centers(self):
        for center in range(self.k):
            self.centers[center] = np.average(np.array([self.x[x] for x in self.clusters[center]]),axis=0 )

    #main function called to classify and obtain cost value
    def clusterify(self):
        self.get_random_center()
        i = 1
        while True:
            self.assign_clusters()
            centers = copy.deepcopy(self.centers)
            self.find_new_centers()
            i +=1
            if self.compare_centers(self.centers,centers):
                break
        return self.get_j()

    # Returns cost value
    def get_j(self):
        j = 0
        for k in range(self.k):
            center = self.centers[k]
            for data_point in self.clusters[k]:
                j += np.sum(self._square_distance(center,self.x[data_point]))
        return j

    #Compare centers to say wether the kmeans has convereged
    def compare_centers(self,c1,c2):
        return np.array_equal(c1,c2)

    def plot(self):
        plt.figure(figsize=(5, 5))
        colmap = ['red', 'blue', 'green', 'yellow', 'grey', 'saffron', 'cyan', 'magenta']
        for keys in self.clusters.keys():
            x_values = []
            y_values = []
            for data in self.clusters[keys]:
                x_values.append(k.x[data][0])
                y_values.append(k.x[data][1])
            plt.scatter(x_values, y_values, color=colmap[keys])
        plt.show()


if __name__ == '__main__':
    for i in range(2,11):
        k = Kmeans('kmeans_data.csv',i)
        print k.clusterify()

