import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

data = pd.read_csv("fake_or_real_news.csv")
data['fake'] = data['label'].apply(lambda x: 0 if x == 'REAL' else 1)
data = data.drop("label", axis=1)

x, y, = data['text'], data['fake']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)
x_train_vectorized = vectorizer.fit_transform(x_train)
x_test_vectorized = vectorizer.transform(x_test)

clf = LinearSVC()
clf.fit(x_train_vectorized, y_train)
score = clf.score(x_test_vectorized, y_test)

print("Sample length " + str(len(y_test)))
print("Score " + str(score))

with open("mytext.txt", "w", encoding="utf-8") as f:
    f. write(x_test.iloc[10])
    print("Written to mytext.txt")

with open("mytext.txt", "r", encoding="utf-8") as f:
    text = f.read()
    print(text)

vectorized_text = vectorizer.transform([text])
final = clf.predict(vectorized_text)
print("Final score: " + str(final))
