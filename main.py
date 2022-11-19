import PySimpleGUI as sg
import json



try:
    file = open('./db.json', 'r')


except FileNotFoundError:
    file = open('./db.json','w')
    file.write( json.dumps( {}, indent=4))
    file.close()





layout = [  
    [sg.Text( "Student registration Number " ,size=(20,1 )), sg.Input(size=(20,1), key="registration") ],
    [sg.Text('Student Name', size=(14,1) ), sg.Input(size=(20,1),key="name" )],
    [sg.Text("Student contact number", size=(18,1)), sg.Input(size=(20,1), key="number") ],
    [sg.Text('Student Email', size=(13,1)), sg.Input(size=(20,1), key="email")],
    [sg.HSeparator()],
    [sg.Button("Save"), sg.Button("Get"), sg.Button("Exit")]
]




window = sg.Window(title="Student data manager" ,layout=layout)


def Save(values:list):
    registration = values['registration']
    name = values['name']
    number = values['number']
    email = values['email']
    

    with open('./db.json', 'r')as f:
        db = json.load(f)
        db[registration]= {
                    "name": name,
                    "number": number,
                    "email": email,
                    
                }

    with open('./db.json', 'w')as f:
        f.write(json.dumps(db, indent=4) )
        
        

def Get(registration):
    with open('./db.json', 'r')as f:
        db = json.load(f)
        if registration in db:
            window['name'].update(db[registration]["name"] )
            window['number'].update(db[registration]["number"])
            window['email'].update(db[registration]["email"] )
           
        else:
            sg.popup("Entry for given registration number does not exist", keep_on_top=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event =="Exit":
        break
    if event == "Save":
        Save(values)
    if event == "Get":
        Get(values['registration'])

window.close()