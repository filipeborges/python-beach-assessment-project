from lib.file import deleteSavedUserInput, loadSavedBeachName, initializeUserInputDictionary, loadBeachesIndexesResult, loadSavedUserInputDictionary, saveFinalResult, saveUserInput
from lib.result import calculateCategoriesNormalizedResult, calculateDomainGrade, calculateDomainIndexAndReturn, printBeachIndexRanking, printFinalBeachIndex
from lib.signalHandler import initializeEndProgramHandler
from lib.userInput import captureBeachNameAndReturn, captureBeachTypeInputAndReturn, captureCategoriesIndicatorValue, clearTerminal, captureIndicatorValueAndUpdate, isValueMatchedOnRegex, printAssessInitialMessage, captureValue, captureGenericDataValueAndReturn

userInputDictionary = {
    "Recreational": {
        "Access & Parking": {
            "Path to the beach": 0,
            "Public transport": 0,
            "Access Road": 0,
            "Parking": 0,
            "Bicycle parking": 0,
        },
         "Carrying capacity": {
            "Availability of sand by user": 0,
        },
        "Facilities & Services": {
            "Umbrellas and chairs": 0,
            "Dinning facilities": 0,
            "Adaptations for disabled users": 0,
            "Facilities for children": 0,
            "Showers": 0,
            "Sports facilities": 0,
        },
        "Scenic Value": {
            "Color of Sand": 0,
            "Color of Water": 0,
            "Skyline": 0,
            "Vegetation cover": 0,
            "Coastal Features": 0,
            "Water clarity": 0,
            "Vista": 0,
        },
        "Safety": {
            "Lifeguards": 0,
            "Signposting": 0,
            "Dangerous animals (jellyfish, sharks)": 0,
            "Dangerous cliffs": 0,
            "Pickpockets & crime": 0,
            "Wave regime risk": 0,
            "Rip Currents": 0,
            "Rescue material": 0,
            "Zoning of activities (e.g.bathing, surfing)": 0,
        },
    },
    "Protection": {
        "Storm Buffer": {
            "Beach Width": 0,
            "Beach slope": 0,
            "Dune type": 0,
        },
        "Shoreline Stability": {
            "Vulnerability to erosion": 0,
            "Dune condition": 0,
            "Sediment budget ": 0,
            "Hard coastal defence": 0,
        },
        "Induced Changes": {
            "Impervious surface": 0,
            "Changes in grain size": 0,
            "Changes in volume (nourishment)": 0,
        },
        "Energy dissipation": {
            "Bathing area protection": 0,
            "Bathing area material": 0,
            "Morphodynamic state": 0,
        },
        "Hazard": {
            "Harmful storms": 0,
            "Sea level rise": 0,
            "Natural disaster": 0,
            "Exposure to waves": 0,
        },
    },
    "Conservation": {
        "Environmental quality": {
            "Noise": 0,
            "Degree of urbanization": 0,
            "Air quality": 0,
            "Concentration of Nutrients": 0,
        },
        "Management Actions": {
            "Restrictions & Regulations": 0,
            "Protected areas": 0,
            "Environmental Educational": 0,
        },
        "Habitat": {
            "Ecosystem connectivity": 0,
            "Ecosystem condition": 0,
        },
        "Species": {
            "Diversity & Abundance": 0,
            "Endangered and iconic": 0,
            "Invasive species ": 0,
        },
        "Heritage": {
            "Geological interest": 0,
            "Historic, archaeological, cultural & scientific interest": 0,
        },
    },
    "Sanitary": {  
        "Water quality": {
            "Sewage discharge evidence": 0,
            "Microbiological water quality": 0,
        },
        "Sand quality": {
            "Accumulation of marine debris/macroalgae": 0,
            "Unpleasant Odors": 0,
            "Feaces on the sand": 0,
        },
        "Episodic Pollution": {
            "Blooms": 0,
            "Oil spills": 0,
        },
        "Sanitary facilities & Services": {
            "Cleaning of the beach": 0,
            "Litter bins": 0,
            "Toilet provision": 0,
        },
        "Litter & Waste": {
            "Floating debris/litter": 0,
            "Solid human waste": 0,
            "Oil & tar balls": 0,
        },
    }
}

