import csv
import math
import json

#CLASS START
class prefConv:

    collections = []
    interests = []
    variables = []

    def __init__(self, collections, interests):
        self.collections = collections
        self.interests = self.loadJson(interests)

#STATIC METHODS

    @staticmethod
    def loadJson(obj):
        jsonStr = obj.decode("utf-8")
        return json.loads(jsonStr)

    #variable transfer towards 'filename'
    @staticmethod
    def transferData(filename, variables, datafile):
        with open(filename, 'r+') as file:
            for i in range(len(variables)):
                file.write(str(variables[i][1])+", ")

    #SUBJECT TO INEFFICENCIES
    def findExternalities(self, collectionTitle):
        externality = 0
        collectionVariables = self.findCollectionVariables(collectionTitle)

        #begins the determinance of the externality quantities (future examinance of the process necessary)
        for i in self.collections:
            if i != collectionTitle:
                for j in self.collections[i]:
                    for k in range(len(collectionVariables)):
                        if collectionVariables[k] == j:
                            externality += self.collections[i][j]
        print  math.sqrt(externality * .15)
        return math.sqrt(externality * .15)

    
    #adds all of the variables within the given collection to the collectionVariables array
    def findCollectionVariables(self, collectionTitle):
        collectionVariables = []
        for variable in self.collections[collectionTitle]:
            for interest in self.interests["interests"]:
                if str(interest) == variable:
                    collectionVariables.append(variable)
        return collectionVariables


    def weightsToVals(self):
        values = []

        #SUBJECT TO INEFFINCIES
        for i in self.collections:
            weight = 0
            for j in self.collections[i]:
                for k in self.interests["interests"]:
                    if j == str(k):
                        weight += self.collections[i][j]
                        weight += self.findExternalities(i)
            values.append((i, weight))
        return values
