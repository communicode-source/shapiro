import csv
import math
import operator

#CLASS START
class feed:
    
    """
    GLOBAL VARIABLES: 
    order - List
    training - Dict
    testInstance - Dict
    """

    def __init__(self, testInstance, training, order):
        self.order = order
        self.training = training
        self.testInstance = testInstance

   
    def euclideanDistance(self, trainingInstance, testInstance):
        distance = 0
        for collection in self.order:
                distance += pow((trainingInstance[collection] - testInstance[collection]), 2)
        return 1 - (math.sqrt(distance) *.1)
                   
    """
    Finds "k" amount of neighbors using
    data from self.training and self.testInstance. 
    By utilizing the euclideanDistance method, the knn
    function can accurately determine the local affinity
    between the testInstance and the trainingInstance, allowing
    for useful results.
    """

    def knn(self, k, distances = {}):
        for trainingInstance in self.training:
            distances[trainingInstance["nonprofitId"]] = self.euclideanDistance(trainingInstance["preferences"], self.testInstance["preferences"])

        sortedDistances = sorted(distances.items(), key=operator.itemgetter(1), reverse = True)

        neighbors = dict(sortedDistances[0:k])

        return neighbors

    
