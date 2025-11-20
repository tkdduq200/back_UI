import pandas as pd
from belong.ml.config import DATA_PATH

class CorrelationRepository:

    def load(self):
        return pd.read_csv(DATA_PATH)
