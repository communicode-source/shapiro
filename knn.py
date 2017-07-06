import csv
import math
import operator

#CLASS START
class feedTesting:
        
        training = []
        testInstance = []

        def __init__(self, testInstance):
                self.testInstance = testInstance

#STATIC METHODS

        #sqr(sums of (differences squared))        
        @staticmethod
        def euclideanDistance(trainingInstance, testInstance, length):
                distance = 0
                for i in range(length):
                        distance += pow((trainingInstance[i] - testInstance[i]), 2)
                return 1- (math.sqrt(distance) *.1)

        """
        loadDataSet:
        Converts filename.data into a
        usable trainingSet array
        """
        def setTraining(self, dataset):
                temp = []
                for i in dataset:
                        temp.append(i["preferences"])
                self.training = temp

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

        def findNeighbors(self, k, edges):
                distances = []
                for x in range(len(self.training)):
                        arrIndex = x
                        aff = feedTesting.euclideanDistance(self.training[x], self.testInstance, len(self.testInstance)-1)
                        distances.append((self.training[x], aff))

                distances.sort(key=operator.itemgetter(1), reverse = True)
                neighbors = [[]]

                iterator = 0
                for i in range(k):
                        neighbors[0].append(distances[i])
                        distances[i] = None

                distancesOrig = distances
                yIndex = []         
                for i in range(edges):
                        newNeighbors = []
                        distances = []
                        
                        for j in range(len(neighbors[i])):
                                #Removes the previously declared neighbor values before
                                for x in range(len(distancesOrig)):
                                        #All distances for both neighbors are saved to the same array, just organized with an additional X value alongside their original Y index
                                        if distancesOrig[x] != None:
                                                localAff = feedTesting.euclideanDistance(distancesOrig[x][0], neighbors[i][j][0], len(self.testInstance)-1)
                                                if i == 0:
                                                        completeAff = neighbors[0][j][1] * localAff
                                                else:
                                                        completeAff = neighbors[i][j][2] * localAff
                                                distances.append((distancesOrig[x][0], localAff, completeAff, j, x))
        
                        distances.sort(key=operator.itemgetter(1), reverse = True)

                        #yIndex marks all already used distance values (reduces overlap)    
                        excludeIndexes = []
                        for j in range(len(neighbors[i])):
                                count = 0
                                index = 0

                                while count < k:
                                        
                                        cont = True
                                        for l in range(len(excludeIndexes)):
                                                if distances[index][4] == excludeIndexes[l]:
                                                        cont = False

                                        if distances[index][3] == j and cont == True:
                                                newNeighbors.append(distances[index])
                                                excludeIndexes.append(distances[index][4])
                                                distancesOrig[distances[index][4]] = None
                                                count += 1
                                        index += 1

                        neighbors.append((newNeighbors))

                return neighbors
        
