"""
Author: Elaine Baroni, Filipe Borges
Email: elaine.bo@hotmail.com, filipebkc2209@gmail.com
"""

import re
import os

END_ASSESSMENT_MESSAGE = """
------------------------------------------------------------------------
| type [CTRL + C] anytime to pause current assessment and return later |
------------------------------------------------------------------------
"""

# ======= private functions ============

def __isIndicatorValueNotSetted(value):
    return type(value) is int and value == 0

def __buildDataInputTuple(dataDictionary):
    dataDictionaryLength = len(dataDictionary)
    return dataDictionary, str(dataDictionaryLength)

# ======= public functions  ============

def isValueMatchedOnRegex(valueString, regexString):
    regexValidator = re.compile(regexString)
    return bool(regexValidator.match(valueString))

def builDictionaryFormattedToPrint(dataDictionary):
    dictionaryFormatted = ''
    for key, value in dataDictionary.items():
        dictionaryFormatted += str(key) + ' - ' + str(value) + '\n'
    return dictionaryFormatted

def captureGenericDataValueAndReturn(dataSelectionQuestion, dataDictionaryWithIntKey):
    dataInputTuple = __buildDataInputTuple(dataDictionaryWithIntKey)
    dataInputDictionary = dataInputTuple[0]
    dataInputMaxValueStr = dataInputTuple[1]
    selectedDataIndex = captureValue(
        dataSelectionQuestion + builDictionaryFormattedToPrint(dataDictionaryWithIntKey),
        '^[1-' + dataInputMaxValueStr + ']$',
        'Invalid value. Valid values are 1 to ' + dataInputMaxValueStr + '\n'
    )
    clearTerminal()
    return dataInputDictionary[int(selectedDataIndex)]

def captureIndicatorValueAndUpdate(categoryIndicators, indicator):
    indicatorValue = captureValue(
        valueSelectionQuestion=indicator + '\n',
        valueSelectedRegexValidation='^[1-5]$',
        invalidValueSelectedMsg='Invalid indicator value. Valid values are 1 to 5'
    )
    categoryIndicators[indicator] = int(indicatorValue)

def captureValue(valueSelectionQuestion, valueSelectedRegexValidation, invalidValueSelectedMsg):
    def isSelectedValueInvalid(selectedValue):
        return not(isValueMatchedOnRegex(selectedValue, valueSelectedRegexValidation))
    selectedValue = input(valueSelectionQuestion)
    while isSelectedValueInvalid(selectedValue):
        print(invalidValueSelectedMsg)
        selectedValue = input(valueSelectionQuestion)
    return selectedValue

def captureBeachTypeInputAndReturn(beachTypeDictionary):
    return captureGenericDataValueAndReturn(
        dataSelectionQuestion = 'Specify the type of the beach:\n',
        dataDictionaryWithIntKey = beachTypeDictionary
    )

def captureCategoriesIndicatorValue(userInputDictionary):
    for domain, domainCategories in userInputDictionary.items():
        for category, categoryIndicators in domainCategories.items():
            for indicator, indicatorValue in categoryIndicators.items():
                if __isIndicatorValueNotSetted(indicatorValue):
                    captureIndicatorValueAndUpdate(categoryIndicators, indicator)

def printAssessInitialMessage(currentBeachNameInAssessment):
    print(END_ASSESSMENT_MESSAGE)
    print('In progress assessment for beach: ' + currentBeachNameInAssessment + '\n\n')

def captureBeachNameAndReturn(currentBeachName):
    if currentBeachName == None:
        return captureValue(
            valueSelectionQuestion = 'Inform the beach name:\n',
            valueSelectedRegexValidation = '\w+',
            invalidValueSelectedMsg = 'Invalid beach name.\n'
        )
    else:
        return currentBeachName

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def captureUserSelectedFunctionalityAndReturn(validationRegex, invalidFunctionalityMsg):
    return captureValue(
        valueSelectionQuestion = 'Inform desired functionality:\n',
        valueSelectedRegexValidation = validationRegex,
        invalidValueSelectedMsg = invalidFunctionalityMsg
    )