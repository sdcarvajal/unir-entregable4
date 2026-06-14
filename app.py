from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify(
        message="Hola. Aplicacion Flask desplegada con GitHub Actions, Azure ACR y Azure ACI.",
        status="ok"
    ), 200


@app.get("/health")
def health():
    return jsonify(status="healthy"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
