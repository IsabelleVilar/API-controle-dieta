from flask import Flask, request, jsonify
from database import db
from models import Refeicao
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Postgres123@localhost:5432/controle-dieta'
db.init_app(app)
migrate = Migrate(app, db)

# registrar uma refeição
@app.route('/refeicoes', methods=['POST'])
def registrar_refeicao():
    data = request.json
    nome = data.get('nome')
    descricao = data.get('descricao')
    data_hora = data.get('data_hora')
    esta_na_dieta = data.get('esta_na_dieta')
    if nome and data_hora:
        refeicao = Refeicao(nome=nome, descricao=descricao, data_hora=data_hora, esta_na_dieta=esta_na_dieta)
        db.session.add(refeicao)
        db.session.commit()
        return jsonify({'message': 'Refeição registrada com sucesso'}), 201
    return jsonify({'message': 'Dados inválidos'}), 400

# editar uma refeição
@app.route('/refeicoes/<int:id>', methods=['PUT'])
def editar_refeicao(id):
    data = request.json
    refeicao = Refeicao.query.get(id)
    if refeicao:
        refeicao.nome = data.get('nome')
        refeicao.descricao = data.get('descricao')
        refeicao.data_hora = data.get('data_hora')
        refeicao.esta_na_dieta = data.get('esta_na_dieta')
        db.session.commit()
        return jsonify({'message': 'Refeição editada com sucesso'}), 200
    return jsonify({'message': 'Refeição não encontrada'}), 404

# apagar uma refeição
@app.route('/refeicoes/<int:id>', methods=['DELETE'])
def apagar_refeicao(id):
    refeicao = Refeicao.query.get(id)
    if refeicao:
        db.session.delete(refeicao)
        db.session.commit()
        return jsonify({'message': f'Refeição {id} apagada com sucesso'})
    return jsonify({'message': 'Refeição não encontrada'})

# listar todas as refeições
@app.route('/refeicoes', methods=['GET'])
def listar_refeicoes():
    refeicoes = Refeicao.query.all()
    if refeicoes:
        lista_refeicoes = [{'id': refeicao.id,
                            'nome': refeicao.nome,
                            'descricao': refeicao.descricao,
                            'data_hora': refeicao.data_hora,
                            'esta_na_dieta': refeicao.esta_na_dieta} for refeicao in refeicoes]
        return jsonify(lista_refeicoes)
    return jsonify({'message': 'Nenhuma refeição encontrada'}), 404
    
# visualizar uma única refeição
@app.route('/refeicoes/<int:id>', methods=['GET'])
def visualizar_refeicao(id):
    refeicao = Refeicao.query.get(id)
    if refeicao:
        return {'nome': refeicao.nome,
                'descricao': refeicao.descricao,
                'data_hora': refeicao.data_hora,
                'esta_na_dieta': refeicao.esta_na_dieta}
    return jsonify({'message': 'Refeição não encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)