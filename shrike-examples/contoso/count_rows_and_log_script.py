import argparse
import pandas as pd
import logging
import shrike  # do we need this 
from shrike.compliant_logging import enable_compliant_logging 
import os # do we need this 


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

    enable_compliant_logging()
    logger = logging.getLogger(__name__)

    # print the dataset path
    logger.info("Path to the input dataset is '" + args["input_data"] + "'.") # args["input_data"] should be a string.

    # print the row counts
    csvdataset = pd.read_csv(args["input_data"] + "/iris.csv") # need to be consist with the input path
    num_rows = csvdataset.count()[0]
    logger.info("the dataset contains {0} rows".format(num_rows))

    logger.info(csvdataset.to_string())

    # get the average file size
    file_no = 0
    file_size = 0
    for path, dirs, files in os.walk(args["input_data"]):
        for f in files:
            fp = os.path.join(path, f)
            file_size += os.path.getsize(fp)
            file_no += 1
    logger.info(f"There are {file_no} files in total.")
    logger.info(f"Total file size is {file_size} bytes.")
    avg_file_size = file_size / file_no
    logger.info(f"The average file size is {avg_file_size} bytes.")

if __name__ == "__main__":
    main()
