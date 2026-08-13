# Q6: Sort the DataFrame by 'Total' marks in descending order.

import pandas as pd


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


if __name__ == "__main__":
    main()
