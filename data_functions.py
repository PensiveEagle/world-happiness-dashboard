import pandas as pd

def get_data_from_csv( filepath: str = "Data/happy.csv" ) -> pd.DataFrame:
    data = pd.read_csv( filepath )
    return data

if __name__ == "__main__":
    print( get_data_from_csv() )