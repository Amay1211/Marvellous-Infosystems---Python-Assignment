import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def WeatherPrediction(datasetPath):
    df = pd.read_csv(datasetPath)
    print("Dateset loaded successfully")
    print("Shape of dateset", df.shape)
    print("First few entries are ")
    print(df.head())

    print("Columns are ", list(df.columns))
    df["Wether"] = df["Wether"].map({"Sunny": 0, "Overcast": 1, "Rainy": 2})
    df["Temperature"] = df["Temperature"].map({"Cool": 0, "Mild": 1, "Hot": 2})

    x = df.drop(columns=["Play"])
    y = df["Play"]

    k = 19

    xTrain, xTest, yTrain, yTest = train_test_split(
        x, y, test_size=0.2, random_state=42
    )
    print(xTrain, xTest, yTrain, yTest)

    model = KNeighborsClassifier(n_neighbors=k)
    model = model.fit(xTrain, yTrain)
    yPred = model.predict(xTest)

    accuracy = accuracy_score(yTest, yPred) * 100
    print(accuracy)

    print("Confusion Matrix : ")
    print(confusion_matrix(yTest, yPred))

    print("Classification Report ")
    print(classification_report(yTest, yPred))


def main():
    WeatherPrediction("MarvellousInfosystems_PlayPredictor.csv")


if __name__ == "__main__":
    main()
