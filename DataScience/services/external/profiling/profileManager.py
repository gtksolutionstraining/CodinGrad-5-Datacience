import pandas as pd
from services.external.profiling.pandasProfiler import PandasProfiler
from services.external.profiling.customProfiler import CustomProfiler

class ProfileManager:
    def __init__(self,df:pd.DataFrame) -> None:
        self.df = df
        self.pandasProfiler = PandasProfiler(self.df)
        self.customProfiler = CustomProfiler(self.df)

    def profile(self):
        self.no_features = self.customProfiler.no_features
        self.features = self.customProfiler.features