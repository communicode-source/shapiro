import sys
sys.path.append("../")
import preferenceConversions, knn
from preferenceConversions import prefConv
from knn import feedTesting
import json

#variables
collections = [ ["environmentalism", ["environment", .4], ["wildlife", .1], ["preservation", .1], ["international", .05], ["health", .05], ["legal", .05] ],
                ["human_services", ["human_services", .25], ["civil_rights", .1], ["youth_aid", .05], ["poverty_support", .1], ["food_services", .05], ["public_safety", .15], ["health", .1], ["legal", .05] ],
                ["stem", ["science", .15], ["engineering", .15], ["technology", .15], ["mathematics", .15], ["internet", .05], ["design", .1], ["education", .05], ["research", .05] ],
                ["health", ["health", .255], ["public_safety", .2125], ["disease", .1775], ["research", .085], ["food_services", .051], ["poverty_support", .0595], ["youth_aid", .0595] ],
                ["the_arts", ["arts_and_culture", .3], ["religion", .1], ["design", .15], ["tv_and_media", .15], ["youth_aid", .15] ],
                ["education", ["education", .2], ["science", .0375], ["technology", .0375], ["engineering", .0375], ["mathematics", .0375], ["arts_and_culture", .1], ["athletics", .1], ["youth_aid", .2], ["historical", .1] ],
                ["business", ["business_and_marketing", .3], ["finance", .2], ["fundraising", .075], ["poverty_support", .075], ["international", .125], ["legal", .075] ],
                ["urban_planning", ["urban_management", .3], ["construction", .1], ["parks_and_recreation", .1], ["poverty_support", .05], ["design", .1], ["public_safety", .1], ["engineering", .05], ["technology", .05] ],
                ["international", ["international", .3], ["trade", .15], ["environment", .075], ["war_relief", .1], ["peace_efforts", .075], ["human_services", .05] ],
                ["legal", ["legal", .25], ["education", .2], ["civil_rights", .2], ["criminal", .2] ] ]

categories = ["parks_and_recreation", "environment1", "science", "wildlife", "preservation", "human_services",
              "civil_rights", "arts_and_culture", "education", "engineering", "mathematics", "technology",
              "food_services", "urban_management", "business_and_marketing", "international", "criminal", "athletics",
              "internet", "health", "public_safety", "youth_aid", "construction", "tv_and_media",
              "religion", "war_relief", "peace_efforts", "poverty_support", "legal", "design",
              "research", "disease", "fundraising", "finance", "trade", "historical"]

binValues = {
    "interests" : {
        "parks_and_recreation": "0",
        "environment1": "1",
        "science": "0",
        "wildlife": "0",
        "preservation": "0",
        "human_services": "1",
        "civil_rights": "1",
        "arts_and_culture": "1",
        "education": "0",
        "engineering": "0",
        "mathematics": "0",
        "technology": "0",
        "food_services": "0",
        "urban_management": "1",
        "business_and_marketing": "1",
        "international": "0",
        "criminal":  "0",
        "athletics": "0",
        "internet": "0",
        "health": "0",
        "public_safety": "1",
        "youth_aid": "1",
        "construction": "1",
        "tv_and_media": "1",
        "religion": "1",
        "war_relief": "0",
        "peace_efforts": "0",
        "poverty_support": "0",
        "legal": "0",
        "design": "0",
        "research": "0",
        "disease": "0",
        "fundraising": "1",
        "finance": "1",
        "trade": "0",
        "historical": "1"
    }
}

binValues = json.dumps(binValues)

"""
for a in binValues["interests"]:
    print a, binValues["interests"][a]"""

ran = 10
k = 2

testInstance = [0,0,0,0,0,0,0,0,0,0]

#preferenceConversion declaration and method calls
prefconv = prefConv(collections, categories)
print "Binary Values\n"
print binValues, "\n"

variables = prefconv.weightsToVals(binValues)
print "Converted Variables\n"
print variables

print prefConv.getNonprofitId("data.json")
prefConv.transferData("testfile.data", variables, "data.json")

#feedTesting declaration and method calls
feedtesting = feedTesting(testInstance)
feedtesting.loadDataSet(ran, 'testfile.data')
neighbors = feedtesting.findNeighbors(k, 2)
print "\nNeighbors\n"
for x in range(len(neighbors)):
    print neighbors[x], "\n"
