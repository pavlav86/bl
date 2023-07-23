
from datetime import datetime
import json

FILE_PATH = r'data.txt'

with open (FILE_PATH) as f:
    dict_notes = json.load(f)

def add_note():
    title = input("\nPlease input the note title: ")
    body = input("Please input the note body: ")    
    date = datetime.today().strftime("%d/%m/%Y")
    time = datetime.now().strftime("%H:%M:%S")
    

    if len(dict_notes) != 0:
        keys = [int(item) for item in dict_notes.keys()]
        id = str(max(keys) + 1)
    else: id = "1"
    
    dict_notes.update({id: {
        "title": title,
        "body": body,
        "date": date,
        "time": time
    }})
    print("\nYour note was successfully added!")

def edit_note():
    print()
    print_dict()
    id = input("\nPlease enter the id of the note you would like to edit: ")
    if id not in dict_notes.keys():
        print("Unfortunately there is no note with such id.")
    else:
        print(f'{id}. {dict_notes.get(id).get("title")} {dict_notes.get(id).get("body")} {dict_notes.get(id).get("date")} {dict_notes.get(id).get("time")}')
    
        title = input("\nIf you would like to edit title please write the new one: ")
        body = input("If you would like to edit body please write the new one: ")
        date = datetime.today().strftime("%d/%m/%Y")
        time = datetime.now().strftime("%H:%M:%S")
        dict_notes.update({id: {
            "title": title if title else dict_notes.get(id).get("title"),
            "body": body if body else dict_notes.get(id).get("body"),
            "date": date,
            "time": time
        }
        }
        )
        print("\nYour note was successfully edited!")

def delete_note():
    id = input("Please enter the id of the note you would like to delete: ")
    if id not in dict_notes.keys():
        print("Unfortunately there is no note with such id.")
    else: 
        dict_notes.pop(id)
        print("Your note was successfully deleted!")

def date_filter():
    required_date = input("\nPlease enter the date in dd/mm/yyyy format to filter the notes: ")
    print()
    for id in dict_notes:
        counter = 0
        if dict_notes.get(id).get("date") == required_date:
            counter += 1
            print(f'{id}. {dict_notes.get(id).get("title")} {dict_notes.get(id).get("body")} {dict_notes.get(id).get("date")} {dict_notes.get(id).get("time")}')
            
    if counter == 0:
        print("Unfortunately nothing was found.")
    
def print_dict():
     for id in dict_notes:
        print(f'{id}. {dict_notes.get(id).get("title")} {dict_notes.get(id).get("body")} {dict_notes.get(id).get("date")} {dict_notes.get(id).get("time")}')



while (user_action := int(input("[1] - Print all notes\n[2] - Add a new note\n[3] - Filter by the date\n[4] - Edit the note\n[5] - Exit the program\n\nPlease choose the action: "))) != 5:
    match user_action:
        case 1:
            print()
            print_dict()
            print()
        case 2:
            
            add_note()  
            print() 
        case 3:
            date_filter()
            print()
        case 4:
            edit_note()
            print()
        case 5:
            print("Good bye!")             
                           
        case _:
            print("Wrong input, please try again")

with open (FILE_PATH, 'w', encoding='utf8') as f:    
            json.dump(dict_notes, f, indent = 4)