categoriesNormalizedDictionary = {
    "Recreational": {
        "Access & Parking": 0,
        "Carrying capacity": 0,
        "Facilities & Services": 0,
        "Scenic Value": 0,
        "Safety": 0
    },
    "Protection": {
        "Storm Buffer": 0,
        "Shoreline Stability": 0,
        "Induced Changes": 0,
        "Energy dissipation": 0, 
        "Hazard": 0,
    },
    "Conservation": {
        "Environmental quality": 0,
        "Management Actions": 0,
        "Habitat": 0,
        "Species": 0,
        "Heritage": 0,
    },
    "Sanitary": {  
        "Water quality": 0,
        "Sand quality": 0,
        "Episodic Pollution": 0,
        "Sanitary facilities & Services": 0,
        "Litter & Waste": 0,
    }
}

categoryWeight = {
    "Urban": {
        "Recreational": {
            "Access & Parking": 0.222,
            "Carrying capacity": 0.098,
            "Facilities & Services": 0.365,
            "Scenic Value": 0.051,
            "Safety": 0.264
        },
        "Protection": {
            "Storm Buffer": 0.334,
            "Shoreline Stability": 0.274,
            "Induced Changes": 0.192,
            "Energy dissipation": 0.086, 
            "Hazard": 0.114,
        },
        "Conservation": {
            "Environmental quality": 0.411,
            "Management Actions": 0.311,
            "Habitat": 0.114,
            "Species": 0.087,
            "Heritage": 0.077,
        },
        "Sanitary": {  
            "Water quality": 0.333,
            "Sand quality": 0.167,
            "Episodic Pollution": 0.167,
            "Sanitary facilities & Services": 0.167,
            "Litter & Waste": 0.167,
        }
    },
    "Natural": {
        "Recreational": {
            "Access & Parking": 0.072,
            "Carrying capacity": 0.214,
            "Facilities & Services": 0.047,
            "Scenic Value": 0.393,
            "Safety": 0.274
        },
        "Protection": {
            "Storm Buffer": 0.404,
            "Shoreline Stability": 0.266,
            "Induced Changes": 0.176,
            "Energy dissipation": 0.086, 
            "Hazard": 0.069,
        },
        "Conservation": {
            "Environmental quality": 0.116,
            "Management Actions": 0.081,
            "Habitat": 0.368,
            "Species": 0.368,
            "Heritage": 0.067,
        },
        "Sanitary": {  
            "Water quality": 0.316,
            "Sand quality": 0.146,
            "Episodic Pollution": 0.134,
            "Sanitary facilities & Services": 0.062,
            "Litter & Waste": 0.342,
        }
    }
}

domainWeight = {
        "Urban": {
            "Recreational": 0.4,
            "Protection": 0.2,
            "Conservation": 0.1,
            "Sanitary": 0.4
        },
        "Natural": {
            "Recreational": 0.1,
            "Protection": 0.1,
            "Conservation": 0.5,
            "Sanitary": 0.3
        }
    }

domainGrade = {
    "Recreational": 0,
    "Protection": 0,
    "Conservation": 0,
    "Sanitary": 0
}

beachType = {
    1: "Urban",
    2: "Natural"
}

# ======= private functions ============

def __buildEditValueTuple(dictionary):
    currentIndex = 1
    valueToEditDictionaryWithIntKey = {}
    for key, value in dictionary.items():
        valueToEditDictionaryWithIntKey[currentIndex] = key
        currentIndex += 1
    return valueToEditDictionaryWithIntKey, str(currentIndex - 1)

def __askDomainAndReturn(savedUserInputDictionary):
    domainToEditTuple = __buildEditValueTuple(savedUserInputDictionary)
    domainToEditDictionaryWithIntKey = domainToEditTuple[0]
    return captureGenericDataValueAndReturn(
        dataSelectionQuestion = 'Inform the domain you want:\n',
        dataDictionaryWithIntKey = domainToEditDictionaryWithIntKey
    )

def __askCategoryAndReturn(categoriesDictionary, selectedDomain):
    selectedDomainMessage = "'" + selectedDomain + "'"
    categoryToEditTuple = __buildEditValueTuple(categoriesDictionary)
    categoryToEditDictionary = categoryToEditTuple[0]
    return captureGenericDataValueAndReturn(
        dataSelectionQuestion = 'Inform the category you want on domain ' + selectedDomainMessage + ':\n',
        dataDictionaryWithIntKey = categoryToEditDictionary
    )

