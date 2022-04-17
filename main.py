"""
Author: Elaine Baroni, Filipe Borges
Email: elaine.bo@hotmail.com, filipebkc2209@gmail.com
"""

from lib.functionality import assessBeach, editCurrentValue, printRanking
from lib.userInput import captureUserSelectedFunctionalityAndReturn, clearTerminal

PROGRAM_MENU_MESSAGE = """
----------------------------------------------------
|    Beach assessment program - v1.0               |
----------------------------------------------------
|    1- Assess new beach/Continue existing one     |
|    2- Present beach ranking by index             |
|    3- Visualize/Edit indicators                  |
|    4- Exit program                               |
----------------------------------------------------
"""

functionalityMap = {
    '1': assessBeach,
    '2': printRanking,
    '3': editCurrentValue,
    '4': exit
}

def executeFunctionality():
    print(PROGRAM_MENU_MESSAGE)
    selectedFunctionality = captureUserSelectedFunctionalityAndReturn('^[1-4]$', 'Invalid functionality value. Valid values are 1 to 4')
    functionalityToExecute = functionalityMap[selectedFunctionality]
    clearTerminal()
    functionalityToExecute()

def runProgram():
    clearTerminal()
    executeFunctionality()
    input('\n\nPress enter to continue...\n')

while True:
    runProgram()