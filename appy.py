from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Cargar modelo entrenado
with open("modelo.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    categoria = mensaje = ""
    if request.method == "POST":
        texto = request.form["descripcion"]
        X = vectorizer.transform([texto])
        categoria = model.predict(X)[0]

        if categoria == "Urgente":
            mensaje = "ALERTA: Este trámite debe ser priorizado."
        elif categoria == "Rechazado":
            mensaje = "ALERTA: El currículo no cumple los requisitos."
        else:
            mensaje = "Trámite o currículo en estado normal."

    return render_template("index.html", categoria=categoria, mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)
