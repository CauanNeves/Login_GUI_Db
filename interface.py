import PySimpleGUI as sg

#Tema
sg.theme('LightBlue3')

#Layout
layout= [
    [sg.Text('Usuário:')],
    [sg.Input(key= 'login')],
    [sg.Text('Senha:')],
    [sg.Input(key= 'password')],
    [sg.Button(button_text='Login', expand_x= True), sg.Button(button_text= 'Sign up!',  expand_x= True)]
]

#Janela
window= sg.Window('Tela', layout= layout)

#leitura
while True:
    event, values= window.read()
    #Ler e reagir aos eventos
    if event == sg.WIN_CLOSED:
        break
    elif event == 'OK':
        print('Clicou no botão "OK"')
    print(values)
    