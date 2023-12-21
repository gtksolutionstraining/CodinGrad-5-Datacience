import argparse
from services.internal.validator import Validator
from services.internal.data import Data
from services.internal.logger import getLogger

def main(args:argparse.Namespace):
    print("Welcome to Data Science Automated Tool")
    logging = getLogger()
    validator = Validator(logging)
    validator.set_args(args)
    validator.validate()
    data = Data(args.input_csv)
    data = data.read_data()
    pm = 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Command Line Arguments for Data Science Automation Tool")
    parser.add_argument("--input-csv", help="Please provide input CSV Path",required=True)
    parser.add_argument("--verbose", help="Please select for Logging by default false",default=False)
    parser.add_argument("--output-dir", help="Please provide Output Directory for the report")
    args = parser.parse_args()
    main(args)