import os
import joblib
from sklearn.pipeline import Pipeline

# Carregando o modelo
model_file = os.path.join(os.path.dirname(__file__), "newsgroups_model.joblib")
loaded_model: tuple[Pipeline, list[str]] = joblib.load(model_file)
model, targets = loaded_model

# Executar uma predição
p = model.predict(["computer cpu memory ram"])
print(targets[p[0]])