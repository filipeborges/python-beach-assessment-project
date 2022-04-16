"""
Author: Elaine Baroni, Filipe Borges
Email: elaine.bo@hotmail.com, filipebkc2209@gmail.com
"""

import re

# ======= private functions - dont need to be accessed on main.py ============
def __isIndicatorValueInvalid(indicatorValue):
    regexValidator = re.compile('^[1-5]$')
    return not(bool(regexValidator.match(indicatorValue)))

def __gatherCategoryValueFromUserInput(categoryIndicators, indicator):
    indicatorValue = __askAndCaptureUserIndicatorValue(indicator)

    while __isIndicatorValueInvalid(indicatorValue):
        print('Invalid indicator value. Valid values are 1 to 5')
        indicatorValue = __askAndCaptureUserIndicatorValue(indicator)

    categoryIndicators[indicator] = int(indicatorValue)

def __askAndCaptureUserIndicatorValue(indicator):
    return input(indicator + '\n')

def __isBeachTypeValueInvalid(beachType):
    regexValidator = re.compile('^[1-2]$')
    return not(bool(regexValidator.match(beachType)))

def __askAndCaptureBeachTypeValue():
    return input('Specify the type of the beach:\n1- Urban\n2- Natural\n')

def __isIndicatorValueNotSetted(value):
    return type(value) is int and value == 0

# ======= public functions - accessed on main.py ============
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

def captureUserInput(userInputDictionary):
    for domain, domainCategories in userInputDictionary.items():
        for category, categoryIndicators in domainCategories.items():
            for indicator, indicatorValue in categoryIndicators.items():
                if __isIndicatorValueNotSetted(indicatorValue):
                    __gatherCategoryValueFromUserInput(categoryIndicators, indicator)