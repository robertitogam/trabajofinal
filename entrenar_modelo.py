import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Datos de ejemplo
data = {
    'texto': [
        "Trámite urgente de licencia",
        "Solicitud común de permiso",
        "Currículo con experiencia",
        "Currículo sin experiencia",
        "Trámite de servicio público",
        "Renovación urgente de licencia"
    ],
    'categoria': [
        "Urgente", "Normal", "Aceptable", "Rechazado", "Normal", "Urgente"
    ]
}

df = pd.DataFrame(data)

# Modelo
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['texto'])
y = df['categoria']
model = MultinomialNB()
model.fit(X, y)

# Guardar modelo y vectorizer
with open("modelo.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)
