binValues = {
    "interests" : [
        "environment1",
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
        "finance",
        "historical",
        "international
   ]
}

try:
    print binValues["interests"]

except KeyError:
    print "error"
