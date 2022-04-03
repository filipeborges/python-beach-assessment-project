"""
Author: Elaine Baroni, Filipe Borges
Email: elaine.bo@hotmail.com, filipebkc2209@gmail.com
"""

from userInput import *
from categoryNormalized import *

# TODO: Add remaining domains/categories
userInputDictionary = {  # userInputDictionary
    "Recreational": {  # domainCategories
        "Access & Parking": {  # categoryIndicators
            "Path to the beach": 0,  # indicator , #indicatorValue
            "Public transport": 0,
            "Access Road": 0,
            "Parking": 0,
            "Bicycle parking": 0,
        },
        "Carrying capacity": {
            "Carrying capacity": 0,
            "Beach Area": 0
        },
    }
}

# TODO: Add remaining domains/categories
categoriesNormalizedDictionary = {
    "Recreational": {
        "Access & Parking": 0,
        "Carrying capacity": 0
    }
}

# TODO: Add remaining domains/categories
categoryWeight = {
    "Urban": {
        "Recreational": {
            "Access & Parking": 0.222,
            "Carrying capacity": 0.098
        }
    },
    "Natural": {
        "Recreational": {
            "Access & Parking": 0.072,
            "Carrying capacity": 0.214
        }
    }
}

# TODO: Add remaining domains
domainWeight = {
    "Urban": {
        "Recreational": 0.4
    },
    "Natural": {
        "Recreational": 0.1
    }
}


captureUserInput(userInputDictionary)
print(str(userInputDictionary))

calculateCategoriesNormalizedResult(userInputDictionary, categoriesNormalizedDictionary)
print(str(categoriesNormalizedDictionary))
