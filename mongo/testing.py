from mongo import mongo

post = {
"nonprofitId" : 12321415215,
"preferences" : [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
}

mongo = mongo("preferences", "nonprofit")
mongo.insert_one(post)
preferences = mongo.find({"nonprofitId" : 12321415215})
for i in preferences:
	print (i["preferences"])

mongo.change_collection("preferences")
preferences = mongo.find()
for i in preferences:
	print (i["preferences"])