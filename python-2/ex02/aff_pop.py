import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from load_csv import load


def preproccess(value:str):
    num = float(value[:-1])
    if value.endswith("K"):
        return num / 1000
    elif value.endswith("M"):
        return num
    else:
        return None


def display(data: pd.DataFrame) -> None:
    SouthKorea_data = data.loc['South Korea', : "2050"].apply(preproccess)
    print(SouthKorea_data.values)
    SouthKorea_data.index = SouthKorea_data.index.astype('uint64')
    France_data = data.loc['France', : "2050"].apply(preproccess)
    France_data.index = France_data.index.astype('uint64')
    ax = SouthKorea_data.plot(title="Population Projections")
    ax.set_xlabel("Year")
    ax.set_ylabel("Population")
    ax.set_xlim(1790, 2060)
    ax.set_xticks(np.arange(1800, 2050, 40))
    ax.set_yticks(np.arange(0, 80, 20))
    ax.set_yticklabels(f'{val}M' for val in np.arange(0, 80, 20))
    France_data.plot(ax=ax)
    plt.legend(loc="lower right")
    plt.show()

def main():
    data = load("population_total.csv")
    display(data)

if __name__ == "__main__":
    main()