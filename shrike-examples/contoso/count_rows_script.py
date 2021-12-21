import argparse
import pandas as pd

def get_arg_parser(parser=None):
    """Parse the command line arguments for merge using argparse

    Args:
        parser (argparse.ArgumentParser or CompliantArgumentParser): an argument parser instance

    Returns:
        ArgumentParser: the argument parser instance

    Notes:
        if parser is None, creates a new parser instance
    """
    # add arguments that are specific to the component
    if parser is None:
        parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('--input_data', required=True, type=str, help="path to the input data")

    return parser

def main():
    """The main function"""
    
    # get the arguments
    parser = get_arg_parser()
    args = parser.parse_args()
    args = vars(args)


    # print the dataset path
    print("Path to the input dataset is '" + args["input_data"] + "'.") # args["input_data"] should be a string.

    # print the row counts
    csvdataset = pd.read_csv(args["input_data"] + "/iris.csv") # need to be consist with the input path
    num_rows = csvdataset.count()[0]
    print("the dataset contains {0} rows".format(num_rows))

if __name__ == "__main__":
    main()
