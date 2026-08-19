import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
)
import joblib
import numpy as np


def loadData(fileName):
    df = pd.read_csv(fileName)
    print("Dataset loaded successfuly")
    print("Inital Entries of dataset are as follows : ")
    print(df.head())
    return df


def preprocessData(df):
    unnamedColumns = df.columns[df.columns.str.contains("unnamed", case=False)]
    df.drop(unnamedColumns, axis=1, inplace=True)
    df.dropna(inplace=True)
    df = df.drop(["CodeNumber"], axis=1)

    columnsWithQuestionMark = df.columns[df.astype(str).eq("?").any()]
    print("Columns with ? :", columnsWithQuestionMark)

    # Replace ? with NaN
    df["BareNuclei"] = df["BareNuclei"].replace("?", np.nan)

    # Convert column to numeric
    df["BareNuclei"] = pd.to_numeric(df["BareNuclei"])

    # Replace NaN with mode
    df["BareNuclei"] = df["BareNuclei"].fillna(df["BareNuclei"].mode()[0])

    # Check again
    columnsWithQuestionMark = df.columns[df.astype(str).eq("?").any()]
    print("Columns with ? after replacing ? :", columnsWithQuestionMark)

    print("Number of missing values : ", df.isnull().sum())
    print("Preprocessed data as follows : ")
    print(df.head())
    return df


def splitData(df):
    x = df.drop(["CancerType"], axis=1)
    y = df["CancerType"]
    print("Features of data : ", x.head())
    print("Labels of data : ", y.head())

    xTrain, xTest, yTrain, yTest = train_test_split(
        x, y, test_size=0.2, random_state=42
    )
    return xTrain, xTest, yTrain, yTest


def trainModel(xTrain, yTrain):
    model = DecisionTreeClassifier(max_depth=4)
    model = model.fit(xTrain, yTrain)
    print("Model Trained successfully")
    return model


def testModel(model, xTest):
    pred = model.predict(xTest)
    return pred


def evaluateModel(yTest, yPred):
    print("Accuracy: ", accuracy_score(yTest, yPred) * 100)
    print("Confusion Matrix", confusion_matrix(yTest, yPred))
    print("Precision Score", precision_score(yTest, yPred, pos_label=4) * 100)
    print("recall Score", recall_score(yTest, yPred, pos_label=4) * 100)
    print("f1 score", f1_score(yTest, yPred, pos_label=4) * 100)


def preserveModel(model, fileName):
    joblib.dump(model, fileName)
    print("Model Preserve with name : ", fileName)


def main():
    df = loadData("breast-cancer-wisconsin.csv")
    df = preprocessData(df)
    xTrain, xTest, yTrain, yTest = splitData(df)
    model = trainModel(xTrain, yTrain)
    yPred = testModel(model, xTest)
    evaluateModel(yTest, yPred)

    modelFile = "BreastCancerDecisionModel.pkl"
    preserveModel(model, modelFile)


if __name__ == "__main__":
    main()
