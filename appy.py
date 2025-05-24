from flask import Flask, render_template, request, flash, redirect, url_for
import pickle
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Necesario para usar mensajes flash

# Cargar modelo entrenado al iniciar la app para no cargarlo cada vez
try:
    with open("modelo.pkl", "rb") as f:
        vectorizer, model = pickle.load(f)
except FileNotFoundError:
    vectorizer, model = None, None
    print("Error: No se encontró el archivo modelo.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    categoria = mensaje = ""
    if not vectorizer or not model:
        mensaje = "El modelo no está disponible, por favor revisa la configuración."
        flash(mensaje, "error")
        return render_template("index.html", categoria=categoria, mensaje=mensaje)

    if request.method == "POST":
        texto = request.form.get("descripcion", "").strip()

        if not texto:
            flash("Por favor selecciona un trámite o currículo.", "warning")
            return redirect(url_for("index"))

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
