import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (accuracy_score, confusion_matrix, classification_report)

def winePrediction(datasetPath):
  BORDER = "-" * 50

  ##########################################################
  # Step 1 : Load the dataset
  ##########################################################

  print("Step 1 : Load the dataset")
  print(BORDER)

  df =  pd.read_csv(datasetPath)
  print("Dataset loaded successfully")
  print("Initial entries from dataset are : ")
  print(df.head())
  print("Last entries from dataset are : ")
  print(df.tail())

  ##########################################################
  # Step 2 : Data analysis
  ##########################################################

  print(BORDER)
  print("Step 2 : Data analysis")
  print(BORDER)

  print("Shape of data : ", df.shape)
  print("Columns names : ", list(df.columns))

  print("Missing values per column")
  print(df.isnull().value_counts())

  df.dropna(inplace=True)
  print("Data has been cleaned")

  print("Statical report of dataset")
  print(df.describe())

  ##########################################################
  # Step 3 : Decide dependent and independent variables
  ##########################################################
  
  print(BORDER)
  print("Step 3 : Decide dependent and independent variables")
  print(BORDER)

  x = df.drop(columns=["Class"])
  y = df['Class']

  print("Independent variables shape : ",x.shape)
  print("Dependent variables shape : ", y.shape)

  ##########################################################
  # Step 4 : Split data in training and testing dataset
  ##########################################################

  print(BORDER)
  print("Step 4 : Split data in training and testing dataset")
  print(BORDER)

  xTrain, Xtest, yTrain, yTest = train_test_split(x, y, test_size=0.5, random_state=42)

  print("Shape of xTrain : ",xTrain.shape)
  print("Shape of xTest : ",Xtest.shape)
  print("Shape of yTrain : ",yTrain.shape)
  print("Shape of yTest : ",yTest.shape)

  ##########################################################
  # Step 5 : Build the model
  ##########################################################

  print(BORDER)
  print("Step 5: Build the model")
  print(BORDER)

  model = DecisionTreeClassifier(max_depth=5)
  print("Model has been created")
  
  ##########################################################
  # Step 6 : Train the model
  ##########################################################

  print(BORDER)
  print("Step 6: Train the model")
  print(BORDER)

  model = model.fit(xTrain, yTrain)
  print("Model Trained successfully")

  print("Inportant Features")
  print(model.feature_importances_)

  ##########################################################
  # Step 7 : Test the model
  ##########################################################
  
  print(BORDER)
  print("Step 7: Train the model")
  print(BORDER)

  yPred = model.predict(Xtest)
  
  print("Model testing sucessfully")
  print("Expected answers : ")
  print(yTrain)
  
  print("Predicted answers : ")
  print(yPred)


  ##########################################################
  # Step 8 : Evaluate the model performance
  ##########################################################

  print(BORDER)
  print("Step 8: Evaluate the model Performance")
  print(BORDER)

  accuracy = accuracy_score(yTest, yPred)
  print("Accuracy of model is ", accuracy * 100)

  print("Confusion matrix")
  cm = confusion_matrix(yTest,yPred)
  print(cm)

  print("classification report")
  print(classification_report(yTest,yPred))


  ##########################################################
  # Step 9 : Hyper parameter tunning(max-depth)
  ##########################################################

  print(BORDER)
  print("Step 9: Hyper parameter tunning")
  print(BORDER)

  accuracyScore = []
  maxDepthRange = range(1,20)

  for maxDepth in maxDepthRange:
    model = DecisionTreeClassifier(max_depth=maxDepth)
    model = model.fit(xTrain, yTrain)
    yPred = model.predict(Xtest)
    accuracy = accuracy_score(yTest,yPred)
    accuracyScore.append(accuracy)

  print("Accuracy report : ")

  for no in accuracyScore:
    print(no)
     
def main():
  winePrediction("WinePredictor.csv")

if __name__ == "__main__":
  main()