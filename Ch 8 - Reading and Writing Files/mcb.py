#! python3
# mcb.py - saves and loads pieces of text to the clipboard
# Usage:    py.exe mcb.py save <keyword> - saves clipboard to keyword
#           py.exe mcb.py <keyword> - loads the keyword to the clipboard
#           py.exe mcb.py list - loads all keywords to the clipboard
#           py.exe mcb.py delete - deletes all keywords from the clipboard
#           py.exe mcb.py delete <keyword> - deletes the keyword from the clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
