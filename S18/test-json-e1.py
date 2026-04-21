import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-e1.json").read_text()

# Create the object person from the json string
people = json.loads(jsonstring)

# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'

# Print the information on the console, in colors
for a in people:
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(a['Firstname'], a['Lastname'])
    termcolor.cprint("Age: ", 'green', end="")
    print(a['age'])

    # Get the phoneNumber list
    phoneNumbers = a['phoneNumber']

# Print the number of elements in the list
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

# Print all the numbers
    for i, dictnum in enumerate(phoneNumbers):
        termcolor.cprint("  Phone " + str(i + 1) + ": ", 'blue')

        # The element num contains 2 fields: number and type
        termcolor.cprint("\t- Type: ", 'red', end='')
        print(dictnum['type'])
        termcolor.cprint("\t- Number: ", 'red', end='')
        print(dictnum['number'])
