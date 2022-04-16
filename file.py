"""
Author: Elaine Baroni, Filipe Borges
Email: elaine.bo@hotmail.com, filipebkc2209@gmail.com
"""

from pathlib import Path

DEFAULT_FILE_NAME = 'data.tmp'
DEFAULT_ENCODING = 'utf-8'

# ======= private functions - dont need to be accessed on main.py ============
def __writeDataOnFile(data, fileName = DEFAULT_FILE_NAME):
    p = Path(fileName)
    p.write_text(str(data), DEFAULT_ENCODING)

def __loadDataFromFile(fileName = DEFAULT_FILE_NAME):
    p = Path(fileName)
    return eval(p.read_text(DEFAULT_ENCODING))

def __fileExists(fileName = DEFAULT_FILE_NAME):
    return Path(fileName).exists()

def __loadUserInput():
    return __loadDataFromFile()

def __existsUserInputSaved():
    return __fileExists()

def __removeFile(fileName = DEFAULT_FILE_NAME):
    p = Path(fileName)
    p.unlink(True)

# ======= public functions - accessed on main.py ============
def saveUserInput(userInputDictionary):
    __writeDataOnFile(userInputDictionary)

def initializeUserInputDictionary(defaultUserInputDictionary):
    if (__existsUserInputSaved()):
        return __loadUserInput()
    else:
        return defaultUserInputDictionary

def deleteSavedUserInput():
    __removeFile()