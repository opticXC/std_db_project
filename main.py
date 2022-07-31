import PySimpleGUI as sg
import json


subjects = ["english","physics", "chemistry", "maths", "phe", "computer", "painting" ]


layout = [
    [sg.Text( "Enter Roll Number " ,size=(14,1 )), sg.Input(size=(5,1),key="roll") ],
    [sg.Text('Enter Name', size=(14,1) ),sg.Input(size=(14,1), key="name")],
    [sg.HSeparator()],
    [sg.Text("Marks", size=(5,1))]
]
for i in subjects:
    layout += [[sg.Text(i, size=(10,1)), sg.Input(size=(6,1), key=i ) ]]
layout += [
    [sg.HSeparator()],
    [sg.Button("Save"), sg.Button("Get"), sg.Button("Exit")]
]


window = sg.Window(title="Student data manager" ,layout=layout)


def Save(values:list):
    roll = values['roll']
    name = values['name']
    
    english = values['english']
    physics = values['physics']
    chemistry = values['chemistry']
    maths = values['maths']
    phe = values['phe']
    computer = values['computer']
    painting = values['painting']

    with open('./db.json', 'r')as f:
        db = json.load(f)
        db[roll]= {
                    "name": name,
                    "marks" : {
                        "english": english,
                        "physics": physics,
                        "chemistry": chemistry,
                        "maths": maths,
                        "phe": phe,
                        "computer": computer,
                        "painting": painting
                    }
                }

    with open('./db.json', 'w')as f:
        f.write(json.dumps(db, indent=4) )
        
        f.close()

def Get(roll):
    with open('./db.json', 'r')as f:
        db = json.load(f)
        if roll in db:
            window['name'].update(db[roll]["name"] )
            window['english'].update(db[roll]["marks"]["english"])
            window['physics'].update(db[roll]["marks"]["physics"])
            window['chemistry'].update(db[roll]["marks"]["chemistry"])
            window['maths'].update(db[roll]["marks"]["maths"])
            window['phe'].update(db[roll]["marks"]["phe"])
            window['computer'].update(db[roll]["marks"]["computer"])
            window['painting'].update(db[roll]["marks"]["painting"])
        else:
            sg.popup("Entry for given rollnumber does not exist", keep_on_top=True)
        f.close()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event =="Exit":
        break
    if event == "Save":
        Save(values)
    if event == "Get":
        Get(values['roll'])

window.close()