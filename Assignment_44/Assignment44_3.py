# Q3: Add a new column 'Total' to the DataFrame as the sum of all subject marks.

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


if __name__ == "__main__":
    main()
