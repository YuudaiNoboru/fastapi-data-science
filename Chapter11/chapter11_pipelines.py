import pandas as pd
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Carregando algumas categorias do conjunto newsgroups
categories = [
    "soc.religion.christian",
    "talk.religion.misc",
    "comp.sys.mac.hardware",
    "sci.crypt",
]

newsgroups_training = fetch_20newsgroups(
    subset="train", categories=categories, random_state=0
)
newsgroups_testing = fetch_20newsgroups(
    subset="test", categories=categories, random_state=0
)

# Criando pipeline
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Trainando o modelo
model.fit(newsgroups_training.data, newsgroups_training.target)

# Realizando a predição no conjunto de teste
predicted_targets = model.predict(newsgroups_testing.data)

# Computando a acurácia
accuracy = accuracy_score(newsgroups_testing.target, predicted_targets)
print(accuracy)

# Exibindo a matrix de confusão
confusion = confusion_matrix(newsgroups_testing.target, predicted_targets)
confusion_df = pd.DataFrame(
    confusion,
    index=pd.Index(newsgroups_testing.target_names, name="True"),
    columns=pd.Index(newsgroups_testing.target_names, name="Predicted"),
)
print(confusion_df)
