# Import String for handling words
# Import Sys for handling
# Import Colorama for epic

from colorama import Fore
from readoc import *
import string

# Make fun of Devin
print(Fore.RED + """"\
▓█████▄ ▓█████ ██▒   █▓ ██▓ ███▄    █      ██████  █    ██  ▄████▄   ██ ▄█▀  ██████ 
▒██▀ ██▌▓█   ▀▓██░   █▒▓██▒ ██ ▀█   █    ▒██    ▒  ██  ▓██▒▒██▀ ▀█   ██▄█▒ ▒██    ▒ 
░██   █▌▒███   ▓██  █▒░▒██▒▓██  ▀█ ██▒   ░ ▓██▄   ▓██  ▒██░▒▓█    ▄ ▓███▄░ ░ ▓██▄   
░▓█▄   ▌▒▓█  ▄  ▒██ █░░░██░▓██▒  ▐▌██▒     ▒   ██▒▓▓█  ░██░▒▓▓▄ ▄██▒▓██ █▄   ▒   ██▒
░▒████▓ ░▒████▒  ▒▀█░  ░██░▒██░   ▓██░   ▒██████▒▒▒▒█████▓ ▒ ▓███▀ ░▒██▒ █▄▒██████▒▒
 ▒▒▓  ▒ ░░ ▒░ ░  ░ ▐░  ░▓  ░ ▒░   ▒ ▒    ▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ░ ░▒ ▒  ░▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░
 ░ ▒  ▒  ░ ░  ░  ░ ░░   ▒ ░░ ░░   ░ ▒░   ░ ░▒  ░ ░░░▒░ ░ ░   ░  ▒   ░ ░▒ ▒░░ ░▒  ░ ░ 
""" + Fore.RESET)

# Used to gather user input
# Went this way so I could later
# Create Optional inputs
def prompt(text):
    return input(text).strip()

# Optional if theres nothing
# It returns piltos (never being used)
def optional(text, default):
    var = prompt(text)
    if var:
        return var
    else:
        return default

# Prompt for file name
essay_prompt = prompt("Please provide file name (or link): ")

# Checks if its a link
# If it is it grabs content
# And saves it to a .txt file
if "https:" in essay_prompt:
    document_id_link = essay_prompt.split('/')[-2]
    var = read_document(document_id_link)
    price = 33.3
    with open("temp.txt", "w") as text_file:
        text_file.write(var)
    essay = open("temp.txt")
else:
    essay = open(essay_prompt)

# Prompt for other words
word_prompt = optional("Any other words to look for? (Separated by spaces) ", "piltos")
if word_prompt == "piltos":
    print("No other words specified")
    cwlist = False
else:
    cwlist = word_prompt.split()

# Create word lists
dwlist = [
    'so',
    'fun',
    'cute',
    'really',
    'things',
    'interesting',
    'very',
    'nice',
    'good',
    'great',
    'dumb',
    'boring',
    'exciting',
    'neat',
    'a lot',
    'alot',
    'stuff',
    'awesome',
    ]
bvlist = [
    'is',
    'was',
    'were',
    'am',
    'are',
    'be',
    'being',
    'been',
    ]

# Create an empty dictionary
d = dict()
b = dict()
c = dict()

# Loop through each line of the file
for line in essay:
    # Remove the leading spaces and newline character
    line = line.strip()

    # Convert the characters in line to
    # lowercase to avoid case mismatch
    line = line.lower()

    # Remove the punctuation marks from the line
    line = line.translate(line.maketrans('', '', string.punctuation))

    # Split the line into words
    words = line.split(' ')

    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1

        elif word in dwlist:
            # Add the word to dictionary with count 1
            d[word] = 1

    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in b:
            # Increment count of word by 1
            b[word] = b[word] + 1

        elif word in bvlist:
            # Add the word to dictionary with count 1
            b[word] = 1

    if cwlist is not False:
        # Iterate over each word in line
        for word in words:
            # Check if the word is already in dictionary
            if word in c:
                # Increment count of word by 1
                c[word] = c[word] + 1

            elif word in cwlist:
                # Add the word to dictionary with count 1
                c[word] = 1

# Print the contents of dictionary
if d:
    print('Dead words')
    for key in list(d.keys()):
        print(key, "\b:", d[key])

    print('Total dead words: ', sum(d.values()))
else:
    print('No dead words found.')

if b:
    print('\nBe verbs')
    for key in list(b.keys()):
        print(key, "\b:", b[key])
    print('Total be verbs: ', sum(b.values()))
else:
    print('No be verbs found.')

if cwlist is not False:
    if c:
        print("\nOther Words")
        for key in list(c.keys()):
            print(key, "\b:", c[key])
        print('Total custom words: ', sum(c.values()))
else:
    print('\nNo custom words found.')



