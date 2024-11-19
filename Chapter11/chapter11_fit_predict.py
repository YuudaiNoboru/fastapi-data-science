from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

digits = load_digits()
data = digits.data
targets = digits.target

#Divisão entre dados de treino e de teste.
training_data, testing_data, training_targets, testing_targets = train_test_split(data, targets, random_state=0)

#Treinando o modelo.
model = GaussianNB()
model.fit(training_data, training_targets)

#Fazendo predições no conjunto de testes.
predicted_targets = model.predict(testing_data)

#Calculando a acurácia.
accuracy = accuracy_score(testing_targets, predicted_targets)
print(accuracy)