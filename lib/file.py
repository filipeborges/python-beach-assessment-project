"""
Author: Elaine Baroni, Filipe Borges
Email: elaine.bo@hotmail.com, filipebkc2209@gmail.com
"""

from pathlib import Path

DEFAULT_FILE_NAME = 'data.tmp'
DEFAULT_ENCODING = 'utf-8'
NEW_LINE = '\n'
RESULT_FILE_NAME = 'result.sav'
RESULT_FILE_DATA_SEPARATOR = '#'

__savedContent = None

# ======= private functions - dont need to be accessed on main.py ============
def __appendDataOnFile(data, fileName, prefixNewLine = True):
    p = Path(fileName)
    file = p.open('at')
    if prefixNewLine:
        data = NEW_LINE + data
    file.write(data)
    file.close()

def __writeDataOnFile(data, fileName = DEFAULT_FILE_NAME):
    p = Path(fileName)
    p.write_text(str(data), DEFAULT_ENCODING)

def __loadDataFromFile(fileName = DEFAULT_FILE_NAME):
    p = Path(fileName)
    return p.read_text(DEFAULT_ENCODING)

def __fileExists(fileName = DEFAULT_FILE_NAME):
    return Path(fileName).exists()

def __loadUserInput():
    global __savedContent
    if __savedContent is None:
        __savedContent = __loadDataFromFile()
    return __savedContent

def __existsUserInputSaved():
    return __fileExists()

def __existsFinalResultSaved():
    return __fileExists(RESULT_FILE_NAME)

def __removeFile(fileName = DEFAULT_FILE_NAME):
    p = Path(fileName)
    p.unlink(True)

def __formatUserInputForSave(userInputDictionary, beachName):
    return beachName + '\n' + str(userInputDictionary)

def __formatFinalResultForSave(beachName, beachIndex, domainGradeResultDictionary):
    return beachName + RESULT_FILE_DATA_SEPARATOR + str(beachIndex) + RESULT_FILE_DATA_SEPARATOR + str(domainGradeResultDictionary)

# ======= public functions - accessed on main.py ============
def saveUserInput(userInputDictionary, beachName):
    __writeDataOnFile(__formatUserInputForSave(userInputDictionary, beachName))

def initializeUserInputDictionary(defaultUserInputDictionary):
    if (__existsUserInputSaved()):
        savedContent = __loadUserInput()
        return eval(savedContent.split(NEW_LINE)[1])
    else:
        return defaultUserInputDictionary

def initializeBeachName(defaultBeachName):
    if (__existsUserInputSaved()):
        savedContent = __loadUserInput()
        return savedContent.split(NEW_LINE)[0]
    else:
        return defaultBeachName

def deleteSavedUserInput():
    __removeFile()

def saveFinalResult(beachName, beachIndex, domainGradeResultDictionary):
    prefixNewLine = True if __existsFinalResultSaved() else False
    __appendDataOnFile(
        __formatFinalResultForSave(beachName, beachIndex, domainGradeResultDictionary),
        RESULT_FILE_NAME,
        prefixNewLine
    )
