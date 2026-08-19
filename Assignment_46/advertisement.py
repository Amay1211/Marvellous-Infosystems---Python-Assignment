import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, root_mean_squared_error, r2_score
import joblib


def loadData(fileName):
    df = pd.read_csv(fileName)
    print("Dataset loaded successfuly")
    print("Inital Entries of dataset are as follows : ")
    print(df.head())
    return df


def preprocessData(df):
    unnamedColumns = df.columns[df.columns.str.contains("unnamed", case=False)]
    df.drop(unnamedColumns, axis=1, inplace=True)
    print("Number of missing values : ", df.isnull().sum())
    print("Preprocessed data as follows : ")
    print(df.head())
    return df


def splitData(df):
    x = df[["TV", "radio", "newspaper"]]
    y = df["sales"]
    print("Features of data : ", x)
    print("Labels of data : ", y)

    xTrain, xTest, yTrain, yTest = train_test_split(
        x, y, test_size=0.2, random_state=42
    )
    return xTrain, xTest, yTrain, yTest


def trainModel(xTrain, yTrain):
    model = LinearRegression()
    model = model.fit(xTrain, yTrain)
    print("Model Trained successfully")
    return model


def testModel(model, xTest):
    pred = model.predict(xTest)
    return pred


def evaluateModel(yTest, yPred):
    MSE = mean_squared_error(yTest, yPred)
    RMSE = root_mean_squared_error(yTest, yPred)
    R2 = r2_score(yTest, yPred)

    print("MSE : ", MSE)
    print("RMSE : ", RMSE)
    print("R Square : ", R2)


def preserveModel(model, fileName):
    joblib.dump(model, fileName)
    print("Model Preserve with name : ", fileName)


def main():
    df = loadData("Advertising.csv")
    df = preprocessData(df)
    xTrain, xTest, yTrain, yTest = splitData(df)
    model = trainModel(xTrain, yTrain)
    yPred = testModel(model, xTest)
    evaluateModel(yTest, yPred)

    modelFile = "AdvertisingLinearModel.pkl"
    preserveModel(model, modelFile)


if __name__ == "__main__":
    main()
