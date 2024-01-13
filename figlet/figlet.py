import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

isRandomFont = True
if (len(sys.argv) == 3) and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    isRandomFont = False
else:
    sys.exit(1)


if isRandomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())

given = input("Input: ")
print("Output:", figlet.renderText(given))
