from flask import Flask, jsonify, request


app = Flask(__name__)



livros = [
    {
        'id':1,
        'título': 'O Senhor dos Aneis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'

},

    {
        'id':2,
        'título': 'Cidade de Papel',
        'autor': 'Jhon Grenn'

},

    {   'id':3,
        'título': 'O Guia Definitivo do Mochileiro das Galaxias',
        'autor': 'Douglas Adams'


},


]

#consultar(todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)


#consultar(id)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)


#editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])


#incluir
@app.route('/livros',methods=['POST'])
def incluir_novo_livro(id):
    novo_livro = request.get_json()
    livros.append(novo_livro)


#excluir
@app.route('/livros',methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify(livros)  

app.run(port=5000,host='localhost',debug=True)