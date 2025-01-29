import PySimpleGUI as sg

#Alterando cursor
def set_cursor(element, cursor):
    widget= element.Widget
    widget.configure(cursor=cursor)

#Tema
sg.theme('LightBlue3')

#Layout
layout= [
    [sg.Text('Usuário:')],
    [sg.Input(key= 'login')],
    [sg.Text(size= 0, key= 'error_login')],
    [sg.Text('Senha:')],
    [sg.Input(key= 'password')],
    [sg.Text(size= 0, key= 'error_password')],
    [sg.Button(button_text='Entrar', key= 'login', size= 10)],
    [sg.Text('Não possui cadastro? Clique aqui!', enable_events= True, expand_x= True, key= 'sign_up', text_color= 'blue', font= ('Helvetica', 10, 'underline'))]
]

#Janela
window= sg.Window('Tela', layout= layout, finalize= True)

#Alterando o cursor
set_cursor(window['sign_up'], 'hand2')

#leitura
while True:
    event, values= window.read()
    #Ler e reagir aos eventos
    if event == sg.WIN_CLOSED:
        break
    elif event == 'login':
        print('Clicou no botão "Login"')
    elif event == 'sign_up':
        print('Mover para área de cadastro')
    print(values)
