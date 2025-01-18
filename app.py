from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST'])
def cadastro():
    nome = request.form.get('nome')
    email = request.form.get('email')

    # Salvando o cadastro no arquivo
    with open('usuarios.txt', 'a') as file:
        file.write(f'{nome} - {email}\n')

    # Liberar Wi-Fi (simulação)
    liberar_wifi(email)

    print(f'Novo cadastro: Nome: {nome}, E-mail: {email}')
    return redirect('/sucesso')

@app.route('/sucesso')
def sucesso():
    return "Cadastro realizado com sucesso! Agora você pode usar o Wi-Fi."

def liberar_wifi(email):
    # Exemplo: Adicionar regras de acesso usando iptables ou outro método
    print(f"Liberando Wi-Fi para o usuário com e-mail: {email}")
    # Simulação: Substitua pelo comando necessário no Termux
    # os.system(f"iptables -A INPUT -m mac --mac-source {mac_address} -j ACCEPT")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