def __askIndicatorAndReturn(categoryIndicatorsDictionary, selectedDomain, selectedCategory):
    selectedDomainMessage = "'" + selectedDomain + "'"
    selectedCategoryMessage = "'" + selectedCategory + "'"
    categoryIndicatorToEditTuple = __buildEditValueTuple(categoryIndicatorsDictionary)
    categoryIndicatorToEditDictionary = categoryIndicatorToEditTuple[0]
    return captureGenericDataValueAndReturn(
        dataSelectionQuestion = 'Inform the indicator you want on domain ' + selectedDomainMessage + ' and category ' + selectedCategoryMessage + ':\n',
        dataDictionaryWithIntKey = categoryIndicatorToEditDictionary
    )

def __captureEditValueAndReturn():
    value = captureValue(
        'Inform if you want to edit it\'s current value (1- Yes, 2- No):\n',
        '^[1-2]$',
        'Invalid option informed. Valid values are 1 or 2'
    )
    return int(value)

def __showCategoryIndicatorCurrentValue(selectedCategoryIndicator, currentCategoryIndicatorValue):
    print('Current value for \'' + selectedCategoryIndicator + '\': ' + str(currentCategoryIndicatorValue) + '\n')

def __showOrUpdateSavedUserInput(beachName, savedUserInputDictionary, selectedDomain, selectedCategory, selectedCategoryIndicator):
    indicatorToEdit = selectedDomain + ' / ' + selectedCategory + ' / ' + selectedCategoryIndicator
    currentCategoryIndicatorValue = savedUserInputDictionary[selectedDomain][selectedCategory][selectedCategoryIndicator]
    clearTerminal()
    if currentCategoryIndicatorValue == 0:
        print('You had not setted value for \'' + indicatorToEdit + '\'')
    else:
        __showCategoryIndicatorCurrentValue(indicatorToEdit, currentCategoryIndicatorValue)
        selectedOption = __captureEditValueAndReturn()
        if selectedOption == 1:
            captureIndicatorValueAndUpdate(savedUserInputDictionary[selectedDomain][selectedCategory], selectedCategoryIndicator)
            saveUserInput(savedUserInputDictionary, beachName)

# ======= public functions  ============

def assessBeach():
    global userInputDictionary, categoriesNormalizedDictionary, categoryWeight, domainWeight, domainGrade, beachType

    beachName = captureBeachNameAndReturn(loadSavedBeachName())

    userInputDictionary = initializeUserInputDictionary(userInputDictionary)

    clearTerminal()

    printAssessInitialMessage(beachName)

    initializeEndProgramHandler(userInputDictionary, beachName)

    captureCategoriesIndicatorValue(userInputDictionary)

    calculateCategoriesNormalizedResult(userInputDictionary, categoriesNormalizedDictionary)

    selectedBeachType = captureBeachTypeInputAndReturn(beachType)

    calculateDomainGrade(domainGrade, selectedBeachType, categoryWeight, categoriesNormalizedDictionary)

    beachIndex = calculateDomainIndexAndReturn(domainGrade, domainWeight, selectedBeachType)

    deleteSavedUserInput()

    saveFinalResult(beachName, beachIndex, domainGrade)

    printFinalBeachIndex(beachName, beachIndex)

def printRanking():
    printBeachIndexRanking(loadBeachesIndexesResult())

def editCurrentValue():
    savedUserInputDictionary = loadSavedUserInputDictionary()
    if savedUserInputDictionary != None:
        beachName = loadSavedBeachName()
        selectedDomain = __askDomainAndReturn(savedUserInputDictionary)
        selectedCategory = __askCategoryAndReturn(
            categoriesDictionary = savedUserInputDictionary[selectedDomain],
            selectedDomain = selectedDomain
        )
        selectedCategoryIndicator = __askIndicatorAndReturn(
            categoryIndicatorsDictionary = savedUserInputDictionary[selectedDomain][selectedCategory],
            selectedDomain = selectedDomain,
            selectedCategory = selectedCategory
        )
        __showOrUpdateSavedUserInput(beachName, savedUserInputDictionary, selectedDomain, selectedCategory, selectedCategoryIndicator)
    else:
        print('You don\'t have any beach assessment in progress!')