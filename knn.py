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

        def findNeighbors(self, k):
                distances = []
                for x in range(len(self.training)):
                        arrIndex = x
                        aff = feedTesting.euclideanDistance(self.training[x], self.testInstance, len(self.testInstance)-1)
                        distances.append((self.training[x], aff))

                distances.sort(key=operator.itemgetter(1), reverse = True)
                neighbors = [[]]

                for range(k):
                        neighbors[0].append(distances[0])
                        distances.pop(0)
        
                #2nd Edge
                tempDist = []
                for i in range(len(neighbors[0])):
                #Removes the previously declared neighbor values before
                        for j in range(len(distances)):
                                #All distances for both neighbors are saved to the same array, just organized with an additional X value alongside their original Y index
                                localAff = feedTesting.euclideanDistance(distances[j][0], neighbors[0][i][0], len(self.testInstance)-1)
                                completeAff = neighbors[0][i][1] * localAff
                        
                                #replaces the previously declared distance variables from the first edge
                                if i == 0:
                                        distances[j] = (distances[j][0], localAff, completeAff, i, j)
                                #appends to the distances array as the second round of neighboring
                                else:
                                        distances.append((distances[j][0], localAff, completeAff, i, j))
        
                distances.sort(key=operator.itemgetter(1), reverse = True)

                #yIndex marks all already used distance values (reduces overlap)   
                yIndex = []      
                for i in range(len(neighbors[0])):
                        count = 0
                        index = 0

                        while count < k:
                                cont = True 
                                for j in range(len(yIndex)):
                                        if distances[index][4] == yIndex[j]:
                                                cont = False
                                if distances[index][3] == i and cont == True:
                                        tempDist.append(distances[index])
                                        yIndex.append(distances[index][4])
                                
                                        count += 1
                                index += 1

                neighbors.append((tempDist))

            return neighbors
        
