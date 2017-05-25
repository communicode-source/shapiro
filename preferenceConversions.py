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
        for x in range(len(collections)):
            for y in range(1, len(collections[x])):
                if collections[x][0] == collectionTitle:
                    for j in range(len(binaryValues)):
                        if binaryValues[j][0] == collections[x][y][0] and binaryValues[j][1] == 1:
                            collectionVariables.append(collections[x][y][0])
    
        #begins the determinance of the externality quantities (future examinance of the process necessary)
        for x in range(len(collections)):
            for y in range(1, len(collections[x])):
                tempTitle = collections[x][y][0]
                for j in range(len(collectionVariables)):
                    if collections[x][0] != collectionTitle and collectionVariables[j] == collections[x][y][0]:
                        externality += collections[x][y][1]
        
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
        with open(filename, 'aw+') as file:
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
        for x in range(len(self.collections)):
            weight = 0
            for y in range(len(self.collections[x])-1):
                found = False
                pos = 1 + y
                index = 0

            
                for i in range(len(binValues)):
                    if self.collections[x][pos][0] == binValues[i][0]:
                        index = i
                weight += self.collections[x][pos][1] * binValues[index][1]
                weight += prefConv.findExternalities(self.collections, self.collections[x][0], binValues)
            values.append((self.collections[x][0], weight))
        return values
