import pandas as pd

class Data:
    def __init__(self,dataPath) -> None:
        self.dataPath = dataPath

    def read_data(self):
        if "csv" in self.dataPath:
            data = pd.read_csv(self.dataPath)
        elif "xls" in self.dataPath or "xlsx" in self.dataPath:
            data = pd.read_excel(self.dataPath)
        
        self.data = data
