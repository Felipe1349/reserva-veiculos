from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite que o frontend acesse a API

@app.route("/")
def home():
    return {"message": "API de Reserva de Veículos rodando"}

if __name__ == "__main__":
    app.run(debug=True)
