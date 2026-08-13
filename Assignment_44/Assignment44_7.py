# Q7: Create a bar plot of student names vs total marks.

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
    print("Shape of dataset : ", df.shape)
    print("Columns : ", list(df.columns))
    print(type(df))

    print(df.describe())

    df["total"] = df["Math"] + df["Science"] + df["English"]
    print("Shape of dataset : ", df.shape)
    print("Columns : ", list(df.columns))
    print(df.head())

    print("Student who scored more than 85 in Science ")
    print(df[df["Science"] > 85])

    print(df["Name"] == "Pooja")

    df.loc[df["Name"] == "Pooja", "Name"] = "Puja"

    print("DataFrame is ", df)

    sortedData = df.sort_values(by="total")
    print("Sorted data : ", sortedData)

    print("Bar Plot of Students Name vs Total Marks")

    plt.bar(
        df["Name"],
        df["total"],
        width=0.6,
        edgecolor="black",
        linewidth=1,
        alpha=0.8,
        label="Students",
    )

    plt.title("Students Name vs Total Marks")
    plt.xlabel("Students Names")
    plt.ylabel("Students Total")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
