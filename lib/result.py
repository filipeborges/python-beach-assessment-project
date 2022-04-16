"""
Author: Elaine Baroni, Filipe Borges
Email: elaine.bo@hotmail.com, filipebkc2209@gmail.com
"""

# ======= private functions - dont need to be accessed on main.py ============
def __calculateSingleCategoryNormalizedResult(categoryIndicators):
    categoryIndicatorsSum = 0
    numberOfIndicators = len(categoryIndicators)

    for indicator, indicatorValue in categoryIndicators.items():
        categoryIndicatorsSum += categoryIndicators[indicator]
    categoryNormalizedResult = categoryIndicatorsSum / (numberOfIndicators * 5)
    return categoryNormalizedResult

def calculateCategoriesNormalizedResult(userInputDictionary, categoriesNormalizedResult):
    for domain, domainCategories in userInputDictionary.items():
        for category, categoryIndicators in domainCategories.items():
            categoriesNormalizedResult[domain][category] = __calculateSingleCategoryNormalizedResult(categoryIndicators)

# ======= public functions - accessed on main.py ============
def calculateDomainGrade(domainGrade, beachType, categoryWeight, categoriesNormalizedDictionary):
    selectedDomainCategoryDictionary = categoryWeight[beachType]
    for domain, domainCategoriesWeight in selectedDomainCategoryDictionary.items():
        domainResult = 0
        for category, _categoryWeightValue in domainCategoriesWeight.items():
            domainResult += categoryWeight[beachType][domain][category] * categoriesNormalizedDictionary[domain][category]
        domainGrade[domain] = domainResult

def calculateDomainIndexAndReturn(domainGradeDictionary, domainWeightDictionary, beachType):
    beachIndex = 0
    for domain, domainGradeValue in domainGradeDictionary.items():
        beachIndex += domainGradeValue * domainWeightDictionary[beachType][domain]
    return beachIndex