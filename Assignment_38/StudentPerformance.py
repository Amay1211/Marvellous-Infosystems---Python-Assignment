import pandas as pd
import matplotlib.pyplot as plt

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

featuresColumns = ['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted', 'SleepHours']

features = df[featuresColumns]
result = df["FinalResult"]

print("Features Shape : ", features.shape)
print("Result Shape : ", result.shape)

print(BORDER)
print("Step 4 - Visualisation of dataset")
print(BORDER)

plt.figure(figsize=(7,5))

plt.hist(df["StudyHours"].tolist())
plt.show()

plt.scatter(df["StudyHours"].tolist(),df["PreviousScore"].tolist())
plt.show()

plt.boxplot(df["Attendance"].tolist())
plt.show()

plt.plot(df["AssignmentsCompleted"].tolist(),df["FinalResult"].tolist())
plt.show()


plt.plot(df["SleepHours"].tolist(),df["FinalResult"].tolist())
plt.show()