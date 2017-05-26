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
           for x in range(length):
               distance += pow((trainingInstance[x] - testInstance[x]), 2)
           if distance == 0:
                   return 1
           else:
                   return 1- (math.sqrt(distance) *.1)
        



        def loadDataSet(self, dataValTotal, filename, trainingSet=[]):
                with open(filename, 'rb') as csvfile:
                    lines = csv.reader(csvfile)
                    dataset = list(lines)
                    for x in range(len(dataset)-1):
                        #change the range value depending on the amount of variables being considered
                       for y in range(dataValTotal):
                           dataset[x][y] = float(dataset[x][y])
                       trainingSet.append(dataset[x])
                self.training = trainingSet
                       


        def findNeighbors(self, k):
            distances = []
            for x in range(len(self.training)):
                arrIndex = x
                aff = feedTesting.euclideanDistance(self.training[x], self.testInstance, len(self.testInstance)-1)
                distances.append((self.training[x], aff))

            distances.sort(key=operator.itemgetter(1), reverse = True)
            neighbors = [[]]

            for x in range(k):
                neighbors[0].append(distances[0])
                distances.pop(0)
        
            #Finds the "2nd layer" of neighbors (1st edge)
            lengthNeigh = len(neighbors)

            tempDist = []
            for x in range(len(neighbors[0])):
               #Removes the previously declared neighbor values before
               for y in range(len(distances)):
                    #distUser = feedTesting.euclideanDistance(self.training[y], self.testInstance, len(self.testInstance)-1)
                    localAff = feedTesting.euclideanDistance(distances[y][0], neighbors[0][x][0], len(self.testInstance)-1)
                    completeAff = neighbors[0][x][1] * localAff

                    if x == 0:
                            distances[y] = (distances[y][0], localAff, completeAff, x, y)
                    else:
                            distances.append((distances[y][0], localAff, completeAff, x, y))

            distances.sort(key=operator.itemgetter(1), reverse = True)
               
            yIndex = []      
            for x in range(len(neighbors[0])):   
                    count = 0
                    index = 0

                    while count < k:
                        cont = True 
                        for i in range(len(yIndex)):
                                if distances[index][4] == yIndex[i]:
                                        cont = False
                        if distances[index][3] == x and cont == True:
                                tempDist.append(distances[index])
                                yIndex.append(distances[index][4])
                                
                                count += 1
                        index += 1
                                                        
            neighbors.append((tempDist))

            return neighbors
        
