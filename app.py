from flask import Flask, request, redirect, render_template
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST'])
def cadastro():
    nome = request.form.get('nome')
    email = request.form.get('email')
    mac_address = request.remote_addr  

    with open('usuarios.txt', 'a') as file:
        file.write(f'{nome} - {email}\n')

    liberar_wifi(email, mac_address)

    print(f'Novo cadastro: Nome: {nome}, E-mail: {email}')
    return redirect('/sucesso')

@app.route('/sucesso')
def sucesso():
    return "Cadastro realizado com sucesso! Agora você pode usar o Wi-Fi."

def liberar_wifi(email, mac_address):
    try:
        command = f"iptables -A INPUT -m mac --mac-source {mac_address} -j ACCEPT"
        subprocess.run(command, shell=True, executable='/data/data/com.termux/files/usr/bin/bash')
    except Exception as e:
        print(f"Erro ao tentar executar iptables: {e}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
