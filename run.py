import os
import sys

from Chess import Chess

########################################################
# Console Configuration
########################################################
# Define a new console prefix
sys.prefix = ">"

# Set Encoder to UTF-8
os.system('chcp 65001')

# Set window size
#os.system('mode con: cols=40 lines=18')
# Set window name
os.system("title Chess - A Python Interpretation")

# Clear Console
clear = lambda: os.system('cls')
clear()


########################################################
# Instantiate a game of Chess
########################################################
# Initialising a new game instance
chess = Chess()
chess.play()


########################################################
# End of Program
########################################################
# Grid is solved
x = input("\nPress Enter to exit ... ")

# Terminate Program
os.system('exit')


