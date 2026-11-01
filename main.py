import pandas as pd
import json\

with open("Data/monsters_attributes_parsed.json", "r", encoding="utf-8") as file:
    data = json.load(file)

monsters = data["monsters"]

df = pd.json_normalize(monsters)

df = df.drop(columns= ["attribution", "id", "source"])

#print(df.head())

df["cr_group"] = pd.cut(df["cr_numeric"], bins = [-1, 4, 16, 23, float("inf")], labels = ["Tier 1", "Tier 2", "Tier 3", "Tier 4"])

X = df.drop(columns = ["cr_numeric", "cr_group"])
y = df["cr_group"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=17, test_size= 0.2, stratify=y)

from sklearn.tree import DecisionTreeClassifier

dtc = DecisionTreeClassifier()

dtc.fit(X_train, y_train)

y_pred = dtc.predict(X_test)

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))









