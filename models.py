from database import db

class Refeicao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    data_hora = db.Column(db.DateTime, nullable=False)
    esta_na_dieta = db.Column(db.Boolean, default=True, nullable=False)

    def __repr__(self):
        return f"<Refeição {self.id}>"
