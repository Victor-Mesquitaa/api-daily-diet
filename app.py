from flask import Flask, request, jsonify
from database import db
from models.refeicao import Refeicao

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin@localhost:3306/api-daily-diet'
id_control = 1
refeicoes = []

db.init_app(app)

@app.route('/refeicoes', methods=['POST'])
def insert_food():
    global id_control

    data = request.json

    alimento = data.get('alimento')
    descricao = data.get('descricao')
    dia = data.get('dia')
    indicador = data.get('indicador_dieta')

    if not alimento or not descricao or not dia:
        return jsonify({'message': 'alimento, descição e dia são obrigatórios'}), 400

    try:
        dia = date.fromisoformat(dia)
    except ValueError:
        return jsonify({'message': 'dia deve estar no formato AAAA-MM-DD'}), 400

    nova_refeicao = Refeicao(
        alimento=alimento,
        descricao=descricao,
        dia=dia,
        indicador_dieta=indicador
    )

    db.session.add(nova_refeicao)
    db.session.commit()

    return jsonify({'message': 'Refeição cadastrada com sucesso', 'id': nova_refeicao.id}), 201


if __name__ == '__main__':
    with app.app_context(): db.create_all()
    app.run(debug=True)