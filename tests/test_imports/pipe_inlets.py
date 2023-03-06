import pandas as pd


def pipe_inlet_csv(filename, **kwargs):
    return pd.read_csv(filename, **kwargs)

def pipe_inlet_excel(filename, **kwargs):
    return pd.read_excel(filename, **kwargs)

def pipe_inlet_json(filename, **kwargs):
    return pd.read_json(filename, **kwargs)
