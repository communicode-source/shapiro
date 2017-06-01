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
        for i in range(len(collections)):
            for j in range(1, len(collections[i])):
                if collections[i][0] == collectionTitle:
                    for k in range(len(binaryValues)):
                        if binaryValues[k][0] == collections[i][j][0] and binaryValues[k][1] == 1:
                            collectionVariables.append(collections[i][j][0])
    
        #begins the determinance of the externality quantities (future examinance of the process necessary)
        for i in range(len(collections)):
            for j in range(1, len(collections[i])):
                tempTitle = collections[i][j][0]
                for k in range(len(collectionVariables)):
                    if collections[i][0] != collectionTitle and collectionVariables[k] == collections[i][j][0]:
                        externality += collections[i][j][1]
        
        return math.sqrt(externality * .15)

    #returns nonprofitId from json
    @staticmethod
    def getNonprofitId(filename):
        with open(filename) as data_file:
            data = json.load(data_file)
        return data["nonprofit"]["info"]["nonprofitId"]

    #variable transfer towards 'filename'
    @staticmethod
    def transferData(filename, variables, datafile):
        with open(filename, 'r+') as file:
            for i in range(len(variables)):
                file.write(str(variables[i][1])+", ")
            file.write(prefConv.getNonprofitId("data.json")+"\n")



    # Variable -> BinVal (['variable', BinVal])
    def binValues(self, filename):
        binValues = []
        with open(filename) as data_file:
            data = json.load(data_file)
            for i in range(len(self.categories)):
                temp = data["nonprofit"]["preferences"][self.categories[i]]["binValue"]
                binValues.append((self.categories[i],int(temp)))
        return binValues


    def weightsToVals(self, binValues):
        values = []

        #SUBJECT TO INEFFINCIES
        for i in range(len(self.collections)):
            weight = 0
            for j in range(1, len(self.collections[i])-1):
                found = False
                index = 0

            
                for k in range(len(binValues)):
                    if self.collections[i][j][0] == binValues[k][0]:
                        index = i
                weight += self.collections[i][j][1] * binValues[index][1]
                weight += prefConv.findExternalities(self.collections, self.collections[i][0], binValues)
            values.append((self.collections[i][0], weight))
        return values
