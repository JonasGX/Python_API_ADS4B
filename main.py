from flask import Flask, render_template, request, redirect

class Profissao:
    def __init__(self, cpf, nome, profissao):
        self.cpf = cpf
        self.nome = nome
        self.profissao = profissao

func1 = Profissao('1234','Jonas', 'Engenheiro de Software')
func2 = Profissao('3456','Maria', 'Desenvolvedor Back-end')

lista = [func1, func2]


app = Flask(__name__, template_folder='template')
 
@app.route('/',)
def inicio():
    return render_template('index.html', titulo='FUNCIONÁRIOS', funcionarios=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Cadastrar Funcionários')

@app.route('/criar', methods=['POST',])
def criar():
    cpf = request.form['cpf']
    nomes = request.form['nome']
    profissao = request.form['profissao']
    profissoes = Profissao(cpf, nomes, profissao)
    lista.append(profissoes)
    return redirect('/')

app.run(debug=True)