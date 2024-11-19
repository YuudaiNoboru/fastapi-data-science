from sklearn.datasets import load_digits
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB

digits = load_digits()
data = digits.data
target = digits.target

# Criando o modelo.
model = GaussianNB()

# Executando a validação cruzada.
score = cross_val_score(model, data, target)
print(score)
print(score.mean())