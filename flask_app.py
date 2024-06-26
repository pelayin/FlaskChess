from flask import Flask, render_template
from chess_engine import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/move/<int:depth>/<path:fen>/")
def get_move(depth, fen):
    print("Calculando...")
    engine = Engine(fen)
    move = engine.iterative_deepening(depth - 1)
    print("¡Movimiento encontrado!", move)
    print(move)
    return move


@app.route("/test/<string:tester>")
def test_get(tester):
    return tester


# Aquí inicia la Aplicación
if __name__ == "__main__":
    app.run(debug=True)
