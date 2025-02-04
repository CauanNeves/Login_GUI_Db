import PySimpleGUI as sg
import hashlib
from database import Database

db = Database('C:\\db_users\\database.db')  # Instanciando a classe Database
if db.table_exists() == False:
    db.create_table()
else:
    pass


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
                hash = db.get_user(values['-user-'])
                if hash is not None:
                    if PasswordMatches(password= values['-password-'], a_hash= hash[0]):
                        sg.popup('Login Efetuado com sucesso!')
                        window.close()
                else:
                    sg.popup('Usuário não encontrado')


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
                    if values['-user-'] != '' and values['-password-'] != '':
                        window.close()
                        user_create = db.add(user= values['-user-'], hash= values['hash'])
                        if user_create ==  True:
                            print('User criado com sucesso!')
                            return values['-user-'], values['hash']
                        else:
                            print('User existente')                        
                    else:
                        print('Preencha os campos acima!')

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
    
#Cauan
#Senha.123