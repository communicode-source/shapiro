import sys
sys.path.append("../")
import preferenceConversions, knn
from preferenceConversions import prefConv
from knn import feed
sys.path.append("../mongo")
from mongo import mongo
import json

#variables

collections = { 'environmentalism' : { 'environment' : .4,
                                       'wildlife' : .1,
                                       'preservation' : .1,
                                       'international' : .05,
                                       'health' : .05,
                                       'legal' : .05 },
                'human_services' : { 'human_services' : .25,
                                     'civil_rights' : .1,
                                     'youth_aid' : .05,
                                     'poverty_support' : .1,
                                     'food_services' : .05,
                                     'public_safety' : .15,
                                     'health' : .1,
                                     'legal' : .05 },
                'stem' : { 'science' : .15,
                           'engineering' : .15,
                           'technology' : .15,
                           'mathematics' : .15,
                           'internet' : .05,
                           'design' : .1,
                           'education' : .05,
                           'research' : .05 },
                'health' : { 'health' : .255,
                             'public_safety' : .2125,
                             'disease' : .1775,
                             'research' : .085,
                             'food_services' : .051,
                             'poverty_support' : .0595,
                             'youth_aid' : .0595 },
                'the_arts' : { 'arts_and_culture' : .3,
                               'religion' : .1,
                               'design' : .15,
                               'tv_and_media' : .15,
                               'youth_aid' : .15 },
                'education' : { 'education' : .2,
                                'science' : .0375,
                                'technology' : .0375,
                                'engineering' : .0375,
                                'mathematics' : .0375,
                                'arts_and_culture' : .1,
                                'athletics' : .1,
                                'youth_aid' : .2,
                                'historical' : .1 },
                'business' : { 'business_and_marketing' : .3,
                               'finance' : .2,
                               'fundraising' : .075,
                               'poverty_support' : .075,
                               'international' : .125,
                               'legal' : .075 },
                'urban_planning' : { 'urban_management' : .3,
                                     'construction' : .1,
                                     'parks_and_recreation' : .1,
                                     'poverty_support' : .05,
                                     'design' : .1,
                                     'public_safety' : .1,
                                     'engineering' : .05,
                                     'technology' : .05 },
                'international' : { 'international' : .3,
                                    'trade' : .15,
                                    'environment' : .075,
                                    'war_relief' : .1,
                                    'peace_efforts' : .075,
                                    'human_services' : .05 },
                'legal' : { 'legal' : .25,
                           'education' : .2,
                           'civil_rights' : .2,
                           'criminal' : .2 }
                }

categories = ["parks_and_recreation", "environment", "science", "wildlife", "preservation", "human_services",
              "civil_rights", "arts_and_culture", "education", "engineering", "mathematics", "technology",
              "food_services", "urban_management", "business_and_marketing", "international", "criminal", "athletics",
              "internet", "health", "public_safety", "youth_aid", "construction", "tv_and_media",
              "religion", "war_relief", "peace_efforts", "poverty_support", "legal", "design",
              "research", "disease", "fundraising", "finance", "trade", "historical"]

binValues = {
    "nonprofitId" : 132143213,
    "interests" : [
        "environment",
        "human_services",
        "civil_rights",
        "arts_and_culture",
        "urban_management",
        "business_and_marketing",
        "public_safety",
        "youth_aid",
        "construction",
        "tv_and_media",
        "religion",
        "fundraising",
        "science"
   ]
}

binValues = json.dumps(binValues)

testingTestInstance = {
  "preferences" : {
    'environmentalism' : 1,
    'human_services' : 0,
    'stem' : 0,
    'health' : 0,
    'the_arts' : 0,
    'education' : 0,
    'business' : 0,
    'urban_planning' : 0, 
    'international' : 0,
    'legal' : 1
    },
  "nonprofitId" : 123241
}

#preferenceConversion declaration and method calls
prefconv = prefConv(collections, binValues)
print("Binary Values\n")
print(binValues, "\n")

variables = prefconv.weightsToVals()
print("Converted Variables\n")
print(variables)

#prefConv.transferData("testfile.data", variables, "data.json")

mongo = mongo("test", "nonprofit")
mongo.insert_one(variables)
training = mongo.find()

#feedTesting declaration and method calls
feed = feed(testingTestInstance, training)
neighbors = feed.knn(k=5)
print("\nNeighbors\n")
for x in neighbors:
    print("NonprofitId: {}, Affinity: {}".format(x, neighbors[x]))
