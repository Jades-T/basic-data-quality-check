import pandas as pd

def quality_check():
    """ Function that checks the quality of the csv file. """

    dataframe = pd.read_csv("data.csv")
    report = {
        "rows": len(dataframe),
        "nulls": dataframe.isnull().sum().to_dict(),
        "duplicates": dataframe.duplicated().sum(),
    }
    print(report)


if __name__ == '__main__':
    quality_check()