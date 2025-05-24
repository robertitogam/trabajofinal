from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Cargar modelo y vectorizer
with open("modelo.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

# Opciones predefinidas
opciones = [
    "Trámite urgente de licencia",
    "Solicitud común de permiso",
    "Currículo con experiencia",
    "Currículo sin experiencia",
    "Trámite de servicio público",
    "Renovación urgente de licencia"
]

@app.route('/', methods=['GET', 'POST'])
def index():
    categoria = None
    texto = None

    if request.method == 'POST':
        texto = request.form.get('texto_opcion')
        if texto:
            X = vectorizer.transform([texto])
            categoria = model.predict(X)[0]

    return render_template('index.html', opciones=opciones, categoria=categoria, texto=texto)

if __name__ == '__main__':
    app.run(debug=True)
