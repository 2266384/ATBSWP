#! python3
# strongPW.py - checks if a password is strong
# Strong criteria is defined as having at least 8 characters and consist of both upper and lower character and numeric digits

import re

def strongPW(myString):
    lowerRegex = re.compile(r'[a-z]+')          # consist of any number of lower case characters
    upperRegex = re.compile(r'[A-Z]+')          # consists on any number of upper case characters
    numericRegex = re.compile(r'[0-9]+')        # consists of any number of numeric digits

    if len(myString) < 8:
        return 'Password is not long enough'

    if lowerRegex.search(myString) and upperRegex.search(myString) and numericRegex.search(myString):
        return 'Strong'
    else:
        return 'Weak'

print(strongPW('abcABC'))
print(strongPW('ABCabc123'))
print(strongPW('a1Ab2Bc3C'))
print(strongPW('1234abcd'))
