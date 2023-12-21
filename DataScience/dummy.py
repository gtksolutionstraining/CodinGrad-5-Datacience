import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Command Line Arguments for Data Science Automation Tool")
    parser.add_argument("--input-csv", help="Please provide input CSV Path")
    parser.add_argument("--verbose", help="Please select for Logging by default false",default=False)
    parser.add_argument("--output-dir", help="Please provide Output Directory for the report")
    args = parser.parse_args()
    print(args)
    print(type(args))
    print(dir(args))
    print(args.__dict__)