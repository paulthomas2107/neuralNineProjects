import numpy as np

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = load_breast_cancer()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

tree_list = []
for i in range(100):
    tree = DecisionTreeClassifier(max_features='sqrt')
    subset_indices = np.random.choice(np.arange(len(X_train)), size=(len(X_train) // 2))
    X_train_subset = X_train[subset_indices]
    Y_train_subset = y_train[subset_indices]
    tree.fit(X_train_subset, Y_train_subset)
    tree_list.append(tree)

preds = []
for i, tree in enumerate(tree_list):
    individual_preds = tree.predict(X_test)
    individual_accuracy = accuracy_score(y_test, individual_preds)
    print(f"Tree {i + 1} has accuracy : {individual_accuracy}")
    preds.append(individual_preds)

preds = np.array(preds)
ensemble_predictions = np.round(np.mean(preds, axis=0))

ensemble_accuracy = accuracy_score(y_test, ensemble_predictions)

print(f"Accuracy :     {ensemble_accuracy}")

rf = RandomForestClassifier(n_estimators=100)
rf.fit(X_train, y_train)
rf_preds = rf.predict(X_test)

print(f"Accuracy RFC : {accuracy_score(y_test, rf_preds)}")