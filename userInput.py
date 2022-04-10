"""
Author: Elaine Baroni, Filipe Borges
Email: elaine.bo@hotmail.com, filipebkc2209@gmail.com
"""

import re

# private function - dont need to be accessed on main.py
def __isIndicatorValueInvalid(indicatorValue):
    regexValidator = re.compile('^[1-5]$')
    return not(bool(regexValidator.match(indicatorValue)))

# private function - dont need to be accessed on main.py
def __gatherCategoryValueFromUserInput(categoryIndicators, indicator):
    indicatorValue = __askAndCaptureUserIndicatorValue(indicator)

    while __isIndicatorValueInvalid(indicatorValue):
        print('Invalid indicator value. Valid values are 1 to 5')
        indicatorValue = __askAndCaptureUserIndicatorValue(indicator)

    categoryIndicators[indicator] = int(indicatorValue)

# private function - dont need to be accessed on main.py
def __askAndCaptureUserIndicatorValue(indicator):
    return input(indicator + '\n')

# public function - accessed on main.py
def captureUserInput(userInputDictionary):
    for domain, domainCategories in userInputDictionary.items():
        for category, categoryIndicators in domainCategories.items():
            for indicator, indicatorValue in categoryIndicators.items():
                __gatherCategoryValueFromUserInput(categoryIndicators, indicator)

# private function - dont need to be accessed on main.py
def __isBeachTypeValueInvalid(beachType):
    regexValidator = re.compile('^[1-2]$')
    return not(bool(regexValidator.match(beachType)))

# private function - dont need to be accessed on main.py
def __askAndCaptureBeachTypeValue():
    return input('Specify the type of the beach:\n1- Urban\n2- Natural\n')

def captureBeachTypeInputAndReturn():
    beachTypeDictionary = {
        '1': "Urban",
        '2': "Natural"
    }
    beachType = __askAndCaptureBeachTypeValue()
    while __isBeachTypeValueInvalid(beachType):
        print('Invalid beach type.\n')
        beachType = __askAndCaptureBeachTypeValue()
    return beachTypeDictionary[beachType]