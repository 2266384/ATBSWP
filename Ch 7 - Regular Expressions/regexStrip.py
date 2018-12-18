#! python3
# regexStrip.py - Function to strip spaces OR specified characters from a string

import re

def regexStrip(myString, character=' '):
    defRegex = re.compile(r'^[\s]+|[\s]+$')
    myRegex = re.compile(r'' + re.escape(character))

    if character == ' ':
        return defRegex.sub('', myString)
    else:
        return myRegex.sub('', myString)

print(regexStrip('   hello   world   '))
print(regexStrip('   hello   world   ', 'e'))
print(regexStrip('   hello   world   ', 'l'))
print(regexStrip('   hello   world   ', 'lo'))
