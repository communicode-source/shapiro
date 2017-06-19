import csv
import math
import json

#CLASS START
class prefConv:

    collections = []
    categories = []
    binValues = []
    variables = []

    def __init__(self, collections, categories):
        prefConv.collections = collections
        prefConv.categories = categories

#STATIC METHODS

    #SUBJECT TO INEFFICENCIES
    @staticmethod
    def findExternalities(collections, collectionTitle, binaryValues):
        collectionVariables = []
        externality = 0

        #adds all of the variables within the given collection to the collectionVariables array
        for i in collections[collectionTitle]:
            for j in binaryValues["interests"]:
                if str(j) == i:
                    collectionVariables.append(i)
    ###########
        #begins the determinance of the externality quantities (future examinance of the process necessary)
        for i in collections:
            if i != collectionTitle:
                for j in collections[i]:
                    for k in range(len(collectionVariables)):
                        if collectionVariables[k] == j:
                            externality += collections[i][j]
        return math.sqrt(externality * .15)

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

    def weightsToVals(self, binValues):
        binValues = prefConv.loadJson(binValues)
        values = []

        #SUBJECT TO INEFFINCIES
        for i in self.collections:
            weight = 0
            for j in self.collections[i]:
                for k in binValues["interests"]:
                    if j == str(k):
                        weight += self.collections[i][j]
                        weight += prefConv.findExternalities(self.collections, i, binValues)
            values.append((i, weight))
        return values
