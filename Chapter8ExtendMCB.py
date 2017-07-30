#! usr/bin/env python3
#Saves and loads pieces of text to the clipboard.
#python Chapter8extendMCB.py save <keyword> - Saves clipboard to keyword.
#python Chapter8extendMCB.py <keyword> - Loads keyword to clipboard.
#python Chapter8extendMCB.py list - Loads all keywords to clipboard.
#python Chapter8extendMCB.py delete <keyword> - Delete keywoard from the shelf
#python Chapter8extendMCB.py delete - Delete all keywords

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    #List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    #Delete all keywords
    elif sys.argv[1].lower() == 'delete':
        for i in range(len(mcbShelf)):
            var = list(mcbShelf.keys())
            del mcbShelf[var[0]]
#Delete keyword
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]

mcbShelf.close()
