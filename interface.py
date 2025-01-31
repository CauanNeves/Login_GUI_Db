import PySimpleGUI as sg
import hashlib

#Alterando cursor
def set_cursor(element, cursor):
    widget= element.Widget
    widget.configure(cursor=cursor)

#Layouts
def main():
    #Janela login
    def window_login():
        layout= [
            [sg.Text('Login', expand_x= True ,justification= 'c')],
            [sg.Text('Usuário:')],
            [sg.Input(key= '-user-', expand_x= True)],
            [sg.Text('Senha:')],
            [sg.Input(key= '-password-', expand_x= True)],
            [sg.Button(button_text='Entrar', key= '-login-', expand_x= True)],
            [sg.Text('Não possui cadastro? Clique aqui!', enable_events= True, expand_x= True, key= '-sign_up-', text_color= 'blue', font= ('Helvetica', 10, 'underline'))]
        ]
        window = sg.Window('Cadastrar', layout= layout,
                    finalize= True,
                    auto_size_text=False,
                    text_justification='l',
                    return_keyboard_events=True,
                    grab_anywhere=False)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == '-sign_up-':
                window.close()
                window_sign_up()
            if event == '-login-':
                if values['-user-'] == 'Cauan' and values['-password-'] == 'senha':
                    print('Login efetuado com sucesso')
                else:
                    print('Usuário ou senha inválidos')


    #Janela Cadastro
    def window_sign_up():
        layout=[
            [sg.Input('Nome de Usuário', expand_x= True, key= '-user-')],
            [sg.Input('Senha', expand_x= True, key= '-password-')],
            [sg.Input('', size=(40, 1), key='hash')],
            [sg.Button('Cadastrar', expand_x= True)]
        ]

        window = sg.Window('Cadastrar', layout= layout,
                            finalize= True,
                            auto_size_text=False,
                            default_element_size=(20, 1),
                            text_justification='r',
                            return_keyboard_events=True,
                            grab_anywhere=False)

        #leitura
        while True:
            event, values= window.read()
            #Ler e reagir aos eventos
            if event is None:
                break

            password = values['-password-']
            try:
                password_utf = password.encode('utf-8')
                sha1hash = hashlib.sha1()
                sha1hash.update(password_utf)
                password_hash = sha1hash.hexdigest()
                window['hash'].update(password_hash)
            except:
                pass

            if event == sg.WIN_CLOSED:
                break
            elif values['-user-'] == 'usuario':
                print('Já existe esse nome de usuário')

    def PasswordMatches(password, a_hash):
        password_utf = password.encode('utf-8')
        sha1hash = hashlib.sha1()
        sha1hash.update(password_utf)
        password_hash = sha1hash.hexdigest()
        return password_hash == a_hash


    window_login()

if __name__ == '__main__':
    sg.theme('LightBlue3')
    main()