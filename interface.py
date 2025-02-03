import PySimpleGUI as sg
import hashlib
from database import Database

db = Database

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
                window.hide()
                user, password = window_sign_up()
                window.un_hide()
            if event == '-login-':
                try:
                    if values['-user-'] == user and PasswordMatches(values['-password-'], password):
                        print('Login efetuado com sucesso!')
                    else:
                        print('Usuário ou senha inválidos')
                except:
                    print('Nenhum usuário cadastrado')


    #Janela Cadastro
    def window_sign_up():
        layout=[
            [sg.Input('Nome de Usuário', expand_x= True, key= '-user-')],
            [sg.Input('Senha', expand_x= True, key= '-password-')],
            [sg.Input('', size=(40, 1), key='hash')],
            [sg.Button('Cadastrar', expand_x= True, key= '-sign_up-')]
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
            elif event == '-sign_up-':
                while True:
                    if values['-user-'] is not None and values['-password-'] is not None:
                        window.close()
                        db.add(user= values['-user-'], hash= values['hash'])
                        return values['-user-'], values['hash']
                    else:
                        pass


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