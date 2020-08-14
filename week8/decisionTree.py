import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def runDecisionTree(dataSet, targetColumn, columnsToRemove):
    df = pd.read_csv(dataSet)
    df2 = df[df.columns.difference(columnsToRemove)]
    x = df2.loc[:, df2.columns != targetColumn]
    y = df2[targetColumn]
    X_train = pd.get_dummies(x)
    labels = X_train.columns.values

    # Standardizing the data  OPTIONAL

    scaler = StandardScaler()

    # We need to fit the scaler to our data before transformation
    x_train = scaler.fit_transform(
        x.loc[:])
    # train test split

    x_train, x_test, y_train, y_test = train_test_split(x_train, y_test, test_size=0.15, random_state=42)

    dt = DecisionTreeClassifier()
    dt.fit(x_train, y_train)
    print("score :", dt.score(x_test, y_test))


runDecisionTree("heart.csv", "cp", "target")
