import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
  accuracy_score,
  confusion_matrix,
  classification_report
)

BORDER = "-" * 40

print(BORDER)
print("----Student Performance Case Student----")
print(BORDER)

print(BORDER)
print("Step 1 : Load the dataset")
print(BORDER)

dataPath = "student_performance_ml.csv"
df = pd.read_csv(dataPath)


print("Dataset loaded successfulluy")
df.drop("SleepHours",axis=1)
print("SleepHours Columns dropped")

print("Initial entries from dataset are as following : ")
print(df.head())
print("Last 5 entries from dataset are as following : ")
print(df.tail())


print(BORDER)
print("Step 2 : Data analysis(EDA)")
print(BORDER)

print("Shape of data : ", df.shape)
print("Columns Names : ", list(df.columns))
print("Data type of columns : ", df.dtypes) 

print("Missing values per column : ")
print(df.isnull().sum())

print("Class distribution ")
print(df["FinalResult"].value_counts())
print("Statistical report of dataset")
print(df.describe())
print("Average Studyhours : ", df["StudyHours"].mean())
print("Average Attendace : ", df["Attendance"].mean())
print("Minimum Sleephours : ",df["StudyHours"].min())
print("Maximum Attendace : ",df["Attendance"].max())
print("Percentage of Pass Students : ",df["FinalResult"].value_counts(normalize=True).get(1, 0) * 100)
print("Percentage of Fail Students : ",df["FinalResult"].value_counts(normalize=True).get(0, 0) * 100)

print(BORDER)
print("Step 3 : Deside dependant and independent variables")
print(BORDER)

featuresColumns = ['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted']

X = df[featuresColumns]
Y = df["FinalResult"]

print("Features Shape : ", X.shape)
print("Result Shape : ", Y.shape)

# print(BORDER)
# print("Step 4 - Visualisation of dataset")
# print(BORDER)

# plt.figure(figsize=(7,5))

# plt.hist(df["StudyHours"].tolist())
# plt.show()

# plt.scatter(df["StudyHours"].tolist(),df["PreviousScore"].tolist())
# plt.show()

# plt.boxplot(df["Attendance"].tolist())
# plt.show()

# plt.plot(df["AssignmentsCompleted"].tolist(),df["FinalResult"].tolist())
# plt.show()


# plt.plot(df["SleepHours"].tolist(),df["FinalResult"].tolist())
# plt.show()

print(BORDER)
print("Step 5 - Split Data in training and test datasets")
print(BORDER)


X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5, random_state=42)

print("Data splitting activity done")
print("X_train", X_train.shape) 
print("X_test", X_test.shape)   
print("Y_train", Y_train.shape) 
print("Y_test", Y_test.shape)   

print(BORDER)
print("Step 6 - Build the model")
print(BORDER)

# underfitting(poor training and testing accuracy), Good Fit, Overfitting(learning training data, not a pattern(Good trainig accuracy, poor testing accurary)cclar)
mode = DecisionTreeClassifier(max_depth=4)
print("Model gets created sucessfully")

print(BORDER)
print("Step 7 - Train the model")
print(BORDER)

model = mode.fit(X_train,Y_train)
print("Model trained sucessfully")


print(BORDER)
print("Step 8 - Test the model")
print(BORDER)

Y_pred = model.predict(X_test)
print("Model testing sucessfully")
print("Expected answers : ")
print(Y_test)

print("Predicted answers : ")
print(Y_pred)

print(BORDER)
print("Step 9 - Evaluate the model performance")
print(BORDER)

accuracy = accuracy_score(Y_test, Y_pred)
print("accuracy of model is : ", accuracy * 100)

print("confusion matrix")
cm = confusion_matrix(Y_test,Y_pred)
print(cm)


print("Classification report ")
print(classification_report(Y_test, Y_pred))

single_sample = pd.DataFrame([[6, 85, 66, 7]], columns=featuresColumns)
predictedOutput = model.predict(single_sample)
print("Student is failes or not - ", predictedOutput)

print(BORDER)
print("Step 10 - Model features importance")
print(BORDER)

for i,v in enumerate(model.feature_importances_):
  print(f"Feature {i}({featuresColumns[i]}), score: {v:.5f}")