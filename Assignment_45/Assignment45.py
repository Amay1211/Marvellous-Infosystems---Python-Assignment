# Q1: Normalize the 'Math' scores using Min-Max scaling.
# Q2: Create a gender column and perform one-hot encoding.
# Q3: Group students by gender and calculate average marks.
# Q4: Plot a pie chart of subject marks for 'Sagar'.
# Q5: Add a new column 'Status' where students with total >= 250 are 'Pass', else 'Fail'.
# Q6: Count how many students passed.
# Q7: Export the final DataFrame to a CSV file.
# Q8: Plot a histogram of math marks.
# Q9: Rename 'Math' column to 'Mathematics'.
# Q10: Plot a boxplot for English marks to check distribution and outliers.

import pandas as pd
import matplotlib.pyplot as plt


def main():
    data = {
        "Name": ["Amit", "Sagar", "Pooja"],
        "Math": [85, 90, 78],
        "Science": [92, 88, 80],
        "English": [75, 85, 82],
    }
    df = pd.DataFrame(data)
    print("Initial Dataframe: ", df)

    df["Math"] = (df["Math"] - df["Math"].min()) / (df["Math"].max() - df["Math"].min())

    print("Math column after normalization : ", df)

    df["Gender"] = [
        "Male",
        "Male",
        "Female",
    ]
    print("Dataframe after gender column", df)

    df["Gender"] = df["Gender"].map({"Male": 0, "Female": 1})
    print("Encoded Gender Columns", df)

    df["total"] = df["Math"] + df["Science"] + df["English"]
    print("Grouped Gender and Average of Marks", df.groupby("Gender")["total"].mean())

    print("Plot a pie chart of subject marks for 'Sagar'")

    sagar = df[df["Name"] == "Sagar"].iloc[0]
    plt.pie(
        [sagar["Math"], sagar["Science"], sagar["English"]],
        labels=["Math", "Science", "English"],
    )

    plt.show()

    df["Status"] = df["total"].apply(lambda total: "Pass" if total >= 250 else "Fail")

    print("Passed Student: ", (df["Status"] == "Pass").sum())

    df.to_csv("students_final.csv", index=False)

    print("DataFrame exported to students_final.csv")

    plt.figure()
    plt.hist(df["Math"], bins=5)
    plt.xlabel("Math Marks")
    plt.ylabel("Number of Students")
    plt.title("Distribution of Math Marks")
    plt.show()

    df.rename(columns={"Math": "Mathematics"}, inplace=True)

    print("\nQ9 - After renaming Math:")
    print(df)

    plt.figure()
    plt.boxplot(df["English"])
    plt.ylabel("English Marks")
    plt.title("English Marks Distribution")
    plt.show()


if __name__ == "__main__":
    main()
