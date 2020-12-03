import json
import sys
import os

notes = {}

def user_in():
    header = input('Heading:  ')
    body = input('\n > ')

    notes[header] = body

    return header, body

def clear():
    os.system('clear')

def loading():
    with open('notes.json', 'r') as file_:
        open_json = json.load(file_)
    for k in open_json.items():
        print(k)


def main():
    header, body = user_in()
    clear()
    note = json.dumps(notes, indent=4)

    with open('notes.json','w') as out:
        out.write(f"{note}\n")
    
    loading()


main()
# loading()