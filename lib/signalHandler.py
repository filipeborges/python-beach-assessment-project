"""
Author: Elaine Baroni, Filipe Borges
Email: elaine.bo@hotmail.com, filipebkc2209@gmail.com
"""

import signal
import sys
from lib.file import saveUserInput

def __beachNameIsNotEmtpy(beachName):
    return len(beachName) > 0

# ======= public functions - accessed on main.py ============
def initializeSaveUserInputWhenEndProgramCommand(userInputDictionary, beachName):
    def handleSigIntSignal(signalNumber, currentStackFrame):
        saveUserInput(userInputDictionary, beachName)
        sys.exit(0)
    if __beachNameIsNotEmtpy(beachName):
        signal.signal(signal.SIGINT, handleSigIntSignal)