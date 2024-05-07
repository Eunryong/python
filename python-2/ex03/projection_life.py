from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def preproccess(value:str):
    if type(value) is int or type(value) is float:
        return value
    num = float(value[:-1])
    if value.endswith("k"):
        return num * 1000
    else:
        return None


def display(data:pd.DataFrame, subdata:pd.DataFrame):
    df1 = data.loc[:,"1900"].apply(preproccess)
    df2 = subdata.loc[:, "1900"].apply(preproccess)
    # print(df1, df2)
    # merged = pd.merge(df1, df2, left_index=True, right_index=True)
    plt.scatter(df1, df2)
    plt.xlim(300, 10000)
    plt.xticks([300])
    plt.xticks([1000, 10000], minor=True)
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.title("1900")
    plt.show()



def main():
    life_data = load("life_expectancy_years.csv")
    income_data = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    display(income_data, life_data)
    

if __name__ == "__main__":
    main()