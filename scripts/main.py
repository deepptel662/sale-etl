import pandas as pd

def main():
    df= pd.read_csv(f"data\sales_data_dirty.csv")
    print(df.columns)





if __name__ == "__main__":
    main()

