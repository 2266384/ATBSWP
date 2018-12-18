import re

# Regex for US Phone Number recognition
# Use r before the Regex Pattern string to pass the string as RAW
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())
print(mo.groups())

areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

# Escape characters to include brackets as part of Regex
phoneNumRegex2 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')

mo = phoneNumRegex2.search('My number is (415) 555-4242.')
print(mo.group(1))
print(mo.group(2))

# Pipe will search for OR in Regex but will only return the FIRST MATCH
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

# Piped values enclosed in brackets search for prefix followed by any of the suffix values enclosed in the brackets
# e.g. BatMAN, BatMOBILE, BatCOPTER, or BatBAT
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo3 = batRegex.search("Batmobile lost it's wheel")
print(mo3.group())
print(mo.group(1))

# Use ? after parentheses to indicate that part of Regex string is optional
batRegex2 = re.compile(r'Bat(wo)?man')
mo4 = batRegex2.search('The Adventures of Batman')
print(mo4.group())

mo5 = batRegex2.search('The adventures of Batwoman')
print(mo5.group())

phoneNumRegex3 = re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d\d)')

mo6 = phoneNumRegex3.search('My number is 415-555-4242.')
print(mo6.group())

mo7 = phoneNumRegex3.search('My number is 555-4242')
print(mo7.group())

# Use asterisk after parentheses to search for 'ZERO OR MORE' of the value
batRegex3 = re.compile(r'Bat(wo)*man')
mo8 = batRegex3.search('The Adventures of Batman')
mo9 = batRegex3.search('The Adventures of Batwoman')
mo10 = batRegex3.search('The Adventures of Batwowowowoman')

print(mo8.group())
print(mo9.group())
print(mo10.group())

# Use plus after parentheses to search for 'ONE OR MORE' of the value
batRegex4 = re.compile(r'Bat(wo)+man')
mo11 = batRegex4.search('The Adventures of Batman')
mo12 = batRegex4.search('The Adventures of Batwoman')
mo13 = batRegex4.search('The Adventures of Batwowowowoman')

print(mo13.group())
print(mo12.group())
print(mo11 == None)

# Use curly brackets to search for multiple iterations of the value in brackets
haRegex = re.compile(r'(Ha){3}')
mo14 = haRegex.search('HaHaHa')
print(mo14.group())

mo15 = haRegex.search('Ha')
print(mo15 == None)

# Regex will return the longest possible match unless you use a ? after the closing curly bracket when it will
# return the shortest possible match
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo16 = greedyHaRegex.search('HaHaHaHaHa')
print(mo16.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo17 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo17.group())

# Regex.search() will only return the first instance that matches the pattern
phonenumRegex4 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo18 = phonenumRegex4.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo18.group())

# Regex.findall() will return all instances that match the pattern
# If there are no groups in the pattern returns a list of all matching values
phonenumRegex5 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo19 = phonenumRegex5.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo19)

# If there are groups in the pattern returns a List of Tuples of Strings
phonenumRegex6 = re.compile(f'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo20 = phonenumRegex6.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo20)

# Using character classes
xmasRegex = re.compile(r'\d+\s\w+')     # Finds any number of digits followed by a space followed by any number of letters
xmas = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, _'
                            '5 rings, 4 birds, 3 hens, 2 doves, 1 patridge')
print(xmas)

# Making your own character classes - enter characters in square brackets to define
vowelRegex = re.compile(r'[aeiouAEIOU]')        # Returns only vowels
vowels = vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
print(vowels)

# Adding a caret (^) reverses the character class returns values that DON'T match
consonantRegex = re.compile(r'[^aeiosAEIOU]')   # Returns any character or space that's not a vowel
consonants = consonantRegex.findall('Robocop eats baby food. BABY FOOD')
print(consonants)

# Add a caret at the beginning of the Regex statement to indicate that only substrings that start with thee
# element should be returned
beginsWithHelloRegex = re.compile(r'Hello')
beginsWithHello = beginsWithHelloRegex.search('Hello World!')
print(beginsWithHello.group())
print(beginsWithHelloRegex.search('He said hello.') == None)

# Add a $ at the end of the Regex string to indicate that the substring should end with the given value
endsWithNumberRegex = re.compile(r'\d$')
endsWithNumber = endsWithNumberRegex.search('Your number is 42')
print(endsWithNumber.group())
print(endsWithNumberRegex.search('Your number is forty two') == None)

# Add a ^ and $ to the front and end of the regex to indicate the substring
# should begin and end with a given value
wholeStringIsNumRegex = re.compile(r'^\d+$')        # String should start and end with one or more numeric digits
wholeStringIsNum = wholeStringIsNumRegex.search('1234567890')
print(wholeStringIsNum.group())
print(wholeStringIsNumRegex.search('12345xyz67890') == None)
print(wholeStringIsNumRegex.search('12  34567890') == None)

# The . character can be used to represent any character EXCEPT a NewLine
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat'))

# Use .* to return zero or more characters from the substring
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo21 = nameRegex.search('First Name: Al Last Name: Smith')
print(mo21.group(1))
print(mo21.group(2))

# Use .*? to return zero or more characters in a NON-GREEDY way
nonGreedyRegex = re.compile(r'<.*?>')           # Stops at FIRST > character
mo22 = nonGreedyRegex.search('<To serve man> for dinner.>')
print(mo22.group())

greedyRegex = re.compile(r'<.*>')               # Stops at LAST > character
mo23 = greedyRegex.search('<To serve man> for dinner.>')
print(mo23.group())

# Use re.DOTALL to tell regex to match a NewLine when using the . character
noNewLineRegex = re.compile(r'.*')
noNewLine = noNewLineRegex.search('Serve the public trust. \nProtect the innocent. \nUphold the law.')
print(noNewLine.group())

newLineRegex = re.compile(r'.*', re.DOTALL)
newLine = newLineRegex.search('Serve the public trust. \nProtect the innocent. \nUphold the law.')
print(newLine.group())

# Use re.IGNORECASE or re.I to make your regex case insensitive
robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machine, all cop').group())
print(robocop.search('ROBOCOP protects the innocent').group())
print(robocop.search('Al, why does your programming book talk about robocop so much?').group())

# Substitute strings using regex by using the sub method
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

# You can use the \1, \2, \3 etc argument as part of the sub method to keep part of the string
agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent'))

# Use re.VERBOSE to tell python to ignore comments and whitespaces in regex statements
# instead of this:
phoneRegex = re.compile(r'((\d{3}|\(|d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

# use this:
phoneRegex = re.compile(r'''(                               # NOTE the triple quote marks
                        (\d{3}|\(|d{3}\))?                  # area code
                        (\s|-|\.)?                          # separator
                        \d{3}                               # first 3 digits
                        (\s|-|\.)                           # separator
                        \d{4}                               # last 4 digits
                        (\s*(ext|x|ext.)\s*\d{2,5})?        # extension
                        )''', re.VERBOSE)
