import PySimpleGUI as sg
import random

sg.theme('BlueMono')

drop_down = ['Rock', 'Paper', 'Scissors']

opponent = random.choice(drop_down)

layout = [[sg.Text('Rock, Paper, Scissors?', size=20)],
          [sg.Listbox(values=['Rock', 'Paper', 'Scissors'], size=(20, 3))],
          [sg.Text('Your opponent chose: ', size=(40, 1), k='-OUT-')],
          [sg.Button('OK'), sg.Button('Play Again'), sg.Button('Exit')]]


window = sg.Window('Rock, Paper, Scissors', layout, element_justification='c')

while True:
    event, values = window.read()

    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    elif event == 'OK':
        if values[0][0] == "Rock":
            if opponent == "Scissors":
                window['-OUT-'].update(f"Your opponent chose: {opponent}. You Win!.")
            elif opponent == "Rock":
                window['-OUT-'].update(f"Your opponent chose: {opponent}. You Draw!.")
            else:
                window['-OUT-'].update(f"Your opponent chose: {opponent}. You Lose!.")
        elif values[0][0] == "Paper":
            if opponent == "Rock":
                window['-OUT-'].update(f"Your opponent chose: {opponent}. You Win!.")
            elif opponent == "Paper":
                window['-OUT-'].update(f"Your opponent chose: {opponent}. You Draw!.")
            else:
                window['-OUT-'].update(f"Your opponent chose: {opponent}. You Lose!.")
        elif values[0][0] == "Scissors":
            if opponent == "Paper":
                window['-OUT-'].update(f"Your opponent chose: {opponent}. You Win!.")
            elif opponent == "Scissors":
                window['-OUT-'].update(f"Your opponent chose: {opponent}. You Draw!.")
            else:
                window['-OUT-'].update(f"Your opponent chose: {opponent}. You Lose!.")
    elif event == 'Play Again':
        opponent = random.choice(drop_down)


window.close()
