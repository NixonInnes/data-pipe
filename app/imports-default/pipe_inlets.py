import pandas as pd

def pipe_inlet_csv(filename, **kwargs):
    return pd.read_csv(filename, **kwargs)

