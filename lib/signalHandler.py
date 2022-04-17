"""
Author: Elaine Baroni, Filipe Borges
Email: elaine.bo@hotmail.com, filipebkc2209@gmail.com
"""

import signal
import sys
from lib.file import saveUserInput

# ======= private functions ============

def __beachNameIsNotEmtpy(beachName):
    return len(beachName) > 0

# ======= public functions  ============

def initializeEndProgramHandler(userInputDictionary, beachName):
    def handleSigIntSignal(signalNumber, currentStackFrame):
        saveUserInput(userInputDictionary, beachName)
        sys.exit(0)
    if __beachNameIsNotEmtpy(beachName):
        signal.signal(signal.SIGINT, handleSigIntSignal)