import argparse

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

    parser.add_argument('--value', type = int, default = 0, help = 'input value') # add the value to the parser

    return parser

def main():
    """The main function"""
    
    # get the arguments
    parser = get_arg_parser()
    args = parser.parse_args()
    args = vars(args)

    value_inp = args['value']
    value_add = value_inp + 1000
    print('The input value is {0}, and the output value is {1}'.format(value_inp, value_add))

if __name__ == "__main__":
    main()
