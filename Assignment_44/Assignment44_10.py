# Q9: Create a DataFrame with missing values and fill them with column mean.
# data2 = {
# 'Name': ['Amit', 'Sagar', 'Pooja'],
# 'Math': [np.nan, 76, 88],
# 'Science': [91, np.nan, 85]
# }

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():
    data = {
        "Name": ["Amit", "Sagar", "Pooja"],
        "Math": [85, 90, 78],
        "Science": [np.nan, 88, 80],
        "English": [75, np.nan, 82],
    }

    df = pd.DataFrame(data)
    print("Dataframe is ", df)

    df.drop(columns=["English"], inplace=True)
    print("Updated dataframe", df)


if __name__ == "__main__":
    main()
