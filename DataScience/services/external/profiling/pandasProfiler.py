import pandas as pd
import ydata_profiling as yp

class PandasProfiler:
    def __init__(self,data:pd.DataFrame) -> None:
        self.data = data

    def profile(self):
        report = yp.ProfileReport(self.data)
        self.report = report.get_description()