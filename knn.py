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

#STATIC METHODS

        #sqr(sums of (differences squared))        
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
        Finds neighbors(under the k value) with the testInstance
        provided via the constructor. First edge removes (pops)
        the given index value from the distances array. When the
        second edge arrives, a method of index recording/ignoring
        is used due to inefficiencies with index popping.
        """

        def knn(self, k, distances = {}):

                for x in self.training:
                        trainingInstance = x["preferences"]
                        distances[x["nonprofitId"]] = self.euclideanDistance(trainingInstance, self.testInstance["preferences"])

                sortedDistances = sorted(distances.items(), key=operator.itemgetter(1), reverse = True)

                neighbors = dict(sortedDistances[0:k])

                return neighbors

        
