import pandas as pd
class CustomProfiler:
    def __init__(self,data:pd.DataFrame) -> None:
        self.data = data
        self.__get_features()

    def __get_features(self):
        self.features = self.data.columns
        self.no_features = len(self.features)
