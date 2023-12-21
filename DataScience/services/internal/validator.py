import argparse
import os

class Validator:

    def __init__(self,logging) -> None:
        self.logging = logging
        self.verbose = False

    def set_args(self,args:argparse.Namespace):
        self.args = args.__dict__
        self.verbose = self.args["verbose"]

    def get_args(self):
        if self.verbose:
            self.logging.info(f"Returning Arguments: {self.args}")
        return self.args
    
    def get_yes_no_choice(self):
        if self.verbose:
            self.logging(f"Getting Yes/No Choice for creating Output Directory")
        flag = True
        while flag:
            choice = input()
            if choice in ["y","n","yes","no"]:
                flag = False
            else:
                print("Please provide [y','n','yes','no']")
        if self.verbose:
            self.logging(f"Got the choice: {choice}  for creating Output Directory.")
        return choice
    
    def validate(self):
        if not os.path.isfile(self.args["input_csv"]):
            print("Error: Input CSV doesn't exist. Please provide valide input_csv")
            exit()
        if self.args["output_dir"] is None or not os.path.isdir(self.args["output_dir"]):
            print("Warning: output directory doesn't exist, Do you want to me create ? (y/n)")
            choice = self.get_yes_no_choice()
            if "y" in choice:
                if self.args["output_dir"] is None:
                    os.makedirs("assets",exist_ok=True)
                else:
                    os.makedirs(self.args["output_dir"],exist_ok=True)
            else:
                print("Please provide Valide Output Directory")
                exit()
