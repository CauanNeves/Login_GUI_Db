import PySimpleGUI as sg

#Alterando cursor
def set_cursor(element, cursor):
    widget= element.Widget
    widget.configure(cursor=cursor)

#Tema
sg.theme('LightBlue3')

#Layouts
#Janela login
def window_login():
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
    return sg.Window('Login', layout= layout, finalize= True)

#Janela Cadastro
def window_sign_up():
    layout=[
        [sg.Text('Está vai ser a tela de cadastro do usuário')]
    ]
    return sg.Window('Cadastrar', layout= layout, finalize= True)

window_login_, window_sign_up_ = window_login(), None

#Alterando o cursor
set_cursor(window_login_['sign_up'], 'hand2')

#leitura
while True:
    window, event, values= sg.read_all_windows()
    #Ler e reagir aos eventos
    if event == sg.WIN_CLOSED:
        break
    if window == window_login_ and event == 'sign_up':
        window_sign_up_ = window_sign_up()
        window_login_.hide() #.un_hide() para exibir novamente a janela
    print(values)
