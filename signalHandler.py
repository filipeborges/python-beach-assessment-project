"""
Author: Elaine Baroni, Filipe Borges
Email: elaine.bo@hotmail.com, filipebkc2209@gmail.com
"""

import signal
import sys
from file import saveUserInput

# ======= public functions - accessed on main.py ============
def initializeSaveUserInputWhenEndProgramCommand(userInputDictionary):
    def handleSigIntSignal(signalNumber, currentStackFrame):
        saveUserInput(userInputDictionary)
        sys.exit(0)
    signal.signal(signal.SIGINT, handleSigIntSignal)