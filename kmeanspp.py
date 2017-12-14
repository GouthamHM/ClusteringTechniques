import numpy as np
import random
import math
import operator
import copy


class KmeansPP():
    def __init__(self,file_name,no_of_cluster):
        self.file_name = file_name
        self.k = no_of_cluster
        self.x = np.genfromtxt(self.file_name,delimiter=',')

    #Getter for Data Points
    def get_x_array(self):
        return self.x

    #Finding the minimum distance for each points from the centers
    def get_d2(self):
        self.D2 = np.array([min([self._square_distance(center,x) for center in self.centers])for x in self.x])

    def get_next_center(self):
        probs = self.D2/self.D2.sum()
        probs.sort()
        cumprobs = probs.cumsum()
        cumprobs.sort()
        r = random.random()
        index = np.where(cumprobs >= r)[0][0]
        return (self.x[index])

        # dice_roll = np.random.rand()
        # min_over_roll = probs[probs.cumsum() >= dice_roll].min()
        # index = np.where(min_over_roll== min_over_roll)[0][0]

    #Initialize first center
    def get_initial_centers(self):
        centers = np.zeros(shape = (self.k,self.x.shape[1]))
        self.centers = centers
        print centers.shape
        #Set a random Center as 1st center
        self.centers[0] =(self.x[random.randint(0,len(self.x)-1)])
        for i in range(1,self.k):
            self.get_d2()
            self.centers[i] = self.get_next_center()

        return self.centers

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
        self.get_initial_centers()
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

if __name__ == '__main__':
    for i in range(2,11):
        k = KmeansPP('kmeans_data.csv',i)
        print k.clusterify()