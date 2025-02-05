import PySimpleGUI as sg
import bcrypt
from database import Database

db = Database('C:\\db_users\\database.db')  # Instanciando a classe Database
if not db.table_exists():
    db.create_table()

# Funções de Senha
def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)

# Janela de Login
def window_login():
    layout = [
        [sg.Text('Login', expand_x=True, justification='c', font='Courier 22 italic bold underline')],
        [sg.Text('Usuário:')],
        [sg.Input(key='-user-', expand_x=True)],
        [sg.Text('Senha:')],
        [sg.Input(key='-password-', expand_x=True, password_char='*')],
        [sg.Button('Entrar', key='-login-', expand_x=True)],
        [sg.Text('Não possui cadastro? Clique aqui!', enable_events=True, expand_x=True, key='-sign_up-', text_color='blue', font=('Helvetica', 10, 'underline'))]
    ]

    window = sg.Window('Login', layout, finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == '-sign_up-':
            window.hide()
            window_sign_up()
            window.un_hide()
        if event == '-login-':
            user = values['-user-']
            password = values['-password-']
            stored_hash = db.get_user(user)

            if stored_hash and verify_password(password, stored_hash[0].encode()):
                sg.popup('Login Efetuado com sucesso!')
                window.close()
            else:
                sg.popup('Usuário ou senha incorretos!')

# Janela de Cadastro
def window_sign_up():
    layout = [
        [sg.Text('Cadastro', expand_x=True, justification='c', font='Courier 22 italic bold underline')],
        [sg.Text('Nome de usuário:')],
        [sg.Input(expand_x=True, key='-user-')],
        [sg.Text('Senha:')],
        [sg.Input(expand_x=True, key='-password-', password_char='*')],
        [sg.Text('', size=(40, 1), key='-msg-', text_color='red')],
        [sg.Button('Cadastrar', expand_x=True, key='-sign_up-')]
    ]

    window = sg.Window('Cadastro', layout, finalize=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, None):
            break

        user = values['-user-']
        password = values['-password-']

        if not user or not password:
            window['-msg-'].update('Preencha os campos acima!')
            continue

        hashed_password = hash_password(password)

        if db.add(user, hashed_password.decode()):
            sg.popup('Usuário cadastrado com sucesso!')
            window.close()
        else:
            sg.popup('Usuário já existe!')

# Executar
if __name__ == '__main__':
    sg.theme('LightBlue3')
    window_login()