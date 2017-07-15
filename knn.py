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
                for i in self.order:
                        distance += pow((trainingInstance[i] - testInstance[i]), 2)
                return 1- (math.sqrt(distance) *.1)

        """
        loadDataSet:
        Converts filename.data into a
        usable trainingSet array
        """

        def loadDataSet(self, dataValTotal, filename, trainingSet=[]):
                with open(filename, 'rb') as csvfile:
                        lines = csv.reader(csvfile)
                        dataset = list(lines)
                        for i in range(len(dataset)-1):
                                #change the range value depending on the amount of variables being considered
                                for j in range(dataValTotal):
                                        dataset[i][j] = float(dataset[i][j])
                                trainingSet.append(dataset[i])
                self.training = trainingSet
                       
        """
        Finds "k" amount of neighbors using
        data from self.training and self.testInstance. 
        By utilizing the euclideanDistance method, the knn
        function can accurately determine the local affinity
        between the testInstance and the trainingInstance, allowing
        for useful results.
        """

        def knn(self, k, distances = {}):
                for x in self.training:
                        distances[x["nonprofitId"]] = self.euclideanDistance(x["preferences"], self.testInstance["preferences"])

                sortedDistances = sorted(distances.items(), key=operator.itemgetter(1), reverse = True)

                neighbors = dict(sortedDistances[0:k])

                return neighbors

        
