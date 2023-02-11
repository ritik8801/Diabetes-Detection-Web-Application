import argparse
from preprocessing.dataloading import DataIngestion
from preprocessing.plots import Plot
from modelbuilding.model import ModelBuilding



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv")
    parser.add_argument("plot")
    args = parser.parse_args()
    #import the dataset
    di = DataIngestion()
    di.load_data(path=args.csv)
    m = ModelBuilding(df, path=args.plot) # noqa: F821
    
