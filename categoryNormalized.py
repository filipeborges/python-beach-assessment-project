"""
Author: Elaine Baroni, Filipe Borges
Email: elaine.bo@hotmail.com, filipebkc2209@gmail.com
"""

# private function - dont need to be accessed on main.py
def __calculateSingleCategoryNormalizedResult(categoryIndicators):
    categoryIndicatorsSum = 0
    numberOfIndicators = len(categoryIndicators)

    for indicator, indicatorValue in categoryIndicators.items():
        categoryIndicatorsSum += categoryIndicators[indicator]
    categoryNormalizedResult = categoryIndicatorsSum / (numberOfIndicators * 5)
    return categoryNormalizedResult

# public function - accessed on main.py
def calculateCategoriesNormalizedResult(userInputDictionary, categoriesNormalizedResult):
    for domain, domainCategories in userInputDictionary.items():
        for category, categoryIndicators in domainCategories.items():
            categoriesNormalizedResult[domain][category] = __calculateSingleCategoryNormalizedResult(categoryIndicators)