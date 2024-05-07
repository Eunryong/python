import pandas as pd
import os

def load(path: str) -> pd.DataFrame:
    try :    
        pwd = os.getcwd()
        file_path = path if os.path.isabs(path) else os.path.join(pwd, path)
        assert os.path.isfile(file_path), "File not found"
        file_extention = os.path.splitext(path)[1]
        assert file_extention and file_extention.lower() == '.csv', "File extention error"
        data = pd.read_csv(file_path, index_col=0)
        return data
    except AssertionError as e:
        print("AssertionError:", e)
        exit(1)

def main():
    print(load("life_expectancy_years.csv"))


if __name__ == "__main__":
    main()
