import PySimpleGUI as sg
import json

try:
    file = open('./db.json', 'r')

except FileNotFoundError:
    file = open('./db.json','w')
    file.write(
        json.dumps( {
            "test": "pass"
        }, indent=4)
    )
    file.close()
file.close()

subjects = ["english","physics", "chemistry", "maths", "phe", "computer", "painting" ]


left_lay = [
    [sg.Text( "Enter Roll Number " ,size=(14,1 )), sg.Input(size=(5,1),key="roll") ],
    [sg.Text('Enter Name', size=(14,1) ),sg.Input(size=(14,1), key="name")],
    [sg.HSeparator()],
    [sg.Text("Marks", size=(5,1))]
]
for i in subjects:
    left_lay += [[sg.Text(i, size=(10,1)), sg.Input(size=(6,1), key=i ) ]]
left_lay += [
    [sg.HSeparator()],
    [sg.Button("Save"), sg.Button("Get"), sg.Button("Exit")]
]
right_lay = [
    [sg.Text("Help")], [sg.HSeparator()],
    [sg.Text("Save -> ", text_color="Black" ), sg.Text("updated data entered in the fields to the db.json file ") ] , [sg.HSeparator()],
    [sg.Text("Get - >", text_color="Black" ), sg.Text("Gets data for the roll number provided in the roll number field\n!!ANY UNSAVED DATA IN THE FIELDS WILL NOT BE SAVED!! ") ],
    [sg.HSeparator()],
    [sg.Text(" " )]
]

layout = [
    [sg.Column(left_lay), sg.VSeparator(), sg.Column(right_lay) ]]
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

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event =="Exit":
        break
    if event == "Save":
        Save(values)
    if event == "Get":
        Get(values['roll'])

window.close()