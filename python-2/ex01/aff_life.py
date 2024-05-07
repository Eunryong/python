import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from load_csv import load


def display(data: pd.DataFrame) -> None:
    SouthKorea_data = data.loc['South Korea']
    SouthKorea_data.index = SouthKorea_data.index.astype('uint64')
    ax = SouthKorea_data.plot(title="France Lifr expectancty Projections")
    ax.set_xlabel("Year")
    ax.set_ylabel("Life expectancty")
    ax.set_xticks(np.arange(1800, 2100, 40))
    plt.show()


def main():
    data = load("life_expectancy_years.csv")
    display(data)


if __name__ == "__main__":
    main()
