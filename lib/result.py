"""
Author: Elaine Baroni, Filipe Borges
Email: elaine.bo@hotmail.com, filipebkc2209@gmail.com
"""

from string import Template

# ======= private functions ============

def __calculateSingleCategoryNormalizedResult(categoryIndicators):
    categoryIndicatorsSum = 0
    numberOfIndicators = len(categoryIndicators)

    for indicator, indicatorValue in categoryIndicators.items():
        categoryIndicatorsSum += categoryIndicators[indicator]
    categoryNormalizedResult = categoryIndicatorsSum / (numberOfIndicators * 5)
    return categoryNormalizedResult

def __printIndexRanking(sortedBeachRankingByIndex):
    isEmptyRanking = len(sortedBeachRankingByIndex) == 0
    if isEmptyRanking:
        print("You should assess at least one beach first!")
    else:
        rankingTitle = """
------------------------------------------
|         Beach ranking by index         |
------------------------------------------
"""
        rankingLineTemplate = Template('$beachName: $index')
        print(rankingTitle)
        for beachName, index in sortedBeachRankingByIndex.items():
            roundedIndex = __roundBeachIndex(index)
            print(rankingLineTemplate.substitute(beachName=beachName, index=roundedIndex))

def __roundBeachIndex(beachIndex):
    return round(beachIndex, 2)

# ======= public functions ============

def printFinalBeachIndex(beachName, beachIndex):
    print('Beach \'' + beachName + '\' assesment complete. The beach index is: ' + str(__roundBeachIndex(beachIndex)))

def calculateDomainGrade(domainGrade, beachType, categoryWeight, categoriesNormalizedDictionary):
    selectedDomainCategoryDictionary = categoryWeight[beachType]
    for domain, domainCategoriesWeight in selectedDomainCategoryDictionary.items():
        domainResult = 0
        for category, _categoryWeightValue in domainCategoriesWeight.items():
            domainResult += _categoryWeightValue * categoriesNormalizedDictionary[domain][category]
        domainGrade[domain] = domainResult

def calculateDomainIndexAndReturn(domainGradeDictionary, domainWeightDictionary, beachType):
    beachIndex = 0
    for domain, domainGradeValue in domainGradeDictionary.items():
        beachIndex += domainGradeValue * domainWeightDictionary[beachType][domain]
    return beachIndex

def calculateCategoriesNormalizedResult(userInputDictionary, categoriesNormalizedResult):
    for domain, domainCategories in userInputDictionary.items():
        for category, categoryIndicators in domainCategories.items():
            categoriesNormalizedResult[domain][category] = __calculateSingleCategoryNormalizedResult(categoryIndicators)

def printBeachIndexRanking(beachesIndexes):
    def extractBeachIndexValue(beachIndexDataTuple):
        return beachIndexDataTuple[1]
    sortedBeachRankingByIndex = dict(sorted(beachesIndexes.items(), key=extractBeachIndexValue, reverse=True))
    __printIndexRanking(sortedBeachRankingByIndex)